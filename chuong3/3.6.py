import numpy as np
# Bước 1: Tạo array arr có kích thước 3x3 với các giá trị True
arr = np.full((3, 3), True)
print("Array 3x3 với giá trị True:\n", arr)
# Bước 2: Tạo array 1 chiều arr_ID và chuyển đổi thành array 2 chiều 3x3
arr_ID = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_ID.reshape((3, 3))
print("\nArray 2 chiều 3x3 từ arr_ID:\n", arr_2D)
# Chuyển cột 1 sang cột 3 và ngược lại
arr_2D[:, [1, 2]] = arr_2D[:, [2, 1]]
print("\nArray 2D sau khi chuyển đổi cột:\n", arr_2D)
# Bước 3: Chuyển dòng 1 sang dòng 2 và ngược lại
arr_2D[[0, 1]] = arr_2D[[1, 0]]
print("\nArray 2D sau khi chuyển đổi dòng:\n", arr_2D)
# Bước 4: Đảo ngược các dòng của arr_2D
arr_2D_reversed_rows = arr_2D[::-1]
print("\nArray 2D sau khi đảo ngược các dòng:\n", arr_2D_reversed_rows)
# Bước 5: Đảo ngược các cột của arr_2D
arr_2D_reversed_cols = arr_2D_reversed_rows[:, ::-1]
print("\nArray 2D sau khi đảo ngược các cột:\n", arr_2D_reversed_cols)
# Bước 6: Tạo arr_2D_null và kiểm tra giá trị rỗng
arr_2D_null = np.array([[1, 2, 3], [np.nan, 5, 6], [7, np.nan, 9], [4, 5, 6]])
print("\nKiểm tra giá trị rỗng trong arr_2D_null:")
has_nan = np.isnan(arr_2D_null).any()
print("Có giá trị rỗng (NaN) không?:", has_nan)
# Bước 7: Thay thế giá trị null bằng 0
arr_2D_null_filled = np.nan_to_num(arr_2D_null, nan=0)
print("\nArray 2D sau khi thay thế giá trị null bằng 0:\n", arr_2D_null_filled)