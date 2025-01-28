SELECT p.category, SUM(oi.price * oi.quantity) as total_sold_per_category
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY p.category
ORDER BY total_sold_per_category DESC;