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

os.system(f'sudo -u {db_user} psql -d {db_name} < {query_all_customers}.sql')   