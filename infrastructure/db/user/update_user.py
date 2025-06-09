from ..connection import connect_db

def update_user(user_id, user_data):
    conn = connect_db()
    cur = conn.cursor()
    
    query = """UPDATE users
                SET name = %s,
                    phone = %s,
                    email = %s,
                    health_unit = %s,
                    municipality = %s,
                    responsible_analyst = %s,
                    responsible_manager = %s,
                    id_department = %s
                WHERE id = %s;
                """
                
    cur.execute(query, (
        user_data['name'],
        user_data.get('phone'),
        user_data.get('email'),
        user_data.get('health_unit'),
        user_data.get('municipality'),
        user_data.get('responsible_analyst'),
        user_data.get('responsible_manager'),
        user_data.get('id_department'),
     user_id 
    ))
    
    conn.commit()
    cur.close()
    conn.close()