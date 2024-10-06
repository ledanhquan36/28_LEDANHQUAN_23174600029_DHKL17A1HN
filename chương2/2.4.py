import xml.dom.minidom
path = 'sample.xml'
doc = xml.dom.minidom.parse(path)
company_name = doc.getElementsByTagName('name')[0].firstChild.nodeValue
print(f'Tên công ty: {company_name}')
print('---')
staff_list = doc.getElementsByTagName('staff')
for staff in staff_list:
    staff_id = staff.getAttribute('id')  
    staff_name = staff.getElementsByTagName('name')[0].firstChild.nodeValue
    salary = staff.getElementsByTagName('salary')[0].firstChild.nodeValue

    print(f'Nhân viên ID: {staff_id}')
    print(f'Tên: {staff_name}')
    print(f'Lương: {salary}')
    print('---')
