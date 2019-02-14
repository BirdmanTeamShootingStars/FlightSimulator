import param
from flight_simulator import *

#objective function
def obj_func(alpha_list):
    dt = 0.01
    t_list = np.arange(0, 15, dt)
    state_list = runge_kutta(param.STATE0, dt, t_list, alpha_list)

#derivative function of objective function
def grad_obj_func(alpha_list):
    result_list = np.zeros(len(alpha_list))
    for i in range(len(alpha_list)):
        alpha_list_plus = alpha_list;
        alpha_list_plus[i] += 0.01
        alpha_list_minus = alpha_list;
        alpha_list_minus[i] -= 0.01
        result_list[i] = (obj_func(alpha_list_plus)-obj_func(alpha_list_minus))/(2*0.01)

    return result_list


