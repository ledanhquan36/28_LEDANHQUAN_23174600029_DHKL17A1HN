import numpy as np
# 1. Tạo mảng 2D từ tệp baseball.txt
# Giả sử tệp có cấu trúc gồm cột chiều cao (inch) và cân nặng (pounds)
np_baseball = np.loadtxt('Bài 3.7\\baseball_2D.txt', delimiter=',')
# 2 In giá trị của dòng thứ 50 trong np_baseball
print("Dòng thứ 50 trong np_baseball:")
print(np_baseball[49])
# 3. Cho biết chiều cao của các cầu thủ từ dòng 124 trở đi
print("\nChiều cao của các cầu thủ từ dòng 124 trở đi:")
print(np_baseball[123:, 0])  # Giả sử chiều cao nằm ở cột đầu tiên
# 4. Tính chiều cao trung bình của tất cả các cầu thủ
mean_height = np.mean(np_baseball[:, 0])  # Giả sử chiều cao nằm ở cột đầu tiên
print("\nChiều cao trung bình của các cầu thủ:")
print(mean_height)
correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("\nHệ số tương quan giữa chiều cao và cân nặng:")
print(correlation[0, 1])