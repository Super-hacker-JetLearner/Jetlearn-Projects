xs = [1,2,3,4,5]
ys = [2,5,4,5,6]

mean_x = sum(xs)/len(xs)
mean_y = sum(ys)/len(ys)


numerator = []
denominator = []

for x,y in zip(xs,ys):
    numerator.append(((x-mean_x)*(y-mean_y)))
    
    denominator.append((x-mean_x)**2)
    
    

numerator = sum(numerator)
denominator = sum(denominator)


slope = numerator/denominator
 
 
c = mean_y-slope*mean_x

print(slope,c)


total_error = 0

for x,y in zip(xs,ys):
    predicted = x*slope + c
    print(predicted,y)
    error = abs(predicted-y)
    total_error += error
    
average_error = total_error/len(xs)
print(average_error)


import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


xs_array = np.array(xs).reshape(-1,1)
ys_array = np.array(ys)

model = LinearRegression()
model = model.fit(xs_array,ys_array)

m = model.coef_
c = model.intercept_

print(m,c)

y_predicted = model.predict(xs_array)
print(y_predicted)

plt.scatter(xs,ys)
plt.scatter(xs,y_predicted)
plt.legend(labels=['real','predicted'])

plt.show()
