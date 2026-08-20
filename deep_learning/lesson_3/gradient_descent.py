import numpy as np
import matplotlib.pyplot as plt

def cost_function(x):
    return x**2

def derivative(x):
    return 2*x

def gradient_descent(starting_point, learning_rate, epoch):
    x = starting_point
    path = [x]
    
    for _ in range(epoch):
        grad=derivative(x)
        x -= grad * learning_rate
        path.append(x)
    return path

starting_point = 10
learning_rate = 0.01
epoch = 200

path = gradient_descent(starting_point,learning_rate,epoch)

x_vals = np.linspace(-10,10,400)
y_vals = cost_function(x_vals)

plt.figure(figsize=(10,6))
plt.plot(x_vals,y_vals, label="Cost Function  f(x)-x^2",color="blue")
plt.scatter(path, cost_function(np.array(path)), color="red", label='Gradient Descent Path', s=100)

plt.title('Gradient Descent Visualization')
plt.xlabel('x')
plt.ylabel('Cost')
plt.legend()
plt.grid()
plt.show()