from avaliation.infrastructure.db.connection import connect_db

def get_all_users():
    conn = connect_db()
    cur = conn.cursor()

    query = "SELECT * FROM users ORDER BY id DESC;"
    cur.execute(query)
    results = cur.fetchall()

    cur.close()
    conn.close()

    keys = ["id", "name", "phone", "email", "health_unit", "municipality", "responsible_analyst", "responsible_manager"]
    return [dict(zip(keys, row)) for row in results]
