import sympy 

def Task_1_solve_the_equation(): 
    x = sympy.Symbol('x') 
    rooot=sympy.solve((x**3)+3*(x**2)-10*x+5, x) 
    print(rooot) 

def Task_2_work_with_file(filename): 
    filef=open(filename, 'r') 
    allFile=filef.read() 
    filef.close() 

    print(allFile) 

    filef=open(filename, 'w') 
    filef.write(allFile+allFile) 
    filef.close()