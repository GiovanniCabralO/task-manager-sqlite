import sqlite3

def report_by_status():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT status, COUNT(*) FROM tasks GROUP BY status")

    rows = cursor.fetchall() 
    for row in rows:
        print(row)

def report_by_prioriy():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT priority, COUNT(*), SUM(CASE WHEN status = 'done' THEN 1 ELSE 0 END)
                   FROM tasks GROUP BY priority""")
    
    rows = cursor.fetchall() 
    for row in rows:
        print(row)

