# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:09:29 2020

@author: Alan
"""
import random
import numpy as np
from Function import F20 as Fn 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def init(Xrange,N):
    b=Xrange[:,0]
    a=Xrange[:,1]
    X = b - (b-a)*np.random.rand(N,2)
    return X
def mutacion(X,F,N):
    a=X.shape[0]
    b=X.shape[1]
    V=np.zeros((a,b))
    t = np.arange(N)
    t2=np.arange(N)
    for i in range(N):
        j=t[i]
        k=t2[i]
        while i==k:
             k=random.randint (0,a-1)
        V[i]=X[i]+F*(X[j]-X[k])
    return V

def Recombinacion(X,V,D,N,CR):
    LG1=1*(np.random.rand(N,2)<=CR)
    LG2=1*(np.random.rand(2,N).round()==[[0],[1]])
    LG=np.multiply(LG1,LG2.T)
    U=np.multiply(LG,V)+np.multiply(1-LG,V)
    return U

def Seleccion(X,U,N,F):
    a=X.shape[0]
    b=X.shape[1]
    S=np.zeros((a,b))
    for i in range(N):
        if Fn(X[i])>Fn(U[i]):
            S[i]=U[i]
        else:
            S[i]=X[i]
            
    return S


F=0.1
CR=0.2
N=20 #Poblacion
D=2  #Individuos
Xrange=np.array([[-10,10],[-10,10]]) #rango de busqueda
NG=800 #generaciones 
X=init(Xrange,N)# Poblacion inicial
G2=X
d=Fn(X[2])
for i in range(NG):
    V=mutacion(X,F,N)
    U=Recombinacion(X,V,D,N,CR)
    X=Seleccion(X,U,N,F)

best=np.argsort(Fn(X))

a1=-10
a2=-10
b1=10
b2=10
G=X
k=X[best[0]]
ax = plt.axes(projection='3d')
x = np.linspace(a1,b1, 200)
y = np.linspace(a2,b2, 200)
X, Y = np.meshgrid(x, y)

X1= np.zeros((np.size(X),2))
X1[:,0]=X1[:,0]+X.flatten()
X1[:,1]=X1[:,1]+Y.flatten()
Z1 =Fn(X1)
Z=Z1.reshape(len(X),len(X))
# Plot the figure
ax.plot_wireframe(X, Y, Z, linewidth=0.2)
# Plot the minimum value
ax.scatter(G[:,0],G[:,1], Fn(G), 'o', color='red')
ax.scatter(G2[:,0],G2[:,1], Fn(G2), 'o', color='black')
plt.show()

print('Minimo encontrado en ')
print(k)