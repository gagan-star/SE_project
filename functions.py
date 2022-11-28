import mysql.connector
import streamlit as st
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ya@636156",
    database="PERISHABLE_MANAGEMENT"
)
c=mydb.cursor()
def table_create():
    c.execute("CREATE TABLE IF NOT EXISTS PERISHABLE(PRODUCT_ID VARCHAR(20),PRODUCT_NAME VARCHAR(20),START_DATE DATE,LIFE_SPAN INT,TYPE VARCHAR(20),BOOKING_STATUS VARCHAR(20))")
    c.execute("CREATE TABLE IF NOT EXISTS USER_LOGIN(USER_ID VARCHAR(20),PASSWORD VARCHAR(20))")
    c.execute("CREATE TABLE IF NOT EXISTS ADMIN_LOGIN(ADMIN_ID VARCHAR(20),PASSWORD VARCHAR(20))")



def add(PRODUCT_ID,PRODUCT_NAME,START_DATE,LIFE_SPAN,TYPE,BOOKING_STATUS):
    c.execute("INSERT INTO PERISHABLE VALUES('{}','{}','{}','{}','{}','{}')".format(PRODUCT_ID,PRODUCT_NAME,START_DATE,LIFE_SPAN,TYPE,BOOKING_STATUS))
    mydb.commit()

def view_all():
    c.execute("SELECT*FROM PERISHABLE")
    data=c.fetchall()
    return data
def delete_data(PRODUCT_ID):
    c.execute("DELETE FROM PERISHABLE WHERE PRODUCT_ID='{}'".format(PRODUCT_ID))
    mydb.commit()
def get_specific_product(PRODUCT_ID):
    c.execute("SELECT *FROM PERISHABLE WHERE PRODUCT_ID='{}'".format(PRODUCT_ID))
    data=c.fetchall()
    return data
def update_info(PRODUCT_ID,NEW_BOOKING_STATUS,BOOKING_STATUS):
    c.execute("UPDATE PERISHABLE SET BOOKING_STATUS='{}' WHERE PRODUCT_ID='{}'".format(NEW_BOOKING_STATUS,PRODUCT_ID))
    mydb.commit()
    data=c.fetchall()
    return data
def view_id():
    c.execute("SELECT PRODUCT_ID FROM PERISHABLE")
    data=c.fetchall()
    return data

def view_all_lesslifespan(lifespan):
    c.execute("SELECT *FROM PERISHABLE WHERE PERISHABLE.LIFE_SPAN <='{}'".format(lifespan))
    data=c.fetchall()
    return data
def view_all_morelifespan(lifespan):
    c.execute("SELECT *FROM PERISHABLE WHERE PERISHABLE.LIFE_SPAN >='{}'".format(lifespan))
    data=c.fetchall()
    return data
def view_all_based_on_name(product_name):
    c.execute("SELECT *FROM PERISHABLE WHERE PERISHABLE.PRODUCT_NAME ='{}'".format(product_name))
    data=c.fetchall()
    return data
def view_all_based_on_booking(status):
    c.execute("SELECT *FROM PERISHABLE WHERE PERISHABLE.BOOKING_STATUS ='{}'".format(status))
    data=c.fetchall()
    return data



def user_login_check(id,password):
    c.execute("SELECT*FROM USER_LOGIN WHERE USER_LOGIN.USER_ID='{}' AND USER_LOGIN.PASSWORD='{}'".format(id,password))
    result=c.fetchall()
    if result:
        return 1
    else:
        return 0
def admin_login_check(id,password):
    c.execute("SELECT*FROM ADMIN_LOGIN WHERE ADMIN_LOGIN.ADMIN_ID='{}' AND ADMIN_LOGIN.PASSWORD='{}'".format(id,password))
    result=c.fetchall()
    if result:
        return 1
    else:
        return 0
def user_view_all():
    c.execute("SELECT*FROM PERISHABLE WHERE PERISHABLE.BOOKING_STATUS='NO'")
    data=c.fetchall()
    return data

def user_view_all_lesslifespan(lifespan):
    c.execute("SELECT *FROM PERISHABLE WHERE PERISHABLE.LIFE_SPAN <='{}'AND PERISHABLE.BOOKING_STATUS='NO'".format(lifespan))
    data=c.fetchall()
    return data
def user_view_all_morelifespan(lifespan):
    c.execute("SELECT *FROM PERISHABLE WHERE PERISHABLE.LIFE_SPAN >='{}' AND PERISHABLE.BOOKING_STATUS='NO'".format(lifespan))
    data=c.fetchall()
    return data
def user_view_all_based_on_name(product_name):
    c.execute("SELECT *FROM PERISHABLE WHERE PERISHABLE.PRODUCT_NAME ='{}' AND PERISHABLE.BOOKING_STATUS='NO'".format(product_name))
    data=c.fetchall()
    return data
def user_view_id():
    c.execute("SELECT PRODUCT_ID FROM PERISHABLE WHERE PERISHABLE.BOOKING_STATUS='NO'")
    data=c.fetchall()
    return data
def user_signup(id,password):
    c.execute("INSERT INTO USER_LOGIN VALUES('{}','{}')".format(id,password))
    mydb.commit()

def check_id(id):
    c.execute("SELECT * FROM PERISHABLE WHERE PERISHABLE.PRODUCT_ID='{}'".format(id))
    data=c.fetchall()
    if(data):
        return 0
    return 1


