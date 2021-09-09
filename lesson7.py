import sqlite3

db = sqlite3.connect('mock_data.db')

SELECT_STATEMENT = """
        SELECT device_id, temperature 
        FROM tutorial
        WHERE location_id=335;
"""

data1 = db.execute(SELECT_STATEMENT).fetchone()
print(data1)

print()

data2 = db.execute(SELECT_STATEMENT).fetchall()
print(data2)

db.close()