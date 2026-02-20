import pandas as pd
import sqlite3

# Static input file name
INPUT_FILE = "etl_input.csv"
OUTPUT_DB = "etl_output.db"
OUTPUT_TABLE = "etl_table"

def extract():
    """Extract data from a static CSV file."""
    print(f"Extracting data from {INPUT_FILE}...")
    df = pd.read_csv(INPUT_FILE)
    return df

def transform(df):
    """Transform data (cleaning, filtering, aggregating)."""
    print("Transforming data...")
    # Example: drop missing values
    df = df.dropna()
    # Example: convert column type
    if 'amount' in df.columns:
        df['amount'] = df['amount'].astype(float)
        # Add a calculated column
        df['amount_usd'] = df['amount'] * 1.1
    return df

def load(df):
    """Load data into a static SQLite database and table."""
    print(f"Loading data into {OUTPUT_DB}...")
    conn = sqlite3.connect(OUTPUT_DB)
    df.to_sql(OUTPUT_TABLE, conn, if_exists="replace", index=False)
    conn.close()
    print("Data loaded successfully.")

def main():
    data = extract()
    transformed = transform(data)
    load(transformed)

if __name__ == "__main__":
    main()
