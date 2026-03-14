x = [1,2,3,4,5]
y = [2,5,4,5,6]

mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)


numerator = []
denominator = []

for x,y in zip(x,y):
    numerator.append(((x-mean_x)*(y-mean_y)))
    
    denominator.append((x-mean_x)**2)
    
    

numerator = sum(numerator)
denominator = sum(denominator)


answer = numerator/denominator
 
 
 
print(answer)   
    
