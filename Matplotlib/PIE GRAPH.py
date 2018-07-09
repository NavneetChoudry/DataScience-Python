# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 12:05:43 2018

@author: Navneet Choudry
PIE GRAPH
"""
#ploting in pie antopct-automatically convert to %
import matplotlib.pyplot as plt
slices=[7,2,2,13]
activities =['sleeping','eating','working','playing']
cols=['c','m','r','b']
plt.pie(slices, labels=activities,colors=cols,startangle=90,shadow=True,explode=(0,0,0,0),autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()