import streamlit as st
from data_engine import query

st.title("Top Investor Groups")

sql = """
SELECT
    Owner,
    COUNT(*) AS Property_Count,
    SUM(
        TRY_CAST(
            Assessed_Total AS DOUBLE
        )
    ) AS Portfolio_Value
FROM 'data/parquet/demo.parquet'
WHERE Owner IS NOT NULL
GROUP BY Owner
HAVING COUNT(*) > 1
ORDER BY Property_Count DESC
LIMIT 500
"""

df = query(sql)

investor_keywords = [
    "LLC",
    "REALTY",
    "PROPERTIES",
    "PROPERTY",
    "TRUST",
    "HOLDINGS",
    "ENTERPRISES",
    "INVESTMENTS",
    "ASSOCIATES",
    "GROUP",
    "MANAGEMENT"
]

mask = (
    df["Owner"]
    .fillna("")
    .str.upper()
    .str.contains(
        "|".join(investor_keywords)
    )
)

df = df[mask]

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)