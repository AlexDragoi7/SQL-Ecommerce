from db_connection import connection
from db_connection import cursor

def create_customers(table):
    new_table = f'''CREATE TABLE IF NOT EXISTS {table} (customer_id serial primary key, email VARCHAR(50) NOT NULL,
                    registration_date DATE, location VARCHAR(100) NOT NULL)'''
    cursor.execute(new_table)
    connection.commit()
    print(f"Table {table} was created")

def create_orders(table):
    new_table = f'''CREATE TABLE IF NOT EXISTS {table} (order_id serial primary key, customer_id INT,
                    order_date DATE, total_amount DECIMAL, order_status VARCHAR(30) NOT NULL,
                    CONSTRAINT fk_customer 
                        FOREIGN KEY(customer_id) 
                            REFERENCES Customers(customer_id))'''
    cursor.execute(new_table)
    connection.commit()
    print(f"Table {table} was created")

def create_products(table):
    new_table = f'''CREATE TABLE IF NOT EXISTS {table} (product_id serial primary key, product_name VARCHAR(200) NOT NULL,
                    category VARCHAR(50) NOT NULL, price DECIMAL, stock_level VARCHAR(50) NOT NULL)'''
    cursor.execute(new_table)
    connection.commit()
    print(f"Table {table} was created")

def create_order_items(table):
    new_table = f'''CREATE TABLE IF NOT EXISTS {table} (order_item_id serial primary key, order_id INT, product_id INT, quantity INT, price DECIMAL,
                    CONSTRAINT fk_order_id
                        FOREIGN KEY(order_id)
                            REFERENCES Orders(order_id),
                    CONSTRAINT fk_product_id
                        FOREIGN KEY(product_id)
                            REFERENCES Products(product_id))'''
    cursor.execute(new_table)
    connection.commit()
    print(f"Table {table} was created")