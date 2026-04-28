import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,          
        priority TEXT DEFAULT 'medium',
        status TEXT DEFAULT 'pending',       
        due_date TEXT
        )
        """)


conn.commit()
print("Banco de dados criado.")

conn.close()
