import streamlit as st
from userlogin import userlogin
from adminlogin import adminlogin
from usersignup_page import usersignup

def main():
    st.title("welcome to store team 7")
    st.subheader("please login")
    options=['userlogin','adminlogin','user signup']
    choice = st.sidebar.selectbox("menu", options)

    if choice==options[0]:
        userlogin()
    elif choice==options[1]:
        adminlogin()
    elif choice==options[2]:
        usersignup()
    else:
        st.subheader("about tasks:")

if __name__ == '__main__':
    main()

