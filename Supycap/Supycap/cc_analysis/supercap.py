from numpy import*
from matplotlib import* 
from matplotlib import pylab, mlab, pyplot
from matplotlib.font_manager import FontProperties
from pylab import*
from scipy.signal import find_peaks
from IPython.core.pylabtools import figsize, getfigs

from .cccap.utilities import ConstantDeriv, ConstantPoints, ESR_ls, ESR_dv2, Half_pt_ind, Cap_ls



#accept current in mA, output current in mA. 
#accept masses in mg, output in mg
#The capacitpor is assumed to be the 2-electrode type and symmertric (the two electrodes can have different masses)
class Supercap():
    """
    Stores all relevant information for the capacitance/ESR analysis of the supercapacitor
    
    Available methods
    -----------------
    __init__
    __repr__
    ESR_method_change
    Show_dV2
    Cap_vs_cycles
    Get_info
    Check_analysis
    
    """

 
    
    def __init__(self, current,  t_V_ls, masses, cap_ls, esr_ls, extrema, cycle_n, m_error, ESR_method, cap_method, faulty_cycles):
        """
        Initialize a :class:`.Supercap`.
        
        
        Notes
        -----
        All current values are in mA
        All mass values are in mg 
        
       
        Parameters
        ----------
        current : :class:`float`
            Current at which the GCD analysis is undertaken. The current is in mA.    
        
        t_V_ls : :class:`list`
            The raw data of the GCD analysis
            Input:[[list of time readings], [list of voltage readings]]  
        
        masses : :class:`list`
            The mass measurements for the two electrodes. The mass is in mg.
            Input:[[average mass of m1, std of m1], [average mass of m2, std of m2]]

        cap_ls : :class:`list`
            The calculated capacitance for each cycle
            input: [list of calculated capacitance for each cycle]

        esr_ls : :class:`list`
            The calculated ESR values for each cycle
            input: [list of calculated ESR value for each cycle]   
 
        extrema : :class:`list`
            The indices for the peaks and troughs of the voltage readings
            input: [[peak indices], [trough indices]] 
            
        cycle_n : :class:`int`
            Number of cycles conducted
            input: number of cycles

        m_error : :class:`list` 
            The uncertainty for each calculated capacitance value
            input: [list of uncertainties]            

        ESR_method : :class:`int`
            The method for ESR analysis
            ESR_method = 1/102/2/202

        cap_method : :class:`int`
            The method for capacitance analysis
            cap_method = 1/2
            
        faulty_cycles : :class:`list`
            A list of cycle numbers for the faulty cycles
            input: [list of faulty cycle numbers]
            
       """
        
        self.current = current
        self.masses = masses #output as: [average mass of m1, std of m1], [average mass of m2, std of m2]
        self.t_ls = t_V_ls[0]
        self.V_ls = t_V_ls[1]
        self.cap_ls = array(cap_ls)
        self.esr_ls = array(esr_ls)
        self.cycle_n = int(cycle_n) #has to be an interger value!
        self.error = m_error #only mass error is considered
        self.peaks = extrema[0] #output the indices of all the peaks in the dataset
        self.troughs = extrema[1] #output the indices of all the troughs in the dataset
        self.esr_method = ESR_method#[ESR method, setting]
        self.cap_method = cap_method
        self.faulty_cycles = array(faulty_cycles)+1 #cycle number for the faulty cycles (starting from 1)
        
    def __repr__(self):
        """
        Initialize a :class:`.Supercap`.
        
        Return
        -----
        Returns a string which state the current, maximum voltage and number of cycle analysed in the Supercap class
        
        """
        peak_step = int(floor(len(self.peaks)/10))+1
        ave_peak = mean(self.V_ls[self.peaks[::peak_step]])
        
        return f'<Class_{self.__class__.__name__}: {self.current} mA, max voltage {round(ave_peak,2)} V, {self.cycle_n} cycle(s), ESR method {self.esr_method[0]} (setting = {self.esr_method[1]}), cap_method {self.cap_method}>'
    
    def ESR_method_change(self, ESR_method = True, setting = False):
        """
        Initialize from a :class:`.Supercap`.
        
        
        Notes
        -----
        Changing the ESR analysis method used for calculating esr_ls      
       
        Parameters
        ----------
        ESR_method : :class:`int`, optional
            The method for ESR analysis.
            ESR_method = 1 (default constant point analyis using the first point after the peak for calculating voltage drop) 
                       = 101 (constant point analysis using the nth point after the peak, where n is specified using setting)
                       = 2 or True (default constant second derivative method where the cut off second derivative is greater than 1)
                       = 201 (constant second derivative method where the cut off derivative is specified using setting)
                       
        setting : :class:`float`, optional
            The setting for ESR analysis
            setting = False for ESR_method = 1, 2 or True
            setting = nth point/cut off second derivative depending on the ESR_method

        Return 
        ------
        :class:`.Supercap`
            self.esr_ls        
        
        """
        print('The original ESR method is', self.esr_method[0], ', and the setting is', self.esr_method[1])
        
        if ESR_method is True:
            ESR_method = 2
            print('ESR method is changed to the default constant second derivative analysis, where the cut off second derivative is 1')
        elif ESR_method is False:
            print('ESR calculation is turned off')
        else:
            pass
        
        if ESR_method is 101 and setting is False:
            setting = int(input('How many points after the peak would you like to be considered for the ESR analysis? (the default value is 1)'))
        
        elif ESR_method is 201 and setting is False:
            setting = float(input('Please specify a cut-off derivative (the default value is 1)'))
            
        elif ESR_method is 1:
            setting = 1
       
        elif ESR_method is 2:
            setting = 1
            
        else:
            pass
        
        if ESR_method is 1 or ESR_method is 101:
            esr_v = [ConstantPoints(self.V_ls, self.peaks[i], set_n = setting) for i in range(self.cycle_n)]
      
        elif ESR_method is 2 or ESR_method is 201:
            esr_v = [ConstantDeriv(self.t_ls, self.V_ls, self.peaks[i], self.troughs[i], set_deriv = setting) for i in range(self.cycle_n)]
                      
        else:
            esr_v = False
        
            
        self.esr_ls = array(ESR_ls(esr_v, self.current*10**(-3)))
        self.esr_method=[ESR_method, setting]
        
        return self.esr_ls
        
        
    def Cap_method_change(self, cap_method = False, cap_grav = True, m1 = False, m2 = False):
        print('The original cap_method is {}'.format(self.cap_method))
        
        if cap_method is False:
            cap_method = int(input('Please enter the desired cap_method: (1/2)'))
        print('The cap_method is changed to {}'.format(cap_method))

        if cap_grav is True:
            print('Gravimetric capacitance (F g^-1) is being calculated.')
            if m1 is False or m2 is False:
                if mean(self.masses[0]) == False or  mean(self.masses[1]) == False:
                    print('electrode masses are missing for the gravimetric capacitance calculation.')
                    m1 = float(input('Please enter the mass of one of the electrode (mg):'))
                    m2 = float(input('Please enter the mass of the other electrode (mg):'))
                   
                else:
                    print('Electrode masses are taken as specified previously.')
                    m1 = mean(self.masses[0])
                    m2 = mean(self.masses[1])
                    
            else:
                pass
        else:
            print('Non-gravimetric capacitance (F) is being calculated.')
                       
        mid_ind = [Half_pt_ind(self.V_ls[self.peaks[i]:self.troughs[i]],(self.V_ls[self.peaks[i]]+self.V_ls[self.troughs[i]])/2) for i in range(len(self.peaks))]
    
        cc_grad = []
        faulty_cyc_ind = []
        for i in range(len(self.peaks)):
            if i<=10:
                sel_peaks = self.peaks[:10]
                ave_len = mean([len(self.t_ls[self.peaks[k]:self.troughs[k]]) for k in range(len(sel_peaks))])
            else:
                ave_len = mean([len(self.t_ls[self.peaks[k]:self.troughs[k]]) for k in range(i-10, i)])
            
            if len(self.t_ls[self.peaks[i]:self.troughs[i]]) < ave_len*0.5:
                faulty_cyc_ind += [i]
                print('Cycle ' + str(i+1)+ ' has insufficient data points (50% less than average). Skipped for capacitance calculation') 
            
            elif len(self.t_ls[self.peaks[i]:self.troughs[i]]) > ave_len*1.5:
                faulty_cyc_ind += [i]
                print('Cycle ' + str(i+1)+ ' has significantly more data points (50% more than average). Skipped for capacitance calculation') 
        
            else:
                if cap_method is 1 or cap_method is False:
                    try:
                        cc_grad += [polyfit(self.t_ls[self.peaks[i]:self.troughs[i]][mid_ind[i]:], self.V_ls[self.peaks[i]:self.troughs[i]][mid_ind[i]:],1, cov=False)[0]]
                    except:
                        faulty_cyc_ind += [i]
                        print('Error found in cycle ' + str(i+1)+ '. Skipped for capacitance calculation')
                  
                elif cap_method is 2:
                    try:
                        cc_grad += [polyfit(self.t_ls[self.peaks[i]:self.troughs[i]][:mid_ind[i]], self.V_ls[self.peaks[i]:self.troughs[i]][:mid_ind[i]],1, cov=False)[0]]
                    except:
                        faulty_cyc_ind += [i]
                        print('Error found in cycle ' + str(i+1)+ '. Skipped for capacitance calculation')  
  
        if cap_grav is True:
            cap_ls_calc = Cap_ls(cc_grad, self.current*10**(-3), m1*10**(-3), m2*10**(-3))
        
        else:
            cap_ls_calc = Cap_ls(cc_grad, self.current*10**(-3), cap_grav = False)
        
        self.cap_ls = array(cap_ls_calc)
        self.cap_method = cap_method
        
        return self.cap_ls
        
    
        
    
    #For visualising the second derivative for method 2 and/or method 201 and manually changing the second derivative cutt off point
    def Show_dV2(self, cycle_check = False, zoom_in = False):
        """
        Initialize from a :class:`.Supercap`.
           
        Notes
        -----
        Visualising the second derivative and the charge/discharge curve of a specified cycle with the option of changing the ESR analysis method used for calculating esr_ls      
       
        Parameters
        ----------
        cycle_check : :class:`int`, optional
            The method for ESR analysis.
            Specify the cycle of the charge/discharge curve and the second derivative to be plotted on the same axes
            input: a interger between 0 and the total number of cycles
              
        setting : :class:`float`, optional
            The setting for ESR analysis
            setting = the cut off second derivative being used in the ESR_method. (setting = 1 for ESR_method = 1 or 2)

        Return 
        ------
        A plot of charge discharge curve and the corresponding second derivative
        :class:`.Supercap`, optional
            self.esr_ls           

        """
        
        if self.esr_method[0] != 2 and self.esr_method[0] != 201:
            print('The current ESR method is neither 2 or 201. Please change the ESR method to constant second derivative analysis using .ESR_method_change().')
            return False
        else:
            pass
        
        if cycle_check is False:
            cycle_check = int(input('Of which cycle would you like to see the second derivative? enter a number between 1 and '+str(self.cycle_n)))
        else:
            pass 
        
        proceed = True
        cycle_check -= 1
        
        while proceed is True:
            if cycle_check in self.faulty_cycles:
                cycle_check = int(input('The cycle enteres is a faulty cycle. Please enter another number between 1 and '+str(self.cycle_n)))
                cycle_check -= 1
            else:
                proceed = False

        
        setting = self.esr_method[1]
        while proceed is False:
            print('The cut off second derivative currently being used is '+str(setting))
            esr_dV2 = [ESR_dv2(self.t_ls, self.V_ls, self.peaks[i], self.troughs[i], set_deriv = setting)[1] for i in range(self.cycle_n)]
            num_pt = [ESR_dv2(self.t_ls, self.V_ls, self.peaks[i], self.troughs[i], set_deriv = setting)[2] for i in range(self.cycle_n)]
        
            peak1 = self.peaks[cycle_check]
            trough1 = self.troughs[cycle_check]
            num1 = num_pt[cycle_check]
            dV_ls1 = esr_dV2[cycle_check]
            t_ls1 = array(self.t_ls[peak1:trough1])-self.t_ls[peak1]
            V_ls1 = self.V_ls[peak1:trough1]
            
            if zoom_in is False:
                zoom_in = int(floor(len(t_ls1)/2))
            

            figure(figsize(20,15))
            fig, ax1 = plt.subplots()
            
            font = FontProperties()
            font.set_family('sans-serif')
            font.set_name('Arial')
            font.set_size(35)

            color = 'tab:red'
            ax1.set_xlabel('Time (s)', fontproperties=font)
            ax1.set_ylabel('Second derivative $ dV^2/dt $', color=color, fontproperties=font)
            ax1.plot(t_ls1[1:zoom_in-2], dV_ls1[:zoom_in-3], linewidth=5, marker='x', ms=12, mew=5, color=color)
            ax1.plot(t_ls1[num1+2], dV_ls1[num1+1], linewidth=5, marker='x', ms=20, mew=6, color='g')
            ax1.tick_params(axis='y', labelcolor=color)
            

            ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
            color = 'tab:blue'
            ax2.set_ylabel('Voltage (V)', color=color, fontproperties=font)  # we already handled the x-label with ax1
            ax2.plot(t_ls1[:zoom_in-2], V_ls1[:zoom_in-2],  linewidth=5, marker='x',ms=12, mew=5, color=color)
            ax2.plot(t_ls1[num1+1], V_ls1[num1+1],  linewidth=5, marker='x',ms=20, mew=6, color='g')
            ax2.tick_params(axis='y', labelcolor=color)


            ax = gca()
            for label in ax1.get_xticklabels() + ax1.get_yticklabels()  + ax2.get_yticklabels():
                label.set_fontsize(30)
                label.set_family('sans-serif')
                label.set_name('Arial')
            
            show()
            
            opinion = input('Are you happy with the cut off point? (yes/no)')
            if opinion == 'yes':
                proceed = True 
                change_setting = input('Do you wish to change the cut off point to the current value? (setting =' + str(setting)+ ')[yes/no]')
                if change_setting == 'yes':
                    self.ESR_method_change(ESR_method = 201, setting = setting)
                    break
                    
            else:
                setting = float(input('Please input the value of desired cut off second derivative.'))
 

        
    #Tp plot capacitance against the number of cycles
    def Cap_vs_cycles(self, set_fig=False, save_fig=False):
        """
        Initialize from a :class:`.Supercap`.
        
        
        Notes
        -----
        Plotting capacitance against cycle and saving it as 'current mA_cap_vs_cycles_datetime.png'
        
        Parameter
        ----------
        set_fig : :class:`bool`, optional
            Changing the setting of the figure

        save_fig : :class:`bool`, optional
            whether the figure will be saved

        Return 
        ------
        A figure of capacitance over cycle number
        
        """
        
        if set_fig ==True:
            length = float(input('Please input length for the figure:'))
            width = float(input('Please input width for the figure:'))
            label_size = float(input('Please input the font size for the figure:'))
            lw = float(input('Please input the line width for the figure:'))
            clr = input('Please input the line colour for the figure:')
        else: 
            length = 20
            width = 15
            label_size = 40
            lw =5
            clr = 'black'
        
        figure(figsize(length,width))
        ax = gca()
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontsize(label_size)
            label.set_family('sans-serif')
            label.set_name('Arial')
            
            
        tx = ax.yaxis.get_offset_text()
        tx.set_fontsize(label_size)
        tx.set_family('sans-serif')
        tx.set_name('Arial')
        
       
        font = FontProperties()
        font.set_family('sans-serif')
        font.set_name('Arial')
        font.set_size(label_size + 10)
        
        xlabel('Number of cycles', fontproperties=font)        
        if self.error is False:
            ylabel('Non-gravimetric capacitance $F$', fontproperties=font)
        else:
            ylabel('Capacitance $F g^{-1}$', fontproperties=font)

        plot(range(1, self.cycle_n-len(self.faulty_cycles)+1), self.cap_ls, color= clr , linewidth = lw)
        
        if save_fig is True:
            savefig(str(self.current)+'mA_cap_vs_cycles_'+'Date{0:%d%m}_Time{0:%I_%M}'.format(datetime.datetime.now())+'.png', transparent = True)
        else:
            pass
    
    #To get general info of the capacitance analysis
    def Get_info(self):
        """
        Initialize from a :class:`.Supercap`.
        
        Notes
        -----
        Printing the basic information of the Supercap class
        
        Parameter
        ----------
        None

        Return 
        ------
        :class:`string`, optional
            The number of cycles, the average capacitance, the std of capacitance, the average ESR and its std, the ESR_method and cap_method used.
        
        """
        
        print('The number of cycle(s) analysed is', self.cycle_n)
        print('The number of faulty cycle is', len(self.faulty_cycles))
        print('The average capacitance is', round(mean(self.cap_ls),4), 'F g^(-1)')
        print('The standard deviation of the average is', round(std(self.cap_ls),4))
        print('The average ESRs is', round(mean(self.esr_ls),4), 'Ohms')
        print('The standard deviation of the ESRs is', round(std(self.esr_ls),4))
        if self.cap_method is 1:
            print('Lower half of the voltage range in the discharge curve was used for capacitance calculations')
        else:
            print('Upper half of the voltage range in the discharge curve was used for capacitance calculations')
        if self.esr_method[0] is True or self.esr_method[0]==2 or self.esr_method[0] == 202:
            print('Constant second derivative method was used for ESR calculations')
        else:
            print('Constant point method was used for ESR calculations')
    
    #To check whether the code is running correctly by visualising a small section of the analysis
    def Check_analysis(self, begin = False, end = False, set_fig = False, save_fig = False):
        """
        Initialize from a :class:`.Supercap`.
        
        Notes
        -----
        Plotting the charge/discharge curve and visualising how the data is analysed (indicate the slope fitting for capacitance and the voltage drop for ESR)
        
        Parameter
        ----------
        begin: :class:`int`, optional
            The first cycle to be visualised
            
        end : :class:`int`, optional
            The last cycle to be visualised

        set_fig : :class:`bool`, optional
            Changing the setting of the figure

        save_fig : :class:`bool` or `str`, optional
            save_fig = False, the plot will not be saved 
            save_fig = True, the plot will be saved as 'Check_analysis_[datetime].png'
            save_fig = class:`str` , the plot will be saved as 'the input string.png'
            
            
        Return 
        ------
        A plot of the charge/discharge curve with liniearly fitted slope and voltage drop
        
        """
        
        if begin is False or end is False:
            print('Please enter the first cycle number for the check, the cycle number should be an interger between 1 and '+ str(self.cycle_n))

        if begin is False:
            begin = int(input('Please enter the first cycle number for the check'))
        else:
            pass
        
        
        if end is False:
            end = int(input('Please enter the last cycle number for the check'))
        else:
            pass 
        
        if set_fig ==True:
            length = float(input('Please input length for the figure:'))
            width = float(input('Please input width for the figure:'))
            label_size = float(input('Please input the font size for the figure:'))
            lw = float(input('Please input the line width for the figure:'))
            ms = float(input('Please input the marker size for the figure:'))
            mew = float(input('Please input the marker weight for the figure:'))
            degrees = float(input('Please input the rotation degrees for the x ticks:'))
        else: 
            length = 10
            width = 7
            label_size = 30
            lw = 5
            ms = 25
            mew = 5
            degrees = 45
        
        
        figure(figsize(length, width))
        ax = gca()
        for label in ax.get_xticklabels() + ax.get_yticklabels(): 
                label.set_fontsize(label_size)
                label.set_family('sans-serif')
                label.set_name('Arial')
                
        tx = ax.xaxis.get_offset_text()
        tx.set_fontsize(label_size)
        tx.set_family('sans-serif')
        tx.set_name('Arial')
        
        if begin is 1:
            plot(self.t_ls[0:self.troughs[end-1]], self.V_ls[0:self.troughs[end-1]], label=str(self.current)+' mA', linewidth=lw, c='black') 
        else:
            plot(self.t_ls[self.troughs[begin-2]:self.troughs[end-1]], self.V_ls[self.troughs[begin-2]:self.troughs[end-1]], label=str(self.current)+' mA', linewidth=lw, c='black')       
            
        mid_ind = [Half_pt_ind(self.V_ls[self.peaks[i]:self.troughs[i]],(self.V_ls[self.peaks[i]]+ self.V_ls[self.troughs[i]])/2) for i in range(len(self.peaks))]
        
        for i in range(begin-1, end):
            if i+1 in self.faulty_cycles:
                print('Cycle '+str(i+1)+' was skipped for calculation due to errors')
                
            else:
                peaki = self.peaks[i]
                troughi = self.troughs[i]
                ipeakx = self.t_ls[peaki]
                itroughx = self.t_ls[troughi]
                
                if self.cap_method is 1:
                    fit = polyfit(self.t_ls[peaki:troughi][mid_ind[i]:], self.V_ls[peaki:troughi][mid_ind[i]:],1, cov=True)[0]
                    fitx = linspace(ipeakx*0.8+itroughx*0.2, itroughx, 20)
                    fity = fitx*fit[0]+fit[1]  
                            
                    plot(fitx, fity, linewidth=lw, linestyle='--', color='red')
                    plot([ipeakx + 0.035*(itroughx-ipeakx)*(end-begin+1)]*100, linspace(self.V_ls[peaki], self.V_ls[peaki]-self.esr_ls[i]*2*self.current*10**(-3), 100), color='b', linewidth=lw, linestyle=':')
                    plot(ipeakx, self.V_ls[peaki]-self.esr_ls[i]*2*self.current*10**(-3), linestyle='', marker=1, ms=ms, mew=mew, color='b')
                    plot(ipeakx, self.V_ls[peaki], linestyle='', marker=1, ms=ms, mew=mew, color='b')
                    plot(self.t_ls[peaki:troughi][mid_ind[i]], self.V_ls[peaki:troughi][mid_ind[i]], linestyle='', marker='+', ms=ms, mew=mew, color='r')
                    plot(itroughx, self.V_ls[troughi], linestyle='', marker='+', ms=ms, mew=mew, color='r')
                    
                else:
                    fit = polyfit(self.t_ls[peaki:troughi][:mid_ind[i]], self.V_ls[peaki:troughi][:mid_ind[i]],1, cov=True)[0]
                    fitx = linspace(1.4*ipeakx-0.4*itroughx, ipeakx*0.45 + itroughx*0.55, 20)
                    fity = fitx*fit[0]+fit[1]  
                            
                    plot(fitx, fity, linewidth=lw, linestyle='--', color='red')
                    plot([ipeakx + 0.035*(itroughx-ipeakx)*(end-begin+1)]*100, linspace(self.V_ls[peaki], self.V_ls[peaki]-self.esr_ls[i]*2*self.current*10**(-3), 100), color='b', linewidth=lw, linestyle=':')
                    plot(ipeakx, self.V_ls[peaki]-self.esr_ls[i]*2*self.current*10**(-3), linestyle='', marker=1, ms=ms, mew=mew, color='b')
                    plot(ipeakx, self.V_ls[peaki], linestyle='', marker=1, ms=ms, mew=mew, color='b')
                    plot(self.t_ls[peaki:troughi][mid_ind[i]], self.V_ls[peaki:troughi][mid_ind[i]], linestyle='', marker='+', ms=ms, mew=mew, color='r')
                    plot(ipeakx, self.V_ls[peaki], linestyle='', marker='+', ms=ms, mew=mew, color='r')                    
        
        font = FontProperties()
        font.set_family('sans-serif')
        font.set_name('Arial')
        font.set_size(label_size + 5)
        
        xticks(rotation = degrees)
        xlabel('Time (s)', fontproperties = font)
        ylabel('Voltage (V)', fontproperties = font)
        font.set_size(label_size)
        legend(fontsize=label_size)
        
        if save_fig == True: 
            savefig('Check_analysis_'+'Date{0:%d%m}_Time{0:%I_%M}_'.format(datetime.datetime.now())+'.png', transparent=True)
        elif save_fig == False:
            pass   
        else:
             savefig(str(save_fig)+'.png', transparent=True)

####CHANGE CHECK ANALYSIS TO EXCLUDE WRONG DATA POINTS!