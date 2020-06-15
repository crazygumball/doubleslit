from vpython import *
d = 0.0002
L = 100
landa = 532*10**-9
f = 3*10**8/landa
a0 = 0.5
s1 = sphere(pos=vector(0,d/2,0),radius=0.2*d,color=color.red)
s2 = sphere(pos=vector(0,-d/2,0),radius=0.2*d,color=color.blue)
r1_list = []
for n in range(0,2001,1):
    r1 = s1.pos - vector(L,-1+0.001*n,0)
    r1_m = mag(r1)
    r1_list.append(r1_m)

r2_list = []
for n in range(0,2001,1):
    r2 = s2.pos - vector(L,-1+0.001*n,0)
    r2_m = mag(r2)
    r2_list.append(r2_m)

gd = graph(title="Y-I plot", width=500, height=450, x=0, y=0, xtitle="Y", ytitle="Intensity")
YI = gcurve(graph=gd, color=color.red)

intensity_list = []
for n in range(0,2001,1):
    delta_r = r1_list[n] - r2_list[n]
    delta_landa = delta_r - (delta_r//landa) * landa
    delta_theta = ( 2 * pi / landa ) * delta_landa
    I = (mag((a0/r1_list[n])*vector(1,0,0) + vector((a0/r2_list[n]) * cos(delta_theta),(a0/r2_list[n])*sin(delta_theta),0)))**2
    intensity_list.append(I)
