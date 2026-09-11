import duckdb

con = duckdb.connect()

count = con.execute("""
SELECT COUNT(*)
FROM 'data/parquet/parcels.parquet'
""").fetchone()[0]

print(count)

glastonbury = con.execute("""
SELECT
    Full_Address,
    Owner,
    Assessed_Total
FROM 'data/parquet/parcels.parquet'
WHERE Town_Name = 'Glastonbury'
LIMIT 10
""").df()

print(glastonbury)