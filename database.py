import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
        ); 
        """)

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,          
        priority TEXT DEFAULT 'média',
        status TEXT DEFAULT 'pendente',       
        due_date TEXT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories (id)
        );
        """)


conn.commit()
print("Banco de dados criado.")

conn.close()
