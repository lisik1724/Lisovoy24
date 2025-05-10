import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'C:\Users\1\Lisovoy24\become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")
    
    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record 
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '(name)', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()
    
    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
    
    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    


    def __init__(self):
        self.connection = sqlite3.connect("your_database.db")  # або шлях до вашої бази
        self.cursor = self.connection.cursor()

    def test_connection(self):
        self.cursor.execute("SELECT sqlite_version();")
        print("SQLite version:", self.cursor.fetchone()[0])

    def get_all_users(self):
        self.cursor.execute("SELECT name, address, city FROM customers")
        return self.cursor.fetchall()

    def get_user_address_by_name(self, name):
        self.cursor.execute("""
            SELECT address, city, postalCode, country FROM customers WHERE name = ?
        """, (name,))
        return self.cursor.fetchone()

    def update_product_qnt_by_id(self, product_id, qnt):
        self.cursor.execute("""
            UPDATE products SET quantity = ? WHERE id = ?
        """, (qnt, product_id))
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        self.cursor.execute("""
            SELECT quantity FROM products WHERE id = ?
        """, (product_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def insert_product(self, product_id, name, description, qnt):
        self.cursor.execute("""
            INSERT OR REPLACE INTO products (id, name, description, quantity)
            VALUES (?, ?, ?, ?)
        """, (product_id, name, description, qnt))
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.connection.commit()

    def get_detailed_orders(self):
        self.cursor.execute("""
            SELECT orders.id, customers.name, products.name, products.description, orders.order_date
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            JOIN products ON orders.product_id = products.id
        """)
        return self.cursor.fetchall()

      
             
             
            
        
