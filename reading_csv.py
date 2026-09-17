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