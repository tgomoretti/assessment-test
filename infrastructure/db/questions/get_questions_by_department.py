import psycopg2
from avaliation.infrastructure.db.connection import connect_db

def get_questions_by_department(department_id):
    """
    Retorna uma lista de questões (id, question_text) do departamento informado.
    """
    conn = None
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
             SELECT 
                id, 
                question_text, 
                alternative_a, 
                alternative_b, 
                alternative_c, 
                alternative_d, 
                correct_answer
            FROM questions
            WHERE department_id = %s
            ORDER BY id;
        """, (department_id,))
        questions = cur.fetchall()
        cur.close()
        return questions
    except Exception as e:
        print(f"Erro ao buscar questões por departamento: {e}")
        return []
    finally:
        if conn:
            conn.close()
