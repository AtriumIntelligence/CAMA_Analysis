import streamlit as st
from data_engine import query

st.title("Town Explorer")

towns = query("""
SELECT DISTINCT Town_Name
FROM 'data/parquet/demo.parquet'
ORDER BY Town_Name
""")

selected_town = st.selectbox(
    "Select Town",
    towns["Town_Name"]
)

sql = f"""
SELECT
    Full_Address,
    Owner,
    Assessed_Total,
    Land_Acres,
    Sale_Price,
    Sale_Date
FROM 'data/parquet/demo.parquet'
WHERE Town_Name = '{selected_town}'
LIMIT 1000
"""

df = query(sql)

count = query(f"""
SELECT COUNT(*) AS total
FROM 'data/parquet/demo.parquet'
WHERE Town_Name = '{selected_town}'
""")

st.metric(
    "Parcels",
    int(count.iloc[0]["total"])
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)