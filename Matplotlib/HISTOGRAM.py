# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:03:24 2018

@author: Navneet Choudry
HISTOGRAM
"""
#comparision within a graph-BARGRAPH.Comparision with a other graph-HISTOGRAM
import matplotlib.pyplot as plt
population_ages=[22,55,62,45,21,22,34,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,55]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.legend()
plt.show()