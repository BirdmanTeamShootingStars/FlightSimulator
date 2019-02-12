from math import *
import numpy as np
import param
from State import *
   
#ordinary differential equation
def func(state,t,dt):
    return state.dt(dt)

def runge_kutta(t0,state0,end_t,dt,func):
    t_list = np.arange(t0,end_t+dt,dt)
    state_list = [state0]
    for t in t_list:
        

if __name__ == '__main__':
    state0 = State(1.,1.,1.,1.,1.)
    dt = 0.1
    t0 = 0
    end_t = 15
    runge_kutta(t0,state0,end_t,dt,func)
