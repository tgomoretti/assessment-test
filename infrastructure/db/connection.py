import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "avaliacao",
    "user": "tiago",
    "password": "admin"
}

def connect_db():
    return psycopg2.connect(**DB_CONFIG)
