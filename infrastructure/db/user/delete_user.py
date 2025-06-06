from ..connection import connect_db

def delete_user(user_id):
    conn = connect_db()
    cur = conn.cursor()
    
    query = "DELETE FROM users WHERE id = %s;"
    cur.execute(query, (user_id,))
    conn.commit()
    cur.close()
    conn.close()