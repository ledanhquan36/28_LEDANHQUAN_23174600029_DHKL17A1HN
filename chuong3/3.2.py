import numpy as np
# Câu 1: Tạo numpy array arr có giá trị từ 0-9, hiển thị các phần tử, kiểu dữ liệu và kích thước
arr = np.arange(10)
print("Array arr:", arr)
print("Kiểu dữ liệu:", arr.dtype)
print("Kích thước:", arr.size)
# Câu 2: Tạo arr_odd (các phần tử lẻ) và arr_even (các phần tử chẵn)
arr_odd = arr[arr % 2 != 0]
arr_even = arr[arr % 2 == 0]
print("Array arr_odd:", arr_odd)
print("Array arr_even:", arr_even)
# Câu 3: Tạo arr_update_1, các phần tử lẻ thay bằng 100
arr_update_1 = np.where(arr % 2 != 0, 100, arr)
print("Array arr_update_1:", arr_update_1)