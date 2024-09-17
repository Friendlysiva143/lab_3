# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:21:28 2024
stochastic gradiant decent
@author: it351
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.simplefilter("ignore")
def predict(row,coefficents):
    yhat=coefficents[0]
    for i in range(len(row)-1):
        yhat+=coefficents[i+1]*row[i]
    return yhat
def sgd(train,learning_rate,epochs):
    coef=[0.0 for i in range(len(train.columns))]
    m=len(train.index)
    for epoch in range(epochs):
        sum_error=0
        for _ in range(len(train.index)):
            random_index=np.random.randint(m)
            row=train.iloc[random_index,:]
            yhat=predict(row,coef)
            error=yhat-row[-1]
            sum_error+=error**2
            coef[0]=coef[0]-learning_rate*error
            for i in range(len(train.columns)-1):
                coef[i+1]=coef[i+1]-learning_rate*error*row[i]
        print("epoch=%d,learning_rate=%.3f,error=%.3f"%(epoch,learning_rate,sum_error))
    return coef
df=pd.read_csv("salary_data.csv")
learning_rate=0.001
epochs=10
coef=sgd(df,learning_rate,epochs)
print("coefficents:",coef)
plt.scatter(df.iloc[:,0],df.iloc[:,1],color='blue',label='data points')
plt.xlabel('x')
plt.ylabel('y')
x_values=np.linspace(min(df.iloc[:,0]),max(df.iloc[:,0]),100)
y_values=coef[0]+coef[1]*x_values
plt.plot(x_values,y_values,color='red',label='Regression line')
plt.legend(["predicted data","given data"])
plt.show()