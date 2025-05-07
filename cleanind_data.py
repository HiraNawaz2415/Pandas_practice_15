import pandas as pd
df = pd.read_csv('data.csv')  # Load the data from a CSV file
# handling missing data
new_df = df.dropna()  # Remove rows with missing values
print(new_df)  # Display the new DataFrame
#dropna() removes all rows that have empty cells.
#to_string() is used to print the entire DataFrame properly.
#he original DataFrame remains unchanged. If you want to modify it directly, use inplace=True:
df1=df.dropna(inplace=True)
print(df.head())
df.fillna(130, inplace=True)  # Replace all empty cells with 130
df["Calories"] = df["Calories"].fillna(130)  # Correct way to replace empty values
 # Replace empty values in the 'Calories' column only change specific column value
#fillna(value)	Replaces empty values with a specific value
# fillna(df["Column"].mean())	Replaces empty values with the column's mean (average)
# fillna(df["Column"].median())	Replaces empty values with the column's median
# fillna(df["Column"].mode()[0])	Replaces empty values with the column's most frequent value
df["Calories"] = df["Calories"].fillna(df["Calories"].mean())  # Replace empty values with mean

# same like for mode and median


#check for duplocate values
print(df.duplicated())
df.drop_duplicates(inplace=True)

#Grouping & Aggregation in Pandas
# In Pandas, grouping means organizing data based on a specific column, and aggregation means applying functions (like sum, mean, etc.) to those groups.
# for example, suppose we have a dataset of people in different cities with their ages:
import pandas as pd

data = {
    "City": ["New York", "Los Angeles", "New York", "Chicago", "Chicago"],
    "Age": [25, 30, 35, 40, 45]
}

df = pd.DataFrame(data)
print(df)
#To group the data by the "City" column and calculate the average age for each city
df_grouped = df.groupby("City")["Age"].mean()
print(df_grouped)
#Merging DataFrames
# Merging combines two tables based on a common column.

df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["A", "B", "C"]})
df2 = pd.DataFrame({"ID": [1, 2, 3], "Salary": [1000, 2000, 3000]})

# Merge both DataFrames using "ID" as the common column
merged_df = pd.merge(df1, df2, on="ID")
print(merged_df)

df1.set_index("ID", inplace=True)
df2.set_index("ID", inplace=True)

joined_df = df1.join(df2)
print(joined_df)

#Applying Functions to Data
#Pandas provides apply() and map() functions to modify column values.
# Using apply() Function
# You can use apply() when you want to apply a function to each value in a column.
# Example: Categorizing ages into "Young" and "Old"
df["Age_Group"] = df["Age"].apply(lambda x: "Young" if x < 30 else "Old")
print(df)
df["Age"] = df["Age"].map(lambda x: x + 5)
print(df)

#apply() is more flexible (can be used on multiple columns or even rows).
# map() is mainly for single-column transformations.
import matplotlib.pyplot as plt
df["Age"].plot(kind="bar")
plt.show()


import pandas as pd

# Creating a dataset
data = {
    'Employee': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Charlie'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance'],
    'Salary': [50000, 60000, 52000, 61000, 70000, 71000]
}

df = pd.DataFrame(data)

# Creating a pivot table to calculate the average salary per department
pivot = df.pivot_table(values='Salary', index='Department', aggfunc='mean')

print(pivot)
"""Salary
Department        
Finance    70500.0
HR         51000.0
IT         60500.0
Explanation:
values='Salary' → The column we want to summarize.
index='Department' → Groups data by the Department column.
aggfunc='mean' → Calculates the average salary for each department."""

"""crosstab() – Creating Frequency Tables
The crosstab() function counts occurrences of values in different categories. This is useful for analyzing relationships between two columns.

Example: Counting Employees in Each Department
Let's count how many times each employee appears in different departments."""


import pandas as pd

# Creating a dataset
data = {
    'Employee': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Charlie'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance']
}

df = pd.DataFrame(data)

# Creating a crosstab to count employees in each department
cross_tab = pd.crosstab(df['Employee'], df['Department'])

print(cross_tab)

"""This table shows how many times each employee appears in each department.
For example:
Alice appears 2 times in HR.
Bob appears 2 times in IT.
Charlie appears 2 times in Finance"""

"""melt() – Reshaping Data
The melt() function is used to convert wide-format data into long-format. This makes it easier to analyze and process.

Example: Transforming Salary Data
Suppose we have salaries for employees in different years:"""

import pandas as pd

# Creating a dataset
data = {
    'Employee': ['Alice', 'Bob', 'Charlie'],
    'Salary_2023': [50000, 60000, 70000],
    'Salary_2024': [52000, 61000, 71000]
}

df = pd.DataFrame(data)

# Melting the DataFrame to reshape it
melted = pd.melt(df, id_vars=['Employee'], var_name='Year', value_name='Salary')

print(melted)
"""Output:

  Employee         Year  Salary
0    Alice  Salary_2023   50000
1      Bob  Salary_2023   60000
2  Charlie  Salary_2023   70000
3    Alice  Salary_2024   52000
4      Bob  Salary_2024   61000
5  Charlie  Salary_2024   71000
Explanation:
Before melting, the salary columns were separate for each year (Salary_2023, Salary_2024).
After melting:
The column names (Salary_2023 and Salary_2024) are transformed into rows.
A new "Year" column is created.
The salaries are placed in a single column named "Salary".
📌 Summary

Function	Purpose
pivot_table()	Summarizes data by grouping values and applying calculations (mean, sum, etc.).
crosstab()	Counts occurrences of values in different categories.
melt()	Reshapes data from wide format to long format."""



"""id_vars=['Employee'] → Keeps the Employee column as it is.
var_name='Year' → Converts column names (Salary_2023, Salary_2024) into values inside a new column called "Year".
value_name='Salary' → Places all salary values under one column called "Salary"."""
