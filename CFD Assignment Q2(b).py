#!/usr/bin/env python
# coding: utf-8

# In[5]:

#...................................


import numpy
from matplotlib import pyplot
import math
get_ipython().run_line_magic('matplotlib', 'inline')

#........Defining Funtion
def fx(t):
    w = 1
    phi0 = 1
    t0 = 0
    phi = phi0 * math.cos(w * (t - t0))
    return -phi

#.......Main body
n = [2.1, .6, .1]                                           #Step size

for dt in n:
    t = numpy.arange(0, 10 + dt, dt)
    y = [0] * len(t)
    
    #......Actual solution
    for i in range(len(t)):
        y[i] = -fx(t[i])

    #.......Explicit Euler
    ya1 = [0] * len(t)
    ya2 = ya1.copy()
    ya1[0] = 1
    ya2[0] = 0
    
    for i in range(len(t) - 1):
        ya1[i + 1] = ya1[i] + dt * ya2[i]
        ya2[i + 1] = ya2[i] + dt * fx(t[i])
        
    #......Implicit Euler solution
    yb1 = [0] * len(t)
    yb2 = yb1.copy()
    yb2[0] = 0
    yb1[0] = 1

    for i in range(len(t) - 1):
        yb1[i + 1] = yb1[i] + dt * yb2[i]
        yb2[i + 1] = yb2[i] + dt * fx(t[i + 1])
        
    #......Crank-Nicolson Method
    yc1 = [0] * len(t)
    yc2 = yc1.copy()
    yc1[0] = 1
    yc2[0] = 0

    for i in range(len(t) - 1):
        yc1[i + 1] = yc1[i] + dt * yc2[i]
        yc2[i + 1] = yc2[i] + (dt / 2) * (fx(t[i]) + fx(t[i + 1]))
        
    #......Plot all the graphs   
    pyplot.figure(figsize  = (10, 8), dpi = 100)
    pyplot.plot(t, y,'g', marker = '', label = 'Actual plot')
    pyplot.plot(t, ya1,'bo--', marker  = '.', label = 'Explicit Euler')
    pyplot.plot(t, yb1,'ro--', marker  = '.', label = 'Implicit Euler')
    pyplot.plot(t, yc1,'mo--', marker  = '.', label = 'C-N Method')
    pyplot.title(('Approximate and Exact Solution for dt = ', dt))
    pyplot.xlabel('Time')
    pyplot.ylabel('f(x)')
    pyplot.legend(loc  = 'upper left')


# In[ ]:





# In[ ]:




