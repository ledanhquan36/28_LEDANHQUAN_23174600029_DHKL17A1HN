import math  

class Point:  
    def __init__(self, x=0, y=0):  
        """Khởi tạo một điểm với tọa độ x và y."""  
        self.x = x  
        self.y = y  

    def __str__(self):  
        return f"Point({self.x}, {self.y})"  


class Ellipse(Point):  
    def __init__(self, x, y, semi_major_axis, semi_minor_axis):  
        """Khởi tạo một elip với trung tâm tại (x, y) và bán trục lớn, bán trục nhỏ."""  
        super().__init__(x, y)  
        self.semi_major_axis = semi_major_axis  
        self.semi_minor_axis = semi_minor_axis  

    def area(self):  
        """Tính diện tích của elip."""  
        return math.pi * self.semi_major_axis * self.semi_minor_axis  

    def __str__(self):  
        return f"Ellipse(center=({self.x}, {self.y}), semi_major_axis={self.semi_major_axis}, semi_minor_axis={self.semi_minor_axis})"  


class Circle(Ellipse):  
    def __init__(self, x, y, radius):  
        """Khởi tạo một đường tròn với trung tâm tại (x, y) và bán kính."""  
        super().__init__(x, y, radius, radius)  # Một đường tròn là một elip với bán trục lớn = bán trục nhỏ  
        self.radius = radius  

    def area(self):  
        """Tính diện tích của đường tròn."""  
        return math.pi * self.radius ** 2  

    def __str__(self):  
        return f"Circle(center=({self.x}, {self.y}), radius={self.radius})"  


# Chương trình chính để nhập vào các thuộc tính và tính diện tích  
if __name__ == "__main__":  
    print("Nhập các thông tin cho elip:")  
    x = float(input("Nhập tọa độ x của tâm elip: "))  
    y = float(input("Nhập tọa độ y của tâm elip: "))  
    semi_major_axis = float(input("Nhập bán trục lớn của elip: "))  
    semi_minor_axis = float(input("Nhập bán trục nhỏ của elip: "))  

    ellipse = Ellipse(x, y, semi_major_axis, semi_minor_axis)  
    print(f"Thông tin elip: {ellipse}")  
    print(f"Diện tích của elip: {ellipse.area()}")  

    # Nhập thông tin cho đường tròn  
    print("\nNhập bán kính cho đường tròn:")  
    radius = semi_major_axis  # Có thể dùng bán trục lớn của elip làm bán kính  
    circle = Circle(x, y, radius)  
    print(f"Thông tin đường tròn: {circle}")  
    print(f"Diện tích của đường tròn: {circle.area()}")