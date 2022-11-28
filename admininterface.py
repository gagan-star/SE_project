import streamlit as st
from functions import table_create, view_all, view_all_morelifespan, view_all_lesslifespan, view_all_based_on_booking, \
    view_all_based_on_name
from tablefill import tablefill
from delete import delete



from display import display


def main():
    st.title("PERISHABLE MANAGEMENT SYSTEM:")
    menu = ["queries", "delete", 'add']
    choice = st.sidebar.selectbox("menu", menu)
    table_create()

    if choice == "delete":
        st.subheader("deleting task choosen:")
        delete()
    elif choice == "add":
        st.subheader("add new data into perishable management database:")
        tablefill()




    elif choice == "queries":
        opt = ['view all', 'view products having lesser life span than entered value',
               'view products having more life span than entered value', 'view based on product name',
               'view based on booking status']
        question = st.selectbox("select queries", opt)
        if question == opt[0]:
            result = view_all()
            display(result)
        elif question == opt[1]:
            st.subheader("view all product with less lifespan than entered value")
            lifespan = st.number_input("enter lifespan:")
            result = view_all_lesslifespan(lifespan)
            display(result)
        elif question == opt[2]:
            st.subheader("view all product with more lifespan than entered value")
            lifespan = st.number_input("enter lifespan:")
            result = view_all_morelifespan(lifespan)
            display(result)
        elif question == opt[3]:
            st.subheader("view based on product name")
            name = st.text_input("enter product name to search:")
            result = view_all_based_on_name(name)
            if result:
                display(result)
            else:
                st.error("'{}' not in database".format(name))
        elif question == opt[4]:
            st.subheader("view products based on booking status:")
            booking_status = st.text_input("enter booking status(YES/NO):")
            if st.button("view"):
                if booking_status == 'YES' or booking_status == 'NO':
                    result = view_all_based_on_booking(booking_status)
                    if result:
                        display(result)
                    else:
                        st.error("currently no element with booking status:'{}'".format(booking_status))

                else:
                    st.error("enter YES/NO , value entered :'{}'".format(booking_status))

    else:
        st.subheader("about tasks:")


if __name__ == '__main__':
    main()


