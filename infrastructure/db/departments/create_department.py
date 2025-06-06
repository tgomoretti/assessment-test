import psycopg2
from psycopg2 import sql
from avaliation.infrastructure.db.connection import connect_db

def create_department(department_name):
    conn = connect_db()
    cur = conn.cursor()
    query = sql.SQL("""
        INSERT INTO departments (name)
        VALUES (%s)
        RETURNING id;
    """)
    cur.execute(query, (department_name,))
    department_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return department_id
