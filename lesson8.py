import sqlite3

db = sqlite3.connect('mock_data.db')

SELECT_STATEMENT = """
        SELECT device_id, temperature 
        FROM tutorial
        WHERE location_id=?;
"""

location = (77, )

data1 = db.execute(SELECT_STATEMENT, location).fetchone()
print(data1)

print()

data2 = db.execute(SELECT_STATEMENT, location).fetchall()
print(data2)

db.close()