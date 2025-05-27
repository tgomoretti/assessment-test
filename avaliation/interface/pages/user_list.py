import streamlit as st
from avaliation.infrastructure.db.user.get_all_users import get_all_users

st.title("Usuários cadastrados")

users = get_all_users()

if users:
    st.dataframe(users)
else:
    st.info("Sem usuários cadastrados.")