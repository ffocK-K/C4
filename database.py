import sqlite3

con = sqlite3.connect('contacts.db')
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    is_starred INTEGER DEFAULT 0
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS contact_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_id INTEGER,
    method_type TEXT,
    method_value TEXT,
    FOREIGN KEY(contact_id) REFERENCES contacts(id)
)
""")

con.commit()
con.close()
