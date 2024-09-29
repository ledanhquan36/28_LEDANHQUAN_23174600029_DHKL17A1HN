import math  

class Triangle:  
    def __init__(self, a, b, c):  
        """Khởi tạo tam giác với ba cạnh a, b và c."""  
        self.a = a  
        self.b = b  
        self.c = c  

        if not self.is_valid():  
            raise ValueError("Ba cạnh không tạo thành một tam giác hợp lệ.")  

    def is_valid(self):  
        """Kiểm tra xem ba cạnh có tạo thành một tam giác hợp lệ hay không."""  
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)  

    def perimeter(self):  
        """Tính chu vi của tam giác."""  
        return self.a + self.b + self.c  

    def area(self):  
        """Tính diện tích của tam giác bằng công thức Heron."""  
        s = self.perimeter() / 2  
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  

    def __str__(self):  
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"  


class RightTriangle(Triangle):  
    def __init__(self, a, b):  
        """Khởi tạo tam giác vuông với hai cạnh góc vuông a và b."""  
        super().__init__(a, b, math.sqrt(a**2 + b**2))  

    def area(self):  
        """Tính diện tích của tam giác vuông."""  
        return (self.a * self.b) / 2  

    def __str__(self):  
        return f"RightTriangle(a={self.a}, b={self.b})"  


class IsoscelesTriangle(Triangle):  
    def __init__(self, base, height):  
        """Khởi tạo tam giác cân với đáy và chiều cao."""  
        self.base = base  
        self.height = height  
        self.a = self.b = math.sqrt((base/2)**2 + height**2)  # Tính độ dài hai cạnh còn lại  

        super().__init__(self.a, self.b, base)  

    def area(self):  
        """Tính diện tích của tam giác cân."""  
        return (self.base * self.height) / 2  

    def __str__(self):  
        return f"IsoscelesTriangle(base={self.base}, height={self.height})"  


class EquilateralTriangle(IsoscelesTriangle):  
    def __init__(self, side):  
        """Khởi tạo tam giác đều với độ dài cạnh."""  
        super().__init__(side, (math.sqrt(3)/2) * side)  # Tính chiều cao của tam giác đều  

    def __str__(self):  
        return f"EquilateralTriangle(side={self.base})"  


# Chương trình chính để nhập vào các thuộc tính và tính diện tích và chu vi  
if __name__ == "__main__":  
    print("Nhập các thông tin cho tam giác:")  
    a = float(input("Nhập cạnh a: "))  
    b = float(input("Nhập cạnh b: "))  
    c = float(input("Nhập cạnh c: "))  

    triangle = Triangle(a, b, c)  
    print(f"Thông tin tam giác: {triangle}")  
    print(f"Chu vi của tam giác: {triangle.perimeter()}")  
    print(f"Diện tích của tam giác: {triangle.area()}")  

    # Nhập thông tin cho tam giác vuông  
    print("\nNhập thông tin cho tam giác vuông:")  
    a = float(input("Nhập cạnh a: "))  
    b = float(input("Nhập cạnh b: "))  
    right_triangle = RightTriangle(a, b)  
    print(f"Thông tin tam giác vuông: {right_triangle}")  
    print(f"Chu vi của tam giác vuông: {right_triangle.perimeter()}")  
    print(f"Diện tích của tam giác vuông: {right_triangle.area()}")  

    # Nhập thông tin cho tam giác cân  
    print("\nNhập thông tin cho tam giác cân:")  
    base = float(input("Nhập đáy: "))  
    height = float(input("Nhập chiều cao: "))  
    isosceles_triangle = IsoscelesTriangle(base, height)  
    print(f"Thông tin tam giác cân: {isosceles_triangle}")  
    print(f"Chu vi của tam giác cân: {isosceles_triangle.perimeter()}")  
    print(f"Diện tích của tam giác cân: {isosceles_triangle.area()}")  

    # Tạo tam giác đều từ cạnh  
    print("\nNhập độ dài cạnh cho tam giác đều:")  
    side = float(input("Nhập cạnh: "))  
    equilateral_triangle = EquilateralTriangle(side)  
    print(f"Thông tin tam giác đều: {equilateral_triangle}")  
    print(f"Chu vi của tam giác đều: {equilateral_triangle.perimeter()}")  
    print(f"Diện tích của tam giác đều: {equilateral_triangle.area()}")