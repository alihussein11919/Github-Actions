import csv
import sqlite3
from datetime import datetime
from copy import deepcopy

OUTPUT_FILE = "orders_from_dict.csv"
DB_FILE = "etl.db"

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


def load_csv(data, output_file=OUTPUT_FILE):
    """Write data to CSV."""
    print(f"Loading data into {output_file}...")

    fieldnames = data[0].keys()
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created successfully.")
    return output_file


def load_sqlite(data, db_file=DB_FILE):
    """Write data to SQLite database."""
    print(f"Loading data into {db_file}...")

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Drop table if exists
    cursor.execute("DROP TABLE IF EXISTS raw_orders")

    # Create table
    cursor.execute("""
        CREATE TABLE raw_orders (
            order_id INTEGER,
            customer_name TEXT,
            order_date TEXT,
            quantity INTEGER,
            unit_price REAL,
            shipping_country TEXT,
            total_amount REAL,
            order_year INTEGER,
            order_month INTEGER,
            order_day_name TEXT,
            high_value_order BOOLEAN
        )
    """)

    # Insert rows
    for row in data:
        cursor.execute("""
            INSERT INTO raw_orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["order_id"],
            row["customer_name"],
            row["order_date"],
            row["quantity"],
            row["unit_price"],
            row["shipping_country"],
            row["total_amount"],
            row["order_year"],
            row["order_month"],
            row["order_day_name"],
            row["high_value_order"]
        ))

    conn.commit()
    conn.close()
    print("SQLite database created successfully.")
    return db_file


def main():
    data = extract()
    transformed = transform(data)
    load_csv(transformed)
    load_sqlite(transformed)


if __name__ == "__main__":
    main()
