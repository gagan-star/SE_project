import streamlit as st
from functions import delete_data,view_all,view_id
import pandas as pd

def delete():
    result=view_all()
    df=pd.DataFrame(result,columns=['PRODUCT ID','PRODUCT NAME','SHOP INRODUCTION DATE','LIFE SPAN','PRODUCT TYPE','BOOKING STATUS'])
    with st.expander("current data"):
        st.dataframe(df)
    list_of_product_id=[i[0] for i in view_id()]
    selected_item=st.selectbox("item to delete",list_of_product_id)
    st.warning("do you want to delete product with id '{}'".format(selected_item))

    if st.button("delete item"):
        delete_data(selected_item)
        st.success("item successfully deleted")
    new_result=view_all()
    df2=pd.DataFrame(new_result,columns=['PRODUCT ID','PRODUCT NAME','SHOP INRODUCTION DATE','LIFE SPAN','PRODUCT TYPE','BOOKING STATUS'])
    with st.expander("updated details:"):
        st.dataframe(df2)
        



