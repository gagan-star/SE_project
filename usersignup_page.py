import streamlit as st
from functions import user_login_check,user_signup




def usersignup():

    user_id = st.text_input("user_id:",'enter id')
    password = st.text_input("password:",'password')
    if st.checkbox('proceed'):
        if user_login_check(user_id, password):
            st.error("credientials alredy exists use different ")

        else:
            user_signup(user_id,password)
            st.success("signed up successfull please log in ")

    return








