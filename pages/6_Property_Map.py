import streamlit as st
import pandas as pd
import sqlite3

st.title("Property Map")

st.warning(
    "Waiting for GIS parcel geometry dataset. "
    "Map functionality coming soon."
)

conn = sqlite3.connect("data/sqlite/cama.db")

query = """
SELECT
    Town_Name,
    COUNT(*) as Parcels,
    ROUND(SUM(Assessed_Total),0) as Total_Value
FROM parcels
GROUP BY Town_Name
ORDER BY Total_Value DESC
LIMIT 50
"""

df = pd.read_sql(query, conn)

conn.close()

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)