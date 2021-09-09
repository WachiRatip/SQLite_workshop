import sqlite3

db = sqlite3.connect('my_db.db')

CREATE_STATEMENT = """
        CREATE TABLE tempyearly (
            year INTEGER,
            temperature REAL
        );
"""

db.execute(CREATE_STATEMENT)

db.close()