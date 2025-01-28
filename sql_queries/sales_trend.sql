SELECT EXTRACT (MONTH FROM o.order_date) AS month, SUM(o.total_amount) AS monthly_sales
FROM orders o
WHERE o.order_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY month
ORDER BY month;