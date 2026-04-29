import sqlite3


def add_task(title, priority, due_date):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (title, priority, due_date) VALUES (?, ?, ?)", (title, priority, due_date))

    conn.commit()
    conn.close()


def list_tasks(priority):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    if priority:
        cursor.execute("SELECT * FROM tasks WHERE priority = ?", (priority,))
        rows = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
    
    print("\n---------- Lista de Tarefas ----------")
    for row in rows:
        print(row)

    conn.close()

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

