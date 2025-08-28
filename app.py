import streamlit as st
from astrix.components import render_header

st.set_page_config(page_title="Astrix Capital v3", layout="wide")

render_header()

st.title("Astrix Capital v3 - Directional Confidence Dashboard")
st.markdown("## Multi-factor trading insights for XAUUSD & more (COT + Sentiment + Macro + Order Flow)")
st.info("This is a skeleton. Plug in your data feeds to go live.")