import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("sample.xml")
    staff_list = doc.getElementsByTagName("staff")
    
    print(f"Tìm thấy {staff_list.length} nhân viên:")
    for staff in staff_list:
        name = staff.getElementsByTagName("name")[0].firstChild.nodeValue
        print(name)

if __name__ == "__main__":
    main()
