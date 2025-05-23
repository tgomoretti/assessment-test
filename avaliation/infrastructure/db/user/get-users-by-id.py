from ...connection import connect_db

def get_user_by_id(user_id):
    conn = connect_db()
    cur = conn.cursor()
    
    query ="SELECT * FROM users WHERE id = %s;"
    cur.execute(query, (user_id,))
    user = cur.fetchone()
    
    cur.close()
    conn.close()
    return user