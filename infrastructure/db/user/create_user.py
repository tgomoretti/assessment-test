import psycopg2
from psycopg2 import sql
from avaliation.infrastructure.db.connection import connect_db

# # Configurações do banco
# DB_CONFIG = {
#     "host": "localhost",
#     "port": 5432,
#     "database": "avaliacao",
#     "user": "tiago",
#     "password": "admin"
# }

# def connect_db():
#     conn = psycopg2.connect(**DB_CONFIG)
#     return conn

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
            responsible_manager
            )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """)
    cur.execute(query, (
        user_data['name'],
        user_data.get('phone'),
        user_data.get('email'),
        user_data.get('health_unit'),
        user_data.get('municipality'),
        user_data.get('responsible_analyst'),
        user_data.get('responsible_manager')
    ))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id

if __name__ == "__main__":
    new_user = {
        "name": "Maria João",
        "phone": "123456789",
        "email": "maria@email.com",
        "health_unit": "Unidade A",
        "municipality": "Cidade X",
        "responsible_analyst": "Analista Y",
        "responsible_manager": "Gestor Z"
    }
    user_id = create_user(new_user)
    print(f"Usuário inserido com id: {user_id}")
