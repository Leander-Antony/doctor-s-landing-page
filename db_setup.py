# db_setup.py
import sqlite3

conn = sqlite3.connect('appointments.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    reason TEXT NOT NULL,
    date TEXT NOT NULL,
    time_slot TEXT NOT NULL
)
''')

conn.commit()
conn.close()
