import duckdb
import os

os.makedirs("data/parquet", exist_ok=True)

con = duckdb.connect()

con.execute("""
COPY (

SELECT *
FROM 'data/parquet/parcels.parquet'

WHERE Town_Name IN (
    'Glastonbury',
    'Manchester',
    'Hebron',
    'Marlborough',
    'Colchester'
)

)

TO 'data/parquet/demo.parquet'
(FORMAT PARQUET);
""")

con.close()