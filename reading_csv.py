import pandas as pd

#loading data from a csv file
titanic_df = pd.read_csv("Data sets/titanic.csv")

#displaying dataframe
#print(titanic_df)

print(titanic_df.head(10)) # just .head gives you the default top 5

#printing specific columns
selected = titanic_df[["Pclass","Name","Fare"]]
print(selected.head(7))

print("-"*50)

#condition-based filtering

#selecting all the columns for the people with age greater than 30
above_30 = titanic_df[titanic_df["Age"]>30]
print(above_30.head())

#finding the mean age for female and male
#1. group all data based on gendre
#2. use the age column to find out both
print(titanic_df.groupby("Sex")["Age"].mean())

print("\n\n")

#Get the mean ticket price for each sex
print(titanic_df.groupby("Sex")["Fare"].mean())

print(titanic_df.groupby(["Pclass","Sex"])["Fare"].mean())

#getting the count of rows in each category
print(titanic_df["Pclass"].value_counts())
print("-*"*50)
print(titanic_df["Parents/Children Aboard"].value_counts())


#Opperations on text data
titanic_df["name_lowercase"] = titanic_df["Name"].str.lower()
print(titanic_df.head())