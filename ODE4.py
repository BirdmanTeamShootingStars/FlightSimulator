#This is Runge-Kutta method

import numpy as np
import matplotlib.pyplot as plt

def ODE4(t0,x0,r,func):
    k1 = func(t0,x0)*r
    k2 = func(t0+0.5*dt,x0+0.5*k1)*r
    k3 = func(t0+0.5*dt,x0+0.5*k2)*r
    k4 = func(t0+dt,x0+k3)*r
    k = (k1 + 2*k2 + 2*k3 + k4)/6
    return k

def func1(t,x):
    func1 = (x + np.sqrt(x*x + t*t))/t
    return func1


if __name__ == '__main__':
    dt = 0.20
    t0 = 1
    T = 11
    t = np.arange(t0,T+dt,dt)

    x0 = np.array([0])
    X = np.zeros((t.size,x0.size))
    X[0,:] = x0
    for n in range(t.size-1):
        X[n+1,:] = X[n,:] + ODE4(t[n],X[n,:],dt,func1)
    print(X)
