import csv
from datetime import datetime
from copy import deepcopy
import sqlite3

conn = sqlite3.connect("etl.db")
df.to_sql("raw_orders", conn, if_exists="replace", index=False)
conn.close()

OUTPUT_FILE = "orders_from_dict.csv"

DUMMY_DATA = [
    {
        "order_id": 1001,
        "customer_name": "Ali Hassan",
        "order_date": "2026-01-03",
        "quantity": 2,
        "unit_price": 150.0,
        "shipping_country": "Egypt"
    },
    {
        "order_id": 1002,
        "customer_name": "Sara Ahmed",
        "order_date": "2026-01-05",
        "quantity": 1,
        "unit_price": 1200.0,
        "shipping_country": "UAE"
    },
    {
        "order_id": 1003,
        "customer_name": "John Smith",
        "order_date": "2026-01-07",
        "quantity": 5,
        "unit_price": 40.0,
        "shipping_country": "USA"
    },
    {
        "order_id": 1004,
        "customer_name": "Omar Khaled",
        "order_date": "2026-01-10",
        "quantity": 3,
        "unit_price": 500.0,
        "shipping_country": "Egypt"
    }
]


def extract():
    """Return a copy of source data."""
    print("Extracting data...")
    return deepcopy(DUMMY_DATA)


def transform(data):
    """Apply business transformations."""
    print("Transforming data...")

    transformed = []

    for row in data:
        new_row = row.copy()

        # Safe numeric conversion
        quantity = int(new_row["quantity"])
        unit_price = float(new_row["unit_price"])

        total_amount = quantity * unit_price

        parsed_date = datetime.strptime(new_row["order_date"], "%Y-%m-%d")

        new_row.update({
            "total_amount": total_amount,
            "order_year": parsed_date.year,
            "order_month": parsed_date.month,
            "order_day_name": parsed_date.strftime("%A"),
            "high_value_order": total_amount > 500
        })

        transformed.append(new_row)

    return transformed


def load(data, output_file=OUTPUT_FILE):
    """Write data to CSV."""
    print(f"Loading data into {output_file}...")

    fieldnames = data[0].keys()

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created successfully.")
    return output_file


def main():
    data = extract()
    transformed = transform(data)
    load(transformed)


if __name__ == "__main__":
    main()