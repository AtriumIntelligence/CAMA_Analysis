import os
import sqlite3
import pandas as pd

CSV_PATH = "data/raw/Connecticut_CAMA_and_Parcel_Layer.csv"
DB_PATH = "data/sqlite/cama.db"

print("Checking files...")

if not os.path.exists(CSV_PATH):
    print(f"CSV not found: {CSV_PATH}")
    quit()

os.makedirs("data/sqlite", exist_ok=True)

print("Loading CSV...")

# Read a sample first so we know it works
df = pd.read_csv(
    CSV_PATH,
    low_memory=False
)

print(f"Rows loaded: {len(df):,}")
print(f"Columns loaded: {len(df.columns)}")

print("\nFirst 10 columns:")
print(df.columns[:10].tolist())

print("\nCreating SQLite database...")

conn = sqlite3.connect(DB_PATH)

df.to_sql(
    "parcels",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nSUCCESS")
print(f"Database saved to: {DB_PATH}")