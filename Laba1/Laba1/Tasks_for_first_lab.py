from sympy import *

def Task_1_solve_the_equation(): 
    x = Symbol('x') 
    rooot=solve((x**3)+3*(x**2)-10*x+5, x) 
    print(rooot) 

def Task_2_work_with_file(filename): 
    filef=open(filename, 'r') 
    allFile=filef.read() 
    filef.close() 

    print(allFile) 

    filef=open(filename, 'w') 
    filef.write(allFile+allFile) 
    filef.close()

def Task_4_find_derivarive():
    x=Symbol('x') 
    y=Symbol('y')
    expr=sin(x)*cos(x**2)*tan(y)+ln(x)*sin(x)*cos(x**2)*tan(y)+ln(x)
    expr_dif=diff(expr, x) 
    print(simplify(expr_dif))