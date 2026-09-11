import duckdb
import os

os.makedirs("data/duckdb", exist_ok=True)

con = duckdb.connect(
    "data/duckdb/cama.duckdb"
)

con.execute("""
CREATE OR REPLACE TABLE parcels AS
SELECT *
FROM read_csv_auto(
    'data/raw/Connecticut_CAMA_and_Parcel_Layer.csv',
    all_varchar=true
)
""")

count = con.execute("""
SELECT COUNT(*)
FROM parcels
""").fetchone()[0]

print(f"Rows loaded: {count:,}")

con.close()