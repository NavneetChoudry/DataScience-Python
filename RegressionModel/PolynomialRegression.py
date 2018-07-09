# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 13:17:56 2018

@author: Navneet Choudry
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def f(x):
    return x*np.sin(x)

x_plot = np.linspace(0,10,100)
x = np.linspace(0,10,100)
rng=np.random.RandomState(0)
rng.shuffle(x)
x=np.sort(x[:20])
y=f(x)

X = x[:,np.newaxis]
X_plot = x_plot[:,np.newaxis]
 
color=['teal','yellow','orange']
lw=2
plt.plot(x_plot,f(x_plot),color = 'cornflowerblue',linewidth=lw,label='ground truth')
plt.scatter(x,y,color='navy',s=30,marker='o',label='training points')
 
for count,degree in enumerate([3,4,5]):
     model=make_pipeline(PolynomialFeatures(degree),Ridge())
     model.fit(X,y)
     y_plot = model.predict(X_plot)
     plt.plot(x_plot,y_plot,color=color[count],linewidth=lw,label="degree %d" % degree)
     plt.legend(loc='lower left')
     plt.show()