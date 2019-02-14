from math import *
import numpy as np
import param
from State import *
import matplotlib.pyplot as plt
from file_func import *

#ordinary differential equation
def func(state, alpha):
    return state.dt(alpha)

def runge_kutta(state0, dt, t_list, alpha_list):
    state_list = [state0]
    for i in range(len(t_list)-1):
        k1 = func(state_list[i], alpha_list[i])*dt
        k2 = func(state_list[i]+k1*0.5, alpha_list[i])*dt
        k3 = func(state_list[i]+k2*0.5, alpha_list[i])*dt
        k4 = func(state_list[i]+k3, alpha_list[i])*dt
        k = (k1 + k2*2 + k3*2 + k4)/6
        state_list.append(state_list[-1] + k)

    return state_list

#show a graph of trajectory
def plot_state_list(state_list):
    x_list = np.zeros(len(state_list))
    y_list = np.zeros(len(state_list))

    for i in range(len(state_list)):
        x_list[i] = state_list[i].x
        y_list[i] = state_list[i].y

    plt.plot(x_list,y_list)
    plt.ylabel('height')
    plt.title('trajectory')
    plt.axes().set_aspect('equal','datalim')
    plt.show()

if __name__ == '__main__':
    state0 = param.STATE0
    dt = 0.1
    t0 = 0
    end_t = 15
    t_list = np.arange(t0,end_t+dt,dt)
    alpha_list = np.zeros(len(t_list))
    state_list = runge_kutta(state0,dt,t_list,alpha_list)
    #store_trajectory(t_list,state_list,alpha_list,'./data/let_it_be.csv')
    plot_state_list(state_list)
