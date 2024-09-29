class Stack:  
    def __init__(self, max_size=10):  
        """Khởi tạo ngăn xếp với kích thước tối đa."""  
        self.max_size = max_size  
        self.stack = []  # Dữ liệu ngăn xếp  

    def push(self, value):  
        """Thêm phần tử vào ngăn xếp."""  
        if self.is_full():  
            raise OverflowError("Ngăn xếp đã đầy. Không thể thêm phần tử.")  
        self.stack.append(value)  # Thêm phần tử vào cuối danh sách  

    def pop(self):  
        """Lấy phần tử ra từ đỉnh ngăn xếp."""  
        if self.is_empty():  
            raise IndexError("Ngăn xếp rỗng. Không thể lấy phần tử.")  
        return self.stack.pop()  # Lấy phần tử cuối của danh sách  

    def is_empty(self):  
        """Kiểm tra ngăn xếp có trống hay không."""  
        return len(self.stack) == 0  

    def is_full(self):  
        """Kiểm tra ngăn xếp có đầy hay không."""  
        return len(self.stack) >= self.max_size  

    def size(self):  
        """Lấy kích thước hiện tại của ngăn xếp."""  
        return len(self.stack)  

    def display(self):  
        """In ra nội dung ngăn xếp."""  
        print("Nội dung ngăn xếp:", self.stack)  


# Chương trình chính để sử dụng lớp Stack  
if __name__ == "__main__":  
    stack = Stack(5)   

    
    try:  
        stack.push(1.1)  
        stack.push(2.2)  
        stack.push(3.3)  
        stack.push(4.4)  
        stack.push(5.5)  
        stack.display()    

        # Lấy các phần tử ra từ ngăn xếp  
        print(f"Lấy ra phần tử: {stack.pop()}")  
        stack.display()   

        print(f"Lấy ra phần tử: {stack.pop()}")  
        stack.display()  

    except (OverflowError, IndexError) as e:  
        print(e)