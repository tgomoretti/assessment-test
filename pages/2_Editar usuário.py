import streamlit as st
from avaliation.infrastructure.db.user.get_user_by_id import get_user_by_id
from avaliation.infrastructure.db.user.update_user import update_user
from avaliation.infrastructure.db.departments.get_departments import get_departments

st.set_page_config(page_title="Cadastrar Usuário", layout="wide")
st.title("Cadastro de Usuário")

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
    id_department = st.text_input("Departamento", user['id_department'])

    submitted = st.form_submit_button("Atualizar")
    
departments = get_departments()
dept_dict = {name: id for id, name in departments} 

current_dept = next((name for name, id_ in dept_dict.items() if id_ == user['id_department']), None)
selected_department = st.selectbox("Departamento", options=list(dept_dict.keys()), index=list(dept_dict.keys()).index(current_dept))

if submitted:
    user_data = {
        "name": name,
        "phone": phone,
        "email": email,
        "health_unit": health_unit,
        "municipality": municipality,
        "responsible_analyst": responsible_analyst,
        "responsible_manager": responsible_manager,
        "id_department": dept_dict[selected_department],
    }
    update_user(user_id, user_data)
    st.success("Usuário atualizado com sucesso!")
