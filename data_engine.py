import duckdb

PARQUET_FILE = "data/parquet/demo.parquet"

def query(sql):
    con = duckdb.connect()

    result = con.execute(sql).df()

    con.close()

    return result