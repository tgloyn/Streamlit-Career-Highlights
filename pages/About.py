import streamlit as st
from helpers import *

st.set_page_config(page_title="About Me", page_icon=":wave:", layout="wide")

headshot_and_title("About Me")

st.write('')
st.write('')
st.write("""
Hello! 

I'm Troy, a dedicated **Data Science professional** with a passion for **improving patient outcomes** and **streamlining emergency department operations**. I have gained extensive experience working with **large datasets, predictive modeling, and data visualization** using electronic medical record (EMR) data, with expertise in **Python and R**. My goal is to leverage my skills and knowledge to enhance the efficiency and effectiveness of emergency care delivery.
""")

st.write("""
Aside from Data Science, I also enjoy reading (mostly non-fiction), strength training, playing and following sports (hockey, golf, tennis, football), and exploring the outdoors.
        """)
