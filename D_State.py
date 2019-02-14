#differential of State class

class D_State():
    def __init__(self,vx,ax,vy,ay,omega):
        self.vx = vx
        self.ax = ax
        self.vy = vy
        self.ay = ay
        self.omega = omega
        self.size = 5

    def __mul__(self,dt):
        return D_State(self.vx*dt, self.ax*dt, self.vy*dt, self.ay*dt, self.omega*dt)

    def __add__(self,other_d_state):
        return D_State(self.vx+other_d_state.vx,
                       self.ax+other_d_state.ax, self.vy+other_d_state.vy,
                       self.ay+other_d_state.ay, self.omega+other_d_state.omega)

    #a is float
    def __truediv__(self,a):
        return D_State(self.vx/a, self.ax/a, self.vy/a, self.ay/a, self.omega/a)
