# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:49:37 2018

@author: Navneet Choudry
STACK PLOT
"""
#Stackplot
import matplotlib.pyplot as plt

days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

plt.plot([],[],color='m',label='sleeping',linewidth=10)
plt.plot([],[],color='c',label='eating',linewidth=10)
plt.plot([],[],color='r',label='working',linewidth=10)
plt.plot([],[],color='k',label='playing',linewidth=10)
plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title("Area Plot")
plt.legend()
plt.show()