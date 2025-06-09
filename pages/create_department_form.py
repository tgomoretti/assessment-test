import streamlit as st
from avaliation.infrastructure.db.departments.create_department import create_department

st.title("Cadastro de Departamento")

with st.form("department_form"):
    department_name = st.text_input("Nome do Departamento *")
    submitted = st.form_submit_button("Salvar")

if submitted:
    if not department_name:
        st.warning("Por favor, preencha o nome do departamento.")
    else:
        department_id = create_department(department_name)
        if department_id:
            st.success(f"Departamento criado com sucesso! ID: {department_id}")
        else:
            st.error("Erro ao cadastrar departamento.")
