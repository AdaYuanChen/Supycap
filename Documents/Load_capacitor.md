[Go Back to Documentations](../README.md)
## <b>Load_capacitor</b><i>(pathway, t_set = False, V_set = False, mass_ls = False, current = False, row_skip = False, ESR_method = True, setting = False, cap_norm = False)</i>
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


2. <b>t_set : <i>int, optional</i></b> <br>
   An integer specifying the coloumn index for time(s) data, with the first coloumn being coloumn 0 starting from left. If t_set = False, column 0 will be used as time(s); if t_set = False, there will be prompt asking for time coloumn index to be entered.
   
   
3. <b>V_set : <i>int, optional</i></b> <br>
   An integer specifying the coloumn index for voltage(V) data, with the first coloumn being coloumn 0 starting from left. If V_set = False, column 1 will be used as Voltage(V); if t_set = False, there will be prompt asking for voltage coloumn index to be entered.
   
4. <b>mass_ls : <i>list, [[measurements of m1], [measurements of m2]], optional</i></b> <br>
   A list specifying the mass of each electrode in the format as shwon above. Multiple measurements for each electrode should be included for calculation of the uncertainty of the data. All masses should be recorded in <b>mg</b>. If mass_ls = False, a non-gravimetric capacitanc will be calculated and the function returns <i><code>[[False, False], [False, False]]</code></i> for the <code>.masses</code> method in the resulting Supercap entity (more details for extracting data from the Supercap class in <a href="#__init__">Supercap class>>init</a>


5. <b>current : <i> float, optional</i></b><br>
   If <b><code>current = False</code></b>, the current value will be directly read from the filename given that it is supplied in the format as specified above in the pathway section. If the current is not included the filename, it should be specified in the form of <code>current =<i>specified_current</i></code>


6. <b>row_skip : <i>int, optional</i></b><br>
   Number of the rows of headers to skip in the txt files. If <b><code>row_skip = False</code></b>, a prompt will ask for rows to skip for the file. Enter <code>row_skip = 0</code> if no rows need to be skipped. 

<div id="ESR_para"></div>

7. <b>ESR_method : <i>int, optional</i></b><br>
   The method for ESR analysis. It is by default <b>(<code>ESR_method = True</code>)</b> that the ESR analysis will be carried out using method 2 (constant derivative). For all methods available please refer to the next session <a href="#method_table">ESR_method</a>. <code>ESR_setting = False</code> will return <code>.esr_ls</code> as <b>False</b> in the Supercap class. Available ESR_methods are: <code>ESR_methods = True, False, 1, 101, 2, 201. </code>


8. <b>setting : <i>float, optional</i></b><br>
   For <code>ESR_methods = True, 1, or 2 </code>, <code>setting = False</code>. For <code>ESR_methods = 101 or 201 </code>, setting is required as the number of points n/second derivative cut off point needed for the constant point method and the constant derivative method, respectively. If <code>ESR_methods = 101 or 201 </code> but <code>setting = False</code>, the function will promt the user to choose a specific value for the ESR analysis before proceeding. 


9. <b>cap_norm : <i>bool, optional</i></b><br>
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
>>>Load_capacitor('./GCD/3.0_1.0V_010120.txt', t_set = 1, V_set = 3, mass_ls = [[12,13,12.2], [11, 10.5, 11.6]], current = 3, ESR_method = 2, setting = 0.1)
<Class_Supercap: 3.0 mA, 1.0 V, 5 cycles, ESR method 2>
```

[Next](Glob_analysis.md)


[Go Back to Documentations](../README.md)
