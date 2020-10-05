from scipy.integrate import simps
from sklearn.metrics import auc
from scipy.signal import find_peaks
from numpy import*

#Read the scan rate in a file name.
#In the filename, the scan rate is stated at the very front of the file, OR
#the scan rate seperated from other elements of the filename and/or seperated by '_' and/or '/'
#current needs to end with '_mvs'
def Read_scan_r(filename):
    for i in range(len(filename)-2):
        if filename[i:i+2] == 'mvs':
            k = i-2
            while filename[k] != '_' and filename[k] != '/' and filename[k] != '\\' and k >= 0:
                k -= 1
            return float(filename[k+1:i-1])


def Pos_split(x, y):

    x_split1=[]
    y_split1=[]
    x_split2=[]
    y_split2=[]
    
    i=0
    max_x = max(x)
    while x[i] < max_x:
        i += 1
        
    x_split2 = x[:i]
    y_split2 = y[:i]
    x_split1 = x[i:]
    y_split1 = y[i:]

    return x_split1, y_split1, x_split2, y_split2


def Neg_split(x, y):

    x_split1=[]
    y_split1=[]
    x_split2=[]
    y_split2=[]
    
    i=0
    while x[i] < max(x):
        i += 1
    
    x_split1 = x[:i]
    y_split1 = y[:i]
    x_split2 = x[i:]
    y_split2 = y[i:]

    return x_split1, y_split1, x_split2, y_split2


def Trapz_area(x_split1, y_split1, x_split2, y_split2):

    try:
        status = 0
        area2 = auc(x_split2, y_split2)
        area1 = auc(x_split1, y_split1)
        
    except: 
        status = 1
        x_split2 = linspace(x_split2[0], x_split2[-1], len(x_split2))
        x_split1 = linspace(x_split1[0], x_split1[-1], len(x_split1))
        bigger_area = auc(x_split2, y_split2)
        smaller_area = auc(x_split1, y_split1)
        
    return bigger_area-smaller_area, status


def Simps_area(x_split1, y_split1, x_split2, y_split2):
    x_split1 = splitted[0]
    y_split1 = splitted[1]
    x_split2 = splitted[2]
    y_split2 = splitted[3]
    
    dx1 =(max(x_split1)-min(x_split1))/len(x_split1)
    dx2 =(max(x_split2)-min(x_split2))/len(x_split2)
    area2 = simps(y_split2, dx=dx2)
    area1 = simps(y_split1, dx=dx1)
    
    return area2 - area1


def Load_cycle(CV_x, CV_y):
    mini, _= find_peaks(-CV_x, prominence = 0.1)
    
    comb_ls = []
    cycle_xls=[]
    cycle_yls=[]
    
    for i in range(len(mini)-1):
        comb_ls += [[mini[i],mini[i+1]]]
        
    for i in comb_ls:
        cycle_xls += [CV_x[i[0]:i[1]]]
        cycle_yls += [CV_y[i[0]:i[1]]]
    return cycle_xls, cycle_yls, len(cycle_xls)
    
    
    

def Pn_slice(cycle_xls, cycle_yls, cycle_n):
    y_pos = []
    x_pos = []
    y_neg = []
    x_neg = []
    
    for i in range(cycle_n):
        cond_p = [yi > 0 for yi in cycle_yls[i]]
        y_pos += [cycle_yls[i][cond_p]]
        x_pos += [cycle_xls[i][cond_p]]
        
        cond_n = [yi < 0 for yi in cycle_yls[i]]
        y_neg += [cycle_yls[i][cond_n]]
        x_neg += [cycle_xls[i][cond_n]]
        
    return x_pos, y_pos, x_neg, y_neg, cycle_n


###scan rate in mv/s and mass in mg!!!
def CV_cap_cal(Integrated, m1, m2, scan_r, potential_r):
    return 1000000 * Integrated * (m1 + m2) / (m1*m2*scan_r)*potential_r