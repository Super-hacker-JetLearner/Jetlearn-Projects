import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y= [1,2,3,4,5]

plot = plt.plot(x,y,'g--') #make plot, can change color
plt.show()

plot2 = plt.plot(x,y)
plt.axis([0,10,0,100])
plt.show()

plt.plot(x,y, label='y=x',linewidth=10)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Title')
plt.legend()
plt.show()

plt.plot([1,2,3,4,5],[1,4,9,16,25],'g--',label='y=x^2',linewidth=5)
plt.plot([1,2,3,4,5], [1,8,27,64,125], 'ro',label='y=x^3',linewidth=2)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Squared and cubed')
plt.legend()
plt.show()

a = np.arange(1,10,0.1)
print(a)

y1 = a**2
y2 = a**3

plt.plot(a,y1,'ro',a,y2,'g--')
plt.show()

x = np.arange(1,100)
print('y = mx+c')
m = int(input('Enter m: '))
c = int(input('Enter c: '))
# y=x
# y = y*m + c
y = x*m + c
plt.plot(x,y,'g--')
plt.show()

x = [1,3,5,7]
y = [6,5,4,3]

plt.bar(x,y,color='r') #make bar graph
plt.bar([2,4,6,8],y,color='b')
plt.show()

plt.bar(['Boys','Girls'],[20,12],color='r') #categorical data
plt.show()

#histograms
plt.hist([10,25,12,6,3,30,5,22,30,15,9,1,16,19,23,27,28],[0,10,20,30], histtype='bar',rwidth=0.9) #histogram
plt.show()

#scatter plot
x = [1,2,3,4,5,6,7,8,9,10]
y = np.random.permutation(10)
plt.plot(x,y,'ro')
plt.show()

plt.scatter(x,y,label='scatter plot',color='r',marker='o') #make scatter plot
plt.show()

