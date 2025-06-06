import streamlit as st
from avaliation.infrastructure.db.questions.create_question import create_question
from avaliation.infrastructure.db.departments.get_departments import get_departments
import os
from dotenv import load_dotenv
load_dotenv()

st.title ("Cadastro de questões")

# Buscar departamentos do banco
departments = get_departments()
department_options = {f"{name} (ID: {id})": id for id, name in departments}

departament_key = st.selectbox("Selecione o departamento", list(department_options.keys()))
department_id = department_options[departament_key]

with st.form("question_form"):
    question_text = st.text_input("Pergunta *")
    alternative_a = st.text_input("Alternativa A *")
    alternative_b = st.text_input("Alternativa B *")
    alternative_c = st.text_input("Alternativa C *")
    alternative_d = st.text_input("Alternativa D *")
    correct_answer = st.selectbox("Alternativa correta *", ["A", "B", "C", "D"])
 
    submitted = st.form_submit_button("Salvar")
    
if submitted:
    if not question_text or not alternative_a or not alternative_b or not alternative_c or not alternative_d or not correct_answer:
        st.warning("Por favor, preencha todos os campos obrigatórios (*).")
    else:
        question_data = {
            "department_id": department_id,
            "question_text": question_text,
            "alternative_a": alternative_a,
            "alternative_b": alternative_b,
            "alternative_c": alternative_c,
            "alternative_d": alternative_d,
            "correct_answer": correct_answer
        }
        
        question_id = create_question(question_data)
        if question_id:
            st.success(f"Questão cadastrada com sucesso! ID: {question_id}")
        else:
            st.error("Erro ao cadastrar questão.")