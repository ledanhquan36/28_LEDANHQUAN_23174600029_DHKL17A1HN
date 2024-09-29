class ThiSinh:  
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):  
        self.ho_ten = ho_ten  
        self.diem_toan = diem_toan  
        self.diem_ly = diem_ly  
        self.diem_hoa = diem_hoa  

    def tinh_tong_diem(self):  
        return self.diem_toan + self.diem_ly + self.diem_hoa  

    def in_thong_tin(self):  
        print(f"Họ tên: {self.ho_ten}, Điểm Toán: {self.diem_toan}, Điểm Lý: {self.diem_ly}, Điểm Hóa: {self.diem_hoa}, Tổng điểm: {self.tinh_tong_diem()}")  


def nhap_thong_tin_thi_sinh():  
    ho_ten = input("Nhập họ tên thí sinh: ")  
    diem_toan = float(input("Nhập điểm môn Toán: "))  
    diem_ly = float(input("Nhập điểm môn Lý: "))  
    diem_hoa = float(input("Nhập điểm môn Hóa: "))  
    return ThiSinh(ho_ten, diem_toan, diem_ly, diem_hoa)  


def in_danh_sach_trung_tuyen(danh_sach, diem_chuan=20):  
    danh_sach_trung_tuyen = [ts for ts in danh_sach if ts.tinh_tong_diem() >= diem_chuan]  
    danh_sach_trung_tuyen.sort(key=lambda x: x.tinh_tong_diem(), reverse=True)  
    
    print("\nDanh sách thí sinh trúng tuyển:")  
    for ts in danh_sach_trung_tuyen:  
        ts.in_thong_tin()  
        print("-" * 30)  


if __name__ == "__main__":  
    danh_sach_thi_sinh = []  
    so_thi_sinh = int(input("Nhập số lượng thí sinh: "))  
    
    for _ in range(so_thi_sinh):  
        ts = nhap_thong_tin_thi_sinh()  
        danh_sach_thi_sinh.append(ts)  
    
    in_danh_sach_trung_tuyen(danh_sach_thi_sinh)