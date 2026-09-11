import streamlit as st
from data_engine import query

st.title("Owner Search")

owner = st.text_input(
    "Search Owner",
    placeholder="Example: INVESTORS TRUST LLC"
)

if owner:

    sql = f"""
    SELECT
        Owner,
        Full_Address,
        Assessed_Total,
        Sale_Price,
        Sale_Date,
        Land_Acres
    FROM 'data/parquet/demo.parquet'
    WHERE Owner ILIKE '%{owner}%'
    ORDER BY TRY_CAST(Assessed_Total AS DOUBLE) DESC
    LIMIT 1000
    """

    df = query(sql)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    if len(df):

        try:

            value = (
                df["Assessed_Total"]
                .astype(float)
                .sum()
            )

            acres = (
                df["Land_Acres"]
                .astype(float)
                .sum()
            )

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Properties",
                len(df)
            )

            c2.metric(
                "Portfolio Value",
                f"${value:,.0f}"
            )

            c3.metric(
                "Acres",
                f"{acres:,.1f}"
            )

        except:
            pass