<img src="https://user-images.githubusercontent.com/70351473/103553331-39218300-4ea5-11eb-955f-54c553c1115b.png" alt="CC analysis" width="300" height="200">

<h1 class="title">
     Table of content
</h1>
<div id="TOC">
    <ul>
        <li>
            <a href="#introduction">Introduction</a>
        </li>
        <li>
            <a href="#Installation">Installation</a>
        </li>
        <li>
            <a href="#Documentations">Documentations</a>
        </li>
    </ul>
</div>

----
<div id="introduction">
    <h2>
        <a href="#TOC">Introduction</a>
    </h2>
    <p>
        Welcome to Supycap! This is a Python library for analysis for the Constant Current <b>(CC)</b> curves as well as the Cyclic Voltammetry <b>(CV)</b> curves of two-electrode, symmetrical supercapacitors. It provides an easy and standardised way to quickly extract useful information from the CC and CV data, including the <b>capacitance</b> and the Equivalent Series Resistance<b>（ESR) </b>of the supercapacitor and how they evolve over cycles, with multiple options offered to suit the need of scientific investigations of supercapacitors. 

<br>
<br>

### CC analysis
For <b>CC</b> analysis, the capacitance is calculated via linear fitting the second half of the discharging slope in each charging/discharging cycle. For <b>gravimetric capacitance, <img src="https://render.githubusercontent.com/render/math?math=C_g"> (<img src="https://render.githubusercontent.com/render/math?math=F%20g^{-1}">)</b>:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_g=%20\frac{m_1%2Bm_2}{m_1%20m_2}%20\frac{I}{\frac{dV}%20{dt}}">
</p>

<i>where <img src="https://render.githubusercontent.com/render/math?math=m_1"> is the mass of one of the two electrodes in the electrochemical cell and <img src="https://render.githubusercontent.com/render/math?math=m_2"> is the mass of the other, both in g; I is the current in A under which the CC anaysis is conducted; <img src="https://render.githubusercontent.com/render/math?math=\frac{dV}%20{dt}"> is the discharge slope, which is the change of voltage (V) with respect to time (s). </i>

<br>
<br>


For <b>non-gravimetric capacitance (F)</b>:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_{non}_{grav}=%20I%20\frac{1}{\frac{dV}%20{dt}}">
</p>

<i>where I is the current in A and <img src="https://render.githubusercontent.com/render/math?math=\frac{dt}%20{dV}"> is the change of time (s) with respect to voltage (V).</i>

<br>
<br>


The <b>ESR (Ω)</b> is calculated using the voltage drop:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=ESR=%20\frac{\Delta%20V_{drop}}{2%20I}">
</p>

<i>where <img src="https://render.githubusercontent.com/render/math?math=\Delta%20V_{drop}"> is the vertical drop in voltage in V at the beginning of the discharging curve as shown in the figure below; I is the current in A under which the CC analysis is conducted. </i>

<br>
<br>


Here is an illustration of how the CC data is analysed: 

<p align="center">
<img src="https://user-images.githubusercontent.com/70351473/103138710-2ea90180-46cd-11eb-9508-913085b99f34.png" alt="CC analysis" width="650" height="400">
</p>

<br>
<br>
<br>

### CV analysis
For <b>CV</b> analysis, the capacitance is calculated via integration of the area enclosed by current as the voltage scanned across the potential window. For <b>gravimetric capacitance (<img src="https://render.githubusercontent.com/render/math?math=F%20g^{-1}">)</b>:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_g=%20\frac{m_1%2Bm_2}{m_1%20m_2}%20\frac{I}{\frac{dV}%20{dt}}%20\frac{1}{\Delta%20V}%20\int_{V_0}^{V_1}%20I%20dV">
</p>

<i>where <img src="https://render.githubusercontent.com/render/math?math=m_1"> is the mass of one of the two electrodes in the electrochemical cell and <img src="https://render.githubusercontent.com/render/math?math=m_2"> is the mass of the other, both in g; <img src="https://render.githubusercontent.com/render/math?math=\frac{dV}{dt}"> is the CV scan rate in <img src="https://render.githubusercontent.com/render/math?math=V s^{-1}">; <img src="https://render.githubusercontent.com/render/math?math=\Delta V"> is the full discharge voltage in V; <img src="https://render.githubusercontent.com/render/math?math=V_0"> and <img src="https://render.githubusercontent.com/render/math?math=V_1"> are the voltages in V at the start of discharge and at the end of discharge, respectively.</i>

<br>
<br>

An illustration of how the CV data is analysed is shown below:

<p align="center">
<img src="https://user-images.githubusercontent.com/70351473/103149865-ac205080-4765-11eb-8832-abab45c0194d.png" alt="CV analysis" width="550" height="400">
</p>



</div>


----
<div id="Installation">
    <h2>
        <a href="#TOC">Installation</a>
    </h2>
    <p>
        <b>Method 1</b>: Please follow the instruction under the 'code' tab.
       <br>
       <br>
<b>Method 2</b>: Alternatively, the library can be directly downloaded from PyPI (https://pypi.org/project/Supycap/) using the following command in terminal:

```python
 pip install Supycap
 ```
                  
   </p>
</div>

-----

<div id="Documentations">
    <h2>
        <a href="#TOC">Documentations</a>
    </h2>
    <p>
        This python library offers means to analyse CC data and CV data in the format of text files or csv files, which can be directlt exported from electrochemistry software such as <code>EC Labs</code>. For <b>CC analysis</b>, the program recognises the first data coloumn as time (s) and the second coloumn as voltage (V) by default. For <b>CV analysis</b>, the program recognises the first data coloumn as voltage (V) and the second coloumn as current (mA) by default. However, the optional arguments, such as <code><i>t_set, V_set, delimeter and row_skip</i></code> for CC analysis and <code><i>V_set, I_set, delimeter and row_skip</i></code> for CV analysis, offers flexibility in dealing with more complex data files which do not meet the default format. For more information, please refer to the documentation for <a href="#Load_capacitor"><b>Load_capacitor</b></a> and <a href="#CV_analysis"><b>CV_analysis</b></a>, respectively. The documentation includes two parts: <b>CC analysis </b>and <b>CV analysis</b>. <b>CC analysis</b> is further divided into </b>Loading data</b>, which are means for loading data into the Supercap class, and <b>Supercap class</b>, which are methods within the Superclass for extracting data from the analysis. 
    </p>
</div>

<br>

<div id="sub_TOC">

### CC analysis
#### <b>Loading data</b>
 * <a href="#Load_capacitor">__Load_capacitor__</a>
 * <a href="#Glob_analysis">__Glob_analysis__</a>
#### <b>Supercap class</b>
 * <a href="#__init__">__init__</a>
 * <a href="#__repr__">__repr__</a>
 * <a href="#ESR_method_change">__ESR_method_change__</a>
 * <a href="#Cap_method_change">__Cap_method_change__</a>
 * <a href="#Show_dV2">__Show_dV2__</a>
 * <a href="#Cap_vs_cycles">__Cap_vs_cycles__</a>
 * <a href="#Get_info">__Get_info__</a>
 * <a href="#Check_analysis">__Check_analysis__</a>
 * <a href="#Export">__Export__</a>
 

### CV analysis
 * <a href="#CV_analysis">__CV_analysis__</a>


<br>
<br>


---
---


<div id="Load_capacitor">
    
## <a href="#sub_TOC"><b>Load_capacitor</b><i>(pathway, t_set = False, V_set = False, delimiter = False, mass_ls = False, current = False, row_skip = False, ESR_method = True, setting = False, cap_method = False, cap_grav = True)</i></a> 
This function loads the txt/csv file specified on the pathway into the <b>Supercap</b> class ,where capacitance and ESR analysis will be carried out. All relevant information can be extracted from the init function.


### Notes
---
This function supports electrochemical data in either txt or csv format. In a txt file, it is by default that the first coloumn of the file is assumed to be time (s), and the second coloumn is assumed to be Voltage (V) for the CC analysis. The two coloumns are assumed to be seperated by space. However, the optional arguments, <i>t_set, V_set, delimeter and row_skip</i>, offers flexibility in dealing with more complex data files. 



### Parameters
---

#### Arguments
1. <b>pathway : <i>file, str, or pathlib.Path</i></b> <br>
    File, filename of the text file to read. Note that if the library is not allocated in the same directory as the file, the pathway to the file has to be given. For <b>``` current=False```</b>, current will be directly read from the filename (i.e. the fielname has to include the current followed by <code>'_mA'</code> and seperated by <code>'_'</code>, <code>'/'</code> or it is the first component of the filename). If current information cannot be obtained from the filename, the current has be specified via the <code>current</code> argument. For more details, refer to the Examples section. This function currently only supports data in the format of txt or csv. 


2. <b>t_set : <i>int/str(csv files only), optional</i></b> <br>
   An integer specifying the coloumn index for time(s) data, with the first coloumn being coloumn 0 starting from left. If t_set = False, column 0 will be used as time(s); if t_set = False, there will be prompt asking for time coloumn index to be entered.For csv files, the coloumn index can also be the name of the coloumn (e.g. <code>t_set = 'time(s)'</code>). 
   
   
3. <b>V_set : <i>int/str(csv files only), optional</i></b> <br>
   An integer specifying the coloumn index for voltage(V) data, with the first coloumn being coloumn 0 starting from left. If V_set = False, column 1 will be used as Voltage(V); if t_set = False, there will be prompt asking for voltage coloumn index to be entered. For csv files, the coloumn index can also be the name of the coloumn (e.g. <code>V_set = 'voltage(V)'</code>). 


4. <b>delimiter : <i>str, optional</i></b> <br>
    A string which is used to seperate the data coloumns in the data file. If <code>delimiter = False</code>, the delimiter is assumed to be space <code>' '</code>.


5. <b>mass_ls : <i>list, [[measurements of m1], [measurements of m2]], optional</i></b> <br>
   A list specifying the mass of each electrode in the format as shwon above. Multiple measurements for each electrode should be included for calculation of the uncertainty of the data. All masses should be recorded in <b>mg</b>. If mass_ls = False, a non-gravimetric capacitanc will be calculated and the function returns <i><code>[[False, False], [False, False]]</code></i> for the <code>.masses</code> method in the resulting Supercap entity (more details for extracting data from the Supercap class in <a href="#__init__">Supercap class>>init</a>


6. <b>current : <i> float, optional</i></b><br>
   If <b><code>current = False</code></b>, the current value will be directly read from the filename given that it is supplied in the format as specified above in the pathway section. If the current is not included the filename, it should be specified in the form of <code>current =<i>specified_current</i></code>. The current value should be recorded in <b>mA</b>.


7. <b>row_skip : <i>int, optional</i></b><br>
   Number of the rows of headers to skip in the txt files. If <b><code>row_skip = False</code></b>, row_skip = 1; if <b><code>row_skip = True</code></b>, a prompt will ask for rows to skip for the file. Enter <code>row_skip = 0</code> if no rows need to be skipped. 

<div id="ESR_para"></div>

8. <b>ESR_method : <i>int, optional</i></b><br>
   The method for ESR analysis. It is by default <b>(<code>ESR_method = True</code>)</b> that the ESR analysis will be carried out using method 2 (constant derivative). For all methods available please refer to the next session <a href="#method_table">ESR_method</a> table. <code>ESR_setting = False</code> will return <code>.esr_ls</code> as <b>False</b> in the Supercap class. Available ESR_methods are: <code>ESR_methods = True, False, 1, 101, 2, 201. </code>


9. <b>setting : <i>float, optional</i></b><br>
   For <code>ESR_methods = True, 1, or 2 </code>, <code>setting = False</code>. For <code>ESR_methods = 101 or 201 </code>, setting is required as the number of points n/second derivative cut off point needed for the constant point method and the constant derivative method, respectively. If <code>ESR_methods = 101 or 201 </code> but <code>setting = False</code>, the function will promt the user to choose a specific value for the ESR analysis before proceeding. 

<div id="cap_para"></div>

10. <b>cap_method : <i>int, optional</i></b><br>
    The method for capacitance analysis which determines whether the upper (cap_method = 2) or lower (cap_method = 1) half of the voltage range of the discharging curve will be used. By default <code>cap_set = False</code> and the program uses the lower half of the discharging curve. For detailed information please refer to the <a href="#cap_method_table">cap_method</a> table below. 


11. <b>cap_grav : <i>bool, optional</i></b><br>
   It is by default that the gravimetric capacitance is calculated. By using <code>cap_grav = False</code> or <code>mass_ls = False</code> , a non-gravimetric capacitance will be calculated. 

<div id="method_table">
</div>

#### <a href="#ESR_para"> ESR_method</a>

Method  |  Description  |
---   |  ---   | 
<b>True</b>   |  Default Method 2   |  
<b>False</b>   |  Returning ESR = False (no ESR calculation)   |  
<b>1</b>    |  Default Method 1. dV is calculatied using the voltage difference between the peak voltage and the fourth data point taken after the peak voltage is reached   |  
<b>101</b>    |  This method prompts the user to enter an interger n, where dV is determined between the peak voltage and the voltage of the nth points after the peak voltage |  
<b>2</b>     |  Default Method 2. dV is calculatied using the voltage difference between the peak voltage and the smallest data point where the second derivative greater than 0.01 (the second derivative decreases during teh discharging process)   |  
<b>201</b>    |  This method prompts the user to enter a float x, where dV is determined between the peak voltage and the voltage of the smallest data point with second derivative over x   |  


<div id="cap_method_table">
</div>

#### <a href="#cap_para"> cap_method</a>

Method  |  Description  |
---   |  ---   | 
<b>False/1</b>   |  Default Method. The lower half of the discharging curve is fitted for capacitance calculation.  |  
<b>2</b>   |  The upper half of the discharging curve is fitted for capacitance calculation.  |  


#### Returns 
<b>out: <i>Supercap</i></b>

>A Supercap entity generated from the text file


### Examples 
---

```python
>>>supercap1 = Load_capacitor('./CC/3.0_mA_1.0V_010120.txt', ESR_method = 2)
Missing current argument. Please include the current argument in mA:
>>>4
Mass of electrodes absents. Non-gravimetric capacitance is returned
Cycle 1387 has insufficient data points (40% less than average). Skipped for capacitance calculation
>>>supercap1
<Class_Supercap: 4.0 mA, max voltage 1.0 V, 2704 cycle(s), ESR method 2 (setting = 0.01), cap_method 1>
```

<br>

```python
>>>supercap2 = Load_capacitor('./CC/3.0_1.0V_010120.txt', t_set = 0, V_set = 1, mass_ls = [[12,13,12.2], [11, 10.5, 11.6]], current = 4, ESR_method = 2)
>>>supercap2
<Class_Supercap: 4.0 mA, max voltage 1.0 V, 2704 cycle(s), ESR method 2 (setting = 0.01), cap_method 1>
```

</div>

<br>
<br>

---
---

<div id="Glob_analysis">
    
## <a href="#sub_TOC">Glob_analysis(path, t_set = False, V_set = False, delimiter = False, mass_ls = False, row_skip = False, ESR_method = True, setting = False, cap_method = False, plot_set = False, plotting = True, save_plot = False)</a> 
Loading all txt/csv files in the folder as specified in path. Good for analysing how capacitance changes with current density. 


### Notes
---
  1. Capacitance and ESR analysis for one supercapacitor under different currents. 
  2. Error bars are calculated from the mass errors of the electrodoes as other errors are insignificant compared to that caused by mass. 
  3. The masses in mass_ls is in <b>mg</b>. 
  4. It is assumed that all data files in the folder are measured from the same capacitor, hence they all have <b>the same mass_ls</b>. 
  5. The current has to be included in the file name in the current format as specified under <a href="#path"> Parameters >> path</a>
       

### Parameters
---

#### Arguments

<div id="path"></div>

1. <b>path : <i>file, str, or pathlib.Path</i></b> <br>
    File, filename of the text file to read. Note that if the library is not allocated in the same directory as the file, the pathway to the file has to be given. For <b>``` current=False```</b>, current will be directly read from the filename (i.e. the fielname has to include the current followed by <code>'_mA'</code> and seperated by <code>'_'</code>, <code>'/'</code> or it is the first component of the filename). Note that the current values must be recorded in <b>mA</b>.For more details, refer to the Examples section.


2. <b>t_set : <i>int/str(csv files only), optional</i></b> <br>
   An integer specifying the coloumn index for time(s) data, with the first coloumn being coloumn 0 starting from left. If t_set = False, column 0 will be used as time(s); if t_set = True, there will be prompt asking for time coloumn index to be entered.For csv files, the coloumn index can also be the name of the coloumn (e.g. <code>t_set = 'time(s)'</code>). 
   
   
3. <b>V_set : <i>int/str(csv files only), optional</i></b> <br>
   An integer specifying the coloumn index for voltage(V) data, with the first coloumn being coloumn 0 starting from left. If V_set = False, column 1 will be used as Voltage(V); if t_set = True, there will be prompt asking for voltage coloumn index to be entered. For csv files, the coloumn index can also be the name of the coloumn (e.g. <code>V_set = 'voltage(V)'</code>). 


4. <b>delimiter : <i>str, optional</i></b> <br>
    A string which is used to seperate the data coloumns in the data file. If <code>delimiter = False</code>, the delimiter is assumed to be space <code>' '</code>.
   

5. <b>mass_ls : <i>list, [[measurements of m1], [measurements of m2]], optional</i></b> <br>
   A list specifying the mass of each electrode in the format as shwon above. Multiple measurements for each electrode should be included for calculation of the uncertainty of the data. All masses should be recorded in <b>mg</b>. If mass_ls = False, a non-gravimetric capacitanc will be calculated and the function returns <i><code>[[False, False], [False, False]]</code></i> for the <code>.masses</code> method in the resulting Supercap entity (more details for extracting data from the Supercap class in <a href="#__init__">Supercap class >> init</a>


6. <b>row_skip : <i>int, optional</i></b><br>
   Number of the rows of headers to skip in the txt files. If <b><code>row_skip = False</code></b>, row_skip = 1; if <b><code>row_skip = True</code></b>, a prompt will ask for rows to skip for the file. Enter <code>row_skip = 0</code> if no rows need to be skipped. 

<div id="ESR_para_glob"></div>

7. <b>ESR_method : <i>int, optional</i></b><br>
   The method for ESR analysis. It is by default <b>(<code>ESR_method = True</code>)</b> that the ESR analysis will be carried out using method 2 (constant derivative). For all methods available please refer to the next session <a href="#glob_method_table">ESR_method</a>. <code>ESR_setting = False</code> will return <code>.esr_ls</code> as <b>False</b> in the Supercap class. Available ESR_methods are: <code>ESR_methods = True, False, 1, 101, 2, 201. </code>


8. <b>setting : <i>float, optional</i></b><br>
   For <code>ESR_methods = True, 1, or 2 </code>, <code>setting = False</code>. For <code>ESR_methods = 101 or 201 </code>, setting is required as the number of points n/second derivative cut off point needed for the constant point method and the constant derivative method, respectively. If <code>ESR_methods = 101 or 201 </code> but <code>setting = False</code>, the function will promt the user to choose a specific value for the ESR analysis before proceeding. 


9. <b>cap_method : <i>bool, optional</i></b><br>
    The method for capacitance analysis which determines whether the upper (cap_method = 2) or lower (cap_method = 1) half of the voltage range of the discharging curve will be used. By default <code>cap_set = False</code> and the program uses the lower half of the discharging curve. For detailed information please refer to the <a href="#cap_method_table">cap_method</a> table below. 


10. <b>plot_set : <i>bool, optional</i></b><br>
    Figure parameters for plotting. If <code>plot_set = False</code>, the defualt settings will be used. If <code>plot_set = True</code>, there will be prompts to allow customised settings for plotting.


11. <b>plotting : <i>bool, optional</i></b><br>
   This argument determines whether the capacitance vs. current density plot will be plotted. It is by default that <code>plotting = True </code>, and  the figure will be plotted. If <code>plotting = False </code>, the figure will not be plotted.
   
   
12. <b>save_plot : <i>bool, optional</i></b><br>
   This argument determines whether the capacitance vs. current density plot will be saved. It is by default that <code>save_plot = True </code>, and  the figure will be saved as 'Gravimetric specific capacitance vs. current density [datetime].png'. If <code>save_plot = False </code>, the figure will not be saved.
   
   
<div id="glob_method_table">
</div>

#### <a href="#ESR_para_glob"> ESR_method</a>

Method  |  Description  |
---   |  ---   | 
<b>True</b>   |  Default Method 2   |  
<b>False</b>   |  Returning ESR = False (no ESR calculation)   |  
<b>1</b>    |  Default Method 1. dV is calculatied using the voltage difference between the peak voltage and the fourth data point taken after the peak voltage is reached   |  
<b>101</b>    |  This method prompts the user to enter an interger n, where dV is determined between the peak voltage and the voltage of the nth points after the peak voltage |  
<b>2</b>     |  Default Method 2. dV is calculatied using the voltage difference between the peak voltage and the smallest data point where the second derivative greater than 0.01 (the second derivative decreases during teh discharging process)   |  
<b>201</b>    |  This method prompts the user to enter a float x, where dV is determined between the peak voltage and the voltage of the smallest data point with second derivative over x   |  


#### Returns 
<b>out: <i>list</i></b>

><i>[[list of current density],[list of Supercap objects]]</i>


### Examples 
---

```python
>>>CC_glob = Glob_analysis('./various_mA_folder/*.txt', mass_ls=[[10.7, 10.5, 11.0], [11.2, 11.2, 11.5 ]], ESR_method = 2, plotting=False)
>>>CC_glob
([0.0034039334341906206,
  0.011346444780635402,
  0.022692889561270805],
[<Class_Supercap: 0.06 mA, max voltage 0.8 V, 4 cycle(s), ESR method 2 (setting = 0.01), cap_method 1>,
  <Class_Supercap: 0.2 mA, max voltage 0.8 V, 4 cycle(s), ESR method 2 (setting = 0.01), cap_method 1>,
  <Class_Supercap: 0.4 mA, max voltage 0.8 V, 4 cycle(s), ESR method 2 (setting = 0.01), cap_method 1>])
```

</div>


<br>
<br>

---
---

<div id="__init__">
    
## <a href="#sub_TOC">__init__(self, current,  t_V_ls, masses, cap_ls, esr_ls, extrema, cycle_n, m_error, ESR_method, cap_method, faulty_cycles)</a> 
Initialize a :class:`.Supercap`.

### Notes
---
Stores all relevant information for the capacitance/ESR analysis of the supercapacitor. All current values are in <b>mA</b> and mass values are in <b>mg</b>. 

Available parameters that can be extracted include:

```python
1. .current
2. .masses
3. .t_ls
4. .V_ls
5. .cap_ls
6. .esr_ls
7. .cycle_n
8. .error
9. .peaks
10. .troughs
11. .esr_method
12. .cap_method
13. .faulty_cycles
```
The above method follows the name of the Supercap variable. More details in the example section.


### Parameters
---

#### Arguments

<div id="path"></div>

1. <b>current : <i>float</i></b> <br>
    Current at which the CC analysis is undertaken. The current is in mA.


2. <b>t_V_ls : <i>list, [[list of time readings], [list of voltage readings]]</i></b> <br>
   The raw data of the CC analysis. 


3. <b>masses : <i>list, [[average mass of m1, std of m1], [average mass of m2, std of m2]]</i></b><br>
   The mass measurements for the two electrodes. The mass is in mg.


4. <b>cap_ls : <i>list, [list of calculated capacitance for each cycle]</i></b><br>
   The calculated capacitance for each cycle.


5. <b>esr_ls : <i>list, [list of calculated ESR value for each cycle]</i></b><br>
   The calculated ESR values for each cycle. 


6. <b>extrema : <i>list, [[peak indices], [trough indices]] </i></b><br>
   The indices for the peaks and troughs of the voltage readings.


7. <b>cycle_n : <i>int</i></b><br>
   The indices for the peaks and troughs of the voltage readings.


8. <b>m_error : <i>list, [list of uncertainties]</i></b><br>
   The uncertainty for each calculated capacitance value.


9. <b>ESR_method : <i>int</i></b><br>
   The method for ESR analysis.
   ESR_method = 1/102/2/202


9. <b>cap_method : <i>int</i></b><br>
   The method for capacitance analysis.
   cap_method = 1/2


11. <b>faulty_cycles : <i>list, [list of faulty cycle numbers]</i></b><br>
   A list of cycle numbers (cycle number starting from 1) for the faulty cycles. The faulty cycle could be due to: 
   1. The discharge slope of a CC cycle has significantly more or less data  points compared to the neighbouring cycles (more than 50% difference).
   2. The discharge slope fails to perform linear fitting.


### Examples 
---

```python
>>>supercap1.current #supercap1 is a Supercap class variable.
4.0
>>>supercap1.masses 
[[10.2, 0.0912], [12.1, 0.0853]]
```

</div>


<div id="__repr__">
    
## <a href="#sub_TOC">__repr__(self)</a> 
Initialize a :class:`.Supercap`.


### Returns
---
Returns a string which state the current, maximum voltage and number of cycle analysed in the Supercap class.


### Examples
---
```python
>>>Supercap2 #variable as saved in the previous example in Load_capacitor
<Class_Supercap: 4.0 mA, max voltage 1.0 V, 2704 cycle(s), ESR method 2 (setting = 0.01), cap_method 1>
```

</div>


<br>
<br>

---
---

<div id="ESR_method_change">
    
## <a href="#sub_TOC">ESR_method_change(self, ESR_method = True, setting = False)</a> 
Initialize from a :class:`.Supercap`.


### Notes
---
Changing the ESR analysis method used for calculating esr_ls.
       

### Parameters
---

#### Arguments

1. <b>ESR_method : <i>int, optional</i></b><br>
   The method for ESR analysis. For all methods available please refer to the next session <a href="#method_table">ESR_method</a>. <code>ESR_setting = True</code> will change the ESR analysis method to default, which is the constant second derivative method with a cut-off second derivative of 0.01. <code>ESR_setting = False</code> will turn off the ESR calculation. Available ESR_methods are: <code>ESR_methods = True, False, 1, 101, 2, 201. </code>


2. <b>setting : <i>float, optional</i></b><br>
   For <code>ESR_methods = True, 1, or 2 </code>, <code>setting = False</code>. For <code>ESR_methods = 101 or 201 </code>, setting is required as the number of points n/second derivative cut off point needed for the constant point method and the constant derivative method, respectively. If <code>ESR_methods = 101 or 201 </code> but <code>setting = False</code>, the function will promt the user to choose a specific value for the ESR analysis before proceeding. 


<div id="method_table">
</div>

#### <a href="#ESR_para"> ESR_method</a>

Method  |  Description  |
---   |  ---   | 
<b>True</b>   |  Default Method 2   |  
<b>False</b>   |  Returning ESR = False (no ESR calculation)   |  
<b>1</b>    |  Default Method 1. dV is calculatied using the voltage difference between the peak voltage and the fourth data point taken after the peak voltage is reached   |  
<b>101</b>    |  This method prompts the user to enter an interger n, where dV is determined between the peak voltage and the voltage of the nth points after the peak voltage |  
<b>2</b>     |  Default Method 2. dV is calculatied using the voltage difference between the peak voltage and the smallest data point where the second derivative greater than 0.01 (the second derivative decreases during teh discharging process)   |  
<b>201</b>    |  This method prompts the user to enter a float x, where dV is determined between the peak voltage and the voltage of the smallest data point with second derivative over x   |  


#### Returns 
<b>out: <i>:class:`.Supercap`</i></b>
>self.esr_ls


### Examples 
---

```python
>>>Supercap2
<Class_Supercap: 4.0 mA, max voltage 1.0 V, 2704 cycle(s), ESR method 2 (setting = 0.01), cap_method 1>
>>>Supercap2.ESR_method_change(ESR_method = 201, setting =1)
The original ESR method is 2 , and the setting is 0.01
array([20.66931875, 20.762845  , 20.72346125, ..., 20.536415  ,
       20.5659475 , 20.570865  ])
>>>Supercap2
<Class_Supercap: 4.0 mA, max voltage 1.0 V, 2704 cycle(s), ESR method 201 (setting = 1), cap_method 1>
```

</div>

<br>
<br>

---
---

<div id="Cap_method_change">
    
## <a href="#sub_TOC">Cap_method_change(self, cap_method = False, cap_grav = True, m1 = False, m2 = False)</a> 
Initialize from a :class:`.Supercap`.


### Notes
---
Changing the cap analysis method used for calculating capacitance.
       

### Parameters
---

#### Arguments

1. <b>cap_method : <i>int</i></b><br>
   The method for capacitance analysis into which is changed. For <code>cap_method = 1 or False</code>)</b>, discharge slope of the lower half of the voltage range will be analysed. For <code>cap_method = 2</code>)</b>, discharge slope of the upper voltage range will be analysed.


2. <b>cap_grav : <i>bool, optional</i></b><br>
   It is by default that the gravimetric capacitance is calculated. By using <code>cap_grav = False</code> or <code>mass_ls = False</code> , a non-gravimetric capacitance will be calculated. 


3. <b>m1 : <i>float, optional</i></b> <br>
    The mass of electrode 1 of the supercapacitor. The mass is in <b>mg</b>.
    
    
4. <b>m2 : <i>float, optional</i></b> <br>
    The mass of electrode 2 of the supercapacitor. The mass is in <b>mg</b>.


#### Returns 
<b>out: <i>:class:`.Supercap`</i></b>
>self.cap_ls


### Examples 
---

```python
>>>Supercap2
<Class_Supercap: 4.0 mA, max voltage 1.0 V, 2704 cycle(s), ESR method 2 (setting = 0.01), cap_method 1>
>>>Supercap2.cap_method_change(cap_method = 2, cap_grav = True)
The original cap_method is 1
The cap_method is changed to 2
Gravimetric capacitance (F g^-1) is being calculated.
Electrode masses are taken as specified previously.
Cycle 1387 has insufficient data points (50% less than average). Skipped for capacitance calculation

array([49.3082373 , 49.37786468, 49.34835958, ..., 51.12061108,
       51.13964009, 51.11665995])

>>>Supercap2.Check_analysis(start = 1387, end = 1389)
Cycle 1387 was skipped for calculation due to errors
```
![cap_method 2, upper voltage range](https://user-images.githubusercontent.com/70351473/103543708-e04aee00-4e96-11eb-98ea-afa38a100d44.png 'cap_method 2, upper voltage range')


```
>>>Supercap2
<Class_Supercap: 4.0 mA, max voltage 1.0 V, 2704 cycle(s), ESR method 2 (setting = 0.01), cap_method 2>
```

</div>

<br>
<br>

---
---

<div id="Show_dV2">
    
## <a href="#sub_TOC">Show_dV2(self, cycle_check = False)</a> 
Initialize from a :class:`.Supercap`.

### Notes
---
Visualising the second derivative and the charge/discharge curve of a specified cycle with the option of changing the ESR analysis method used for calculating esr_ls. <b>It is assumed that <code>ESR_method = 201</code> is used in this function.</b>

### Parameters
---

#### Arguments
1. <b>Cycle_check : <i>int, optional</i></b><br>
   The method for ESR analysis. Specify the cycle of the charge/discharge curve and the second derivative to be plotted on the same axes.If <code>Cycle_check = False</code>, the user will be prompted to select a cycle on the CD curve to view as the reference for adjusting the cut off point. (Note: the cycle number starts from 1)


#### Returns
1. A plot of charge discharge curve and the corresponding second derivative <br>
2. :class:`.Supercap`, optional
>self.esr_ls 


### Examples
---
```python
>>>Supercap2
<Class_Supercap: 4.0 mA, max voltage 1.0 V, 2704 cycle(s), ESR method 201 (setting = 1), cap_method 1>
>>>Supercap1.Show_dV2()
Of which cycle would you like to see the second derivative? enter a number between 1 and 2704
>>>0
The cut off second derivative currently being used is 1
```
![.Show_dV2() example](https://user-images.githubusercontent.com/70351473/91521198-095ae100-e8ef-11ea-94f5-1381dd325cbb.png '.Show_dV2() example 1')
```python
Are you happy with the cut off point? (yes/no)
>>>no
Please input the value of desired cut off second derivative.
>>>0.01
```
![.Show_dV2() example](https://user-images.githubusercontent.com/70351473/91521234-22639200-e8ef-11ea-9cfc-accae0456220.png  '.Show_dV2() example 2')
```python
The cut off second derivative currently being used is 0.01
Are you happy with the cut off point? (yes/no)
>>>yes
Do you wish to change the cut off point to the current value? (setting =0.01)[yes/no]
>>>yes
The original ESR method is 201 , and the setting is 1
>>>Supercap2
<Class_Supercap: 4.0 mA, max voltage 1.0 V, 2704 cycle(s), ESR method 201 (setting = 0.01), cap_method 1>
```

</div>


<br>
<br>

---
---

<div id="Cap_vs_cycles">
    
## <a href="#sub_TOC">Cap_vs_cycles(self, set_fig=False, save_fig=False)</a> 
Initialize from a :class:`.Supercap`.

### Notes
---
Plotting capacitance against cycle and saving it as 'current mA_cap_vs_cycles_datetime.png'

### Parameters
---

#### Arguments
1. <b>set_fig : <i>bool, optional</i></b><br>
   If <code>set_fig = True</code>, the user will be prompted to change the setting of the figure.


2. <b>save_fig : <i>bool, optional</i></b><br>
   If <code>save_fig = True</code>, the figure will be saved under the name '[current] mA_cap_vs_cycles_Date[d/m]_Time[h/m].png'
   
   
#### Returns
A figure of capacitance over cycle number


### Examples
---
```python
>>>Supercap1.Cap_vs_cycles(set_fig = True)
Please input length for the figure:
>>>30
Please input width for the figure:
>>>20
Please input the font size for the figure:
>>>45
Please input the line width for the figure:
>>>7
Please input the line colour for the figure:
>>>'black'
```
![.Cap_vs_cycles() example](https://user-images.githubusercontent.com/70351473/91521000-9f423c00-e8ee-11ea-84f8-264f85f4d3c4.png '.Cap_vs_cycles() example')

</div>


<br>
<br>

---
---

<div id="Get_info">
   
## <a href="#sub_TOC">Get_info(self)</a> 
Initialize from a :class:`.Supercap`.

### Notes
---
Printing the basic information of the Supercap class

### Parameters
---

#### Arguments
None


#### Returns
<b>out:<i>:class:`string`, optional</i></b>
>The number of cycles, the average capacitance, the std of capacitance, the average ESR and its std, the ESR_method and cap_method used. 


### Examples
---
```python
>>>Supercap2.Get_info()
The number of cycle(s) analysed is 2704
The number of faulty cycle is 1
The average capacitance is 60.9025 F g^(-1)
The standard deviation of the average is 0.0101
The average ESRs is 14.3174 Ohms
The standard deviation of the ESRs is 0.4699
Lower half of the voltage range in the discharge curve was used for capacitance calculations
Constant second derivative method was used for ESR calculations
```

</div>

<br>
<br>

---
---


<div id="Check_analysis">
    
## <a href="#sub_TOC">Check_analysis(self, begin = False, end = False, set_fig = False, save_fig = False)</a> 
Initialize from a :class:`.Supercap`.

 

### Notes
---

Plotting the charge/discharge curve and visualising how the data is analysed (indicate the slope fitting for capacitance and the voltage drop for ESR).

 

### Parameters 
---

 

#### Arguments

1. <b>begin : <i>int, optional</i></b><br>

   The first cycle to be visualised. For <code> begin = False </code>, the user will be prompted to choose the first cycle to be visualised. Please note that the cycle number starts from 1. 

 

 

2. <b>end : <i>int, optional</i></b><br>

   The last cycle to be visualised. For <code> end = False </code>, the user will be prompted to choose the last cycle to be visualised.

  

   

3. <b>set_fig : <i>bool, optional</i></b><br>
   If <code>set_fig = True</code>, the user will be prompted to change the setting of the figure.
   
   
   
   
   
4. <b>save_fig : <i>string, optional</i></b><br>

   For <code>save_fig=False</code>, the plot will not be saved.

   For <code>save_fig=True</code>, the plot will be saved as 'Check_analysis_[datetime].png'.

  

 

#### Returns

A plot of the charge/discharge curve with liniearly fitted slope and voltage drop.


### Examples
```python
>>>Supercap1.Check_analysis(begin = 0, end = 4, save_fig = False)
```
![.Check_analysis() example](https://user-images.githubusercontent.com/70351473/102226302-220ff680-3ee0-11eb-849b-743320186013.png  '.Check_analysis() example')

</div>


<br>
<br>

---
---
     
<div id="Export">

## <a href="#sub_TOC">Export(self, name, error = False, delimiter = False)</a> 
Initialize a :class:`.Supercap`.

     
     
### Notes
---
   
Exporting the electrochemical parameters as a txt file
     
     
     
### Parameters 
---
     
     
     
#### Arguments

1. <b>name : <i>str </i></b><br>
     Name of the exported text file.
     
     
1. <b>error : <i>bool, optional</i></b><br>
     Whether a list of uncertainty of capacitance is included. If <code>error = False</code>, which is the default setting, a list of uncertainty will not be included; if <code>error = True</code>, a list of uncertainty will be included. 
   

1. <b>delimiter : <i>str, optional</i></b><br>
     String or character separating columns.
     
     
     
#### Returns
     
Returns a text file 'name.txt' including lists of capacitance, ESR and uncertainty of capacitance (optional).

     
</div>


<br>
<br>

---
---
     
<div id="CV_analysis">
    
## <a href="#sub_TOC"><b>CV_analysis</b><i>(pathway, m1, m2, scan_r = False, row_skip = False, x_name = False, y_name = False, delimiter = False, int_method = False)</i></a>
This function loads the txt/csv file specified on the pathway, where capacitance analysis on the Cyclic Voltammetry will be carried out. The function returns a list of capacitance calculated from each CV cycle. 


### Notes
---
This function supports electrochemical data in either txt or csv format. In a txt file, it is by default that the first coloumn of the file is assumed to be voltage (V), and the second coloumn is assumed to be current (mA) for the CC analysis. The two coloumns are assumed to be seperated by space. However, the optional arguments, <i>x_name, y_name, delimeter and row_skip</i>, offers flexibility in dealing with more complex data files. 



### Parameters
---

#### Arguments
1. <b>pathway : <i>file, str, or pathlib.Path</i></b> <br>
    File, filename of the text file to read. Note that if the library is not allocated in the same directory as the file, the pathway to the file has to be given. For <b>``` scan_r=False```</b>, current will be directly read from the filename (i.e. the fielname has to include the current followed by <code>'_mvs'</code> and seperated by <code>'_'</code>, <code>'/'</code> or it is the first component of the filename). If scan rate information cannot be obtained from the filename, the scan rate has to be specified via the <code>current</code> argument. For more details, refer to the Examples section. This function currently only supports data in the format of txt or csv. 


2. <b>m1 : <i>float, optional</i></b> <br>
    The mass of electrode 1 of the supercapacitor. The mass is in <b>mg</b>.
    
    
3. <b>m2 : <i>float, optional</i></b> <br>
    The mass of electrode 2 of the supercapacitor. The mass is in <b>mg</b>.


4. <b>scan_r : <i> float, optional</i></b><br>
   If <b><code>scan_r = False</code></b>, the scan rate value in <b>mV/s</b> will be directly read from the filename given that it is supplied in the format as specified above in the pathway section. If the current is not included the filename, it should be specified in the form of <code>scan_r =<i>specified_scan_rate</i></code>


5. <b>row_skip : <i>int, optional</i></b><br>
   Number of the rows of headers to skip in the txt files. If <b><code>row_skip = False</code></b>, row_skip = 1; if <b><code>row_skip = True</code></b>, a prompt will ask for rows to skip for the file. Enter <code>row_skip = 0</code> if no rows need to be skipped. 
   
   
6. <b>V_set : <i>int/str(csv files only), optional</i></b> <br>
   An integer specifying the coloumn index for voltage in <b>V</b>, with the first coloumn being coloumn 0 starting from left. If <code>x_name = False</code>, column 0 will be used as voltage(V); if x_name = True, there will be prompt asking for scan rate coloumn index to be entered.For csv files, the coloumn index can also be the name of the coloumn (e.g. <code>x_name = 'voltage(V)'</code>). 
     
     
7. <b>I_set : <i>int/str(csv files only), optional</i></b> <br>
   An integer specifying the coloumn index for voltage(V) data, with the first coloumn being coloumn 0 starting from left. If <code>y_name = False</code>, column 1 will be used as current in <b>mA</b>; if y_name = True, there will be prompt asking for current coloumn index to be entered. For csv files, the coloumn index can also be the name of the coloumn (e.g. <code>I_set = 'current(mA)'</code>). 


8. <b>delimiter : <i>str, optional</i></b> <br>
    A string which is used to seperate the data coloumns in the data file. If <code>delimiter = False</code>, the delimiter is assumed to be space <code>' '</code>.

<div id="int_para"></div>

9. <b>int_method : <i>int, optional</i></b> <br>
   The method for integration of the enclosed area. It is by default <b>(<code>int_method = False</code>)</b> that the area under the curve will be calculated using the Simpson's rule. For all methods available please refer to the next session <a href="#int_method_table">int_method table</a>.

10. <b>calc_method : <i>int, optional</i></b> <br>
   The method which determines whether capacitance or capacity (enclosed area divided by mass) is being calculated. If <code>calc_method = 1 </code>, capacitance is calculated; if <code>calc_method = 2</code>, capacity is calculated by dividng the enclosed area by the mass of the electrodes. 


<br>

<div id="int_method_table">
</div>

#### <a href="#int_para"> int_method</a>

Method  |  Description  |
---   |  ---   | 
<b>False or 1</b>   |  Default method. Integration using the Simpson's rule and integrates over discharging curve only.  |  
<b>101</b>    |  Integration using the Simpson's rule and integrates over both the charging and discharging curves.  |  
<b>2</b>    |  Integration using the trapezoidal rule and integrates over discharging curve only. |  
<b>202</b>     |  Integration using the trapezoidal rule and integrates over both the charging and discharging curves.   |  


#### Returns 
<b>out: <i>[list of calculated gravimetric capacitance]</i> </b>


### Examples 
---

```python
>>>CV_analysis('../cell1_CV/1.2V_CA2.csv', m1=10, m2=9, scan_r=1, x_name = 'voltage', y_name ='current',delimeter=',', int_method=1)
4  CV cycles are being analysed using integration method 1
[86.30233646681373, 88.433682993075, 89.45296144982, 90.0191569583757]
```

</div>
