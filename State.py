from math import *
import param
from D_State import *

class State():
    def __init__(self,x,vx,y,vy,theta):
        self.x = x
        self.vx = vx
        self.y = y
        self.vy = vy
        self.theta = theta
        self.phai = theta - atan(-vy/vx)
        self.size = 5
        
    def calc_phai(self):
        return theta - atan(-vy/vx)
        
    def d_vx(self):
        f_pro = 1 #thrust of propeller
        f_drg = 1 #drag
        f_ele = 1 #lift of the elevator
        f_main = 1 #lift of the main wing
        return (f_pro*cos(self.theta) - f_drg*cos(self.theta)
                - f_ele*sin(self.phai-self.theta)
                - f_main*sin(self.phai-self.theta))*param.RECIP_M
    
    def d_vy(self):
        f_pro = 1 #thrust if propeller
        f_drg = 1 #drag
        f_ele = 1 #lift of the elevator
        f_main = 1 #lift of the main wing
        return (-f_pro*sin(self.theta) + f_drg*sin(self.theta)
                + f_ele*cos(self.phai-self.theta)
                + f_main*cos(self.phai-self.theta) - param.M*param.GRAVITY)*param.RECIP_M

    def d_theta(self):
        f_ele = 1 #lift of the elevator
        return param.R*f_ele*cos(self.phai)*param.RECIP_I

    def d_x(self,dt):
        return self.vx*dt

    def d_y(self,dt):
        return self.vy*dt

    def __add__(self,d_state):
        return State(self.x+d_state.vx ,self.vx+d_state.ax, self.y+d_state.vy, self.vy+d_state.ay, self.theta+d_state.omega)
        
    
    def dt(self,dt,alpha):
        vx = self.d_x(dt)
        ax = self.d_vx()
        vy = self.d_y(dt)
        ay = self.d_vy()
        omega = self.d_theta()
        return D_State(vx,ax,vy,ay,omega)
