SELECT c.customer_id, c.email, c.location, TRIM_SCALE(AVG(oi.price)) AS avg_order_value
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY c.customer_id
ORDER BY avg_order_value DESC
LIMIT 15;