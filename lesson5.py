import sqlite3

db = sqlite3.connect('mock_data.db')

INSERT_STATEMENT = """
        INSERT INTO tutorial 
        VALUES (?, ?, ?, ?, ?, ?, ?);
"""

data = [
    ('2017-01-01 01:02:00',	'abc123', 80, '500MB', 72, 335, 'field'),
    ('2017-01-01 01:02:23',	'def456', 90, '400MB', 64, 335, 'roof'),
    ('2017-01-01 01:02:30',	'ghi789', 120, '0MB', 56, 77, 'roof'),
    ('2017-01-01 01:03:12',	'abc123', 80, '500MB', 72, 335,	'field'),
    ('2017-01-01 01:03:35',	'def456', 95, '350MB', 64, 335,	'roof'),
    ('2017-01-01 01:03:42',	'ghi789', 100, '100MB', 56, 77,	'roof')
]

db.executemany(INSERT_STATEMENT, data)
db.commit()

db.close()