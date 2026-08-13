import streamlit as st
import sqlite3

conn = sqlite3.connect("call_analytics.db")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM calls")
total = cursor.fetchone()[0]

cursor.execute(
    "SELECT COUNT(*) FROM calls WHERE outcome='success'"
)
success = cursor.fetchone()[0]

cursor.execute(
    "SELECT COUNT(*) FROM calls WHERE outcome='failed'"
)
failed = cursor.fetchone()[0]

st.title("📊 Shiksha Saathi Dashboard")

st.metric("Total Calls", total)

st.metric("Successful Calls", success)

st.metric("Failed Calls", failed)