from app.db.client import execute_query

supplier_table = """
CREATE TABLE IF NOT EXISTS suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL
)
"""

inventory_table = """
CREATE TABLE IF NOT EXISTS inventory (
    id SERIAL PRIMARY KEY,
    supplier_id INT NOT NULL REFERENCES suppliers(id) ON DELETE CASCADE,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
)
"""



def create_tables():
    print
    execute_query(supplier_table)
    print("Supplier table created successfully")
    execute_query(inventory_table)
    print("Inventory table created successfully")



print("Tables created successfully")