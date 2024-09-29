class PhanSo:  
    def __init__(self, tu_so=0, mau_so=1):  
        self.tu_so = tu_so  
        self.mau_so = mau_so  
        if not self.kiem_tra_hop_le():  
            raise ValueError("Mẫu số phải khác 0.")  

    def kiem_tra_hop_le(self):  
        """Kiểm tra tính hợp lệ của phân số."""  
        return self.mau_so != 0  

    def nhap_phan_so(self):  
        """Nhập phân số từ bàn phím."""  
        self.tu_so = int(input("Nhập tử số: "))  
        self.mau_so = int(input("Nhập mẫu số: "))  
        if not self.kiem_tra_hop_le():  
            raise ValueError("Mẫu số phải khác 0.")  

    def in_phan_so(self):  
        """In phân số ra màn hình."""  
        print(f"Phân số: {self.tu_so}/{self.mau_so}")  


# Chương trình chính để sử dụng lớp PhanSo  
if __name__ == "__main__":  
    try:  
        ps = PhanSo()  
        ps.nhap_phan_so()  
        ps.in_phan_so()  
    except ValueError as e:  
        print(e)