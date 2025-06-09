import streamlit as st
from avaliation.infrastructure.db.questions.get_questions_by_department import get_questions_by_department
from avaliation.infrastructure.db.questions.update_question import update_question
from avaliation.infrastructure.db.departments.get_departments import get_departments

st.title("Editar Questão")

# Buscar departamentos do banco
departments = get_departments()
department_options = {f"{name} (ID: {id})": id for id, name in departments}

# Seleciona departamento
selected_department_key = st.selectbox("Selecione o departamento", list(department_options.keys()))
selected_department_id = department_options[selected_department_key]

# Busca questões do departamento selecionado
questions = get_questions_by_department(selected_department_id)
if not questions:
    st.info("Nenhuma questão cadastrada para este departamento.")
    st.stop()

# Dicionário para mostrar no selectbox
question_options = {f"ID {id} - {text[:50]}": id for id, text, *_ in questions}

# Seleciona questão para edição
selected_question_key = st.selectbox("Selecione a questão para editar", list(question_options.keys()))
selected_question_id = question_options[selected_question_key]

# Busca dados da questão selecionada para preencher formulário
question_data = next(q for q in questions if q[0] == selected_question_id)
# question_data estrutura: (id, question_text, alternative_a, alternative_b, alternative_c, alternative_d, correct_answer)

with st.form("edit_question_form"):
    question_text = st.text_input("Pergunta *", value=question_data[1])
    alternative_a = st.text_input("Alternativa A *", value=question_data[2])
    alternative_b = st.text_input("Alternativa B *", value=question_data[3])
    alternative_c = st.text_input("Alternativa C *", value=question_data[4])
    alternative_d = st.text_input("Alternativa D *", value=question_data[5])
    correct_answer = st.text_input("Alternativa correta *", value=question_data[6])

    submitted = st.form_submit_button("Salvar alterações")

if submitted:
    if not question_text or not alternative_a or not alternative_b or not alternative_c or not alternative_d or not correct_answer:
        st.warning("Por favor, preencha todos os campos obrigatórios (*).")
    else:
        updated_data = {
            "id": selected_question_id,
            "question_text": question_text,
            "alternative_a": alternative_a,
            "alternative_b": alternative_b,
            "alternative_c": alternative_c,
            "alternative_d": alternative_d,
            "correct_answer": correct_answer
        }
        success = update_question(updated_data)
        if success:
            st.success("Questão atualizada com sucesso!")
        else:
            st.error("Erro ao atualizar a questão.")
