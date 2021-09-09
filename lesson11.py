import sqlite3

db = sqlite3.connect('my_db.db')

SELECT_STATEMENT = """
        SELECT year, temperature
        FROM tempyearly
        WHERE year>2000;
"""

data = db.execute(SELECT_STATEMENT).fetchall()
print(data)

db.close()