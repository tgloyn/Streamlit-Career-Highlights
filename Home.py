import streamlit as st
from streamlit_timeline import timeline
import json
from helpers import *

check_password()

st.set_page_config(page_title="Career Highlights", page_icon=":briefcase:", layout="wide", initial_sidebar_state="expanded")

# Custom CSS to reduce top padding and style header
st.markdown("""
    <style>
        /* Shrink top padding */
        .block-container {
            padding-top: 0.6rem !important;
            padding-bottom: 2rem !important;
        }
        /* Optional: remove extra header space (toolbar) */
        header[data-testid="stHeader"] {
            height: 0px;
            background: transparent;
        }
        /* Optional: hide menu & deploy button if you want it cleaner */
        /* div[data-testid="stToolbar"] { display: none !important; } */
    </style>
""", unsafe_allow_html=True)

headshot_and_title("Career Highlights")

st.write('---')

data = json.load(open('assets/timeline_data.json'))

timeline(data['timeline'], height=650)  # accepts dict or JSON string