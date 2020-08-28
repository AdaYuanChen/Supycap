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
        This is a Python library for analysis for the Galvanostatic Charge Discharge <b>(GCD)</b> curves of two-electrode, symmetrical supercapacitors. It provides an easy and standardised way to quickly extract useful information from the GCD data, especially the <b>capacitance</b> and the <b>ESR </b>of the supercapacitor and how they evolve over time, with multiple options offered to suit the need of scientific investigations of supercapacitors. 

<br>
<br>

In this library, the capacitance is calculated via linear fitting the second half of the discharging slope in each charging/discharging cycle. For <b>gravimetric capacitance (F g^-1)</b>:

<p align="center">
C_g = (m_1 + m_2)/{m_1 m_2} * I * dV</center>
</p>

<br>


For <b>non-gravimetric capacitance (F)</b>:

<p align="center">
C = I * dV 
</p>

<br>


The <b>ESR (Ω)</b> is calculated using the voltage drop:

<p align="center">
ESR = V_drop / (2I) 
</p>

<br>
<br>

An illustration of how the GCD data is analysed is shown below: 

![An analysed GCD curve using the library](https://user-images.githubusercontent.com/70351473/91520899-64400880-e8ee-11ea-9758-75c1b7496c2e.png 'An analysed GCD curve using the library')
    </p>


</div>

----
<div id="Installation">
    <h2>
        <a href="#TOC">Installation</a>
    </h2>
    <p>
        Please follow the instruction as shown on the front of the page using command prompt. 
    </p>
</div>

-----

<div id="Documentations">
    <h2>
        <a href="#TOC">Documentations</a>
    </h2>
    <p>
        This python library offers means to analyse GCD data in the format of text files, which can be directlt exported from electrochemistry software such as <code>EC Labs</code>. <b>The file has to have two and only two coloumns of data, with the first coloumn being time (s), and the second coloumn being Voltage (V).</b> (It is intended to extended the code to enable loading from csv files and/or files with multiple coloumns of data). The documentation includes two parts: means for loading data into the Supercap class and methods within the Superclass. 
    </p>
</div>

<br>

<div id="sub_TOC">
    
* <b>Loading data</b>
 * <a href="#Load_capacitor">__Load_capacitor__</a>
 * <a href="#Glob_analysis">__Glob_analysis__</a>
* <b>Supercap class</b>
 * <a href="#__init__">__init__</a>
 * <a href="#__repr__">__repr__</a>
 * <a href="#ESR_method_change">__ESR_method_change__</a>
 * <a href="#Show_dV2">__Show_dV2__</a>
 * <a href="#Cap_vs_cycles">__Cap_vs_cycles__</a>
 * <a href="#Get_info">__Get_info__</a>
 * <a href="#Check_analysis">__Check_analysis__</a>
 




<br>
<br>


---
---


<div id="Load_capacitor">
    
## <a href="#sub_TOC"><b>Load_capacitor</b><i>(pathway, mass_ls = False, current = False, row_skip = False, ESR_method = True, setting = False, cap_norm = False)</i></a> 
This function loads the text file specified on the pathway into the <b>Supercap</b> class ,where capacitance and ESR analysis will be carried out. All relevant information can be extracted from the init function.


### Notes
---
This function aims to be a fast reader for simpley formatted text files. <b>The first coloumn of the file is assumed to be time (s), and the second coloumn is assumed to be Voltage (V) for the GCD analysis.</b>

<br>

Future development of the code will aim to include loading of csv files and/or files where the location of the data coloumns can be specified. 

### Parameters
---

#### Arguments
1. <b>pathway : <i>file, str, or pathlib.Path</i></b> <br>
    File, filename of the text file to read. Note that if the library is not allocated in the same directory as the file, the pathway to the file has to be given. For <b>``` current=False```</b>, current will be directly read from the filename (i.e. the fielname has to include the current followed by <code>'_mA'</code> and seperated by <code>'_'</code>, <code>'/'</code> or it is the first component of the filename). For more details, refer to the Examples section.


2. <b>mass_ls : <i>list, [[measurements of m1], [measurements of m2]], optional</i></b> <br>
   A list specifying the mass of each electrode in the format as shwon above. Multiple measurements for each electrode should be included for calculation of the uncertainty of the data. All masses should be recorded in <b>mg</b>. If mass_ls = False, a non-gravimetric capacitanc will be calculated and the function returns <i><code>[[False, False], [False, False]]</code></i> for the <code>.masses</code> method in the resulting Supercap entity (more details for extracting data from the Supercap class in <a href="#__init__">Supercap class>>init</a>


3. <b>current : <i> float, optional</i></b><br>
   If <b><code>current = False</code></b>, the current value will be directly read from the filename given that it is supplied in the format as specified above in the pathway section. If the current is not included the filename, it should be specified in the form of <code>current =<i>specified_current</i></code>


4. <b>row_skip : <i>int, optional</i></b><br>
   Number of the rows of headers to skip in the txt files. If <b><code>row_skip = False</code></b>, a prompt will ask for rows to skip for the file. Enter <code>row_skip = 0</code> if no rows need to be skipped. 

<div id="ESR_para"></div>

5. <b>ESR_method : <i>int, optional</i></b><br>
   The method for ESR analysis. It is by default <b>(<code>ESR_method = True</code>)</b> that the ESR analysis will be carried out using method 2 (constant derivative). For all methods available please refer to the next session <a href="#method_table">ESR_method</a>. <code>ESR_setting = False</code> will return <code>.esr_ls</code> as <b>False</b> in the Supercap class. Available ESR_methods are: <code>ESR_methods = True, False, 1, 101, 2, 201. </code>


6. <b>setting : <i>float, optional</i></b><br>
   For <code>ESR_methods = True, 1, or 2 </code>, <code>setting = False</code>. For <code>ESR_methods = 101 or 201 </code>, setting is required as the number of points n/second derivative cut off point needed for the constant point method and the constant derivative method, respectively. If <code>ESR_methods = 101 or 201 </code> but <code>setting = False</code>, the function will promt the user to choose a specific value for the ESR analysis before proceeding. 


7. <b>cap_norm : <i>bool, optional</i></b><br>
   It is by default that the gravimetric capacitance is calculated. By using <code>cap_norm = False</code> or <code>mass_ls = False</code> , a non-gravimetric capacitance will be calculated. 

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
<b>out: <i>Supercap</i></b>

>A Supercap entity generated from the text file


### Examples 
---

```python
>>>Load_capacitor('./GCD/3.0_mA_1.0V_010120.txt', ESR_method = 201)
Please enter the number of header row(s) in this file:
>>>0
Please specify a cut-off derivative (the default value is 0.01)
>>>0.1
<Class_Supercap: 3.0 mA, 1.0 V, 5 cycles, ESR method 201>
```

<br>

```python
>>>Load_capacitor('./GCD/3.0_1.0V_010120.txt', mass_ls = [[12,13,12.2], [11, 10.5, 11.6]], current = 3, ESR_method = 2, setting = 0.1)
<Class_Supercap: 3.0 mA, 1.0 V, 5 cycles, ESR method 2>
```

</div>

<br>
<br>

---
---

<div id="Glob_analysis">
    
## <a href="#sub_TOC">Glob_analysis(path, mass_ls, row_skip=False, ESR_method=True)</a> 
Loading all text files in the folder as specified in path. Good for analysing how capacitance changes with current density. 


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


2. <b>mass_ls : <i>list, [[measurements of m1], [measurements of m2]], optional</i></b> <br>
   A list specifying the mass of each electrode in the format as shwon above. Multiple measurements for each electrode should be included for calculation of the uncertainty of the data. All masses should be recorded in <b>mg</b>. If mass_ls = False, a non-gravimetric capacitanc will be calculated and the function returns <i><code>[[False, False], [False, False]]</code></i> for the <code>.masses</code> method in the resulting Supercap entity (more details for extracting data from the Supercap class in [Supercap class>>init](test.txt))


3. <b>row_skip : <i>int, optional</i></b><br>
   Number of the rows of headers to skip in the txt files. If <b><code>row_skip = False</code></b>, a prompt will ask for rows to skip for the file. Enter <code>row_skip = 0</code> if no rows need to be skipped. 

<div id="ESR_para"></div>

4. <b>ESR_method : <i>int, optional</i></b><br>
   The method for ESR analysis. It is by default <b>(<code>ESR_method = True</code>)</b> that the ESR analysis will be carried out using method 2 (constant derivative). For all methods available please refer to the next session <a href="#method_table">ESR_method</a>. <code>ESR_setting = False</code> will return <code>.esr_ls</code> as <b>False</b> in the Supercap class. Available ESR_methods are: <code>ESR_methods = True, False, 1, 101, 2, 201. </code>


5. <b>setting : <i>float, optional</i></b><br>
   For <code>ESR_methods = True, 1, or 2 </code>, <code>setting = False</code>. For <code>ESR_methods = 101 or 201 </code>, setting is required as the number of points n/second derivative cut off point needed for the constant point method and the constant derivative method, respectively. If <code>ESR_methods = 101 or 201 </code> but <code>setting = False</code>, the function will promt the user to choose a specific value for the ESR analysis before proceeding. 


6. <b>plotting : <i>bool, optional</i></b><br>
   This argument determines whether the capacitance vs. current density plot will be plotted and saved. It is by default that <code>plotting = True </code>, and  the figure will be plotted and saved as 'Gravimetric specific capacitance vs. current density [datetime].png'. If <code>plotting = False </code>, the figure will not be plotted and saved.

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
    
## <a href="#sub_TOC">__init__(self, current,  t_V_ls, masses, cap_ls, esr_ls, extrema, cycle_n, m_error)</a> 
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
```
The above method follows the name of the Supercap variable. More details in the example section.


### Parameters
---

#### Arguments

<div id="path"></div>

1. <b>current : <i>float</i></b> <br>
    Current at which the GCD analysis is undertaken. The current is in mA.


2. <b>t_V_ls : <i>list, [[list of time readings], [list of voltage readings]]</i></b> <br>
   The raw data of the GCD analysis. 


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
    
## <a href="#sub_TOC">Show_dV2(self, cycle_check = False, setting = False)</a> 
Initialize from a :class:`.Supercap`.

### Notes
---
Visualising the second derivative and the charge/discharge curve of a specified cycle with the option of changing the ESR analysis method used for calculating esr_ls. <b>It is assumed that <code>ESR_method = 201</code> is used in this function.</b>

### Parameters
---

#### Arguments
1. <b>Cycle_check : <i>int, optional</i></b><br>
   The method for ESR analysis. Specify the cycle of the charge/discharge curve and the second derivative to be plotted on the same axes.If <code>Cycle_check = False</code>, the user will be prompted to select a cycle on the CD curve to view as the reference for adjusting the cut off point. 


2. <b>setting : <i>float, optional</i></b><br>
   In this case, setting should be the cut off second derivative.If <code>setting = False</code>, the user will be prompted to input the desired cut off derivative manually. For more details please refer to the example. 

#### Returns
1. A plot of charge discharge curve and the corresponding second derivative <br>
2. :class:`.Supercap`, optional
>self.esr_ls 


### Examples
---
```python
>>>Supercap1
<Class_Supercap: 3.0 mA, 1.0 V, 5 cycles, ESR method 2>
>>>Supercap1.Show_dV2(setting = 0.002)
Of which cycle would you like to see the second derivative? enter a number between 0 and 9
>>>0
```
![.Show_dV2() example](Supercap_pic/Show_dV2_1.png '.Show_dV2() example 1')
```python
Are you happy with the cut off point? (yes/no)
>>>no
Please input the value of desired cut off second derivative.
>>>1
```
![.Show_dV2() example](Supercap_pic/Show_dV2_2.png '.Show_dV2() example 2')
```python
Are you happy with the cut off point? (yes/no)
>>>yes
Do you wish to change the cut off point to the current value? (setting =1.0)
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
    
## <a href="#sub_TOC">Cap_vs_cycles(self, set_fig=False)</a> 
Initialize from a :class:`.Supercap`.

### Notes
---
Plotting capacitance against cycle and saving it as 'current mA_cap_vs_cycles_datetime.png'

### Parameters
---

#### Arguments
1. <b>set_fig : <i>bool, optional</i></b><br>
   If <code>set_fig = True</code>, the user will be prompted to change the setting of the figure.


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
![.Cap_vs_cycles() example](Supercap_pic/Cap_vs_cycles.png '.Cap_vs_cycles() example')

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
>The number of cycles, the average capacitance, the std of capacitance, the average ESR and its std 


### Examples
---
```python
>>>Supercap1.Get_info()
'The number of cycle(s) analysed is 9'
'The average capacitance is 24.028444381438409'
'The standard deviation of the average is 0.553348977252065'
'The average ESRs is 11.724686851851855'
'The standard deviation of the ESRs is 0.023315957315381737'
```

</div>

<br>
<br>

---
---


<div id="Check_analysis">
    
## <a href="#sub_TOC">Check_analysis(self, begin = False, end = False, save_fig = False)</a> 
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

  

   

3. <b>save_fig : <i>string, optional</i></b><br>

   For <code>save_fig=False</code>, the plot will not be saved.

   For <code>save_fig=True</code>, the plot will be saved as 'Check_analysis_[datetime].png'.

  

 

#### Returns

A plot of the charge/discharge curve with liniearly fitted slope and voltage drop.


### Examples
```python
>>>Supercap1.Check_analysis(begin = 0, end = 4, save_fig = False)
```
![.Check_analysis() example](Supercap_pic/Check_analysis.png '.Check_analysis() example')

</div>
