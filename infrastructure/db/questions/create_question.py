import psycopg2
from psycopg2 import sql
from avaliation.infrastructure.db.connection import connect_db

def create_question(question_data):
    conn = connect_db()
    cur = conn.cursor()
    query = sql.SQL("""
                    INSERT INTO questions (
                        department_id,
                        question_text,
                        alternative_a,
                        alternative_b,
                        alternative_c,
                        alternative_d,
                        correct_answer
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING id;
                """)
    cur.execute(query, (
        question_data['department_id'],
        question_data['question_text'],
        question_data['alternative_a'],
        question_data['alternative_b'],
        question_data['alternative_c'],
        question_data['alternative_d'],
        question_data['correct_answer']
    ))
    question_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return question_id