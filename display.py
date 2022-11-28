import streamlit as st
import pandas as pd


def display(result):

    df=pd.DataFrame(result,columns=['PRODUCT ID','PRODUCT NAME','SHOP INRODUCTION DATE','LIFE SPAN','PRODUCT TYPE','BOOKING STATUS'])
    with st.expander("store perishable product details"):
        st.dataframe(df)


