import os
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
query_all_customers = 'select_all_customers'
query_all_orders = 'select_all_orders'
query_all_products = 'select_all_products'
query_all_order_items = 'select_all_order_items'
query_top_prods_by_sale = 'top_products_by_sale'
query_customer_lifetime_value = 'customer_lifetime_value'
query_quantity_sold_item = 'quantity_sold_per_item'
query_sales_trend_analysis = 'sales_trend'
query_sold_per_category = 'sales_by_category'
query_avg_order_per_customer = 'average_order_value'

os.system(f'sudo -u {db_user} psql -d {db_name} < {query_avg_order_per_customer}.sql')   