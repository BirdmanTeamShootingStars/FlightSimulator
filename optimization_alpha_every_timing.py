#optimize with respect to all element of alpha_list
#we chose Gradient descent as an algorithm
#
#i.e.  optimize alpha of every timing

import param
from flight_simulator import *
from file_func import *


dt = 0.05
t_list = np.arange(0, 15, dt)

#objective function
def obj_func(alpha_list):
    state_list = runge_kutta(param.STATE0, dt, t_list, alpha_list)
    return 1 # To be implemented
    
#derivative function of objective function
#for optimization of alpha_list for every timing
def grad_obj_func1(alpha_list):
    result_list = np.zeros(len(alpha_list))
    for i in range(len(alpha_list)):
        alpha_list_plus = alpha_list;
        alpha_list_plus[i] += 0.01
        alpha_list_minus = alpha_list;
        alpha_list_minus[i] -= 0.01
        result_list[i] = (obj_func(alpha_list_plus)-obj_func(alpha_list_minus))/(2*0.01)

    return result_list


#calculate norm**2 of vec
def calc_norm2(vec):
    norm2 = 0
    for x in vec:
        norm2 += x**2
    return norm2

#backtracking
#n is number of variables to be optimized
def cal_step_size(alpha_list):
    step_size = 1 #initial step size
    xi = 0.0001
    rho = 0.8 #To be reviewd
    grd = grad_obj_func1(alpha_list)
    
    norm2 = calc_norm2(grd)
    
    #use Armijo condition
    while (obj_func(alpha_list + step_size*grd) > obj_func(alpha_list) + xi*step_size*norm2):
        step_size *= rho
        
    return step_size

    
def main():
    alpha_list = np.zeros(len(t_list))
    epsilon = len(alpha_list)*0.000001
    
    #optimization
    for i in range(100):
        grd = grad_obj_func1(alpha_list)
        if (calc_norm2(grd) <= epsilon**2):
            print("Find best operation!")
            break;

        alpha_list += calc_step_size(alpha_list)*grd

    print("Cost is", obj_func(alpha_list))
    state_list = runge_kutta(param.STATE0,dt,t_list,alpha_list)
    plot_state_list(state_list)
    store_trajectory(t_list,state_list,alpha_list,'./data/best_operation_every_alpha.csv')

if __name__ == '__main__':
    main()
    
