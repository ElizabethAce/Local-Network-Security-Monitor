import sqlite3

# Connects to a database file/creates one if doesn't exist
connection = sqlite3.connect("tutorial.db")

# Creates a cursor object to execute SQL commands
cursor = connection.cursor()

# Creates a table
cursor.execute(
"CREATE TABLE IF NOT EXISTS " \
    "devices(" \
        "device_id INTEGER PRIMARY KEY AUTOINCREMENT, " \
        "Hostname TEXT NOT NULL," \
        "MAC_Address TEXT UNIQUE," \
        "IP_Address TEXT NOT NULL," \
        "First_Seen TEXT)")

# connect.commit()
print("Data inserted successfully.")
# connect.close()