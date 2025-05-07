import pandas as pd
import numpy as np

# Creating a Series
y = [11, 24, 26, 28, 30]
series = pd.Series(y)
print(series)  # ✅ Print the Series

# Creating Series with custom labels
y = pd.Series(y, index=["a", "b", "c", "d", "e"])
print(y)  # ✅ Print labeled Series
print(y["a"])  # ✅ Access value by label

# Creating DataFrame
data = {
    "name": ["Amina", "Hira", "Noor"],
    "CGPA": [3.57, 3.92, 3.45]
}
frame = pd.DataFrame(data, index=["1", "2", "3"])
print(frame)

# Selecting by condition
print("\nStudents with CGPA less than 3.6:")
print(frame[frame["CGPA"] < 3.6])  # ✅ Correct condition filtering

# Access values from DataFrame
print(frame.loc["1", ["name", "CGPA"]])  # ✅ Correct multi-column selection

# Add a new column "Roll no"
frame["Roll no"] = [2401, 2415, 2411]  # ✅ Correct
print("\nDataFrame after adding Roll no:")
print(frame)

# Creating another DataFrame
data2 = {
    "name": ["Hamna", "Khadija", "Zara"],
    "City": ["Gujrat", "Malukhokar", "Malukhokar"]
}
x = pd.DataFrame(data2, index=["1", "2", "3"])
print(x)

# Print DataFrame information (No need to print explicitly)
x.info()

#To get a single column:
df2 = pd.DataFrame(data2)  # ✅ Convert dictionary to DataFrame
# to get multiple columns
print(df2[["name", "City"]])  # ✅ Correct way to access multiple columns

print(data2["name"])


# Correct row selection
print(x.loc["3", ["name", "City"]])  # ✅ Correct
print(x.loc["1"])  # ✅ Correct: Using string index
print(x.loc[["1", "2"]])  # ✅ Access multiple rows
print(x.head(1))  # ✅ Print first row
print(x.tail(1))  # ✅ Print last row
print(x.describe())  # ✅ Print summary statistics

# remove colum
frame=frame.drop(columns=["CGPA"])
print(frame)
# removing row
frame=frame.drop(index="1")
print(frame)
# new dataframe
newdf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
print(newdf)
print(newdf.describe())
print(newdf.dtypes)
print(newdf.index)
print(newdf.columns)
print(newdf.to_numpy())
print(newdf.T)#transpose 

#sorting the data
print(newdf.sort_index(axis=0,ascending=False))
print(type(newdf[0]))
newdf.columns=list("ABCDE")
print(newdf)
newdf.drop("A",axis=1)# it will del the column value at 1s
print(newdf)
print(newdf.loc[[1,2],["A","C"]])
print(newdf.iloc[0,4])# search along index
print(newdf.iloc[[0,1],[1,2]])
newdf.drop(["A"],axis=1)# it will del col A
print(newdf)
newdf.drop(["A","B"],axis=1)
print(newdf)
