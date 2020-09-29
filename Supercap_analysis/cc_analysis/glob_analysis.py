from numpy import*
from matplotlib import* 
from matplotlib import pylab, mlab, pyplot
from pylab import*
from IPython.core.pylabtools import figsize, getfigs
import glob
from functools import reduce
import datetime

from .load_capacitor import Load_capacitor


#Analyse one supercapacitor under different currents (use multiple supercap()) with error bars
#path is directed to the folder which contains all relevant txt files for the analysis
#m1, m2 are recived in unit of mg 
def Glob_analysis(path, t_set = False, V_set = False, delimiter = False, mass_ls = False, row_skip = False, ESR_method = True, setting = False, plot_set = False, plotting = True):
    """
        Loading all text files in the folder as specified in path. Good for analysing how capacitance changes with current density. 
        
        Notes
        -----
        1. Capacitance and ESR analysis for one supercapacitor under different currents. 
        2. Error bars are calculated from the mass errors of the electrodoes as other errors are insignificant compared to that caused by mass. 
        3. The masses in mass_ls is in mg. 
        4. It is assumed that all data files in the folder are measured from the same capacitor, hence they all have the same mass_ls
        5. The current has to be included in the file name in the current format as specified under Parameters >> path
       
        Parameters
        ----------
        path : :class:`str`
            The path in which the data files are located. 
            The current of each file has to be specified and seperated by either '/' or '_' and followed by '_mA' at the end
            Example: './folder_x/0.1_mA_GCD_sample_A.txt'
            
       t_set : :class:`int`, optional
            Specify the coloumn index for the time(s) data, coloumn 0 being the first coloumn starting from the left
            t_set = False (t_set = 0)
                    True (The prompt will ask for the column index to be entered)
                    : :class: `int` (specify the coloumn which will be used as time)
        
        V_set : :class:`int`, optional
            Specify the coloumn index for the Volatge(V) data, coloumn 0 being the first coloumn starting from the left
            V_set = False (V_set = 0)
                    True (The prompt will ask for the column index to be entered)
                    : :class: `int` (specify the coloumn which will be used as time)
        mass_ls : :class:`list`
            Measurements of the mass of each electrode. mass_ls will result in non-gravimetric capacitance being calculated. 
            mass_ls = False (calculate non-gravimetric capacitance)
                    = [[List of mass measurements for electrode 1], [List of mass measurements for electrode 2]]    
                          (calculate gravimetric capacitance)                    
        
        row_skip : :class:`int`
            The number of rows of headers to skip in the text files.
            row_skip = False (The prompt will ask for rows to skip for each files)
                     = : :class:`int` (The specified number of rows will be skipped for all files in the path)
        
        ESR_method : :class:`int`, optional
            The method for ESR analysis.
            ESR_method = 1 (default constant point analyis using the first point after the peak for calculating voltage drop) 
                       = 101 (constant point analysis using the nth point after the peak, where n is specified using setting)
                       = 2 or True (default constant second derivative method using the point where the second derivative is greater than 0.01)
                       = 201 (constant second derivative method where the cut off derivative is specified using setting)
                       = False (ESR value will be returned as False)
                       
        setting : :class:`float`, optional
            The setting for ESR analysis
            setting = False (for ESR_method = 1, 2 or True, the defualt setting will be used)
                    = : :class:`int` (nth point/cut off second derivative depending on the ESR_method)
                    
        plotting : :class:`bool`, optional
            Whether the capacitance vs. current density plot will be saved
            plotting = False (the figure will not be saved)
                    =  True (the figure will be saved as 'Gravimetric specific capacitance vs. current density [datetime].png')

        returns
        -------
        : :class:`Supercap` 
                       
    """
    if row_skip is False:
        decision = input('''Do you want to enter the header's row number for each file individually? yes/no''')
        if decision == 'yes':
            pass
        else:
            row_skip = int(input('Please enter the number of row(s) of headers to skip for all files:'))
    else:
        pass 
    
    if ESR_method == 101 and setting is False:
        setting = int(input('How many points after the peak would you like to be considered for the ESR analysis? (the default value is 1)'))
        
    elif ESR_method == 201 and setting is False:
        setting = float(input('Please specify a cut-off derivative (the default value is 1)'))
    
    elif ESR_method == 1 or ESR_method == 2:
        setting = False

    else:
        pass
    
    #cap_norm setting
    if mass_ls is False:
        cap_norm = True
    else:
        cap_norm = False

    #print(ESR_method, 'glob')
    Glob_set = glob.glob(path)
    
    #loading data into the Supercap file 
    supc_ls = [Load_capacitor(i, t_set = t_set, V_set = V_set, delimiter = delimiter, mass_ls = mass_ls, row_skip = row_skip, ESR_method = ESR_method, setting = setting, cap_norm = cap_norm) for i in Glob_set]
        
    #Analyze each set of data
    Cap_ls_g = [mean(i.cap_ls) for i in supc_ls]
    Cap_error = [i.error for i in supc_ls]
    esr_data = [mean(i.esr_ls) for i in supc_ls]
    
    
    #plot set up
    if plot_set == False:
        width = 30
        length = 30
        font_size = 50
        line_colour = 'black'
        linewidth = 8
        error_bar = 6
        marker = 27
    if plot_set == True: 
        width = int(input('Please specify the width of the figure'))
        length = int(input('Please specify the length of the figure'))
        font_size = int(input('Please specify the font size'))
        line_colour = input('Please specify the colour of the plot')
        linewidth = int(input('Please specify the linewidth'))
        error_bar = int(input('Please specify the size of the error bars'))
        marker = int(input('Please specify the size of the markers'))
 
    #current density
    if mass_ls == False: 
        print('current density cannot be calculated, current (mA) is returned. Non-gravimetric capacitance is calculated.')
        Cd_ls =[i.current for i in supc_ls]
        x_lab = 'Current (mA)'
        y_lab = 'Non-gravimetric capacitance (F)'
        error_bar = 0
    
    else:
        Cd_ls =[i.current/(i.masses[0][0]+i.masses[1][0]) for i in supc_ls]
        x_lab = 'Current density $A g^{-1}$'
        y_lab = '$C_g /F g^{-1}$'
        
        
    #plotting
    if plotting == True: 
        figure(figsize(length, width))
        ax = gca()
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontsize(font_size)
        errorbar(Cd_ls, Cap_ls_g, yerr=Cap_error*array(Cap_ls_g), linewidth = linewidth, elinewidth = error_bar, capthick = error_bar, capsize = error_bar*3, ecolor = line_colour, marker ='x', color = line_colour, ms = marker, mew = marker/3)
        xlabel(x_lab, fontsize = font_size)
        ylabel(y_lab, fontsize = font_size)
        savefig('Gravimetric specific capacitance vs. current density'+' {0:%d%m}_{0:%I_%M}'.format(datetime.datetime.now())+'.png',transparent=True)
        
    else:
        pass
    
#function returns lists of current, current density, averaged capacitance, the standard deviation of capcitance, ESR average, and ESR std accordingly. 
    return Cd_ls, supc_ls

    