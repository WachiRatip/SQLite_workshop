import os 
import re
import sqlite3

path = os.path.join(".", "examples", "mock_data.txt")

with open(path, "r", encoding='utf-8') as file:
    raw = file.read()

list_raw = raw.split("\n")

data = []

for item in list_raw:
    years = ''.join(re.findall(r"^.*?\([^\d]*(\d+)[^\d]*\).*$", item))
    temps = ''.join(re.findall(r"=([^\=]\d+)", item)).replace(" ", "")
    data.append(
        (int(years), float(temps))
    )

print(data, type(data))

# Connect database
db = sqlite3.connect('my_db.db')

# Create table
# Done by lesson10.py

# Insert rows
INSERT_STATEMENT = """
        INSERT INTO tempyearly 
        VALUES (?, ?);
"""
db.executemany(INSERT_STATEMENT, data)
db.commit()

db.close()