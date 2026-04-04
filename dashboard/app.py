import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath("."))

from scripts.run_pipeline import run

# Config da página
st.set_page_config(
    page_title="AlphaPred",
    layout="wide"
)

st.title("📊 AlphaPred Dashboard")
st.markdown("### Market Inefficiency Scanner")

# Rodar pipeline
data = run()

if not data:
    st.warning("No data available")
    st.stop()

# Converter pra DataFrame
df = pd.DataFrame(data)

# Ordenar por alpha absoluto (melhores oportunidades)
df = df.sort_values(by="alpha", key=abs, ascending=False)

# 🎯 KPIs (topo)
col1, col2, col3 = st.columns(3)

col1.metric("Total Events", len(df))
col2.metric("Avg Alpha", round(df["alpha"].mean(), 3))
col3.metric("Strong Signals", len(df[df["signal"].str.contains("STRONG")]))

st.divider()

# 🔥 Top oportunidades
st.subheader("🔥 Top Opportunities")

top = df.head(5)

for _, row in top.iterrows():
    color = "🟢" if row["alpha"] > 0 else "🔴"

    with st.container():
        st.markdown(f"## {color} {row['question']}")
        
        col1, col2, col3, col4 = st.columns(4)
        
        col1.metric("Market", round(row["prob_market"], 2))
        col2.metric("Model", round(row["prob_model"], 2))
        col3.metric("Alpha", round(row["alpha"], 3))
        col4.metric("Signal", row["signal"])
        
        st.progress(min(max(row["prob_model"], 0), 1))

        st.divider()

# 📋 Tabela completa
st.subheader("📋 All Events")

st.dataframe(df, use_container_width=True)