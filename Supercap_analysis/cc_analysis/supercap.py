from numpy import*
from matplotlib import* 
from matplotlib import pylab, mlab, pyplot
from pylab import*
from scipy.signal import find_peaks
from IPython.core.pylabtools import figsize, getfigs

from .cccap.utilities import ConstantDeriv, ConstantPoints, ESR_ls, ESR_dv2



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

 
    
    def __init__(self, current,  t_V_ls, masses, cap_ls, esr_ls, extrema, cycle_n, m_error, ESR_method):
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
        self.esr_method = ESR_method
        
    def __repr__(self):
        """
        Initialize a :class:`.Supercap`.
        
        Return
        -----
        Returns a string which state the current, maximum voltage and number of cycle analysed in the Supercap class
        
        """
        
        return f'<Class_{self.__class__.__name__}: {self.current} mA, {self.V_ls[self.peaks[0]]} V, {self.cycle_n} cycles, ESR method {self.esr_method}>'
    
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
                       = 2 or True (default constant second derivative method using the point where the second derivative is greater than 0.01)
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
        
        if ESR_method == 101 and setting is False:
            setting = int(input('How many points after the peak would you like to be considered for the ESR analysis? (the default value is 1)'))
        
        elif ESR_method == 201 and setting is False:
            setting = float(input('Please specify a cut-off derivative (the default value is 1)'))
            
        elif ESR_method == 1 or ESR_method == 2:
            setting = False
            
        else:
            pass
        
        if ESR_method == 1 or ESR_method == 101:
            esr_v = [ConstantPoints(self.V_ls, self.peaks[i], set_n = setting) for i in range(test_glob[1][0].cycle_n)]
      
        elif ESR_method is True or ESR_method == 2 or ESR_method == 201:
            esr_v = [ConstantDeriv(self.t_ls, self.V_ls, self.peaks[i], self.troughs[i], set_deriv = setting)[0] for i in range(self.cycle_n)]
                      
        else:
            esr_v = False
            
        self.esr_ls = array(ESR_ls(esr_v, self.current*10**(-3)))
  
  
    #For visualising the second derivative for method 2 and/or method 201 and manually changing the second derivative cutt off point
    def Show_dV2(self, cycle_check = False, setting = False):
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
            setting = the cut off second derivative depending on the ESR_method

        Return 
        ------
        A plot of charge discharge curve and the corresponding second derivative
        :class:`.Supercap`, optional
            self.esr_ls           

        """
        
        
        if cycle_check is False:
            cycle_check = int(input('Of which cycle would you like to see the second derivative? enter a number between 0 and '+str(self.cycle_n)))
        else:
            pass 
        
        proceed = False
        
        while proceed is False:
            print('The cut off second derivative currently being used is '+str(setting))
            esr_dV2 = [ESR_dv2(self.t_ls, self.V_ls, self.peaks[i], self.troughs[i], set_deriv = setting)[1] for i in range(self.cycle_n)]
            num_pt = [ESR_dv2(self.t_ls, self.V_ls, self.peaks[i], self.troughs[i], set_deriv = setting)[2] for i in range(self.cycle_n)]
        
            peak1 = self.peaks[cycle_check]
            trough1 = self.troughs[cycle_check]
            num1 = num_pt[cycle_check]
            dV_ls1 = esr_dV2[cycle_check]
            t_ls1 = self.t_ls[peak1:trough1]-self.t_ls[peak1]
            V_ls1 = self.V_ls[peak1:trough1]
            

            figure(figsize(30,20))
            fig, ax1 = plt.subplots()

            color = 'tab:red'
            ax1.set_xlabel('time (s)', fontsize=35)
            ax1.set_ylabel('Second derivative $ dV^2/dt $', color=color, fontsize=35)
            ax1.plot(t_ls1[1:40], dV_ls1[0:39], linewidth=5, marker='x', ms=12, mew=5, color=color)
            ax1.plot(t_ls1[num1+2], dV_ls1[num1+1], linewidth=5, marker='x', ms=20, mew=6, color='y')
            ax1.tick_params(axis='y', labelcolor=color)

            ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
            color = 'tab:blue'
            ax2.set_ylabel('Voltage (V)', color=color, fontsize=35)  # we already handled the x-label with ax1
            ax2.plot(t_ls1[:40], V_ls1[:40],  linewidth=5, marker='x',ms=12, mew=5, color=color)
            ax2.plot(t_ls1[num1+1], V_ls1[num1+1],  linewidth=5, marker='x',ms=20, mew=6, color='y')
            ax2.tick_params(axis='y', labelcolor=color)

            ax = gca()
            for label in ax1.get_xticklabels() + ax1.get_yticklabels()  + ax2.get_yticklabels():
                label.set_fontsize(30)
            
            show()
            
            opinion = input('Are you happy with the cut off point? (yes/no)')
            if opinion == 'yes':
                proceed = True 
                change_setting = input('Do you wish to change the cut off point to the current value? (setting =' + str(setting)+ ')')
                if change_setting == 'yes':
                    self.ESR_method_change(ESR_method = 201, setting = setting)
                    break
                    
            else:
                setting = float(input('Please input the value of desired cut off second derivative.'))
                    
        
    #Tp plot capacitance against the number of cycles
    def Cap_vs_cycles(self, set_fig=False):
        """
        Initialize from a :class:`.Supercap`.
        
        
        Notes
        -----
        Plotting capacitance against cycle and saving it as 'current mA_cap_vs_cycles_datetime.png'
        
        Parameter
        ----------
        set_fig : :class:`bool`, optional
            Changing the setting of the figure


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
            length = 60
            width = 20
            label_size = 30
            lw =5
            clr = 'black'
        figure(figsize(length,width))
        ax = gca()
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontsize(label_size)
        tx = ax.xaxis.get_offset_text()
        tx.set_fontsize(label_size)
        
        xlabel('Number of cycles', fontsize = label_size)        
        if self.masses[0][0] is False:
            ylabel('Non-gravimetric capacitance $F$', fontsize = label_size)
        else:
            ylabel('Capacitance $F g^{-1}$', fontsize = label_size)

        plot(range(1, self.cycle_n+1), self.cap_ls, color= clr , linewidth = lw)

        savefig(str(self.current)+'mA_cap_vs_cycles_'+'{0:%d%m}_{0:%I_%M}'.format(datetime.datetime.now())+'.png', transparent = True)
    
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
            The number of cycles, the average capacitance, the std of capacitance, the average ESR and its std 
        
        """
        
        print('The number of cycle(s) analysed is', self.cycle_n)
        print('The average capacitance is', mean(self.cap_ls), '$F g^{-1}$')
        print('The standard deviation of the average is', std(self.cap_ls))
        print('The average ESRs is', mean(self.esr_ls), '$\Omega $')
        print('The standard deviation of the ESRs is', std(self.esr_ls))       
    
    
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
            length = 30
            width = 20
            label_size = 60
            lw = 8
            ms = 50
            mew = 10
            degrees = 0
        
        
        figure(figsize(length, width))
        ax = gca()
        for label in ax.get_xticklabels() + ax.get_yticklabels():
                label.set_fontsize(label_size)        
        tx = ax.xaxis.get_offset_text()
        tx.set_fontsize(label_size)
        
        if begin is 1:
            plot(self.t_ls[0:self.troughs[end-1]], self.V_ls[0:self.troughs[end-1]], label=str(self.current)+' mA', linewidth=lw, c='black') 
        else:
            plot(self.t_ls[self.troughs[begin-2]:self.troughs[end-1]], self.V_ls[self.troughs[begin-2]:self.troughs[end-1]], label=str(self.current)+' mA', linewidth=lw, c='black')       
        for i in range(begin-1, end):
            peaki = self.peaks[i]
            troughi = self.troughs[i]
            ipeakx = self.t_ls[peaki]
            itroughx = self.t_ls[troughi]
            ind_mid = floor((peaki+troughi)/2)
            ind_mid = int(ind_mid)
            line_adj = (itroughx-ipeakx)*0.7
            
            fit = polyfit(self.t_ls[ind_mid:troughi], self.V_ls[ind_mid:troughi],1, cov=True)
            fitx = linspace(itroughx-line_adj,itroughx,20)
            fity = fitx*fit[0][0]+fit[0][1]  
                            
            plot(fitx, fity, linewidth=lw, linestyle='--', color='red')
            plot([ipeakx + 0.08*(itroughx-ipeakx)]*(end-begin+1)*100, linspace(self.V_ls[peaki], self.V_ls[peaki]-self.esr_ls[i]*2*self.current*10**(-3), 100), color='b', linewidth=lw, linestyle=':')
            plot(ipeakx, self.V_ls[peaki]-self.esr_ls[i]*2*self.current*10**(-3), linestyle='', marker=1, ms=ms, mew=mew, color='b')
            plot(ipeakx, self.V_ls[peaki], linestyle='', marker=1, ms=ms, mew=mew, color='b')
            plot(self.t_ls[ind_mid], self.V_ls[ind_mid], linestyle='', marker='+', ms=ms, mew=mew, color='r')
            plot( itroughx, self.V_ls[troughi], linestyle='', marker='+', ms=ms, mew=mew, color='r')
    
        xticks(rotation = degrees)
        xlabel('Time (s)', fontsize=label_size)
        ylabel('Voltage (V)', fontsize=label_size)
        legend(fontsize = label_size)
        
        if save_fig == True: 
            savefig('Check_analysis_'+'{0:%d%m}_{0:%I_%M}_'.format(datetime.datetime.now())+'.png', transparent=True)
        elif save_fig == False:
            pass   
        else:
             savefig(str(save_fig)+'.png', transparent=True)

