class Polygon:  
    def __init__(self, sides):  
        """Khởi tạo đối tượng Polygon với số cạnh."""  
        self.sides = sides  

    def perimeter(self):  
        """Tính chu vi. Chưa được định nghĩa trong lớp Polygon."""  
        raise NotImplementedError("Phương thức này cần được định nghĩa trong lớp con.")  

    def area(self):  
        """Tính diện tích. Chưa được định nghĩa trong lớp Polygon."""  
        raise NotImplementedError("Phương thức này cần được định nghĩa trong lớp con.")  


class Parallelogram(Polygon):  
    def __init__(self, base, height):  
        """Khởi tạo đối tượng Parallelogram với đáy và chiều cao."""  
        super().__init__(4)  # Hình bình hành có 4 cạnh  
        self.base = base  
        self.height = height  

    def perimeter(self):  
        """Tính chu vi của hình bình hành với đáy và chiều cao (các cạnh khác được nhập từ người dùng)."""  
        side = float(input("Nhập chiều dài cạnh bên của hình bình hành: "))  
        return 2 * (self.base + side)  

    def area(self):  
        """Tính diện tích của hình bình hành."""  
        return self.base * self.height  


class Rectangle(Parallelogram):  
    def __init__(self, width, height):  
        """Khởi tạo đối tượng Rectangle với chiều rộng và chiều cao."""  
        super().__init__(width, height)  # Hình chữ nhật là một hình bình hành  
        self.width = width  

    def perimeter(self):  
        """Tính chu vi của hình chữ nhật."""  
        return 2 * (self.width + self.height)  

    def area(self):  
        """Tính diện tích của hình chữ nhật."""  
        return self.width * self.height  


class Square(Rectangle):  
    def __init__(self, side):  
        """Khởi tạo đối tượng Square với cạnh."""  
        super().__init__(side, side)  # Hình vuông có chiều cao và chiều rộng bằng nhau  
        self.side = side  

    def perimeter(self):  
        """Tính chu vi của hình vuông."""  
        return 4 * self.side  

    def area(self):  
        """Tính diện tích của hình vuông."""  
        return self.side ** 2  


# Chương trình chính để nhập vào các thuộc tính và tính chu vi, diện tích  
if __name__ == "__main__":  
    print("Chọn hình để tính chu vi và diện tích:")  
    print("1. Hình bình hành")  
    print("2. Hình chữ nhật")  
    print("3. Hình vuông")  

    choice = int(input("Nhập số tương ứng với hình bạn muốn chọn (1/2/3): "))  

    if choice == 1:  
        base = float(input("Nhập độ dài đáy của hình bình hành: "))  
        height = float(input("Nhập độ cao của hình bình hành: "))  
        parallelogram = Parallelogram(base, height)  
        print(f"Chu vi của hình bình hành: {parallelogram.perimeter()}")  
        print(f"Diện tích của hình bình hành: {parallelogram.area()}")  

    elif choice == 2:  
        width = float(input("Nhập chiều rộng của hình chữ nhật: "))  
        height = float(input("Nhập chiều cao của hình chữ nhật: "))  
        rectangle = Rectangle(width, height)  
        print(f"Chu vi của hình chữ nhật: {rectangle.perimeter()}")  
        print(f"Diện tích của hình chữ nhật: {rectangle.area()}")  

    elif choice == 3:  
        side = float(input("Nhập độ dài cạnh của hình vuông: "))  
        square = Square(side)  
        print(f"Chu vi của hình vuông: {square.perimeter()}")  
        print(f"Diện tích của hình vuông: {square.area()}")  

    else:  
        print("Lựa chọn không hợp lệ.")