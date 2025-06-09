import psycopg2
from psycopg2 import sql
from avaliation.infrastructure.db.connection import connect_db

def update_question(question_data):
    """
    Atualiza uma questão no banco de dados.

    question_data deve conter:
    - id
    - question_text
    - alternative_a
    - alternative_b
    - alternative_c
    - alternative_d
    - correct_answer
    """
    conn = None
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = sql.SQL("""
            UPDATE questions
            SET
                question_text = %s,
                alternative_a = %s,
                alternative_b = %s,
                alternative_c = %s,
                alternative_d = %s,
                correct_answer = %s
            WHERE id = %s;
        """)
        cur.execute(query, (
            question_data['question_text'],
            question_data['alternative_a'],
            question_data['alternative_b'],
            question_data['alternative_c'],
            question_data['alternative_d'],
            question_data['correct_answer'],
            question_data['id']
        ))
        conn.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Erro ao atualizar questão: {e}")
        return False
    finally:
        if conn:
            conn.close()
