from .utilities import*


###y in mA, voltage in V, scan rate in mv/s!!!
#int_method = 1 or 2. 
## 1 (default) = Trapezoidal
## 2 = Simpson's
#area_method = 1 or 2. 
## 1 (default) = positive side and negative side calculated seperately
## 2 = positive side and negatiive side calculated in reversed manner 
#first cycle and last cycle are omitted as long as they are incomplete

def CV_calc(x, y, m1, m2, scan_r, int_method = False):
    """
        Calculate the gravimetric capacitance from every cycle of CV scans and output a list of calculated capacitance (F g^-1) for all cycles.
        
        Notes
        -----
        For the CV data, the unit is mA for current, V for voltage and mV/s for scan rate. The mass of the electrodes should be recorded in mg. The gravimetric capacitance is output in F g^-1. 
        
        Parameter
        ----------
        x : :class:`numpy.ndarray`
            The voltage readings in V. 
            
        y : :class:`numpy.ndarray`
            The current readings in mA. 
            
        m1 : :class:`float`
            The mass of electrode 1 of the supercapacitor. The mass is in mg.

        m2 : :class:`float`
            The mass of electrode 2 of the supercapacitor. The mass is in mg.
            
        scan_r : :class:`float`
            The scan rate for the CV measurement in mV/s/

        int_method : :class:`bool` or `int`, optional
            The method used for integration (Trapezoidal or Simpsons's rules)
            int_method = False or 1 (Integration using the trapezoidal rule)
            int_method = 2 (Integration using the Simpson's rule)
            
        Return 
        ------
        A list of gravimetric capacitance calculated from each CV cycle.
        
    """
        
    if int_method is False:
        int_method = 1
    elif int_method is True:
        int_method = int(input('Please select the method for integration (1 or 2):'))
    else:
        pass

    y = array(y)/1000
    cycles = Load_cycle(x,y)
    potential_r = (max(x)-min(x))
    x_pos, y_pos, x_neg, y_neg, cycle_n = Pn_slice(cycles[0], cycles[1], cycles[2])
    print(cycle_n, ' CV cycles are being analysed using integration method', int_method)
    
    area_ls = []
    sta = 0
    if int_method is False or int_method is 1:
        for i in range(cycle_n):
            pox1, poy1, pox2, poy2 = Pos_split(x_pos[i], y_pos[i])
            nex1, ney1, nex2, ney2 = Neg_split(x_neg[i], y_neg[i])
            a2, sta2 = Trapz_area(pox1, poy1, pox2, poy2)
            a1, sta1 = Trapz_area(nex1, ney1, nex2, ney2)
            area_ls += [a2-a1]
            sta += sta2 + sta1
            
        if sta != 0:
            print('slicing of x values has been unccessful for', sta/2, ' out of the total', cycle_n, 'cycles')
            print('x values are assumed to be evenly spaced from minimum to maximum voltage for those cycles')
            
        else:
            pass
            
    elif int_method is 2:
        for i in range(sliced_data[4]):
            pox1, poy1, pox2, poy2 = Pos_split(x_pos, y_pos)
            nex1, ney1, nex2, ney2 = Neg_split(x_neg, y_neg)
            a2 = Simps_area(pox1, poy1, pox2, poy2)
            a1 = Simps_area(nex1, ney1, nex2, ney2)
            area_ls += [a2-a1]
    
    else:
        method = int(input('''Integration method has to be either 1 (trapezoidal) or 2 (Simpson's)'''))
        CV_analysis(x,y,method = method)

    CV_ls = [CV_cap_cal(i, m1, m2, scan_r, potential_r) for i in area_ls]
    
    return CV_ls  
