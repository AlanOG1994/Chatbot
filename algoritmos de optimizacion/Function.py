# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:15:00 2020

@author: Alan
"""
from math import pi
import numpy as np
def verif(X):
    if np.size(X)<3:
        x=X[0]
        y=X[1]
    else:
        x=X[:,0]
        y=X[:,1]
    return x,y

def F1(X):#Rastrigin
    x,y=verif(X)
    z=10*2 + pow(x,2)+pow(y,2) - 10*(np.cos(x)+np.cos(y))
    return z
def F2(X):#función Ackley
    x,y=verif(X)
    z=-20*np.exp(-0.2*np.sqrt(.5*(pow(x,2)+pow(y,2))))-np.exp(0.5*(np.cos(2*pi*x)+np.cos(2*pi*y)))+np.exp(1)+20
    return z
def F3(X):#sphere function
    x,y=verif(X)
    z=pow(x,2)+pow(y,2)
    return z
def F4(X):#Rosenbrock
    x,y=verif(X)
    z=100*pow(y-pow(x,2),2)+ pow(1-x,2)
    return z
def F5(X):#Beale 
    x,y=verif(X)
    z=pow(1.5-x+ np.multiply(y,x),2)+pow(2.25-x+np.multiply(pow(y,2),x),2)+pow(2.625-x+np.multiply(pow(y,3),x),2)
    return z
def F6(X):#función Goldstein-precio
    x,y=verif(X)
    z1=1+np.multiply(pow(x+y+1,2),19-14*x+3*pow(x,2)-14*y+6*np.multiply(x,y)+3*pow(y,2))
    z2=30 +np.multiply(pow(2*x-3*y,2),18-32*x+12*pow(x,2)+48*y-36*np.multiply(x,y)+27*pow(y,2))
    z=np.multiply(z1,z2)
    return z
def F7(X):#función de stand
    x,y=verif(X)
    z=pow(x+2*y-7,2)+pow(2*x+y-5,2)
    return z
def F8(X):#Función Bukin N.6
    x,y=verif(X)
    z= 100*np.sqrt(np.absolute(y-0.01*pow(x,2)))+0.01*np.absolute(x+10)
    return z
def F9(X):#function Matyas
     x,y=verif(X)
     z=.26*(pow(x,2)+pow(y,2))+ np.multiply(x,y)*.48
     return z
def F10(X):#Lévi N.13
    x,y=verif(X)
    z=pow(np.sin(3*pi*x),2)+np.multiply(pow(x-1,2),1+pow(np.sin(3*pi*y),2))+np.multiply(pow(y-1,2),1+pow(np.sin(2*pi*y),2))
    return z
def F11(X):#Himmelblau;
    x,y=verif(X)
    z=pow(pow(x,2)+y-11,2)+pow(pow(y,2)+y-7,2)
    return z
def F12(X):#la función de camellos tres joroba
    x,y=verif(X)
    z=2*pow(x,2)+1.05*pow(x,4)+pow(x,6)/6+np.multiply(x,y)+pow(y,2)
    return z
def F13(X):#función Easom
    x,y=verif(X)
    z1=-np.multiply(np.cos(x),np.cos(y))
    z=np.multiply(z1,np.exp(-pow(x-pi,2)-pow(y-pi,2)))
    return z
def F14(X):#Cross-en-bandeja función
    x,y=verif(X)
    z1=np.multiply(np.sin(x),np.sin(y))
    z2=np.exp(np.abs(100-np.sqrt(pow(x,2)+pow(y,2))/pi))
    z=-.0001*pow(np.abs(np.multiply(z1,z2))+1,.1)
    return z
def F15(X):#función eggholder
    x,y=verif(X)
    a=np.sin(np.sqrt(np.abs(x/2+y+47)))
    b=np.sin(np.sqrt(np.abs(x-y+47)))
    z=np.multiply(y+27,a)-np.multiply(x,b)
    return z
def F16(X):#función de la tabla del sostenedor
    x,y=verif(X)
    z1=np.multiply(np.sin(x),np.cos(y))
    z2=np.exp(np.abs(1-np.sqrt(pow(x,2)+pow(y,2))/pi))
    z=-np.abs(np.multiply(z1,z2))
    return z
def F17(X):#función de McCormick
    x,y=verif(X)
    z=np.sin(x+y)+pow(x-y,2)-1.4*x+2.5*y+1
    return z
def F18(X):#función Schaffer N. 2
    x,y=verif(X)
    a=pow(np.sin(pow(x,2)-pow(y,2)),2)-0.5
    b=pow(1+.0001*(pow(x,2)+pow(y,2)),2)
    z=.5+ np.divide(a,b)
    return z
def F19(X):#función Schaffer N. 4
    x,y=verif(X)
    a1=np.sin(np.abs(pow(x,2)-pow(y,2)))
    a=pow(np.cos(a1),2)-0.5
    b=pow(1+.0001*(pow(x,2)+pow(y,2)),2)
    z=.5+ np.divide(a,b)
    return z
def F20(X):#función Styblinski-Tang
    x,y=verif(X)
    z=(pow(x,4)-16*pow(x,2)+5*x+pow(y,4)-16*pow(y,2)+5*y)*.5
    return z