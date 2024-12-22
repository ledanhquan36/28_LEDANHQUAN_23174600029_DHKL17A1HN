import pandas as pd

#  1: Đọc file CSV vào DataFrame stocks2
stocks2 = pd.read_csv(r'D:\17A1KHDL\Lab3\DATA\stocks2.csv')

# Giả sử đã đọc dữ liệu từ file 'stocks1.csv' vào DataFrame stocks1
stocks1 = pd.read_csv(r'D:\17A1KHDL\Lab3\DATA\stocks1.csv')
# Bước 2: Gộp stocks1 và stocks2 thành DataFrame mới stocks
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# Bước 3: Tính giá trung bình (open, high, low, close) cho mỗi ngày
stocks['date'] = pd.to_datetime(stocks['date'])  # Đảm bảo cột 'date' là kiểu datetime
stocks_avg = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()

# Bước 4: Hiển thị 5 dòng đầu tiên của kết quả
print(stocks_avg.head())