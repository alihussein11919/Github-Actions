import pandas as pd

# Static input data (list of strings)
INPUT_DATA = [
    "hello world",
    "python etl",
    "github actions",
    "data pipeline"
]

OUTPUT_FILE = "etl_output.csv"

def extract():
    """Extract static strings into a DataFrame."""
    print("Extracting data...")
    df = pd.DataFrame(INPUT_DATA, columns=["raw_text"])
    return df

def transform(df):
    """Transform strings (example: uppercase and add length)."""
    print("Transforming data...")
    df["upper_text"] = df["raw_text"].str.upper()
    df["text_length"] = df["raw_text"].str.len()
    return df

def load(df):
    """Load transformed data into a CSV file."""
    print(f"Loading data into {OUTPUT_FILE}...")
    df.to_csv(OUTPUT_FILE, index=False)
    print("Data loaded successfully.")

def main():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()
