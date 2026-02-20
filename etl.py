import csv
from datetime import datetime

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
    print("Extracting data from dictionary...")
    return DUMMY_DATA



def transform(data):
    print("Transforming data...")

    for row in data:
        # Calculate total
        row["total_amount"] = row["quantity"] * row["unit_price"]

        # Convert date
        parsed_date = datetime.strptime(row["order_date"], "%Y-%m-%d")
        row["order_year"] = parsed_date.year
        row["order_month"] = parsed_date.month
        row["order_day_name"] = parsed_date.strftime("%A")

        # Business logic flag
        row["high_value_order"] = row["total_amount"] > 500

    return data


def load(data):
    print(f"Loading data into {OUTPUT_FILE}...")

    fieldnames = data[0].keys()

    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created successfully.")



def main():
    data = extract()
    transformed = transform(data)
    load(transformed)


if __name__ == "__main__":
    main()