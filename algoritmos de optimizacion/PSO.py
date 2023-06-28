# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:19:22 2020

@author: Alan
"""

import random
import numpy as np
from Function import F14 as ObjectFun
import matplotlib.pyplot as plt

    
a=-5
b=5
N=40
X = b - (b-a)*np.random.rand(N,2)
t=np.random.rand(3, 2)
c1=0.5
c2=0.5
MaxIter=200
w=0.5
# Evaluacion
itera=1
voisinage = 5
veloc = 0.05
G=1e10
while itera<MaxIter:
    
    Loc=ObjectFun(X)
    indx0 = np.argsort(Loc)
    gbest=X[indx0[0]]
   
    for i in range(N):
        dist=np.sqrt(np.sum(pow(X[i,:]-X,2),1))
        indx=np.argsort(dist)
        Xv=X[indx[0:voisinage],:]
        LocV=Loc[indx[0:voisinage]]
        indx1=np.argsort(LocV)
        pbest=Xv[indx1[0]]
        veloc=w*veloc+c1*np.random.rand()*(pbest-X[i])+c2*np.random.rand()*(gbest-X[i])
        X[i]=X[i]+veloc
        
    itera=itera+1
    
print(gbest)

#np.multiply(b,a)
    