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
        This is a Python library for analysis for the Constant Current <b>(CC)</b> curves as well as the Cyclic Voltammetry <b>(CV)</b> curves of two-electrode, symmetrical supercapacitors. It provides an easy and standardised way to quickly extract useful information from the CC and CV data, including the <b>capacitance</b> and the Equivalent Series Resistance <b>（ESR） </b>of the supercapacitor and how they evolve over cycles, with multiple options offered to suit the need of scientific investigations of supercapacitors. 

<br>
<br>

For <b>CC</b> analysis, the capacitance is calculated via linear fitting the second half of the discharging slope in each charging/discharging cycle. For <b>gravimetric capacitance, <img src="https://render.githubusercontent.com/render/math?math=C_g"> (<img src="https://render.githubusercontent.com/render/math?math=F%20g^{-1}">)</b>:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_g=%20\frac{(m_1%2Bm_2)%20\times%20I%20}{(m_1%20\times%20m_2)%20\times%20\frac{dV}%20{dt}}">
</center>
</p>

<i>where <img src="https://render.githubusercontent.com/render/math?math=m_1"> is the mass of one of the two electrodes in the electrochemical cell and <img src="https://render.githubusercontent.com/render/math?math=m_2"> is the mass of the other, both in mg; I is the current in mA under which the CC anaysis is conducted; <img src="https://render.githubusercontent.com/render/math?math=\frac{dV}%20{dt}"> is the change of voltage (V) with respect to time (s). </i>

<br>
<br>
<br>
<br>


For <b>non-gravimetric capacitance (F)</b>:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_{non}_{grav}=%20I%20\times%20\frac{dt}%20{dV}">
</p>

<i>where I is the current in mA and <img src="https://render.githubusercontent.com/render/math?math=\frac{dt}%20{dV}"> is the change of time (s) with respect to voltage (V).</i>

<br>
<br>
<br>
<br>


The <b>ESR (Ω)</b> is calculated using the voltage drop:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=ESR=%20\frac{V_{drop}}{2%20I}">
</p>

<i>where <img src="https://render.githubusercontent.com/render/math?math=V_{drop}"> is the vertical drop in voltage in V at the beginning of the discharging curve as shown in the figure below; I is the current in mA under which the CC analysis is conducted. </i>

<br>
<br>
<br>
<br>


Here is an illustration of how the CC data is analysed: 

<p align="center">
<img src="https://user-images.githubusercontent.com/70351473/102105162-f8df5f80-3e26-11eb-96a0-44714a6c144f.png" alt="CC analysis" width="600" height="400">
</p>


For <b>CV</b> analysis, the capacitance is calculated via integration of the area enclosed by current as the voltage scanned across the potential window. For <b>gravimetric capacitance (<img src="https://render.githubusercontent.com/render/math?math=F%20g^{-1}">)</b>:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_g=%20\frac{(m_1%20%2B%20m_2)\times%20\int%20I%20dV}{(m_1%20\times%20m_2)\times%20scan%20\space%20\space%20rate%20\times%20potential\space%20window}">
</p>

<br>
<br>

An illustration of how the CV data is analysed is shown below:

<br>

<b>image to be added</b>

</div>


----
<div id="Installation">
    <h2>
        <a href="#TOC">Installation</a>
    </h2>
    <p>
        Please follow the instruction under the 'code' tab.
                  
 Alternatively, use(https://pypi.org/project/Supercap-analysis/):
 ```python
 pip install Supercap-analysis
 ```
        
   </p>
</div>

-----

<div id="Documentations">
    <h2>
        <a href="#TOC">Documentations</a>
    </h2>
    <p>
        This python library offers means to analyse CC data in the format of text files, which can be directlt exported from electrochemistry software such as <code>EC Labs</code>. <b>The file has to have two and only two coloumns of data, with the first coloumn being time (s), and the second coloumn being Voltage (V).</b> (It is intended to extended the code to enable loading from csv files and/or files with multiple coloumns of data). The documentation includes two parts: means for loading data into the Supercap class and methods within the Superclass. 
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
 * <a href="#Show_dV2">__Show_dV2__</a>
 * <a href="#Cap_vs_cycles">__Cap_vs_cycles__</a>
 * <a href="#Get_info">__Get_info__</a>
 * <a href="#Check_analysis">__Check_analysis__</a>
 

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
   If <b><code>current = False</code></b>, the current value will be directly read from the filename given that it is supplied in the format as specified above in the pathway section. If the current is not included the filename, it should be specified in the form of <code>current =<i>specified_current</i></code>


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
>>>Load_capacitor('./CC/3.0_mA_1.0V_010120.txt', ESR_method = 201)
Please enter the number of header row(s) in this file:
>>>0
Please specify a cut-off derivative (the default value is 0.01)
>>>0.1
<Class_Supercap: 3.0 mA, 1.0 V, 5 cycles, ESR method 201>
```

<br>

```python
>>>Load_capacitor('./CC/3.0_1.0V_010120.txt', t_set = 1, V_set = 3, mass_ls = [[12,13,12.2], [11, 10.5, 11.6]], current = 3, ESR_method = 2, setting = 0.1)
<Class_Supercap: 3.0 mA, 1.0 V, 5 cycles, ESR method 2>
```

</div>

<br>
<br>

---
---

<div id="Glob_analysis">
    
## <a href="#sub_TOC">Glob_analysis(path, t_set = False, V_set = False, delimiter = False, mass_ls = False, row_skip = False, ESR_method = True, setting = False, cap_method = False, plot_set = False, plot_save = True)</a> 
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
    File, filename of the text file to read. Note that if the library is not allocated in the same directory as the file, the pathway to the file has to be given. For <b>``` current=False```</b>, current will be directly read from the filename (i.e. the fielname has to include the current followed by <code>'_mA'</code> and seperated by <code>'_'</code>, <code>'/'</code> or it is the first component of the filename). For more details, refer to the Examples section.


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


11. <b>plot_save : <i>bool, optional</i></b><br>
   This argument determines whether the capacitance vs. current density plot will be plotted and saved. It is by default that <code>plotting = True </code>, and  the figure will be plotted and saved as 'Gravimetric specific capacitance vs. current density [datetime].png'. If <code>plotting = False </code>, the figure will not be plotted and saved.

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
>>>Glob_analysis('./various_mA_folder/*.txt', mass_ls = [[12,13,12.2], [11, 10.5, 11.6]], row_skip = 1, ESR_method = 2, plotting = False)
[[0.001, 0.003, 0.005],
[<Class_Supercap: 1.0 mA, 1.0 V, 5 cycles, ESR method 2>,
 <Class_Supercap: 2.0 mA, 1.0 V, 7 cycles, ESR method 2>,
 <Class_Supercap: 3.0 mA, 1.0 V, 5 cycles, ESR method 2>,]]
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
   A list of cycle numbers for the faulty cycles.


### Examples 
---

```python
>>>supercap1.current #supercap1 is a Supercap class variable.
0.5
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
>>>Supercap1
<Class_Supercap: 3.0 mA, 1.0 V, 5 cycles, ESR method 2>
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
   The method for ESR analysis. It is by default <b>(<code>ESR_method = True</code>)</b> that the ESR analysis will be carried out using method 2 (constant derivative). For all methods available please refer to the next session <a href="#method_table">ESR_method</a>. <code>ESR_setting = False</code> will return <code>.esr_ls</code> as <b>False</b> in the Supercap class. Available ESR_methods are: <code>ESR_methods = True, False, 1, 101, 2, 201. </code>


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
>>>Supercap1
<Class_Supercap: 1.0 mA, 1.0 V, 5 cycles, ESR method 2>

>>>Supercap1.ESR_method_change(ESR_method = 101, setting = 201, setting =1)
>>>Supercap1
<Class_Supercap: 1.0 mA, 1.0 V, 5 cycles, ESR method 201>
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
   The method for ESR analysis. Specify the cycle of the charge/discharge curve and the second derivative to be plotted on the same axes.If <code>Cycle_check = False</code>, the user will be prompted to select a cycle on the CD curve to view as the reference for adjusting the cut off point. 


#### Returns
1. A plot of charge discharge curve and the corresponding second derivative <br>
2. :class:`.Supercap`, optional
>self.esr_ls 


### Examples
---
```python
>>>Supercap1
<Class_Supercap: 3.0 mA, 1.0 V, 5 cycles, ESR method 2>
>>>Supercap1.Show_dV2()
Of which cycle would you like to see the second derivative? enter a number between 0 and 9
>>>0
The cut off second derivative currently being used is 0.002
```
![.Show_dV2() example](https://user-images.githubusercontent.com/70351473/91521198-095ae100-e8ef-11ea-94f5-1381dd325cbb.png '.Show_dV2() example 1')
```python
Are you happy with the cut off point? (yes/no)
>>>no
Please input the value of desired cut off second derivative.
>>>1
```
![.Show_dV2() example](https://user-images.githubusercontent.com/70351473/91521234-22639200-e8ef-11ea-9cfc-accae0456220.png  '.Show_dV2() example 2')
```python
Are you happy with the cut off point? (yes/no)
>>>yes
Do you wish to change the cut off point to the current value? (setting =1.0)[yes/no]
>>>yes
>>>Supercap1
<Class_Supercap: 3.0 mA, 1.0 V, 5 cycles, ESR method 201>
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
>>>Supercap1.Get_info()
'The number of cycle(s) analysed is 9'
'The average capacitance is 24.028444381438409'
'The standard deviation of the average is 0.553348977252065'
'The average ESRs is 11.724686851851855'
'The standard deviation of the ESRs is 0.023315957315381737'
'Lower half of the voltage range in the discharge curve was used for capacitance calculations'
'Constant second derivative method was used for ESR calculations'
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

   The first cycle to be visualised. For <code> begin = False </code>, the user will be prompted to choose the first cycle to be visualised.

 

 

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
![.Check_analysis() example](https://user-images.githubusercontent.com/70351473/94346269-5aabdc80-0023-11eb-8486-377e821e86d5.png  '.Check_analysis() example')

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
    The mass of electrode 1 of the supercapacitor. The mass is in mg.
    
    
3. <b>m2 : <i>float, optional</i></b> <br>
    The mass of electrode 2 of the supercapacitor. The mass is in mg.


4. <b>scan_r : <i> float, optional</i></b><br>
   If <b><code>scan_r = False</code></b>, the scan rate value (mV/s) will be directly read from the filename given that it is supplied in the format as specified above in the pathway section. If the current is not included the filename, it should be specified in the form of <code>scan_r =<i>specified_scan_rate</i></code>


5. <b>row_skip : <i>int, optional</i></b><br>
   Number of the rows of headers to skip in the txt files. If <b><code>row_skip = False</code></b>, row_skip = 1; if <b><code>row_skip = True</code></b>, a prompt will ask for rows to skip for the file. Enter <code>row_skip = 0</code> if no rows need to be skipped. 
   
   
6. <b>x_name : <i>int/str(csv files only), optional</i></b> <br>
   An integer specifying the coloumn index for voltage(V) data, with the first coloumn being coloumn 0 starting from left. If <code>x_name = False</code>, column 0 will be used as voltage(V); if x_name = True, there will be prompt asking for scan rate coloumn index to be entered.For csv files, the coloumn index can also be the name of the coloumn (e.g. <code>x_name = 'voltage(V)'</code>). 
     
     
7. <b>y_name : <i>int/str(csv files only), optional</i></b> <br>
   An integer specifying the coloumn index for voltage(V) data, with the first coloumn being coloumn 0 starting from left. If <code>y_name = False</code>, column 1 will be used as current(mA); if y_name = True, there will be prompt asking for current coloumn index to be entered. For csv files, the coloumn index can also be the name of the coloumn (e.g. <code>y_name = 'current(mA)'</code>). 


4. <b>delimiter : <i>str, optional</i></b> <br>
    A string which is used to seperate the data coloumns in the data file. If <code>delimiter = False</code>, the delimiter is assumed to be space <code>' '</code>.

<div id="int_para"></div>

5. <b>int_method : <i>int, optional</i></b> <br>
   The method for integration of the enclosed area. It is by default <b>(<code>int_method = False</code>)</b> that the ESR analysis will be carried out using method 2 (constant derivative). For all methods available please refer to the next session <a href="#int_method_table">int_method table</a>.


<br>

<div id="int_method_table">
</div>

#### <a href="#int_para"> int_method</a>

Method  |  Description  |
---   |  ---   | 
<b>False or 1</b>   |  Default method. Integration using the trapezoidal rule and integrates over discharging curve only.  |  
<b>101</b>    |  Integration using the trapezoidal rule and integrates over both the charging and discharging curves.  |  
<b>2</b>    |  Integration using the Simpson's rule and integrates over discharging curve only. |  
<b>202</b>     |  Integration using the Simpson's rule and integrates over both the charging and discharging curves.   |  


#### Returns 
<b>out: <i>[list of calculated gravimetric capacitance]</i></b>


### Examples 
---

```python
>>>Load_capacitor('../cell1_CV/1.2V_CA2.csv', m1=10, m2=9, scan_r=1, x_name = 'voltage', y_name ='current',delimeter=',', int_method=1)
4  CV cycles are being analysed using integration method 1
[86.30233646681373, 88.433682993075, 89.45296144982, 90.0191569583757]
```

</div>
