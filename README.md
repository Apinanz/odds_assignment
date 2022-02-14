# ODDS_Assignment Test Driven Development

Please follow these component before code!

* Class TestDrivenDevelopment
   1. funA is the first step of work. When the user inputs command of int, it will convert int to String. 
      * Ex. 1 = ‘Odd1’, 2 = ’Even2’, 3 = ’Odd3’, … 12 = ‘Odd1Even2’
      
   2. funB is the second step of work. It will take the result from funA convert String to String. 
      * Ex. ‘Odd1’ = ‘DDO1’, ‘Even2’ = ‘NEVE2’ … 12 = ‘DDO1NEVE2’
      
   3. funC is the third step of work. It will take the result from funB convert String to String of ASCII Code.
      * Ex. ‘DDO1’ = ‘6868791’, ‘NEVE2’ = ‘786986692’, … 12 = ‘6868791786986692’
      
   4. funD is the fouth step of work. It will take the result from funC convert String ASCII Code to String.
      * Ex. ‘6868791’=‘DDO1’, ‘786986692’=‘NEVE2’, … ‘6868791786986692’ = ‘DDO1NEVE2’
      
   5. funE is the five step of work. It will take the result from funD convert String to String.
      * Ex. ‘DDO1’ = ‘Odd1’, ‘NEVE2’ = ‘Even2’… ‘DDO1NEVE2’ = ‘Odd1Even2’
      
   6. funF is the last step of work. It will take the result from funE convert String to int.
      * Ex. ‘Odd1’ = 1, ’Even2’ = 2 , ’Odd3’ = 3, … ‘Odd1Even2’ = 12
    
* def calculator
    - This function compiles a list of all answers. 
    - This function works only when a command is entered via the GUI with the "order" parameter being the next handler.

* class MyWindow
    - This section is a GUI with fields for entering commands, displaying the result, and a button for Generate.

# How To Compile
There are 2 methods
1. Clone my project. You can compile it using the method of the program you use.
2. Online Python Compiler pass [replit_oods_assignment](https://replit.com/@Apinanz/TestDrivenDevelopment#main.py) using as follows
    - Press Run button
    - Input to command field [Only int,not more than 1 million]!!
    - Press Generate button. The program will show all the results.
            

    
    
      


