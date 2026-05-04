import sqlite3
from datetime import datetime 


def add_task(title, priority, category_id):
    data_atual = datetime.now().strftime("%Y-%m-%d")
    
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, priority, due_date, category_id) 
        VALUES (?, ?, ?, ?)
    """, (title, priority, data_atual, category_id))

    conn.commit()
    conn.close()

def list_tasks(priority=None):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    query = """
        SELECT
            tasks.id,
            tasks.title,
            tasks.priority,
            tasks.status,
            categories.name
        FROM tasks
        INNER JOIN categories ON tasks.category_id = categories.id"""

    if priority:
        query += " WHERE tasks.priority = ?"
        cursor.execute(query, (priority,))
    else:
        cursor.execute(query)
    
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_task(id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (id, ))

    conn.commit()
    conn.close()


def update_status(id, status):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, id, ))

    conn.commit()
    conn.close()

def add_category(name):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (name, ))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Categoria já existe.")
    conn.close()

def list_categories():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    rows = cursor.fetchall()
    conn.close()
    print(rows)
    return rows

def get_category_summary():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    query = """
        SELECT c.name, COUNT(t.id)
        FROM categories c
        LEFT JOIN tasks t ON c.id = t.category_id
        GROUP BY c.name
    """

    cursor.execute(query)
    summary = cursor.fetchall()
    conn.close()
    return summary

def get_category_id_by_name(name):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM categories WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None