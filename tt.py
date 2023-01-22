

import _random

import random
import numpy as np
import matplotlib.pyplot as plt
rand_list=[]
delta_t=1
t_range = range(0,31,delta_t)

#u= [1,-1,2,-2,3,-3,4,-4,5,-5]
#u = np.random.normal(loc=0.0, scale=5.0/3, size=(len(t_range)))# normal distribution
#print(u)
t=list(t_range)
print (t)
uc=np.random.normal(loc=2.5, scale=(5.0)/3, size=(len(t_range)))# normal distributio
ud=np.random.normal(loc=2.5, scale=(5.0)/3, size=(len(t_range)))# normal distribution
ud=ud/13
uc=sorted(uc)
ud = sorted(ud)
alpha=1
eta_c=0.6
eta_d=0.4

x=[13.5/2 for i in t_range]
for k in range(len(uc)-1):
    x[k+1]=alpha*x[k]+delta_t*eta_c*uc[k]-(delta_t/eta_d*ud[k])
plt.plot(t,x)
plt.xlabel('Time')
plt.ylabel('State of Charge')


plt.show()
