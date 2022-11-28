import streamlit as st
from functions import add

def tablefill():
    col1,col2=st.columns(2)
    with col1:
        PRODUCT_ID=st.text_input("PRODUCT_ID:")
        PRODUCT_NAME=st.text_input("PRODUCT_NAME:")
    with col2:
        START_DATE=st.date_input("INTRODUCTION DATE:")
        LIFE_SPAN=st.number_input("LIFE SPAN:")
        PRODUCT_TYPE=st.text_input("PRODUCT TYPE:")
        BOOKING_STATUS=st.text_input("BOOKING STATUS(YES/NO):")

    if st.button("add item:"):
        add(PRODUCT_ID.upper(),PRODUCT_NAME.upper(),START_DATE,LIFE_SPAN,PRODUCT_TYPE.upper(),BOOKING_STATUS.upper())
        st.success("successfully added product '{}' with id '{}'".format(PRODUCT_NAME,PRODUCT_ID))