#!/usr/bin/python
import sympy
import scipy.integrate as si
import scipy.optimize as so
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
import random

def sortB(L):
    for i in range(0, len(L)):
        for j in range(0, len(L)):
            if (L[i] < L[j]):
                tmp = L[i]
                L[i] = L[j]
                L[j] = tmp

def main():
#1  slove non-linear equation
    print '1'
    f = lambda x: 5*x**3 - 7*x**2 + 8*x + 4
    r = so.newton(f, 0)
    print r
#2  read -> 2*text -> write
    print '2'
    f = open('file.txt', 'r')
    r = f.read()
    print r*2
    f2 = open('res.txt', 'w')
    f2.write(r*2)
    f.close()
    f2.close()
#3  bubble sort
    print '3'
    l = [8,4,9,2,0,5,6,2,3]
    print l
    sortB(l)
    print l
#4 difference sin(x)*cos^2(x)*tg(y) + ln(x)
    print '4'
    x, y = sympy.symbols('x y')
    f = sympy.sin(x)*sympy.tan(y)*sympy.cos(x)**2 + sympy.log(x)
    r = sympy.diff(f,x)
    print r
#5 integrate x*ln(x) and sin^2(x)/(x+1) from 0 to 1
    print '5'
    f = x*sympy.log(x)
    r = sympy.integrate(f, x)
    print r
    r = si.quad( lambda x: math.sin(x)**2/(x+1),  0, 1)
    print r[0]
#6  create plot sin^2(x)**2(1+x)
    f = lambda x: np.sin(x)**2/(x+1)
    x = np.linspace(0, 50, 500) #?,X width, glad

    fig, ax = plt.subplots()
    line1 = ax.plot(x, (np.sin(x)**2)/(1.0+x), '-', linewidth=2,
                    label='sin^2(x)/(1+x)')

    line2 = ax.plot(np.arange(50), [0.0 for x in range(50)], 'rs',  label='')
    
    ax.legend(loc='upper right')
    plt.show()
#7 create hystogramm [0;1),[1;2)...,[7;8)
# [5, 4, 2, 7, 0, 3, 3, 4]
    fig, ax = plt.subplots()
    x = [ 10000*random.random() for i in range(500)]
    n, bins, patches = ax.hist(x, 8, normed=1)

    # add a 'best fit' line
    ax.set_xlabel('Books')
    ax.set_ylabel('Words')
    ax.set_title(r'Histogram')

    fig.tight_layout() # white
    plt.show()

main()
