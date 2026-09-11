import streamlit as st
from data_engine import query

st.title("Largest Parcels")

sql = """
SELECT
    Full_Address,
    Owner,
    Town_Name,
    TRY_CAST(
        Land_Acres AS DOUBLE
    ) AS Acres,
    Assessed_Total
FROM 'data/parquet/parcels.parquet'
WHERE Land_Acres IS NOT NULL
ORDER BY Acres DESC
LIMIT 500
"""

df = query(sql)

st.metric(
    "Largest Parcel",
    f"{df['Acres'].max():,.1f} Acres"
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)