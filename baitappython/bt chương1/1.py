class HinhChuNhat:  
    def __init__(self):  
        self.do_dai = 0  
        self.rong = 0  

    def nhap_du_lieu(self):  
        self.do_dai = float(input("Nhập độ dài cạnh (b) của hình chữ nhật: "))  
        self.rong = float(input("Nhập độ dài cạnh (h) của hình chữ nhật: "))  

    def tinh_chu_vi(self):  
        return 2 * (self.do_dai + self.rong)  

    def tinh_dien_tich(self):  
        return self.do_dai * self.rong  

    def in_thong_tin(self):  
        chu_vi = self.tinh_chu_vi()  
        dien_tich = self.tinh_dien_tich()  
        print(f"Cạnh dài: {self.do_dai}")  
        print(f"Cạnh ngắn: {self.rong}")  
        print(f"Chu vi: {chu_vi}")  
        print(f"Diện tích: {dien_tich}")  

# Chương trình chính  
if __name__ == "__main__":  
    hcn = HinhChuNhat()  
    hcn.nhap_du_lieu()  
    hcn.in_thong_tin()