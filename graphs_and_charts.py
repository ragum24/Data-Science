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

'''plt.bar(subject,score, color= colours, edgecolor= "black")
plt.xlabel("Subjects")
plt.ylabel("Mean scores")
plt.title("Mean scores in 8K-")
plt.show()'''

#creating a Pie chart
'''daily_activities= ["sleeping","school", "studying" , "actually studying", "guinea pigs"]
time= [9, 6, 3, 1, 2]
explode= [0, 0.2, 0, 0.1, 0]
plt.pie(time, labels= daily_activities, shadow= True, startangle= 270, explode=explode)
plt.title("Average hours spent on my daily activities")
plt.legend()
plt.show()'''

#creating a scatter plot
height= [150, 130, 180, 200, 120]
weight= [50, 40, 40, 199, 45]
colour= ["blue", "orange", "yellow", "pink", "black"]
sizes= [100, 200, 300, 400, 500]

plt.scatter(height, weight, marker= "*", c= colour, s= sizes)
plt.xlabel("Mean height of individuals")
plt.ylabel("Mean weight of each height of individuals")
plt.show()