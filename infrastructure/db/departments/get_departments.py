from avaliation.infrastructure.db.connection import connect_db

def get_departments():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM departments ORDER BY name;")
    departments = cur.fetchall()
    cur.close()
    conn.close()
    return departments
