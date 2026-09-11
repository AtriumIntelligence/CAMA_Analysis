import streamlit as st
from data_engine import query

st.set_page_config(
    page_title="Atrium Property Intelligence",
    page_icon="🏡",
    layout="wide"
)

# -------------------------------------
# SESSION STATE
# -------------------------------------

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# -------------------------------------
# LOGIN PAGE
# -------------------------------------

if not st.session_state.authenticated:

    st.title("🏡 Atrium Property Intelligence")

    st.markdown("""
    ### Connecticut Property Intelligence Platform

    Login to access:

    - Property Search
    - Owner Intelligence
    - Investor Intelligence
    - Town Analytics
    - Land Holdings
    """)

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if (
            username == st.secrets["USERNAME"]
            and password == st.secrets["PASSWORD"]
        ):

            st.session_state.authenticated = True

            st.rerun()

        else:

            st.error(
                "Invalid username or password"
            )

    st.stop()

# -------------------------------------
# MAIN DASHBOARD
# -------------------------------------

st.title("🏡 Atrium Property Intelligence")

col1, col2, col3, col4 = st.columns(4)

try:

    total_properties = query("""
    SELECT COUNT(*) as total
    FROM 'data/parquet/parcels.parquet'
    """).iloc[0]["total"]

    total_towns = query("""
    SELECT COUNT(DISTINCT Town_Name) as total
    FROM 'data/parquet/parcels.parquet'
    """).iloc[0]["total"]

    total_owners = query("""
    SELECT COUNT(DISTINCT Owner) as total
    FROM 'data/parquet/parcels.parquet'
    """).iloc[0]["total"]

    total_value = query("""
    SELECT
        SUM(
            TRY_CAST(
                Assessed_Total AS DOUBLE
            )
        ) as total
    FROM 'data/parquet/parcels.parquet'
    """).iloc[0]["total"]

    col1.metric(
        "Properties",
        f"{int(total_properties):,}"
    )

    col2.metric(
        "Towns",
        f"{int(total_towns):,}"
    )

    col3.metric(
        "Owners",
        f"{int(total_owners):,}"
    )

    col4.metric(
        "Assessed Value",
        f"${total_value/1_000_000_000:.1f}B"
    )

except Exception as e:

    st.error(str(e))

st.divider()

st.subheader("About Atrium")

st.markdown("""
Atrium Property Intelligence provides:

- Property Search
- Owner Search
- Investor Analysis
- Land Ownership Intelligence
- Municipal Ownership Analytics
- Connecticut Property Insights

Use the navigation menu on the left to access reports.
""")

st.divider()

st.subheader("Top Investor Groups")

top_investors = query("""
SELECT
    Owner,
    COUNT(*) as Property_Count,
    SUM(
        TRY_CAST(
            Assessed_Total AS DOUBLE
        )
    ) AS Portfolio_Value
FROM 'data/parquet/parcels.parquet'
WHERE Owner IS NOT NULL
GROUP BY Owner
HAVING COUNT(*) > 10
ORDER BY Property_Count DESC
LIMIT 10
""")

st.dataframe(
    top_investors,
    hide_index=True,
    use_container_width=True
)

if st.button("Logout"):

    st.session_state.authenticated = False

    st.rerun()
