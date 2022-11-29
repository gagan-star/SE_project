import streamlit as st
from functions import table_create,user_view_all,user_view_all_morelifespan,user_view_all_lesslifespan,user_view_all_based_on_name
from update import user_book
from display import display

def main():

        st.title("PERISHABLE MANAGEMENT SYSTEM:")
        menu=["filter",'book']
        choice=st.sidebar.selectbox("menu",menu)
        table_create()



        if choice=="book":
            st.subheader("task opted to update booking status:")
            user_book()
        elif choice=="filter":
            opt=['view all','view products having lesser life span than entered value','view products having more life span than entered value','view based on product name']
            question=st.selectbox("select queries",opt)
            if question==opt[0]:
                result=user_view_all()
                display(result)
            elif question==opt[1]:
                st.subheader("view all product with less lifespan than entered value")
                lifespan=st.number_input("enter lifespan:")
                result=user_view_all_lesslifespan(lifespan)
                display(result)
            elif question==opt[2]:
                st.subheader("view all product with more lifespan than entered value")
                lifespan=st.number_input("enter lifespan:")
                result=user_view_all_morelifespan(lifespan)
                display(result)
            elif question==opt[3]:
                st.subheader("view based on product name")
                name=st.text_input("enter product name to search:")
                name=name.upper()
                result=user_view_all_based_on_name(name)
                if result:
                    display(result)
                else:
                    st.error("'{}' not in database".format(name))


        else:
            st.subheader("about tasks:")
if __name__=='__main__':
        main()


