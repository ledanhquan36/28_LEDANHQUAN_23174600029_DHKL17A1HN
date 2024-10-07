import json  

# Đối tượng Python mẫu  
python_object = {  
    "ten": "Nguyễn Văn A",  
    "tuoi": 23,   
    "dia chi": {  
        "street": "123 Đường ABC",  
        "city": "Hà Nội"  
    }  
}  

# Chuyển đổi đối tượng Python thành chuỗi JSON  
json_data = json.dumps(python_object, ensure_ascii=False, indent=4)  

# In ra chuỗi JSON  
print(json_data)