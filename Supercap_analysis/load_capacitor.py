from numpy import*

from .utilities import*
from .cccap.cc_cap import* 
from .supercap import*

#load a single supercapacitor GDC txt file and save it in the Supercap class. First line being the header. The first coloumn is the elapsed time in second, the second coloumn is Voltage. 
#mass_ls is a list of two lists of the mass of each electrode
#if current is not entered, it is going to be generated from the filename (the file name has to include the current in mA, seperated by '/' or '_' and followed by '_mA')
#recieve mass and current in mg and mA respectively, output as mg and mA
def Load_capacitor(pathway, mass_ls = False, current = False, row_skip = False, ESR_method = True, setting = False, cap_norm = False):
    """
        Loading all relevant information of the measured supercapacitor the of the specified text file
        
        Parameters
        ----------
        path : :class:`str`
            The path in which the data files are located. 
            The current of each file has to be specified and seperated by either '/' or '_' and followed by '_mA' at the end
            Example: './folder_x/0.1_mA_GCD_sample_A.txt'
            
        mass_ls : :class:`list`
            Measurements of the mass of each electrode. mass_ls will result in non-gravimetric capacitance being calculated. 
            mass_ls = False (calculate non-gravimetric capacitance)
                    = [[List of mass measurements for electrode 1], [List of mass measurements for electrode 2]]    
                          (calculate gravimetric capacitance)                    
        
        row_skip : :class:`int`
            The number of rows of headers to skip in the text files.
            row_skip = False (The prompt will ask for rows to skip for the file)
                     = : :class:`int` (The specified number of rows will be skipped for all files in the path)
        
        ESR_method : :class:`int`, optional
            The method for ESR analysis.
            ESR_method = 1 (default constant point analyis using the first point after the peak for calculating voltage drop) 
                       = 101 (constant point analysis using the nth point after the peak, where n is specified using setting)
                       = 2 or True (default constant second derivative method using the point where the second derivative is greater than 0.01)
                       = 201 (constant second derivative method where the cut off derivative is specified using setting)
                       = False (ESR value will be returned as False)
                       
        cap_norm : :class:`bool` 
            norm_cap = False, output gravimetric capacitance
            norm_cap = True, output non-gravimetric capacitance

        returns
        -------
        : :class:`list, list` 
            [list of current density], [list of Supercap classes for each current density], [list of peak indices]
                
            
    """
    if current == False:
        current = Readcurrent(pathway)
    else:
        pass
    
    if row_skip is False:
        row_skip = int(input('Please enter the number of header row(s) in this file:'))
    else:
        pass
    
    GDC = Fast_load(pathway, skip_header = row_skip)
    GDC_t = GDC[0]
    GDC_V = GDC[1]
    
    if mass_ls==False:
        m1 = False
        m2 = False
        error = False
        mm1 = False
        mm2 = False
        std1= False
        std2 = False

    else:
        m1 = mass_ls[0]
        m2 = mass_ls[1]
        error = delt_m(m1, m2)
        mm1 = mean(m1)
        mm2 = mean(m2)
        std1 = std(m1)
        std2 = std(m2)
    
    if ESR_method == 101 and setting is False:
        setting = int(input('How many points after the peak would you like to be considered for the ESR analysis? (the default value is 1)'))
        
    elif ESR_method == 201 and setting is False:
        setting = float(input('Please specify a cut-off derivative (the default value is 0.01)'))
        
    else:
        pass

    if ESR_method is True:
        cap_data = CC_Cap(GDC_t, GDC_V, current, mm1, mm2, norm_cap=cap_norm)

    elif ESR_method is False:
        cap_data = CC_Cap(GDC_t, GDC_V, current, mm1, mm2, ESR_method= False , norm_cap=cap_norm)

    else:
        cap_data = CC_Cap(GDC_t, GDC_V, current, mm1, mm2, ESR_method= ESR_method, setting = setting, norm_cap=cap_norm)
                      
    return Supercap(current, [GDC_t, GDC_V], [[mm1, std1],[mm2, std2]], cap_data[0], cap_data[1], [cap_data[2], cap_data[3]], cap_data[4], error, ESR_method)