import json
ten_giao_dich = input("Nhập tên giao dịch: ")
so_tien = input("Nhập số tiền: ")
loai_giao_dich = input("Nhập loại giao dịch (thu/chi): ")

giao_dich = {
    "ten_giao_dich": ten_giao_dich,
    "so_tien": so_tien,
    "loai_giao_dich": loai_giao_dich
}
ghi_vao_tap = input("Bạn có muốn ghi giao dịch vào tệp không? (1: Có, 0: Không): ")
if ghi_vao_tap == "1":
    # Ghi giao dịch vào tệp JSON
    with open("giao_dich.json", "w") as file:
        json.dump(giao_dich, file)
    print("Giao dịch đã được ghi vào tệp.")
else:
    print("Giao dịch không được ghi.")