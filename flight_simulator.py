from math import *
import numpy as np
import param
from State import *
   
#ordinary differential equation
def func(state,alpha,dt):
    return state.dt(dt,alpha)


def runge_kutta(state0,dt,t_list,alpha_list,func):
    state_list = [state0]
    for i in range(t_list.size):
        state_list.append(state_list[-1] + func(state_list[-1],alpha_list[i],dt)*dt)

    return state_list


if __name__ == '__main__':
    state0 = State(1.,1.,1.,1.,1.) #initial state of plane
    dt = 0.1
    t0 = 0
    end_t = 15
    t_list = np.arange(t0,end_t+dt,dt)
    alpha_list = np.zeros(t_list.size)
    state_list = runge_kutta(state0,dt,t_list,alpha_list,func)
    for state in state_list:
        print(state.y)
