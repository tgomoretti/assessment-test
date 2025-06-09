from psycopg2 import sql
from avaliation.infrastructure.db.connection import connect_db

def create_user(user_data):
    conn = connect_db()
    cur = conn.cursor()
    query = sql.SQL("""
        INSERT INTO users (
            name, 
            phone, 
            email, 
            health_unit,
            municipality, 
            responsible_analyst,
            responsible_manager,
            id_department
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """)
    cur.execute(query, (
        user_data.get('name'),
        user_data.get('phone'),
        user_data.get('email'),
        user_data.get('health_unit'),
        user_data.get('municipality'),
        user_data.get('responsible_analyst'),
        user_data.get('responsible_manager'),
        user_data.get('id_department')
    ))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id