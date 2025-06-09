import streamlit as st
from avaliation.infrastructure.db.departments.get_departments import get_departments
from avaliation.infrastructure.db.questions.get_questions import get_questions_by_department

st.title("Listagem de Questões por Departamento")

# Buscar departamentos
departments = get_departments()
department_options = {f"{name} (ID: {id})": id for id, name in departments}

selected_key = st.selectbox("Selecione o departamento", list(department_options.keys()))

if selected_key:
    department_id = department_options[selected_key]
    questions = get_questions_by_department(department_id)

    if not questions:
        st.warning("Nenhuma questão cadastrada para este departamento.")
    else:
        st.subheader("Questões cadastradas:")
        for q in questions:
            st.markdown(f"""
            **ID:** {q[0]}  
            **Pergunta:** {q[1]}  
            - A: {q[2]}  
            - B: {q[3]}  
            - C: {q[4]}  
            - D: {q[5]}  
            **Correta:** {q[6]}  
            ---
            """)
