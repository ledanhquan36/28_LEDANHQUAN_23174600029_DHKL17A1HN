class Date:  
    def __init__(self, day=1, month=1, year=2023):  
        """Khởi tạo đối tượng Date với ngày, tháng, năm."""  
        self.day = day  
        self.month = month  
        self.year = year  

    def display(self):  
        """In thông tin ngày ra màn hình."""  
        print(f"Ngày: {self.day:02d}/{self.month:02d}/{self.year}")  

    def next(self):  
        """Tính ngày tiếp theo."""  
        # Số ngày trong mỗi tháng  
        days_in_month = [31, 28 + (1 if self.is_leap_year() else 0), 31, 30, 31, 30,   
                         31, 31, 30, 31, 30, 31]  

        # Tăng ngày  
        self.day += 1  

        # Kiểm tra nếu đã qua ngày cuối tháng  
        if self.day > days_in_month[self.month - 1]:  
            self.day = 1  
            self.month += 1  

            # Kiểm tra nếu đã qua tháng 12  
            if self.month > 12:  
                self.month = 1  
                self.year += 1  

    def is_leap_year(self):  
        """Kiểm tra xem năm có phải năm nhuận không."""  
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)  


# Chương trình chính để sử dụng lớp Date  
if __name__ == "__main__":  
    # Tạo một đối tượng Date  
    my_date = Date(28, 2, 2023)  

    # Hiển thị ngày hiện tại  
    my_date.display()  

    # Tính và hiển thị ngày tiếp theo  
    my_date.next()  
    my_date.display()  # Ngày sẽ là 01/03/2023  

    # Tính và hiển thị ngày tiếp theo  
    my_date.next()  
    my_date.display()  # Ngày sẽ là 02/03/2023  

    # Tính đến cuối tháng  
    for _ in range(29):  # Chuyển đến ngày 31/03  
        my_date.next()  
    my_date.display()  # Ngày sẽ là 31/03/2023  

    # Tính sang tháng tiếp theo  
    my_date.next()  
    my_date.display()  # Ngày sẽ là 01/04/2023