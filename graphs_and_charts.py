import matplotlib.pyplot as plt

#creating line graph
days =[1,2,3,4,5,6,7]
temp =[-1,-3,4,7,12,15,20]
'''
plt.plot(days,temp, color= "purple", linewidth= 3, linestyle= "--", marker= "o", markersize= 10, markerfacecolor= "blue", markeredgecolor= "blue", label= "Melborne weather during Spring")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Temperature through the week-")
plt.legend()
plt.show()'''

#Creating a bar chart
subject= ["Math", "English", "Art", "VCD", "P.E","Science"]
score= [80, 90, 98, 75, 66, 100]
colours= ["red", "blue", "orange", "pink", "purple", "yellow"]

plt.bar(subject,score, color= colours, edgecolor= "black")
plt.xlabel("Subjects")
plt.ylabel("Mean scores")
plt.title("Mean scores in 8K-")
plt.show()