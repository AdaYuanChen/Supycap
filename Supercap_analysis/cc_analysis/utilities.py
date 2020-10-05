from numpy import*
import pandas as pd

def Fast_load(path, skip_header, t_set = False, V_set = False, delimiter = False):
    if t_set is False:
        t_set = 0
    elif t_set is True:
        t_set = input('Please eneter the index of the coloumn for x values (staring from zero) or the name of the coloumn (for csv files only):')
    else:
        pass
    
    if V_set is False:
        V_set = 1
    elif V_set is True:
        V_set = input('Please eneter the index of the coloumn for y values (staring from zero) or the name of the coloumn (for csv files only):')
    else:
        pass
        
    
    if '.txt' in path:
        if delimiter == False:
            delimiter = None
        elif delimiter == True:
            delimiter = input('Please enter the delimiter')
        else:
            pass
        
        try:
            t_set = int(t_set)
            V_set = int(V_set)
        except:
            print('The indices for the x and y coloumns have to be integers!')
            t_set = int(input('Please eneter the index of the x coloumn (an INTEGER staring from zero)'))
            V_set = int(input('Please eneter the index of the y coloumn (an INTEGER staring from zero)'))
        with open (path, 'r') as f:
            file = [i.split(delimiter) for i in f][skip_header:]
            xset = [float(i[t_set]) for i in file]
            xset = array(xset)
            yset = [float(i[V_set]) for i in file]
            yset = array(yset)

    elif '.csv' in path:
        if delimiter == False:
            delimiter = ','
        elif delimiter == True:
            delimiter = input('Please enter the delimiter')
        else:
            pass
       
        file = pd.read_csv(path, skiprows = skip_header-1, delimiter = delimiter)
        try:
            indices = [int(t_set), int(V_set)]
            xset = pd.file.iloc[:, indices[0]].to_numpy()
            yset = pd.file.iloc[:,indices[1]].to_numpy()
        except:
            indices = [t_set, V_set]
            xset = pd.file[indices[0]].to_numpy()
            yset = pd.file[indices[1]].to_numpy()
        
    else:
        print('Unsupported format. The program only supports documents in txt and csv formats.')
               
    return xset, yset


#Read the current value in a file name.
#In the filename, the current is stated at the very front of the file 
#current needs to be seperated from other elements of the filename and/or seperated by '_' and '/'
#current needs to end with '_mA'
def Readcurrent(filename):
    for i in range(len(filename)-1):
        if filename[i] + filename[i+1] == 'mA':
            k = i-2
            while filename[k] != '_' and filename[k] != '/' and filename[k] != '\\' and k >= 0:
                k -= 1
            return float(filename[k+1:i-1])

#calculate mass errors as the major source of uncertainties in capacitance
#error analysis: only uncertainty from mass is considered as other errors are insignificant compare to this
def delt_m(m_1, m_2):
    m1 = mean (m_1)
    m2 = mean (m_2)
    d1 = std (m_1)
    d2 = std (m_2)
    p1 = d1/m1
    p2 = d2/m2    
    d1p2_1p2 = (d1**2 + d2**2)**0.5/(m1 + m2)
    d1t2_1t2 = (p1**2 + p2**2)**0.5
    return (d1t2_1t2**2 + d1p2_1p2**2)**0.5
    

