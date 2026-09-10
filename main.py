import pandas as pd

#creating the dataframe using a dictionary

#dataframe = table  :)

df = pd.DataFrame({
    "Name":["darshika","frjncxm","Rashmi", "Niakenzie", "AAAAAA"],
    "Age": [14, 10000, 34, 13, 8.75],
    "Scores":[100000, 1, 99.99, 98, 23]

})
print(df)
print("a"*50)

#printing a certain number of rows
print(df.head(3))
print("*"*50)
#printing selective columns (selecting what columns to print)
print(df[["Name","Scores"]])

#the shape gives the rows and column
print(df.shape)

#applying numpy functions
print(df["Age"].max())

#data type of age
print(type(df["Age"]))

#getting a summary of the data frame
print("_"*50) 
print(df.info())

print(df.describe())  #describe ONLY works wih integer values and caluculates all basic calculations needed