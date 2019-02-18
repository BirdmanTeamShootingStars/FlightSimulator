import numpy as np

sp = np.array([1.75,4.75,7.75,10.75,13.75,16])
beamsp = np.array([1.75,4.75,7.75,10.75,13.0,15.0,16.0])
L = sp[5]
g = 9.797
npartition = int(L/0.025)
nd = L/npartition
tc1=1.75
tc2=4.75
tc3=7.75
tc4=10.75
tc5=13.75
tc6=16.0
q1 = int(tc1/0.025);
q2 = int(tc2/0.025);
q3 = int(tc3/0.025);
q4 = int(tc4/0.025);
q5 = int(tc5/0.025);
q6 = int(tc6/0.025);
q11 = int(beamsp[0]/0.025);
q22 = int(beamsp[1]/0.025);
q33 = int(beamsp[2]/0.025);
q44 = int(beamsp[3]/0.025);
q55 = int(beamsp[4]/0.025);
q66 = int(beamsp[5]/0.025);
q77 = int(beamsp[6]/0.025);

x = np.zeros(npartition)
for i in range(npartition):
    x[i] = nd*i
y = np.zeros(npartition)

chord0 = 1.045
chord1 = 1.04
chord2 = 0.968
chord3 = 0.892
chord4 = 0.786
chord5 = 0.631
chord6 = 0.45

U = 7.2

WW = np.array([300,336])

alpham = 4.5
alpha1 = 4.5
alpha2 = 4.5
alpha3 = 4.4
alpha4 = 4.1
alpha5 = 3.6
alpha6 = 3.0

nu = 1.55*10**(-5)
rho = 1.185

beamin = np.array([0.090,0.090,0.090,0.090,0.080,0.080,0.070,0.070,0.060,0.060,0.035,0.035,0.020,0.025])
ply24 = np.array([2 ,2 ,2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1])
ply40 = np.array([5, 5, 5, 5, 5, 5,7, 7, 6, 6, 6, 6, 6, 6])

beamout = beamin + 0.125*10**(-3)*ply24 + 0.111*10**(-3)

m0beam = np.array([0.35*10**(-3)*g,0.35*10**(-3)*g,0.3*10**(-3)*g,0.25*10**(-3)*g,0.235*10**(-3)*g,0.19*10**(-3)*g,0.08*10**(-3)*g])
m0wing = np.array([0.75*g, 0.7*g, 0.7*g, 0.65*g, 0.5*g, 0.4*g,0.3*g])
E0 = np.array([104.803*10**9, 97.009*10**9, 97.009*10**9, 117.392*10**9, 123.059*10**9, 123.059*10**9, 123.059*10**9 ])

chord = np.zeros(npartition)
for i in range(npartition):
    if i <= q1:
        chord[i] = (chord0-chord1)/(0-q1)*(i-0) + chord0

    elif i <= q2:
        chord[i] = (chord1-chord2)/(q1-q2)*(i-q1) + chord1

    elif i <= q3:
        chord[i] = (chord2-chord3)/(q2-q3)*(i-q2) + chord2

    elif i <= q4
        chord[i] = (chord3-chord4)/(q3-q4)*(i-q3) + chord3

    elif i <= q5
        chord[i] = (chord4-chord5)/(q4-q5)*(i-q4) + chord4

    elif i <= q6
        chord[i] = (chord5-chord6)/(q5-q6)*(i-q5) + chord5

Re = U*chord/nu
