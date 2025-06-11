import streamlit as st
from avaliation.infrastructure.db.user.get_all_users import get_all_users

st.title("Usuários cadastrados")

users = get_all_users()

for user in users:
    st.write(f"**{user['name']}** - {user['email']}")
    if st.button(f"Editar {user['id']}"):
        st.session_state.edit_user_id = user['id']
        st.switch_page("pages/2_Editar usuário.py")
        
st.markdown("---")