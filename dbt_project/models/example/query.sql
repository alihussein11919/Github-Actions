SELECT
    order_id,
    customer_name,
    quantity,
    unit_price,
    quantity * unit_price AS total_amount
FROM raw_orders;
