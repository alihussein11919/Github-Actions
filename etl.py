import csv

# Static input data
INPUT_DATA = [
    "hello world",
    "python etl",
    "github actions",
    "data pipeline"
]

OUTPUT_FILE = "etl_output.csv"

def extract():
    """Extract static strings into a list of dicts."""
    print("Extracting data...")
    return [{"raw_text": text} for text in INPUT_DATA]

def transform(data):
    """Transform strings (uppercase and length)."""
    print("Transforming data...")
    for row in data:
        row["upper_text"] = row["raw_text"].upper()
        row["text_length"] = len(row["raw_text"])
    return data

def load(data):
    """Load transformed data into a CSV file."""
    print(f"Loading data into {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["raw_text", "upper_text", "text_length"])
        writer.writeheader()
        writer.writerows(data)
    print("Data loaded successfully.")

def main():
    data = extract()
    transformed = transform(data)
    load(transformed)

if __name__ == "__main__":
    main()
