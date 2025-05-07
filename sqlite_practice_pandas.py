import sqlite3
import pandas as pd
print(sqlite3.sqlite_version) # Should output something like 2.6.0

# Create (or connect to) a database
conn = sqlite3.connect("sales.db")  # This will create 'sales.db' if it doesn't exist

# Create a cursor to execute SQL queries
cursor = conn.cursor()

#Creating a Table in SQLite
# Create sample data
data = {
    "product": ["Monitor", "Headphones", "Chair"],
    "quantity": [2, 4, 1],
    "price": [150.75, 80.50, 200.00]
}

df = pd.DataFrame(data)

# Write the DataFrame to the database
df.to_sql("sales", conn, if_exists="append", index=False)

print("Data inserted successfully!")

#Read All Data from a Table

df = pd.read_sql_query("SELECT * FROM sales", conn)
print(df)

# Read Specific Columns

df = pd.read_sql_query("SELECT product, price FROM sales", conn)
print(df)
#Read Data with a Filter
df = pd.read_sql_query("SELECT * FROM sales WHERE price > 100", conn)
print(df)
#Update Data in the Table
cursor.execute("UPDATE sales SET price = 130.00 WHERE product = 'Monitor'")
conn.commit()
print("Price updated successfully!")
#Delete Data from the Table
cursor.execute("DELETE FROM sales WHERE product = 'Mouse'")
conn.commit()
print("Product deleted successfully!")
df = pd.read_sql_query("SELECT * FROM sales", conn)
print(df)
#Closing the Database Connection
#After performing database operations, always close the connection to free up resources.
conn.close()
