import streamlit as st
from functions import admin_login_check
from admininterface import main


def adminlogin():
    st.subheader("admin login page")
    user_id = st.text_input("admin_id:",'enter id')
    password = st.text_input("password:",type="password")

    a=st.checkbox('login/logout')
    if a:
        if admin_login_check(user_id, password):
            main()
        else :
            st.error("invalid credentials")


