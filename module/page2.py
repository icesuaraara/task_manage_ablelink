import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
from mysql.connector import Error

def menu_2():
    def create_connection():
        connection = None
        try:
            connection = mysql.connector.connect(
                host='192.168.1.123',  # เปลี่ยนเป็น Hostname หรือ IP ของ MySQL
                user='admin',  # ชื่อผู้ใช้ MySQL
                password='admin1234',  # รหัสผ่าน MySQL
                database='task_manage'  # ชื่อฐานข้อมูล
            )
        except Error as e:
            st.error(f"Error: {e}")
        return connection
    


    st.title('Task Mangaer')
    # สร้างแท็บสองแท็บ: แท็บแรกสำหรับแสดงกราฟ แท็บที่สองสำหรับแสดงข้อมูล
    tab1, tab2, tab3, tab4, tab5= st.tabs(["Website", "SEO","TVT","Spon","Online"])


    # แท็บสำหรับแสดงกราฟ
    with tab1:
        st.header("Website")
        # connection = create_connection()
        # st.write(connection)


    # แท็บสำหรับแสดงข้อมูล
    with tab2:
        st.header("SEO")
        
    
    with tab3:
        st.header("TVT")
        
    
    with tab4:
        st.header("Spon")
        
    
    with tab5:
        st.header("Online")
        