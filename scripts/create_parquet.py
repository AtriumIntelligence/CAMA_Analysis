import duckdb
import os

os.makedirs("data/parquet", exist_ok=True)

con = duckdb.connect()

con.execute("""
COPY (
    SELECT *
    FROM read_csv_auto(
        'data/raw/Connecticut_CAMA_and_Parcel_Layer.csv',
        all_varchar=true
    )
)
TO 'data/parquet/parcels.parquet'
(FORMAT PARQUET);
""")

print("Parquet created.")