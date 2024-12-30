import sqlite3  

def create_connection(db_file):  
    """Tạo một kết nối đến cơ sở dữ liệu SQLite."""  
    conn = sqlite3.connect(db_file)  
    return conn  

# Tạo kết nối với product.db  
connection = create_connection('product.db')  
if connection:  
    print("Đã kết nối với cơ sở dữ liệu 'product.db'")  
else:  
    print("Không thể kết nối với cơ sở dữ liệu.")

def create_table(conn):  
    """Tạo bảng product trong cơ sở dữ liệu."""  
    cursor = conn.cursor()  
    try:  
        cursor.execute('''  
        CREATE TABLE IF NOT EXISTS product (  
            Id INTEGER PRIMARY KEY AUTOINCREMENT,  
            Name TEXT NOT NULL,  
            Price REAL NOT NULL,  
            Amount INTEGER NOT NULL  
        )  
        ''')  
        conn.commit()  
        print("Đã tạo bảng 'product' trong cơ sở dữ liệu.")  
    except sqlite3.Error as e:  
        print(f"Lỗi xảy ra khi tạo bảng: {e}")

# Tạo bảng  
create_table(connection)  
connection.close()  

def add_product(conn, name, price, amount):  
    """Thêm sản phẩm mới vào bảng product."""  
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))  
    conn.commit()  
    print("Sản phẩm đã được thêm thành công.")  

def display_products(conn):  
    """Hiển thị danh sách tất cả sản phẩm trong bảng product."""  
    cursor = conn.cursor()  
    cursor.execute("SELECT * FROM product")  
    products = cursor.fetchall()  
    
    if products:  
        print("Danh Sách Sản Phẩm:")  
        for product in products:  
            print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")  
    else:  
        print("Không có sản phẩm nào trong cơ sở dữ liệu.")  

def search_product(conn, name):  
    """Tìm kiếm sản phẩm theo tên."""  
    cursor = conn.cursor()  
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", ('%' + name + '%',))  
    products = cursor.fetchall()  
    
    if products:  
        print("Kết quả tìm kiếm:")  
        for product in products:  
            print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")  
    else:  
        print("Không tìm thấy sản phẩm.")  

def update_product(conn, product_id, new_price, new_amount):  
    """Cập nhật thông tin sản phẩm dựa trên ID."""  
    cursor = conn.cursor()  
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (new_price, new_amount, product_id))  
    conn.commit()  
    print("Thông tin sản phẩm đã được cập nhật.")  

def delete_product(conn, product_id):  
    """Xóa sản phẩm khỏi bảng product dựa trên ID."""  
    cursor = conn.cursor()  
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))  
    conn.commit()  
    print("Sản phẩm đã được xóa.")