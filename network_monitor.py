'''
Program: Database
File Name: network_monitor.py
Author: Elizabeth Acevedo
Date: 06//2026

Purpose:
    Created and manages the SQLite database used by the 
    Local Network Security Monitor.
'''
import sqlite3

'''Creates the database and devices table if they do not already exist.'''
def init_db():
    # Connects to a database file/creates one if doesn't exist
    connection = sqlite3.connect("netmonitor.db")

    # Creates a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Creates a table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS 
        devices(
            device_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            Hostname TEXT NOT NULL,
            MAC_Address TEXT UNIQUE NOT NULL,
            IP_Address TEXT NOT NULL,
            First_Seen TEXT NOT NULL,
            Last_Seen TEXT NOT NULL
        )
    """)

    connection.commit()

    return connection, cursor

'''Stores a newly discovered device in the database.'''
def save_device(cursor, hostname, mac, ip, first_seen, last_seen):

    cursor.execute(
        """
        INSERT INTO devices(
            Hostname, 
            MAC_Address, 
            IP_Address, 
            First_Seen,
            Last_Seen
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (hostname, mac, ip, first_seen, last_seen)
    )


'''Displays every device currently stored in the database.'''
def show_db(cursor):
    cursor.execute("SELECT * FROM devices")
    rows = cursor.fetchall()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~DATABASE~~~~~~~~~~~~~~~~~~~~~~~~~")
    for row in rows:
        device_id, hostname, mac, ip, first_seen, last_seen = row

        print(f"\nDevice: {device_id}")
        print(f"Hostname: {hostname}")
        print(f"MAC Address: {mac}")
        print(f"IP Address: {ip}")
        print(f"First Seen: {first_seen}")
        print(f"Last Seen: {last_seen}\n")


def clear_database(cursor):
    """Deletes all stored devices while keeping the table and reset device counter."""
    
    cursor.execute("DELETE FROM devices")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='devices'")
    print("Database cleared.")


'''Saves database changes and closes the connection.'''
def close_db(connection):
    connection.commit()
    connection.close()
    print("Database saved and closed.")