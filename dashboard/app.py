import streamlit as st
from scripts.run_pipeline import run

st.title("AlphaPred Dashboard")

data = run()

for e in data:
    st.write(f"### {e['question']}")
    st.write(f"Market: {e['prob_market']:.2f}")
    st.write(f"Model: {e['prob_model']:.2f}")
    st.write(f"Alpha: {e['alpha']:.2f}")
    st.write(f"Signal: {e['signal']}")