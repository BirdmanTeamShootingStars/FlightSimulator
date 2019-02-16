#In this program, it is assumed that a pilot change alpha only twice.
#For the first time, he change alpha from 0 degrees
#to someting, And for the second time,he changes it from something to 0 degrees.
#
#optimize with respect to 
#we chose Gradient descent as an algorithm
#

import param
from flight_simulator import *
from file_func import *


dt = 0.05
t_list = np.arange(0, 15, dt)

#objective function
def obj_func(t1, t2, alpha):
    alpha_list = np.zeros(len(t_list))
    for i in range(len(t_list)):
        if (t_list[i]<t1 or t_list[i]>t2):
            continue;
        
        alpha_list[i] = alpha
        
    state_list = runge_kutta(param.STATE0, dt, t_list, alpha_list)
    return 1 # To be implemented
    
#derivative function of objective function
def grad_obj_func1(t1, t2, alpha):
    result_list = np.zeros(3)

    result_list[0] = (obj_func(t1+dt, t2, alpha) - obj_func(t1-dt, t2, alpha))/(2*dt)
    result_list[1] = (obj_func(t1, t2+dt, alpha) - obj_func(t1, t2-dt, alpha))/(2*dt)
    result_list[2] = (obj_func(t1, t2, alpha+0.3) - obj_func(t1, t2, alpha-0.3))/(2*dt)
    
    return result_list


#calculate norm**2 of vec
def calc_norm2(vec):
    norm2 = 0
    for x in vec:
        norm2 += x**2
    return norm2

#backtracking
#n is number of variables to be optimized
def cal_step_size(t1, t2, alpha):
    step_size = 1 #initial step size
    xi = 0.0001
    rho = 0.8 #To be reviewd
    grd = grad_obj_func1(t1, t2, alpha)
    
    norm2 = calc_norm2(grd)
    
    #use Armijo condition
    while (obj_func(t1+grd[0], t2+grd[1], alpha+grd[2]) > obj_func(t1, t2, alpha) + xi*step_size*norm2):
        step_size *= rho
        
    return step_size

    
def main():
    alpha = radians(5)
    t1 = 3
    t2 = 8
    epsilon = 3*0.000001
    
    #optimization
    for i in range(100):
        grd = grad_obj_func1(t1, t2, alpha)
        if (calc_norm2(grd) <= epsilon**2):
            print("Find best operation!")
            break;

        var_list += calc_step_size(t1, t2, alpha)*grd

    print("Cost is", obj_func(t1, t2, alpha))

    alpha_list = np.zeros(len(t_list))
    for i in range(len(t_list)):
        if (t_list[i]<t1 or t_list[i]>t2):
            continue;
        
        alpha_list[i] = alpha
        
    
    state_list = runge_kutta(param.STATE0,dt,t_list,alpha_list)
    plot_state_list(state_list)
    store_trajectory(t_list,state_list,alpha_list,'./data/best_operation_every_alpha.csv')

if __name__ == '__main__':
    main()
    
