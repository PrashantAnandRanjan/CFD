#!/usr/bin/env python
# coding: utf-8

# In[8]:

#...................................


import numpy
from matplotlib import pyplot
import math
import sympy
get_ipython().run_line_magic('matplotlib', 'inline')

#.......funtion declaration
def B(m):
    
    b = []

    for i in range(1, m + 1):
        eq = x**(i-1)
        k = float(sympy.integrate(eq, (x, 0, 1)))
        b.append(k)
        
    return b

def A(m, n):
    
    a = []
    
    for i in range(1, m + 1):
        an = []
        for j in range(1, n + 1):
            eq = x**(i-1) * (j * x**(j-1) - x**j)
            k = float(sympy.integrate(eq, (x, 0, 1)))
            an.append(k)
        a.append(an) 
    
    return a

#.......Main program 
n = 50                                                 #For the number of points in the plot
x = sympy.Symbol('x')
N = [1, 2, 3, 4, 5, 6, 7]
for m in N:
    #........Common Variable declaration
    print("\n\t\t>>>>>>>>>>>>>>>>>>>>>", m, "<<<<<<<<<<<<<<<<<<<<<<<")
    an = A(m, m)                                      #For the matrix A
    bn = B(m)                                         #For the matrix B
    a = numpy.linalg.solve(an, bn)                    #Solving inv(A).B
    print("Using a = inv(A).B\nWhere A = \n",numpy.array(an),"\nB = ",bn,"\nWe obtained 'a' = ",a)
    
    y = [0] * n                                       #Exact value of 'y'
    yn = y.copy()                                     #Approximated value of 'y'
    xn = numpy.linspace(0, 1, n)

    #........Exact plot for the given funtion
    for i in range(n):
        y[i] = math.exp(xn[i])
    
    #.......Approximated plot for the given funtion
    for i in range(n):
        k = 0                                          #Temperary storing variable
        for j in range(m):
            k = k + a[j] * xn[i]**(j + 1)
        yn[i] = 1 + k 

    #.......Calculating error
    er = []                                            #Error yn - y
    for i in range(n):
        er.append(yn[i] - y[i])
        
    #......Plots
    pyplot.figure(figsize = (8, 4), dpi = 100)
    pyplot.plot(xn, y,'g', label = 'Exact')
    pyplot.plot(xn, yn,'y--', label = 'Approximated')
    pyplot.title(('Approximate and Exact Solution for N ',m))
    pyplot.legend(loc = 'upper left')
    pyplot.xlabel('X')
    pyplot.ylabel('Y')
    pyplot.figure(figsize = (8, 4), dpi = 100)
    pyplot.plot(xn, er, marker = '.', label = ('Error for N = ', m))
    pyplot.title('Error -- [Y(Approximated) - Y(Exact)]')
    pyplot.xlabel('X')
    pyplot.ylabel('Y (approx) - Y (exact)')
    pyplot.legend(loc = 'upper left')
    print("\n\t\t------------------------------------------------")
    


# In[ ]:




