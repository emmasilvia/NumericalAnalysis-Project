# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:42:23 2022

@author: Cris
"""
from scipy.optimize import fsolve
from sympy import *
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
from scipy.optimize import minimize_scalar
from matplotlib import pyplot as plt
import numpy as np

#METODE BISECTIE
def bisectie_err(f,a,b,err):
    while (b-a)/2>err:
        x=(a+b)/2
        if f(x)==0:
            return x
        elif f(a)*f(x)<0:
            b=x
        else: a=x
    return x

def bisectie_it(f,a,b,it):
    for i in range(it):
        x=(a+b)/2
        if f(x)==0:
            return x
        elif f(a)*f(x)<0:
            b=x
        else: 
            a=x
    return x

#METODE TANGENTE
def tangenta_err(f, a, b, err):
    x=Symbol("x")
    f1 = diff(f, x)
    f2 = diff(f, x, 2) 
    f = lambdify(x, f) 
    abs_f1 = 'abs('+str(f1)+')'
    abs_f2 ='1/(abs('+str(f2)+'))'
    f1l = lambdify(x, f1)
    f2l = lambdify(x, f2)
    abs_f1l = lambdify(x, abs_f1)
    abs_f2l = lambdify(x, abs_f2)
    m = minimize_scalar(abs_f1l, bounds = (a, b), method = 'bounded')
    m1 = m.fun
     
    mm = minimize_scalar(abs_f2l, bounds = (a, b), method = 'bounded')
    m2 = (-1)*m.fun
    
    x= np.random.rand()*(b-a)+a
    x_ant = 0
    i=0
    
    while f(x)*f1l(x)<=0:
       x= np.random.rand()*(b-a)+a
       while m2/(2*m1)*abs(x-x_ant)**2 > err:
            x_ant = x
            x = x - f(x)/f1l(x)
            i+=1
    print(i)
    return x

def tangenta_it(f, a, b, n):
    x = Symbol('x')
    f1 = diff(f, x) 
    f2 = diff(f, x, 2) 
    f = lambdify(x, f) 
    abs_f1 = 'abs('+str(f1)+')'
    abs_f2 ='1/(abs('+str(f2)+'))'
    f1l = lambdify(x, f1)
    f2l = lambdify(x, f2)
    abs_f1l = lambdify(x, abs_f1)
    abs_f2l = lambdify(x, abs_f2)
    m = minimize_scalar(abs_f1l, bounds = (a, b), method = 'bounded')
    mm = minimize_scalar(abs_f2l, bounds = (a, b), method = 'bounded')
    m2 = (-1)*m.fun

    x= np.random.rand()*(b-a)+a
    x_ant = 0
    i=0
    
    while f(x)*f1l(x)<=0:
        x= np.random.rand()*(b-a)+a
        for i in range (1,n):
            x_ant = x
            x = x - f(x)/f1l(x)
   
    return x

#METODE COARDA

def coarda_err(f,a,b,err):
    x=Symbol('x')
    f1=diff(f,x)
    f2=diff(f,x,2)
    f=lambdify(x,f)
    abs_f1='abs(' +str(f1)+')'
    f1l=lambdify(x, f1)
    f2l=lambdify(x,f2)
    abs_f1l=lambdify(x, abs_f1)
    m=minimize_scalar(abs_f1l,bounds=(a,b),method='bounded')
    m1=m.fun
    i=0
    if f(a)*f2l(a)<0:
        x=a
        while (abs(f(x))/m1)>err:
            x=x-f(x)/(f(x)-f(b))*(x-b)
            i+=1
    else:
        x=b
        while (abs(f(x))/m1)>err:
            x=x-f(x)/(f(x)-f(a))*(x-a)
    print(i)
    return x

def coarda_it(f,a,b,n):
    x=Symbol('x')
    f1=diff(f,x)
    f2=diff(f,x,2)
    f=lambdify(x,f)
    abs_f1='abs(' +str(f1)+')'
    f1l=lambdify(x, f1)
    f2l=lambdify(x,f2)
    abs_f1l=lambdify(x, abs_f1)
    m=minimize_scalar(abs_f1l,bounds=(a,b),method='bounded')
    m1=m.fun
    if f(a)*f2l(a)<0:
        x=a
        for i in range (n):
            x=x-f(x)/(f(x)-f(b))*(x-b) 
    else:
        x=b
        for i in range(n):
            x=x-f(x)/(f(x)-f(a))*(x-a)    
    return x

#METODE CONTRACTII
def contractii_err(g, a, b, err):
    x=Symbol('x')
    g1=diff(g, x)
    abs_g1='(-1)*abs('+str(g1)+')'
    abs_g1l=lambdify(x, abs_g1)
    m=minimize_scalar(abs_g1l, bounds=(a, b), method='bounded')
    m1=(-1)*m.fun
    alfa=m1
    g = lambdify(x, g)
    x0=np.random.rand()*(b-a)+a
    x1=g(x0)
    ev=(alfa/(1-alfa))*abs(x0 - x1)
    while err<ev:
        x1=g(x1)
        ev*=alfa
    return x1

def contractii_it(g, a, b,n):
   x=Symbol('x')
   
   g = lambdify(x, g)
   x=np.random.rand()*(b-a)+a
   for i in range(1, n + 1):
       x1=g(x)
   return x


# def main():
#     x=Symbol("x")
#     f1 = diff(f, x)
#     f2 = diff(f, x, 2) 
#     f = lambdify(x, f) 
#     abs_f1 = 'abs('+str(f1)+')'
#     abs_f2 ='1/(abs('+str(f2)+'))'
#     f1l = lambdify(x, f1)
#     f2l = lambdify(x, f2)
#     abs_f1l = lambdify(x, abs_f1)
#     abs_f2l = lambdify(x, abs_f2)
#     x_val =np.linspace(a, b,n)
#     plt.plot(x_val,f1l(x_val))
#     m = minimize_scalar(abs_f1l, bounds = (a, b), method = 'bounded')
#     m1 = m.fun
     
#     mm = minimize_scalar(abs_f2l, bounds = (a, b), method = 'bounded')
#     m2 = (-1)*m.fun
    
#     if __name__=='__main__':
#         main()

