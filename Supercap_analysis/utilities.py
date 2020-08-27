from numpy import*

def Fast_load(path, skip_header = False):
    with open (path, 'r') as f:
        file = [i.split() for i in f][skip_header:]
        xset = [float(i[0]) for i in file]
        xset = array(xset)
        yset = [float(i[1]) for i in file]
        yset = array(yset)
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
    

