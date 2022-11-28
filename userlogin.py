import streamlit as st
from functions import user_login_check
from userinterface import main


def userlogin():

    user_id = st.text_input("user_id:",'enter_id')
    password = st.text_input("password:",'password')
    if st.checkbox("login"):
        if user_login_check(user_id, password):
            main()
        else:
            st.error("invalid credentials if not signed signup")

