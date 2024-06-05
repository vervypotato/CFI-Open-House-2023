import matplotlib.pyplot as plt
import numpy as np
import json
import math
from timeit import default_timer as timer

start = timer()
#np.random.seed(10) #can be used to generate same graph

def contains_duplicates(X):             #checks for duplicate birthdays in a list using np.unique method
    return len(np.unique(X)) != len(X)

def overlap(n):                                 #used for plotting theoretical values
    prob = 1 - (math.exp((-n * (n - 1)) / 730))
    return prob


maxLimit = int(input("Enter the maximum limit of people: \n"))
num = int(input("Enter the number of people for which you want to find the corresponding probability: \n"))
iteration = int(input("Enter the number of interations (recommended 10-100): \n"))

common_birthday = 0

people = []
probabilities = []
i = 1
for i in range(1,maxLimit+1): #loops for each value of n
    Sum = 0
    for j in range(0,1000): #loops for 1000 values to return average of iterations
        common_birthday = 0
        for k in range(0,iteration): #iterates "iteration" no. of times.
            
            # assign dates to people
                
            dates = np.random.choice(range(0,365), size=(i)) #creates a list of size i and the elements
                                                             #are randomly chosen integers between 0 and 365

            # check if there are duplicates
            if contains_duplicates(dates):
                common_birthday+=1 # increment shared birthday

        probability = common_birthday/iteration
        Sum += probability

   
    
    
    people.append(i)
    avg_probability = Sum/1000 #average of all the iterations
    probabilities.append(avg_probability) #adding the average value to the list
    
    
people_x = people
prob_y = probabilities

print("The probability of 2 people having the same birthday among",num,"people is ",prob_y[num] * 100, "% \n")

#for printing all theoretical values
i = 0
dict = {}
xlist = []
ylist = []
while (i < maxLimit+1):
    prob = overlap(i)
    dict[i] = prob
    i += 1
    xlist.append(i)
    ylist.append(prob)
#print(json.dumps(dict, indent=4))  #for visual pleasure, prints the dictionary

plt.plot(people_x, prob_y) #plots the monte carlo simulated values 
np_people_x = xlist
np_prob_y = ylist
plt.plot(np_people_x, np_prob_y) #plots the theoretical values 

plt.title("Birthday Paradox [Proabability (P) vs No. of people in sample space (n)]")
plt.xlabel("No. of people in sample space (n)")
plt.ylabel("Probability (P)")
plt.legend(["Simulated values","Theoretical values"])
plt.show()

deviation = [] #error in the simulation
dict2 = {}
i = 0
while (i < maxLimit):
    error = prob_y[i] - np_prob_y[i]
    dict2[i] = error
    deviation.append(error)
    i += 1
    

print("The error value for ", num,"people is", deviation[num-1]*100,"%")
#print(json.dumps(dict2, indent=4))



plt.plot(people_x, deviation)
plt.title("Deviation")
plt.xlabel("No. of people in sample space (n)")
plt.ylabel("error")          
plt.show()
 
end = timer() 
print("Time taken for simulation = ", end-start, " sec") #prints the time taken
                                                         #for the simulation



