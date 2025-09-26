import streamlit as st
from helpers import *

check_password()
st.set_page_config(page_title="Testimonials", page_icon=":speech_balloon:", layout="wide")

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

headshot_and_title("Testimonials")

st.write('---')

st.markdown("""
<style>
/* Apply to all alert boxes: info/success/warning/error */
.stAlert {
  min-height: 500px;         /* tweak to your needs */
  display: flex;              /* let inner wrap stretch */
}
.stAlert > div {
  flex: 1;
}
</style>
""", unsafe_allow_html=True)

testimonials = st.columns(3)

with testimonials[0]:
    st.info("I've had the pleasure to work with Troy for the past two years and he would be a great addition to any data science team. He is a quick learner and takes initiative in his work, independently finding solutions while also collaborating well with other data scientists, research staff, and clinicians. Troy is an effective communicator, able to explain his work to audiences with varying levels of technical expertise. He has been instrumental in building our team's relationship with the emergency department and has contributed positively to our team morale.\n"
            " \n— **Christina Seo, MASc, Data Scientist, Humber River Health**")

with testimonials[1]:
    st.info("I’ve had the pleasure of working with and training many students and colleagues over the course of my PhD, postdoctoral fellowship and as a senior data scientist and Troy is easily one of the strongest colleagues I have mentored. He is a quick learner, an eager data scientist and a consummate professional in the workplace. He often goes above and beyond for a task and his infectious enthusiasm in tackling projects is a wonderful asset I am sure he will carry with him in his future endeavors. He will always put in the extra mile, and I wish him the very best in his career- I am sure he will make it count!\n"
            " \n— **Krutika Joshi, PhD, Data Scientist, Humber River Health**")

with testimonials[2]:
    st.info("I had the chance to work with Troy at ITR Laboratories. His performance was above expectations, he excellently performed the required tasks and beyond, always willing to take new challenges and learn new skills. To add into that he has a calm, easy going and disciplined character, he adapts quickly to changing situations and handles stress very well. "
            "Troy, working with you was awesome and I wish you the great career that you deserve..\n"
            " \n— **Sabrina Makhlouf, MSc, Scientist, ITR Laboratories Inc.**")