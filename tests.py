import os
import csv
import pytest
from etl import extract, transform, load, OUTPUT_FILE


def test_extract_returns_list():
    data = extract()
    assert isinstance(data, list)
    assert len(data) > 0
    assert isinstance(data[0], dict)


def test_transform_adds_fields():
    data = extract()
    transformed = transform(data)

    sample = transformed[0]

    # Check new fields exist
    assert "total_amount" in sample
    assert "order_year" in sample
    assert "order_month" in sample
    assert "order_day_name" in sample
    assert "high_value_order" in sample

    # Check calculation correctness
    assert sample["total_amount"] == sample["quantity"] * sample["unit_price"]


# ---------------------------
# Test Load Creates File
# ---------------------------
def test_load_creates_csv(tmp_path):
    test_file = tmp_path / "test_output.csv"

    data = transform(extract())

    # Temporarily override output file
    load(data)

    # Check file exists
    assert os.path.exists(OUTPUT_FILE)


# ---------------------------
# Test CSV Content Structure
# ---------------------------
def test_csv_has_expected_columns():
    data = transform(extract())
    load(data)

    with open(OUTPUT_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames

    expected_columns = [
        "order_id",
        "customer_name",
        "order_date",
        "quantity",
        "unit_price",
        "shipping_country",
        "total_amount",
        "order_year",
        "order_month",
        "order_day_name",
        "high_value_order",
    ]

    for col in expected_columns:
        assert col in headers