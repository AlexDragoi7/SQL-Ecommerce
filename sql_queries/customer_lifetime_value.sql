SELECT c.customer_id, c.email, SUM(o.total_amount) AS lifetime_value
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_date < '2024-12-31'
GROUP BY c.customer_id, c.email
ORDER BY lifetime_value DESC;