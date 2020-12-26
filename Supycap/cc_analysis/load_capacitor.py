from numpy import*

from .utilities import*
from .cccap.cc_cap import* 
from .supercap import*

#load a single supercapacitor GDC txt file and save it in the Supercap class. First line being the header. The first coloumn is the elapsed time in second, the second coloumn is Voltage. 
#mass_ls is a list of two lists of the mass of each electrode
#if current is not entered, it is going to be generated from the filename (the file name has to include the current in mA, seperated by '/' or '_' and followed by '_mA')
#recieve mass and current in mg and mA respectively, output as mg and mA
def Load_capacitor(pathway, t_set = False, V_set = False, delimiter = False, mass_ls = False, current = False, row_skip = False, ESR_method = True, setting = False, cap_method = False, cap_grav = True):
    """
        Loading all relevant information of the measured supercapacitor the of the specified text file
        
        Parameters
        ----------
        pathway : :class:`str`
            The path in which the data files are located. 
            The current of each file has to be specified and seperated by either '/' or '_' and followed by '_mA' at the end
            Example: './folder_x/0.1_mA_GCD_sample_A.txt'
        
        t_set : :class:`int`, optional
            Specify the coloumn index for the time(s) data, coloumn 0 being the first coloumn starting from the left
            t_set = False (t_set = 0)
                    True (The prompt will ask for the column index to be entered)
                    : :class: `int` (specify the coloumn which will be used as time)
        
        V_set : :class:`int`, optional
            Specify the coloumn index for the volatge(V) data, coloumn 0 being the first coloumn starting from the left
            V_set = False (V_set = 0)
                    True (The prompt will ask for the column index to be entered)
                    : :class: `int` (specify the coloumn which will be used as voltage)
                    
        delimiter : :class:`str`, optional
            The symbol which seperates one data coloumn from the other. If delimiter = False, the delimiter is assumed to be space ''.
                    
        mass_ls : :class:`list`
            Measurements of the mass of each electrode. mass_ls will result in non-gravimetric capacitance being calculated. 
            mass_ls = False (calculate non-gravimetric capacitance)
                    = [[List of mass measurements for electrode 1], [List of mass measurements for electrode 2]]    
                          (calculate gravimetric capacitance)  
        
        current : :class:`float`, optional
            The current for the GCD analysis. If current = False, the program will attempt to extract the current value from the file name.
        
        row_skip : :class:`int`, optional
            The number of rows of headers to skip in the text files.
            row_skip = False (row_skip = 1)
                     = : :class:`int` (The specified number of rows will be skipped for all files in the path)
        
        ESR_method : :class:`int`, optional
            The method for ESR analysis.
            ESR_method = 1 (default constant point analyis using the first point after the peak for calculating voltage drop) 
                       = 101 (constant point analysis using the nth point after the peak, where n is specified using setting)
                       = 2 or True (default constant second derivative method using the point where the second derivative is greater than 0.01)
                       = 201 (constant second derivative method where the cut off derivative is specified using setting)
                       = False (ESR value will be returned as False)
                       
        setting : :class:`int`, optional
            The cut off second derivative or the cut off number of points used for ESR determination.
            setting = False (setting = 1 by default)
                       
        cap_method : :class:`int`, optional
            The method for capacitance analysis. 
            cap_method = 1 or False (the capacitance is analysed from the lower half of the voltage range)
            cap_method = 2 (the capacitance is analysed from the upper half of the voltage range)
                       
        cap_grav : :class:`bool` 
            cap_grav = True, output gravimetric capacitance
            cap_grav = False, output non-gravimetric capacitance

        returns
        -------
        : :class:`list, list` 
            [list of current density], [list of Supercap classes for each current density], [list of peak indices]
                
            
    """
    if current is False:
        current = Readcurrent(pathway)
        if current is False:
            current = float(input('Missing current argument. Please include the current argument in mA:'))
    else:
        pass

    
    if row_skip is False:
        row_skip = 1
    elif row_skip is True:
        row_skip = int(input('Please enter the number of header row(s) in this file:'))
    else:
        pass
    
    
    GDC = Fast_load(pathway, skip_header = row_skip, t_set = t_set, V_set = V_set, delimiter = delimiter)
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
        
    if mass_ls != False and cap_grav is False:
        print('Mass of electrodes presents. Non-gravimetric capacitance is returned')
    elif mass_ls is False and cap_grav is True:
        print('Mass of electrodes absents. Non-gravimetric capacitance is returned')
    else:
        pass
    
    
    if ESR_method == 101 and setting is False:
        setting = int(input('How many points after the peak would you like to be considered for the ESR analysis? (the default value is 1)'))
        
    elif ESR_method == 201 and setting is False:
        setting = float(input('Please specify a cut-off derivative (the default value is 1)'))

    else:
        pass

    
    if ESR_method is 1:
        setting = 1
    elif ESR_method is 2:
        setting = 0.01
    else:
        pass
    
    
    if cap_method is False:
        cap_method = 1
    elif cap_method is True or cap_method not in [1, 2]:
        cap_method = int(input('Please enter the desired capacitance analysis method. (1 or 2)'))
    else:
        pass

    
    cap_data = CC_Cap(GDC_t, GDC_V, current, mm1, mm2, ESR_method= ESR_method, setting = setting, cap_method = cap_method, cap_grav = cap_grav)
    
                      
    return Supercap(current, [GDC_t, GDC_V], [[mm1, std1],[mm2, std2]], cap_data[0], cap_data[1], [cap_data[2], cap_data[3]], cap_data[4], error, [ESR_method, setting], cap_method, cap_data[5])