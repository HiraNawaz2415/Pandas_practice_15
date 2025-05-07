#Writing Data to a JSON File
#You can save a Pandas DataFrame to a JSON file using to_json().
#Example: Writing JSON Data
import pandas as pd
# Sample data
data = {
    "Name": ["Amina", "Noor", "Khadija", "Adeena"],
    "Grade": ["A+", "B", "B+", "A+"]
}
# Convert data to a DataFrame
df = pd.DataFrame(data)
# Write to JSON file
df.to_json("grades.json", orient="records", indent=4)
print("Data written to JSON successfully!")
#Explanation of Parameters:
#orient="records" → Saves data as a list of dictionaries.
#indent=4 → Formats JSON in a readable way with indentation.
#Reading JSON Data
df = pd.read_json("grades.json")
print(df)
#Reading JSON from a URL
#If you have JSON data hosted online, you can read it directly:
url = "https://www.w3schools.com/python/pandas/data.js"
df = pd.read_json(url)
print(df.head())  # Display first 5 rows
