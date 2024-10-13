import json

data = '''
{  
    "company": {  
        "name": "Công Ty ABC",  
        "address": "123 Đường ABC, Quận 1, TP.HN",  
        "employees": [  
            {"name": "Nguyễn Văn A", "unit": "IT"},  
            {"name": "Trần Thị B", "unit": "Marketing"},  
            {"name": "Lê Văn C", "unit": "IT"},  
            {"name": "Phạm Thị D", "unit": "Sales"},  
            {"name": "Nguyễn Thị E", "unit": "Marketing"},  
            {"name": "Trần Văn F", "unit": "Sales"}  
        ]  
    }  
}
'''
data = json.loads(data)
company = data["company"]

unit_stats = {}
for emp in company["employees"]:
    unit_stats[emp["unit"]] = unit_stats.get(emp["unit"], 0) + 1
print(f"Tên công ty: {company['name']}")
print(f"Địa chỉ: {company['address']}")
print(f"Tổng số nhân viên: {len(company['employees'])}")
print("Thống kê nhân viên theo đơn vị:")
for unit, count in unit_stats.items():
    print(f"- {unit}: {count} nhân viên, {count / len(company['employees']) * 100:.2f}%")
