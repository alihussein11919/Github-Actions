import pandas as pd
import sqlite3

def extract():
    """Extract data from source (CSV in this example)."""
    print("Extracting data...")
    df = pd.read_csv("input_data.csv")
    return df

def transform(df):
    """Transform data (cleaning, filtering, aggregating)."""
    print("Transforming data...")
    # Example: drop missing values and convert column types
    df = df.dropna()
    df['amount'] = df['amount'].astype(float)
    # Example: add a calculated column
    df['amount_usd'] = df['amount'] * 1.1
    return df

def load(df):
    """Load data into target (SQLite DB in this example)."""
    print("Loading data...")
    conn = sqlite3.connect("etl_output.db")
    df.to_sql("etl_table", conn, if_exists="replace", index=False)
    conn.close()
    print("Data loaded successfully.")

def main():
    data = extract()
    transformed = transform(data)
    load(transformed)

if __name__ == "__main__":
    main()
