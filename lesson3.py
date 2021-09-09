import sqlite3

db = sqlite3.connect('mock_data.db')

INSERT_STATEMENT = """
        INSERT INTO tutorial 
        VALUES ('2017-01-01 01:02:00', 'abc123', 80, '500MB', 72, 335, 'field');
"""

db.execute(INSERT_STATEMENT)
db.commit()

db.close()