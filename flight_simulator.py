from math import *
import numpy as np
import param
from State import *
import matplotlib.pyplot as plt

#ordinary differential equation
def func(state, alpha):
    return state.dt(alpha)


def runge_kutta(state0, dt, t_list, alpha_list, func):
    state_list = [state0]
    for i in range(t_list.size):
        k1 = func(state_list[i], alpha_list[i])*dt
        k2 = func(state_list[i]+k1*0.5, alpha_list[i])*dt
        k3 = func(state_list[i]+k2*0.5, alpha_list[i])*dt
        k4 = func(state_list[i]+k3, alpha_list[i])*dt
        k = (k1 + k2*2 + k3*2 + k4)/6
        state_list.append(state_list[-1] + k)

    return state_list

#show a graph of trajectory
def plot_state_list(state_list):
    x = []
    y = []
    for state in state_list:
        x.append(state.x)
        y.append(state.y)

    plt.plot(x,y)
    plt.ylabel('height')
    plt.title('trajectory')
    plt.axes().set_aspect('equal','datalim')
    plt.show()

if __name__ == '__main__':
    state0 = State(1.,5.,1.,1.,1.) #initial state of plane
    dt = 0.1
    t0 = 0
    end_t = 15
    t_list = np.arange(t0,end_t+dt,dt)
    alpha_list = np.zeros(t_list.size)
    state_list = runge_kutta(state0,dt,t_list,alpha_list,func)
    plot_state_list(state_list)
