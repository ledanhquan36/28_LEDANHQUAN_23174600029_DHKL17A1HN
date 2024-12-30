import xu_ly as xl

def main_menu():  
    connection = create_connection('product.db')  
    create_table(connection)  

    while True:  
        print("\n--- Quản Lý Sản Phẩm ---")  
        print("1. Hiển Thị Danh Sách Sản Phẩm")  
        print("2. Thêm Sản Phẩm Mới")  
        print("3. Tìm Kiếm Sản Phẩm Theo Tên")  
        print("4. Cập Nhật Thông Tin Sản Phẩm")  
        print("5. Xóa Sản Phẩm")  
        print("6. Thoát")  
        
        choice = input("Chọn một chức năng (1-6): ")  
        
        if choice == '1':  
            display_products(connection)  
        elif choice == '2':  
            name = input("Nhập tên sản phẩm: ")  
            price = float(input("Nhập giá sản phẩm: "))  
            amount = int(input("Nhập số lượng sản phẩm: "))  
            add_product(connection, name, price, amount)  
        elif choice == '3':  
            name = input("Nhập tên sản phẩm cần tìm: ")  
            search_product(connection, name)  
        elif choice == '4':  
            product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))  
            new_price = float(input("Nhập giá mới: "))  
            new_amount = int(input("Nhập số lượng mới: "))  
            update_product(connection, product_id, new_price, new_amount)  
        elif choice == '5':  
            product_id = int(input("Nhập ID sản phẩm cần xóa: "))  
            delete_product(connection, product_id)  
        elif choice == '6':  
            print("Thoát khỏi chương trình.")  
            break  
        else:  
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")  

    connection.close()  

# Chạy chương trình  
if __name__ == "__main__":  
    main_menu()



