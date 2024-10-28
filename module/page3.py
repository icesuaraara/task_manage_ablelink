import streamlit as st
import pandas as pd

def menu_3():
    st.title('Task Insert')
    tab1, tab2, tab3, tab4, tab5= st.tabs(["Website", "SEO","TVT","Spon","Online"])


    # แท็บสำหรับแสดงกราฟ
    with tab1:
        st.header("Website")
        

    # แท็บสำหรับแสดงข้อมูล
    with tab2:
        st.header("SEO")
        
    
    with tab3:
        st.header("TVT")
        
    
    with tab4:
        st.header("Spon")
        
    
    with tab5:
        st.header("Online")