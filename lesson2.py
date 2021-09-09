import sqlite3

db = sqlite3.connect('mock_data.db')

CREATE_STATEMENT = """
        CREATE TABLE tutorial (
            timestamp TEXT,
            device_id TEXT,
            cpu_1m_avg REAL,
            free_mem TEXT,
            temperature	REAL,
            location_id	INTEGER,
            dev_type TEXT
        );
"""

db.execute(CREATE_STATEMENT)

db.close()