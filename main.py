import pandas as pd
# -- ALL ABOUT DATA PRE PROCESSING --
# 1. Data cleaning - removing spaces
# 2. Handling missing values
# 3. Encoding - assigning a number to different data --> non-numerical data
# 4. Feature scaling - all features as 1 unit
# 5. Outlier remover 
# 6. Frame, test, split - dividng data into training an testing


# Create sample dataset (real-world messy data)
data = {
    "Age": [25, 30, None, 35, 40],
    "Gender": [" Male ", "Female", "Female", " Male", None],
    "Salary": [50000, 60000, 55000, None, 65000],
    "Department": [" IT", "HR ", " IT", "Finance", "     HR "],
    "Purchased": ["Yes", "No  ", "Yes", "No  ", "Yes"]
}


df = pd.DataFrame(data)
print(df)

print("-"*200)

#removing spaces from all the text
text_column = df.select_dtypes(include= "object").columns
#in data frame, string columns are considered as object type
print(text_column)

for column in text_column:
    df[column] = df[column].str.strip()
    print("Removed spaces from ",column)
    #column variable gets each string column one by one
    #str is to convert from object type to string type
    #strip fuction removes unessesary spaces before and after each value
print("Cleaning spaces from df:")
print(df)
print("-"*200)