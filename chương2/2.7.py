import json  

json_data = '''  
{  
    "name": "Nguyễn Văn A",  
    "age": 30,   
    "courses": ["Toán", "Lý", "Hóa"],  
    "address": {  
        "street": "123 Đường ABC",  
        "city": "Hà Nội"  
    }  
}  
'''  


python_object = json.loads(json_data)  

print(python_object)  
print(type(python_object))  
print("Tên:", python_object["name"])  
print("Tuổi:", python_object["age"])  
print("Có phải là sinh viên không:", python_object["is_student"])  
print("Các khóa học:", python_object["courses"])  
print("Địa chỉ:", python_object["address"]["street"], ",", python_object["address"]["city"])