# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:31:37 2018

@author: Navneet Choudry
BAR GRAPH AND LINE GRAPH
"""

from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
# for linear representation
x = [5,8,10]
y = [12,16,6]
x2=[6,9,11]
y2=[6,15,7]
plt.plot(x,y,'g',label='LineOne',linewidth=5)
plt.plot(x2,y2,'c',label="lineTwo",linewidth=5)
plt.title("info")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
#for bargraph
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="example one")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="example two",color='g')
plt.legend()#color of each data set to differenciate the 2 data
plt.xlabel("bar number")
plt.ylabel("bar height")
plt.title("bar graph")
plt.show()
