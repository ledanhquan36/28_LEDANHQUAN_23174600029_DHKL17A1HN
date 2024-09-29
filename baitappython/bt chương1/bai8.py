class Date:  
    def __init__(self, day=1, month=1, year=2023):  
        """Khởi tạo đối tượng Date với ngày, tháng, năm."""  
        self.day = day  
        self.month = month  
        self.year = year  

    def display(self):  
        """In thông tin ngày ra màn hình."""  
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")  

    def next(self):  
        """Tính ngày tiếp theo."""  
        days_in_month = [31, 28 + (1 if self.is_leap_year() else 0), 31, 30, 31, 30,   
                         31, 31, 30, 31, 30, 31]  

        self.day += 1  
        
        if self.day > days_in_month[self.month - 1]:  
            self.day = 1  
            self.month += 1  
            
            if self.month > 12:  
                self.month = 1  
                self.year += 1  

    def is_leap_year(self):  
        """Kiểm tra xem năm có phải năm nhuận không."""  
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)  


class Employee:  
    def __init__(self, name, birth_date, start_date):  
        """Khởi tạo đối tượng Employee với tên, ngày sinh và ngày vào công ty."""  
        self.name = name  
        self.birth_date = birth_date  # Ngày sinh (đối tượng kiểu Date)  
        self.start_date = start_date    # Ngày vào công ty (đối tượng kiểu Date)  

    def display(self):  
        """Hiển thị thông tin nhân viên."""  
        print("Thông tin nhân viên:")  
        print(f"Họ tên: {self.name}")  
        print("Ngày sinh:", end=' ')  
        self.birth_date.display()  
        print("Ngày vào công ty:", end=' ')  
        self.start_date.display()  


# Chương trình chính để quản lý nhân viên  
if __name__ == "__main__":  
    # Tạo một số đối tượng Date cho ngày sinh và ngày vào công ty  
    birth_date_1 = Date(15, 5, 1990)  
    start_date_1 = Date(1, 1, 2023)  

    # Tạo đối tượng Employee  
    employee_1 = Employee("Nguyen Van A", birth_date_1, start_date_1)  

    # Hiển thị thông tin nhân viên  
    employee_1.display()  # Hiển thị thông tin nhân viên  

    # Tạo một số đối tượng Date khác cho nhân viên thứ hai  
    birth_date_2 = Date(25, 12, 1985)  
    start_date_2 = Date(10, 2, 2023)  

    # Tạo đối tượng Employee thứ hai  
    employee_2 = Employee("Tran Thi B", birth_date_2, start_date_2)  

    # Hiển thị thông tin nhân viên thứ hai  
    employee_2.display()  # Hiển thị thông tin nhân viên thứ hai