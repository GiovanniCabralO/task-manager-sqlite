import sqlite3

def report_by_status():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT status, COUNT(*) FROM tasks GROUP BY status")

    rows = cursor.fetchall()
    print("\n---------- Relatório por Status ----------")
    for row in rows:
        print(row)

def report_by_priority():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT priority, COUNT(*), SUM(CASE WHEN status = 'finalizada' THEN 1 ELSE 0 END)
                   FROM tasks   
                   GROUP BY priority
                   """)
    
    rows = cursor.fetchall()
    print("\n---------- Relatório por Prioridade ----------")
    for row in rows:
        prioridade, total, concluidas = row
        print(f"Prioridade: {prioridade.capitalize()} | Total: {total} | Concluídas: {concluidas}")
    
    conn.close()

