from numpy import*

#Capacitance timed 2 for symmetrical capacitor, given that the graident is obtained from the decreasing slope
#Recieve current in A and mass in g
def Cap_calc(grad, I, m1, m2):
    return (m1 + m2)*I/(m1*m2*-1*grad)


def Cap_norm(grad, I,):
    return I/(-1*grad)


#Calculating the capacitance given a list of gradients
#Recieve current in A and mass in g
def Cap_ls(gradient_ls, current, m1=False , m2=False, norm_cap=False):
    if norm_cap is False:
        cap_ls = [Cap_calc(i, current, m1, m2) for i in gradient_ls]
        
    elif m1 is False and m2 is False:
         cap_ls = [Cap_norm(i, current,) for i in gradient_ls]
            
    else:
        cap_ls = [Cap_norm(i, current) for i in gradient_ls]
        
    return cap_ls


#finding the intersect between a slope and a vertical line (3 methods available)
#method 0 (no longer used!!)
def Intersect(grad, intc, pk):
    return grad*pk+intc


#method 1 (first n point), at default the first 4 points after the peak are taken
def ConstantPoints(V_ls, pk_index, set_n = False):
    if set_n is False:
        dv = V_ls[pk_index]-V_ls[pk_index + 1]
        
    else:
        dv =V_ls[pk_index]-V_ls[pk_index + set_n]
                                
    return dv


#method 2 (2nd derivative cut off point)
def ConstantDeriv(xset, yset, pk_index, tr_index, set_deriv = False,):
    #calculaltion for first and second derivative
    dy = diff(yset[pk_index:tr_index], 1)
    dx = diff(xset[pk_index:tr_index], 1)
    dV1=dy/dx
    dt1 = 0.5*(xset[pk_index:tr_index][:-1]+xset[pk_index:tr_index][1:])
    
    dy2 = diff(dV1, 1)
    dx2 = diff(dt1, 1)
    dV2=dy2/dx2
    dt2 = 0.5*(dx[:-1]+dx[1:])
    
    if set_deriv is False:
        deriv = 1
    else:
        deriv = set_deriv
    
    num_pt=0
    for i in range(0, len(dV2)):
        if dV2[i] > deriv:
            num_pt = i
       
    dv = yset[pk_index] - yset[pk_index + 1 + num_pt]
    
    return dv, dV2 #num_pt
       

#receive current in A
def ESR_calc(dv, current):
    return dv/(2*current)


#calculate average ESR
#receive current in A
def ESR_ls(esr_ls, current):
    if esr_ls == False:
        return False
    
    else:
        esr=[ESR_calc(i, current) for i in esr_ls]
        
        return esr


def ESR_dv2(xset, yset, pk_index, tr_index, set_deriv = False):
    #calculaltion for first and second derivative
    dy = diff(yset[pk_index:tr_index], 1)
    dx = diff(xset[pk_index:tr_index], 1)
    dV1=dy/dx
    dt1 = 0.5*(xset[pk_index:tr_index][:-1]+xset[pk_index:tr_index][1:])
    
    dy2 = diff(dV1, 1)
    dx2 = diff(dt1, 1)
    dV2=dy2/dx2
    dt2 = 0.5*(dt1[:-1]+dt1[1:])
    
    if set_deriv is False:
        deriv = 0.01
    else:
        deriv = set_deriv
    
    num_pt=0
    for i in range(2, len(dV2)):
        if dV2[i] > deriv:
            num_pt = i
    
    return dt2, dV2, num_pt
