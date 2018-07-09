# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:23:58 2018

@author: Navneet Choudry
SCATTEER
"""
#Scatter represent the point representation

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]
plt.scatter(x,y, label='skitscat',color='k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter')
plt.legend()
plt.show()