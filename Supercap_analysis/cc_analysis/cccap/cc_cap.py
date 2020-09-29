from scipy.signal import find_peaks
from numpy import*

from .utilities import ConstantDeriv, ConstantPoints, ESR_ls, Cap_ls


#Capacitance analysis (given x and y dataset, current and masses)
#Recieve current in mA and mass in mg and convert to A and g for calculations
def CC_Cap(xset, yset, current, m1=False, m2=False, ESR_method = True, setting = False, filename=False, norm_cap=False):
    """
        Data manipulation
        
        
        Notes
        -----
        Capacitance and ESR analysis
       
        Parameters
        ----------
        xset : :class:`list`
            List of time reading   
            
        yset : :class:`list`
            List of corresponding voltage reading  
        
        current : :class:`float`
            The current under which the GCD is operated. The current is in mA. 
        
        m1 : :class:`float`, optional
            The mass of electrode 1 of the supercapacitor. The mass is in mg.

        m2 : :class:`float`, optional
            The mass of electrode 2 of the supercapacitor. The mass is in mg.
            
        ESR_method : :class:`int`, optional
            The method for ESR analysis.
            ESR_method = 1 (default constant point analyis using the first point after the peak for calculating voltage drop) 
                       = 101 (constant point analysis using the nth point after the peak, where n is specified using setting)
                       = 2 or True (default constant second derivative method using the point where the second derivative is greater than 0.01)
                       = 201 (constant second derivative method where the cut off derivative is specified using setting)
        
        setting : :class:`float`, optional
            The setting for ESR analysis
            setting = False for ESR_method = 1, 2 or True
            setting = nth point/cut off second derivative depending on the ESR_method
  
 
        filename : :class:`string`, optional
            Name of the text file being analysed
        

        norm_cap : :class:`bool` 
            norm_cap = False, output gravimetric capacitance
            norm_cap = True, output non-gravimetric capacitance

        returns
        -------
        : :class:`list, list, list, list, int` 
            [list of capacitance], [list of ESR], [list of peak indices], [list of trough indices], number of cycles
                
            
    """

    if filename != False:
        print('The file currently being analysed is:', filename)
        
    else:
        pass 
    

    
    troughs, _= find_peaks(-yset)
    peaks, _= find_peaks(yset)
    N_cycle=0
    
    #Checking the number of cycle(s)
    if len(peaks) == len(troughs):
        N_cycle = len(peaks)
        
    else:
        peaks = peaks[:-1]
        if len(peaks) == len(troughs):
            N_cycle = len(peaks)
        else:
            print('Error! The number of peaks cannot match the number of troughs')
                        

    
    cc_grad = [polyfit(xset[int(floor((peaks[i]+troughs[i])/2)):troughs[i]], yset[int(floor((peaks[i]+troughs[i])/2)):troughs[i]],1, cov=False)[0] for i in range(len(peaks))]
        
    if ESR_method == 1 or ESR_method == 101:
        esr_v = [ConstantPoints(yset, peaks[i], set_n = setting) for i in range(len(peaks))]
      
    elif ESR_method is True or ESR_method == 2 or ESR_method == 201:
        esr_v = [ConstantDeriv(xset, yset, peaks[i], troughs[i], set_deriv = setting)[0] for i in range(len(peaks))]
                      
    else:
        esr_v = False

        
    if norm_cap==True:
        cap_ls_calc = Cap_ls(cc_grad, current*10**(-3), norm_cap=True)
        
    elif m1==False and m2==False:
        cap_ls_calc = Cap_ls(cc_grad, current*10**(-3), norm_cap=True)
        
    else:
        cap_ls_calc = Cap_ls(cc_grad, current*10**(-3), m1*10**(-3), m2*10**(-3))
    
    esr_ls_calc = ESR_ls(esr_v, current*10**(-3))
    
    return cap_ls_calc, esr_ls_calc, peaks, troughs, N_cycle

