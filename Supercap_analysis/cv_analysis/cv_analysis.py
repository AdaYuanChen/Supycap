from ..cc_analysis.utilities import Fast_load
from .cv_calc import*

def CV_analysis(pathway, m1, m2, scan_r = False, row_skip = False, x_name = False, y_name = False, delimiter = False, int_method = False):
    """
        Calculate the gravimetric capacitance from every cycle of CV scans and output a list of calculated capacitance (F g^-1) for all cycles.
        
        Notes
        -----
        UNITS: current(mA), voltage (V), scan rate (mV/s), mass of the electrodes (mg), and capacitance (F g^-1). 
        The scan rate (mV/s) will be directly read from the filename (i.e. the fielname has to include the current followed by '_mvs' and seperated by '_', '/' or it is the first component of the filename).
        
        Parameters
        ----------
        pathway : :class:`str`
            The path in which the data files are located. 
            The scan rate of each file has to be specified and seperated by either '/' or '_' and followed by '_mvs' at the end, otherwise the scan rate needs to be input as scan_r
            Example: './CV_folder/1_mvs_0.8_V_CV.txt'

        m1 : :class:`float`
            The mass of electrode 1 of the supercapacitor. The mass is in mg.

        m2 : :class:`float`
            The mass of electrode 2 of the supercapacitor. The mass is in mg.

        scan_r : :class:`float`, optional
            The scan rate for the CV measurement in mV/s. If scan_r = False, the program will attempt to extract the scan rate from the file name, given that 
            
        delimiter : :class:`str`, optional
            The symbol which seperates one data coloumn from the other. If delimiter = False, the delimiter is assumed to be space ''.
        
        row_skip : :class:`int`, optional
            The number of rows of headers to skip in the text files.
            row_skip = False (row_skip = 1)
                     = : :class:`int` (The specified number of rows will be skipped for all files in the path)
                     
        x_name : :class:`int`, optional
            Specify the coloumn index for the voltage(V) data, coloumn 0 being the first coloumn starting from the left
            x_name = False (t_set = 0)
                    True (The prompt will ask for the column index to be entered)
                    : :class: `int` (specify the coloumn which will be used as current)
        
        y_name : :class:`int`, optional
            Specify the coloumn index for the current(mA) data, coloumn 0 being the first coloumn starting from the left
            y_name = False (V_set = 0)
                    True (The prompt will ask for the column index to be entered)
                    : :class: `int` (specify the coloumn which will be used as voltage)

        
        int_method : :class:`int`, optional
            The method for integration for the enclosed area.
            int_method = 1 or False (integration using trapezoidal rule) 
                       = 2 (integration using Simpson's rule)

                       
        returns
        -------
        : :class:`list
            A list of capacitance calculated from each CV cycle.
    """
    
    if scan_r is False:
        try:
            scan_r = Read_scan_r(pathway)
        except:
            print('Missing scan rate value. Please enter the scan rate for the CV analysis in mV/s:')
    else:
        pass
    
    if row_skip is False:
        row_skip = 1
    elif row_skip is True:
        row_skip = int(input('Please enter the number of header row(s) in this file:'))
    else:
        pass
    
    CV_raw = Fast_load(pathway, skip_header = row_skip, t_set = x_name, V_set = y_name, delimiter = delimiter)
    x = CV_raw[0]
    y = CV_raw[1]
    
    return CV_calc(x, y, m1, m2, scan_r, int_method = False) 