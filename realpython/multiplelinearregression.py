#simple multiple linear regression example

#import packages
import numpy as np 
from sklearn.linear_model import LinearRegression

#build dataset
#reshape x to make it a columnar array
x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]

x = np.array(x)
y = np.array(y)

#build a model
model = LinearRegression()

model.fit(x, y)

#get results
r_sq = model.score(x, y)

print ("R-squared: ", r_sq)
print ("y-intercept: ", model.intercept_)
print ("slope: ", model.coef_)

#predict values
y_pred = model.predict(x)
print ("Predicted response: ", y_pred)

#should be the same as
print ("Predicted response: ", model.intercept_ + np.sum(model.coef_ * x, axis = 1))

#now, lets try to predict with new values
x_new = np.array([65, 75,90,105,145,155]).reshape(-1,2)
y_newpred = model.predict(x_new)
print ("Predicted response: ", y_newpred)

