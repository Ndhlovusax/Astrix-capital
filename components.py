import streamlit as st

def render_header():
    st.image("assets/logo.svg", width=140)
    st.markdown("<h3 style='color:#00E5FF;'>Astrix Capital</h3>", unsafe_allow_html=True)