import streamlit as st
from helpers import *

check_password()
st.set_page_config(page_title="Publications", page_icon=":books:", layout="wide")
headshot_and_title("Publications")

st.write('---')
st.write('')
st.write('')

st.write("""
- Gloyn, T., Seo, C., Godinho, A., Rahul, R., Phadke, S., Fotheringham, H., & Wegier, P. (2025). Using artificial intelligence to predict patient wait times in the emergency department: A scoping review. Artificial Intelligence in Medicine, 103316.
""")

st.write('\n\n')
st.write('\n\n')
st.write('\n\n')
st.subheader("Conferences")

st.write("""
- Gloyn, T. (2025, December 7-10). Emergency Department Surge Forecasting Using Machine Learning Methods. Institute for Healthcare Improvement Forum. Anaheim, California. 
         """)
