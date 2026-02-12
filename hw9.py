import os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('housing.csv')

# setosa = data[data['species']=='setosa']
# print(setosa)

# versicolor = data[data['species']=='versicolor']
# print(versicolor)

# virginica = data[data['species']=='virginica']
# print(virginica)

# species = [setosa,versicolor,virginica]
# colors = ['green','red','blue']   
# # plt.subplot(2,2,1)
# # plt.scatter(x=data['species'=='setosa']['petal_width'],y=data['petal_length'])

# extra challenge
data = data[data['median_house_value']<500000] #this will limit rows to less than 



plt.figure(figsize=(15,7))

plt.suptitle('housing dataset analysis',fontsize=30)

plt.subplot(2,2,1)

plt.scatter(x=data['median_income'],y=data['median_house_value'],c='blue') #scatterplot
    

plt.xlabel('median income')
plt.ylabel('median house value')
plt.title('median income vs median house value')
plt.legend()


plt.subplot(2,2,2)

plt.scatter(x=data['latitude'],y=data['longitude'],c=data['median_house_value']) #scatterplot
    

plt.xlabel('latitude')
plt.ylabel('longitude')
plt.title('latitude vs longitude color is median house value')
plt.legend()



plt.subplot(2,2,3)

plt.hist(data['housing_median_age'], color='blue') #histogram
    
plt.xlabel('housing median age')
plt.ylabel('frequency of each housing median age')
plt.title('housing median age histogram')
plt.legend()




plt.tight_layout()


plt.show()