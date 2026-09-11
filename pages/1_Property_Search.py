import streamlit as st
from data_engine import query

st.title("Property Search")

search = st.text_input(
    "Search Address",
    placeholder="Example: MAIN ST"
)

town_filter = st.text_input(
    "Optional Town Filter",
    placeholder="Example: Glastonbury"
)

if search:

    if town_filter:

        sql = f"""
        SELECT
            Full_Address,
            Owner,
            Assessed_Total,
            Sale_Price,
            Sale_Date,
            Land_Acres
        FROM 'data/parquet/parcels.parquet'
        WHERE Full_Address ILIKE '%{search}%'
        AND Town_Name ILIKE '%{town_filter}%'
        LIMIT 250
        """

    else:

        sql = f"""
        SELECT
            Full_Address,
            Owner,
            Assessed_Total,
            Sale_Price,
            Sale_Date,
            Land_Acres
        FROM 'data/parquet/parcels.parquet'
        WHERE Full_Address ILIKE '%{search}%'
        LIMIT 250
        """

    df = query(sql)

    st.success(f"Found {len(df):,} results")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )