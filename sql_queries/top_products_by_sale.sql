SELECT p.product_name, SUM(oi.quantity * oi.price) as total_sales_in_USD
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_date BETWEEN '1/01/2024' AND '12/31/2024'
GROUP BY p.product_name, o.order_date
ORDER BY total_sales_in_USD DESC
LIMIT 10;