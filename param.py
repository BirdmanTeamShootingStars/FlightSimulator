from math import *
from State import *

#initial state
STATE0 = State(0., 5*cos(radians(3.3)), 10., 5*sin(radians(3.3)), radians(3.3))
M = 96.018 #mass total [kg]
RECIP_M = 1/M 
I = 319.72998 #moment of inertia
RECIP_I = 1/I
GRAVITY = 9.80665 #gravitational acceleration [m/s*s]
R = 1 #length between center of gravity and elevator [m]
