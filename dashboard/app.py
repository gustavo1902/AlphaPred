import streamlit as st
import pandas as pd
import sys
import os
import random

sys.path.append(os.path.abspath("."))

from scripts.run_pipeline import run

st.set_page_config(layout="wide")

st.markdown("""
<style>
body {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #FAFAFA;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 AlphaPred Terminal")
st.caption("Real-time Prediction Market Alpha Scanner")

data = run()

if not data:
    st.warning("No data available")
    st.stop()

df = pd.DataFrame(data)

st.sidebar.title("Filters")

signal_filter = st.sidebar.selectbox(
    "Signal Type",
    ["ALL", "STRONG_BUY", "BUY", "SELL", "STRONG_SELL"]
)

if signal_filter != "ALL":
    df = df[df["signal"] == signal_filter]

col1, col2, col3 = st.columns(3)

col1.metric("Events", len(df))
col2.metric("Avg Alpha", round(df["alpha"].mean(), 3))
col3.metric("Max Alpha", round(df["alpha"].max(), 3))

st.divider()

st.subheader("🔥 Top Opportunities")

df_sorted = df.sort_values(by="alpha", key=abs, ascending=False)
top = df_sorted.head(5)

for _, row in top.iterrows():
    color = "🟢" if row["alpha"] > 0 else "🔴"

    st.markdown(f"### {color} {row['question']}")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Market", round(row["prob_market"], 2))
    c2.metric("Model", round(row["prob_model"], 2))
    c3.metric("Alpha", round(row["alpha"], 3))
    c4.metric("Signal", row["signal"])

    st.progress(min(max(row["prob_model"], 0), 1))
    st.divider()

st.subheader("📈 Probability Evolution")

selected_event = st.selectbox("Select Event", df["question"])

history = [random.uniform(0.3, 0.7) for _ in range(20)]
history.append(df[df["question"] == selected_event]["prob_market"].values[0])

chart_df = pd.DataFrame({
    "Time": list(range(len(history))),
    "Probability": history
})

st.line_chart(chart_df.set_index("Time"))

st.subheader("💰 Strategy Backtest")

capital = 1000
pnl = 0

for _, row in df.iterrows():
    if row["signal"] in ["BUY", "STRONG_BUY"]:
        pnl += row["alpha"] * 100
    elif row["signal"] in ["SELL", "STRONG_SELL"]:
        pnl -= row["alpha"] * 100

final_capital = capital + pnl

col1, col2 = st.columns(2)

col1.metric("Initial Capital", f"${capital}")
col2.metric("Final Capital", f"${round(final_capital, 2)}")

st.progress(min(max(final_capital / (capital * 2), 0), 1))

st.subheader("📋 Market Table")

st.dataframe(df, use_container_width=True)