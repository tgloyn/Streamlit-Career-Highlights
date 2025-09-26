import streamlit as st
from helpers import *

check_password()
st.set_page_config(page_title="Publications", page_icon=":books:", layout="wide")
headshot_and_title("Publications")

st.write('---')
st.write('')
st.write('')

st.write("""
- **Gloyn. T. et al. (2025). Using Artificial Intelligence to 
Predict Patient Wait-Times in the Emergency Department: A Scoping Review. Artificial Intelligence in Medicine.** *Under Review*
""")