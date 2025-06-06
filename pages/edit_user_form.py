import streamlit as st
from avaliation.infrastructure.db.user.get_user_by_id import get_user_by_id
from avaliation.infrastructure.db.user.update_user import update_user

if 'edit_user_id' not in st.session_state:
    st.warning("Por favor, escolha um usuário para editar.")
    st.stop()
    
user_id = st.session_state.edit_user_id
user = get_user_by_id(user_id)

if not user:
    st.error("Usuário nao encontrado.")
    st.stop()
    
with st.form("edit_user_form"):
    name = st.text_input("Nome completo", user['name'])
    phone = st.text_input("Telefone", user['phone'])
    email = st.text_input("Email", user['email'])
    health_unit = st.text_input("Unidade de saúde", user['health_unit'])
    municipality = st.text_input("Município", user['municipality'])
    responsible_analyst = st.text_input("Analista responsável pela capacitação", user['responsible_analyst'])
    responsible_manager = st.text_input("Gestor responsável da unidade", user['responsible_manager'])

    submitted = st.form_submit_button("Atualizar")
    
if submitted:
    user_data = {
        "name": name,
        "phone": phone,
        "email": email,
        "health_unit": health_unit,
        "municipality": municipality,
        "responsible_analyst": responsible_analyst,
        "responsible_manager": responsible_manager
    }
    update_user(user_id, user_data)
    st.success("Usuário atualizado com sucesso!")
