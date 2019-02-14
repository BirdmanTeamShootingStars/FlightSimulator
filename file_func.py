import pandas as pd
from State import *

def trajectory2df(t_list, state_list, alpha_list):
    x_list = []
    vx_list = []
    y_list = []
    vy_list = []
    theta_list = []
    for state in state_list:
        x_list.append(state.x)
        vx_list.append(state.vx)
        y_list.append(state.y)
        vy_list.append(state.vy)
        theta_list.append(state.theta)

    return pd.DataFrame({'t' : x_list, 'x' : x_list,
                         'vx' : vx_list,'y' : y_list,
                         'vy' : vy_list, 'theta' : theta_list,
                         'alpha' : alpha_list})

def store_trajectory(t_list, state_list, alpha_list,file_path):
    trajectory2df(t_list, state_list, alpha_list).to_csv(file_path)

def load_csv(file_path):
    df = pd.read_csv(file_path)
    t_list = df['t'].values
    alpha_list = df['alpha'].values
    state_list = []
    for i in range(len(t_list)):
        state_list.append(State(df['x'].values[i], df['vx'].values[i],
                                df['y'].values[i], df['vy'].values[i],
                                df['theta'].values[i]))

    return t_list, state_list, alpha_list
