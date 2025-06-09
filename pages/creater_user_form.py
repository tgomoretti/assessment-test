import streamlit as st
from avaliation.infrastructure.db.user.create_user import create_user
from avaliation.infrastructure.db.departments.get_departments import get_departments
from avaliation.core.utils.validators import is_valid_email, format_phone
import os
from dotenv import load_dotenv
load_dotenv()

st.title("Cadastro de Participante")

departments = get_departments()
dept_dict = {d[1]: d[0] for d in departments}

with st.form("user_form"):
    name = st.text_input("Nome completo *")
    phone = st.text_input("Telefone * (XX) XXXXX-XXXX")
    email = st.text_input("Email * (Ex: seuemail@example.com)")
    health_unit = st.text_input("Unidade de saúde *")
    municipality = st.text_input("Município *")
    responsible_analyst = st.text_input("Analista responsável pela capacitação *")
    responsible_manager = st.text_input("Gestor responsável da unidade *")
    selected_department = st.selectbox("Departamento *", options=list(dept_dict.keys()))

    submitted = st.form_submit_button("Salvar")

if submitted:
    if not name or not phone or not email or not health_unit or not municipality or not responsible_analyst or not responsible_manager:
        st.warning("Por favor, preencha todos os campos obrigatórios (*).")
    elif not is_valid_email(email):
        st.warning("Por favor, insira um email válido.")
    elif not format_phone(phone):
        st.warning("Por favor, insira um telefone válido.")
    else:
        user_data = {
            "name": name,
            "phone": phone,
            "email": email,
            "health_unit": health_unit,
            "municipality": municipality,
            "responsible_analyst": responsible_analyst,
            "responsible_manager": responsible_manager,
            "id_department": dept_dict[selected_department]
        }

        user_id = create_user(user_data)
        if user_id:
            st.success(f"Usuário cadastrado com sucesso! ID: {user_id}")
        else:
            st.error("Erro ao cadastrar usuário.")
