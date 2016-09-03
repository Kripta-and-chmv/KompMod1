from sympy import *

def Task_1_solve_the_equation(): 
    x = Symbol('x') 
    root=solve((x**3)+3*(x**2)-10*x+5, x) 
    print("The solve of the equation: ",root) 

def Task_2_work_with_file(filename): 
    filef=open(filename, 'r') 
    allFile=filef.read() 
    filef.close() 

    print("Text from file:", allFile) 

    filef=open(filename, 'w') 
    filef.write(allFile+allFile) 
    filef.close()

def Task_4_find_derivative():
    x=Symbol('x') 
    y=Symbol('y')
    expr=sin(x)*cos(x**2)*tan(y)+ln(x)*sin(x)*cos(x**2)*tan(y)+ln(x)
    expr_dif=diff(expr, x) 
    
    print("Derivative: ", simplify(expr_dif))

def Task_5_solve_integrals():
    x=Symbol('x') 
    y=Symbol('y') 

    func1=x*ln(x)
    func2=sin(x)/(x+1)

    undef_integr = integrate(func1, x)

    def_integr = integrate(func2,(x, 0, 1))

    print("Undefind integral :", undef_integr)
    print("Defind integral :", def_integr)