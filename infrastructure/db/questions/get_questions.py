import psycopg2
from avaliation.infrastructure.db.connection import connect_db

def get_questions_by_department(department_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            q.id, 
            q.question_text, 
            q.alternative_a, 
            q.alternative_b, 
            q.alternative_c, 
            q.alternative_d, 
            q.correct_answer
        FROM questions q
        WHERE q.department_id = %s
        ORDER BY q.id;
    """, (department_id,))
    questions = cur.fetchall()
    cur.close()
    conn.close()
    return questions
