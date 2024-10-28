import streamlit as st
from streamlit_option_menu import option_menu

import module.page1 as page1
import module.page2 as page2
import module.page3 as page3
import module.page4 as page4

st.set_page_config(page_title="To do list", 
                   layout="wide")


with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Task Manage','Task Insert','Transform'], 
        icons=['house', 'bi bi-card-checklist','bi bi-pencil-square','file-earmark-arrow-up'], menu_icon="cast", default_index=0)

if selected == 'Home':
    page1.menu_1()

elif selected == 'Task Manage':
    page2.menu_2()

elif selected == 'Task Insert':
    page3.menu_3()

elif selected == 'Transform':
    page4.menu_4()
