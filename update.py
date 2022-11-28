import streamlit as st
from functions import update_info,get_specific_product,view_all,view_id,user_view_all,user_view_id
import pandas as pd

def update():
    result=view_all()
    df=pd.DataFrame(result,columns=['PRODUCT ID','PRODUCT NAME','SHOP INRODUCTION DATE','LIFE SPAN','PRODUCT TYPE','BOOKING STATUS'])
    with st.expander("current data"):
        st.dataframe(df)
    list_of_product_id=[i[0] for i in view_id()]
    selected_item=st.selectbox("select to update:",list_of_product_id)
    selected_result=get_specific_product(selected_item)
    if selected_result:
        PRODUCT_ID=selected_result[0][0]
        BOOKING_STATUS=selected_result[0][5]

        NEW_BOOKING_STATUS=st.text_input("new booking status",BOOKING_STATUS)
        if st.button("update:"):
            if(NEW_BOOKING_STATUS=='YES' or NEW_BOOKING_STATUS=='NO'):
                update_info(PRODUCT_ID,NEW_BOOKING_STATUS.upper(),BOOKING_STATUS)
                st.success("updated successfully from '{}' to '{}'".format(BOOKING_STATUS,NEW_BOOKING_STATUS))
            else:
                st.error("enter either yse or no you entered '{}'".format(NEW_BOOKING_STATUS))
    result2=view_all()
    df2=pd.DataFrame(result2,columns=['PRODUCT ID','PRODUCT NAME','SHOP INRODUCTION DATE','LIFE SPAN','PRODUCT TYPE','BOOKING STATUS'])
    with st.expander("updated data"):
        st.dataframe(df2)
def user_book():
    result=user_view_all()
    df=pd.DataFrame(result,columns=['PRODUCT ID','PRODUCT NAME','SHOP INRODUCTION DATE','LIFE SPAN','PRODUCT TYPE','BOOKING STATUS'])
    with st.expander("current data"):
        st.dataframe(df)
    list_of_product_id=[i[0] for i in user_view_id()]
    selected_item=st.selectbox("select to update:",list_of_product_id)
    selected_result=get_specific_product(selected_item)
    if selected_result:
        PRODUCT_ID=selected_result[0][0]
        BOOKING_STATUS=selected_result[0][5]

        NEW_BOOKING_STATUS=st.text_input("new booking status",BOOKING_STATUS)
        NEW_BOOKING_STATUS=NEW_BOOKING_STATUS.upper()
        if st.button("update:"):
            if(NEW_BOOKING_STATUS=='YES' or NEW_BOOKING_STATUS=='NO'):

                update_info(PRODUCT_ID,NEW_BOOKING_STATUS.upper(),BOOKING_STATUS)
                st.success("updated successfully from '{}' to '{}'".format(BOOKING_STATUS,NEW_BOOKING_STATUS.upper()))
            else:
                st.error("enter either yse or no you entered '{}'".format(NEW_BOOKING_STATUS))

    result2=user_view_all()
    df2=pd.DataFrame(result2,columns=['PRODUCT ID','PRODUCT NAME','SHOP INRODUCTION DATE','LIFE SPAN','PRODUCT TYPE','BOOKING STATUS'])
    with st.expander("updated data"):
        st.dataframe(df2)


