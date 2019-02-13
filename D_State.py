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
