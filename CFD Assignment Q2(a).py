#!/usr/bin/env python
# coding: utf-8

# In[13]:


#...................................


import numpy
from matplotlib import pyplot
import math
get_ipython().run_line_magic('matplotlib', 'inline')

#.......Main body
t = [2.1, .6, .1]                                              #Step Size
l = -1                                                         #value of lambda                               
for dt in t:
    xn = numpy.arange(0, 5 + dt, dt)
    y = [0] * len(xn)
    #.......Actual solution
    for i in range(len(xn)):
        y[i] = math.exp(-xn[i])
    

    #.......Explicit Euler
    ya = [0] * len(xn)
    ya[0] = 1
    for i in range(len(xn) - 1):
        ya[i + 1] = ya[i] + dt * (l * ya[i])

    #......Implicit Euler solution
    yb = [0] * len(xn)
    yb[0] = 1

    for i in range(len(xn) - 1):
        yb[i + 1] = yb[i] / (1 - dt*l)

    #......Crank-Nicolson Method
    yc = [0] * len(xn)
    yc[0] = 1

    for i in range(len(xn) - 1):
        yc[i + 1] = (2 * yc[i] + dt * (l * yc[i])) / (dt + 2)

    #......Low Storage RKW3
    yd = [0] * len(xn)
    yd[0] = 1
    yr = [0] * len(xn)
    for i in range(len(xn) - 1):
        #....1st RK
        yr[i] = yd[i]
        k1 = l * yr[i]
        #....2nd RK
        yr[i] = yr[i] + dt * k1 / 3
        k1 = (-5/9) * k1 + (l * yr[i])
        #....3rd RK
        yr[i] = yr[i] + (15/16) * dt * k1
        k1 = (-153/128) * k1 + (l * yr[i])
        
        yd[i + 1] = yr[i] + (8/15) * dt * k1
          
    
    #......Plot all the graphs   
    pyplot.figure(figsize  = (10, 8), dpi = 100)
    pyplot.plot(xn, y,'g', marker = '', label = 'Actual plot')
    pyplot.plot(xn, ya,'bo--', marker  = '.', label = 'Explicit Euler')
    pyplot.plot(xn, yb,'ro--', marker  = '.', label = 'Implicit Euler')
    pyplot.plot(xn, yc,'mo--', marker  = '.', label = 'C-N Method')
    pyplot.plot(xn, yd,'yo--', marker  = '.', label = 'Low Storage RK3')
    pyplot.title(('Approximate and Exact Solution for dt = ', dt))
    pyplot.xlabel('Time')
    pyplot.ylabel('f(x)')
    pyplot.legend()


# In[ ]:




