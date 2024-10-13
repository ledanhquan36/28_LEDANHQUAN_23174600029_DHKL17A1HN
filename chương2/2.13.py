import requests  

def fetch_data(api_url):  
    try:  
        response = requests.get(api_url)  
        response.raise_for_status()  # Kiểm tra xem có lỗi không  
        return response.json()  # Trả về dữ liệu JSON  
    except requests.exceptions.RequestException as e:  
        print(f"Đã xảy ra lỗi khi lấy dữ liệu: {e}")  
        return None  

def display_data(data):  
    if data is not None:  
        # Tùy thuộc vào cấu trúc dữ liệu, chỉnh sửa phần này cho phù hợp  
        for item in data:  
            print(f"Tên: {item.get('name')}, Mô tả: {item.get('description')}")  
    else:  
        print("Không có dữ liệu để hiển thị.")  

def main():  
    api_url = "https://api.example.com/endpoint"  # Thay thế bằng URL API thực tế  
    data = fetch_data(api_url)  
    display_data(data)  

if __name__ == "__main__":  
    main()