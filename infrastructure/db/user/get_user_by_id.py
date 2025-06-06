from ..connection import connect_db

def get_user_by_id(user_id):
    conn = connect_db()
    cur = conn.cursor()

    query = """
        SELECT id, 
        name,
        phone,
        email,
        health_unit,
        municipality,
        responsible_analyst,
        responsible_manager
        FROM users
        WHERE id = %s;
    """
    cur.execute(query, (user_id,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        keys = [
            "id",
            "name",
            "phone",
            "email",
            "health_unit",
            "municipality",
            "responsible_analyst",
            "responsible_manager"
            ]
        
        return dict(zip(keys, result))
    else:
        return None
