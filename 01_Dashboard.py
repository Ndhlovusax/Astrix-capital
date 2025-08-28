import streamlit as st
from astrix.components import render_header

render_header()
st.title("Dashboard")
st.markdown("Visualize XAUUSD confidence levels, sentiment overlays & COT data here.")