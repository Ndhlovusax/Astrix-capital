import streamlit as st
from astrix.components import render_header

render_header()
st.title("Asset Details")
st.markdown("Detailed view of XAUUSD order flow, liquidity heatmaps, & macro triggers.")