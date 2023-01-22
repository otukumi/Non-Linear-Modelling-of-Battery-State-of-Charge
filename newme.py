
import _random

import random
import numpy as np
import matplotlib.pyplot as plt
delta_t=1
t_range = range(0,31,delta_t)

#u= [1,-1,2,-2,3,-3,4,-4,5,-5]
u = np.random.normal(loc=0.0, scale=5.0/3, size=(len(t_range)))# normal distribution
#u=[-2.6,0.6,-0.60,1.9,-1.9, -0.1,0.5,0.8,-0.6,3.5,0.1,-0.5, -1.4, -2.7,-0.4,2.5, -0.4,3.50.47429285 -0.12023724 -2.2519852   0.4648014   2.32858834 -1.19293194 -0.19579339 -0.86913637 -2.58153747  3.14923591 -0.05098814 -2.40119943 1.60367566]
t=list(t_range)
print (t)
print(u)
alpha=1
eta_c=0.6
eta_d=0.4

x=[13.5/2 for i in t_range]
for k in range(len(u)-1):
    x[k+1]=alpha*x[k]+delta_t*eta_c*u[k]
print(x)
plt.plot(t,x)
plt.xlabel('Time')
plt.ylabel('State of Charge')
plt.show()
