from scipy.signal import find_peaks
from numpy import*

from .utilities import ConstantDeriv, ConstantPoints, ESR_ls, Cap_ls, Half_pt_ind


#Capacitance analysis (given x and y dataset, current and masses)
#Recieve current in mA and mass in mg and convert to A and g for calculations
def CC_Cap(xset, yset, current, m1 = False, m2 = False, ESR_method = True, setting = False, cap_method = False, filename = False, cap_grav = True):
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
                       = 2 or True (default constant second derivative method using the point where the second derivative is greater than 1)
                       = 201 (constant second derivative method where the cut off derivative is specified using setting)
        
        setting : :class:`float`, optional
            The setting for ESR analysis
            setting = False for ESR_method = 1, 2 or True
            setting = nth point/cut off second derivative depending on the ESR_method
            
        cap_method : :class:`int`, optional
            The method for capacitance analysis
            cap_method = 1 (default method where the lower voltage range is used)
                       = 2 (upper voltage range is used)
  
 
        filename : :class:`string`, optional
            Name of the text file being analysed
        

        cap_grav : :class:`bool` 
            cap_grav = False, output non-gravimetric capacitance
            cap_grav = True, output gravimetric capacitance

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
                        
    
    mid_ind = [Half_pt_ind(yset[peaks[i]:troughs[i]],(yset[peaks[i]]+yset[troughs[i]])/2) for i in range(len(peaks))]
    
    peak_step = int(floor(len(peaks)/20))+1
    ave_peak = mean(yset[peaks[::peak_step]])
    ave_trough = mean(yset[troughs[::peak_step]])
    ave_length = ave_peak-ave_trough
    
    
    cc_grad = []
    faulty_cyc_ind = []
    for i in range(len(peaks)):
        if i<=10:
            sel_peaks = peaks[:10]
            ave_len = mean([len(xset[peaks[k]:troughs[k]]) for k in range(len(sel_peaks))])
        else:
            ave_len = mean([len(xset[peaks[k]:troughs[k]]) for k in range(i-10, i)])

        if len(xset[peaks[i]:troughs[i]]) < ave_len*0.5:
            faulty_cyc_ind += [i]
            print('Cycle ' + str(i+1)+ ' has insufficient data points (50% less than average). Skipped for capacitance calculation') 
            
        elif len(xset[peaks[i]:troughs[i]]) > ave_len*1.5:
            faulty_cyc_ind += [i]
            print('Cycle ' + str(i+1)+ ' has significantly more data points (50% more than average). Skipped for capacitance calculation') 
        
        elif yset[peaks[i]] < ave_peak*0.9:
            faulty_cyc_ind += [i]
            print('Cycle ' + str(i+1)+ ' did not reach the maximum cycling voltage ' + str(round(ave_peak, 2)) + ' V. Skipped for capacitance calculation') 
            
        elif yset[peaks[i]]-yset[troughs[i]] < ave_length*0.9 or yset[peaks[i]]-yset[troughs[i]] > ave_length*1.1:
            faulty_cyc_ind += [i]
            print('Cycle ' + str(i+1)+ ' has abnormal charging/discharging voltage range. Skipped for capacitance calculation') 
            
        else:
            if cap_method is 1 or cap_method is False:
                try:
                    cc_grad += [polyfit(xset[peaks[i]:troughs[i]][mid_ind[i]:], yset[peaks[i]:troughs[i]][mid_ind[i]:],1, cov=False)[0]]
                except:
                    faulty_cyc_ind += [i]
                    print('Error found in cycle ' + str(i+1)+ '. Skipped for capacitance calculation')
                  
            elif cap_method is 2:
                try:
                    cc_grad += [polyfit(xset[peaks[i]:troughs[i]][:mid_ind[i]], yset[peaks[i]:troughs[i]][:mid_ind[i]],1, cov=False)[0]]
                except:
                    faulty_cyc_ind += [i]
                    print('Error found in cycle ' + str(i+1)+ '. Skipped for capacitance calculation')         
      
         
                        
    
    if ESR_method == 1 or ESR_method == 101:
        esr_v = [ConstantPoints(yset, peaks[i], set_n = setting) for i in range(len(peaks))]
      
    elif ESR_method is True or ESR_method == 2 or ESR_method == 201:
        esr_v = [ConstantDeriv(xset, yset, peaks[i], troughs[i], set_deriv = setting) for i in range(len(peaks))]
                      
    elif ESR_method is False:
        esr_v = False
        
    else:
        print('ESR method not specified. ESR values will not be calculated.')
        esr_v= False
        
    if cap_grav is True and m1 is not False and m2 is not False:
        cap_ls_calc = Cap_ls(cc_grad, current*10**(-3), m1*10**(-3), m2*10**(-3))
        
    else:
        cap_ls_calc = Cap_ls(cc_grad, current*10**(-3), cap_grav = False)

    
    esr_ls_calc = ESR_ls(esr_v, current*10**(-3))
    
    return cap_ls_calc, esr_ls_calc, peaks, troughs, N_cycle, faulty_cyc_ind


