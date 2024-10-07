import json  
data = {  
    "ten": "Nguyễn Văn A",  
    "tuoi": 30,  
    "tp": "Hà Nội",  
    "nghe nghiep": "Kỹ sư"  
}  
json_data = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)  
print(json_data)