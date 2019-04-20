#simple linear regression example

#import packages
import numpy as np 
from sklearn.linear_model import LinearRegression

#build dataset
#reshape x to make it a columnar array
x = np.array([5, 15,25,35,45,55]).reshape(-1,1)
y = np.array([5,20, 14,22,32,38])

#build a model
model = LinearRegression()

model.fit(x, y)

#get results
r_sq = model.score(x, y)

print ("R-squared: ", r_sq)
print ("y-intercept: ", model.intercept_)
print ("slope: ", model.coef_)

#when provided y as a 2-dimensional array
newmodel = LinearRegression().fit(x, y.reshape(-1,1))

print ("R-squared: ", newmodel.score(x, y.reshape(-1,1)))
print ("y-intercept: ", newmodel.intercept_)
print ("slope: ", newmodel.coef_)

#predict values
y_pred = model.predict(x)
print ("Predicted response: ", y_pred)

#should be the same as
print ("Predicted response: ", model.intercept_ + (model.coef_ * x))

#to get the same dimensionality
print ("Predicted response: ", model.intercept_ + (model.coef_ * x.flatten()))

#now, lets try to predict with new values
x_new = np.array([65, 75,90,105,145,155]).reshape(-1,1)
y_newpred = model.predict(x_new)
print ("Predicted response: ", y_newpred)
