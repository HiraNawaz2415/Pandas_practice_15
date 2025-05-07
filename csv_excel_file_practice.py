#CSV file (Comma separetd file)
import pandas as pd
df = pd.read_csv('data.csv')
#use to_string() to print the entire DataFrame.
print(df.to_string())
# print without to_string()
print(df) 
#max_rows
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the pd.options.display.max_rows statement.
print(pd.options.display.max_rows)
#Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df) 

# Define the dictionary
data2 = {
    "name": ["Hamna", "Khadija", "Zara"],
    "City": ["Gujrat", "Malukhokar", "Malukhokar"]
}

# Convert dictionary to DataFrame
df2 = pd.DataFrame(data2)  

# Write DataFrame to CSV file
df2.to_csv("data1.csv", index=False) 
# Write DataFrame to CSV file
df2.to_csv("data1.csv", index="True") 


# reading excel file
df = pd.read_excel("PassFailTest.xlsx", engine="openpyxl")  # Replace "file.xlsx" with your actual file name
print(df.head())  # Display the first 5 rows
#3. Read a Specific Sheet
#If your Excel file has multiple sheets, specify the sheet name:
#df = pd.read_excel("file.xlsx", sheet_name="Sheet1", engine="openpyxl")
# Read Specific Columns
#If you only need certain columns:
df = pd.read_excel("PassFailTest.xlsx", usecols=["Name", "Grade"], engine="openpyxl")
print(df)
# Handle Missing Values
#If the Excel file has missing values, fill them with:
df.fillna(0, inplace=True)  # Replace NaNs with 0
#Drop Empty Rows
df = df.dropna(how="all")  # Removes rows where all values are NaN
print("After dropping emoty rows",df)

#Reset Index
#If you want to reset the index after removing NaNs:
df = df.dropna(how="all").reset_index(drop=True)


# writing to excel file
# Sample data
data = {
    "Name": ["Amina", "Noor", "Khadija", "Adeena"],
    "Grade": ["A+", "F", "A+", "A+"]
}

df = pd.DataFrame(data)

# Write to Excel file
df.to_excel("output.xlsx", index=False, engine="openpyxl")

print("Excel file saved successfully!")
print(df)

#Write Multiple DataFrames to Different Sheets
with pd.ExcelWriter("output.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)
    df.to_excel(writer, sheet_name="Sheet2", index=False)
    print(df)
