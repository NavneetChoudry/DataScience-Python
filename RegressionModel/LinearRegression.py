"""
Spyder Editor

Linear Regression Model
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score
#load the diabetes dataset
diabetes=datasets.load_diabetes()
#use only one feature
diabetes_x=diabetes.data[:,np.newaxis,7]
#split the data ino training and testing sets
diabetes_x_train =diabetes_x[:-20]
diabetes_x_test =diabetes_x[-20:]
#split the targets ino training and testing sets
diabetes_y_train =diabetes.target[:-20]
diabetes_y_test =diabetes.target[-20:]
# crete linear regrsiion object
regr=linear_model.LinearRegression()
#train the model using the training sets
regr.fit(diabetes_x_train,diabetes_y_train)
#make pridictions using the tetsing sets
diabetes_y_pred=regr.predict(diabetes_x_test)
#the coefficients
print('Coefficients:\n',regr.coef_)
#the mean squared eror

print("Mean sqaured error:%.2f"%mean_squared_error(diabetes_y_test,diabetes_y_pred ))
#explained vaiance score:1 i is perfect preddiction
print('variance score:%.2f' ,r2_score(diabetes_y_test,diabetes_y_pred))
#plot outputs
plt.scatter(diabetes_x_test,diabetes_y_test,color='black')
plt.plot(diabetes_x_test,diabetes_y_pred,color='blue',linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()# -*- coding: utf-8 -*-

