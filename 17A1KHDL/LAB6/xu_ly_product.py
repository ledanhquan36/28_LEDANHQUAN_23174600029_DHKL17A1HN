import sqlite3
conn = sqlite3.connect(r'D:\17A1KHDL\product.db')
cruso = conn.cursor()
cruso.execute("""CREATE TABLE IF NOT EXISTS product(
              id INTEGER PRIMARY KEY,
              'Name' Text Not null,
              'Price' Real Not null,
              'Amount' Interger Not Null)""")


def hien_thi_danh_sach():
    rows = cruso.execute("SELECT * FROM product")
    for row in rows:
        print(row)

def them_san_pham(name=None,price=None,amount=None):
    cruso.execute("INSERT INTO product('Name','Price','Amount') VALUES(?,?,?)",(name,price,amount))
    conn.commit()
    return f'Da them San pham'

def tim_san_pham(name):
    try:
        rows = cruso.execute("SELECT * FROM product WHERE Name = ?", (name,))
        result = []
        for row in rows:
            result.append(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Amount: {row[3]}")
        
        if not result:
            return f"Không tìm thấy sản phẩm có tên '{name}'."
        return "\n".join(result)
    except sqlite3.Error as e:
        return f"Lỗi cơ sở dữ liệu: {e}"

def xoa_san_pham(id):
    cruso.execute("DELETE FROM product WHERE id = ?",(id,))
    conn.commit()
    return f'Da xoa san pham'