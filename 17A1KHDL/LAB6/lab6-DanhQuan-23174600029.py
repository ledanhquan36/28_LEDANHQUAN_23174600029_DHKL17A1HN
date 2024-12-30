import tkinter as tk
import xu_ly_product as xl
window = tk.Tk()
window.title("lab6")
window.geometry('400x400')
Label4 = tk.Label(window,text= 'ID')
Label4.grid(row=0,column=0)

Label = tk.Label(window,text= "Name")
Label.grid(row=1,column=0)

Label1 = tk.Label(window,text= "Price")
Label1.grid(row=2,column=0)

Label2 = tk.Label(window,text= "Amount")
Label2.grid(row=3,column=0)

Id = tk.Entry(window,width=20)
Id.grid(row=0,column=1)

Name = tk.Entry(window,width=20)
Name.grid(row=1,column=1)

Price = tk.Entry(window,width=20)
Price.grid(row=2,column=1)

Amount = tk.Entry(window,width=20)
Amount.grid(row=3,column=1)
def them_san_pham():
    user_name = Name.get()
    user_price = Price.get()
    user_amount = Amount.get()
    text1 = xl.them_san_pham(user_name,user_price,user_amount)
    label3.configure(text=text1)

def cap_nhat():
    user_id = Id.get()
    user_price = Price.get()
    user_amount = Amount.get()
    text2 = xl.cap_nhat_thong_tin(user_id,user_price,user_amount)
    label3.configure(text=text2)

def tim_kiem():
    user_name = Name.get()
    text3 = xl.tim_san_pham(user_name)
    label3.configure(text = text3)
def xoa():
    user_id = Id.get()
    text4 = xl.xoa_san_pham(user_id)
    label3.configure(text= text4)
        
button_them = tk.Button(window,text = "Them",command=them_san_pham)
button_them.grid(row=4,column=0)

button_capnhat = tk.Button(window,text = "Cap Nhat",command=cap_nhat)
button_capnhat.grid(row=4,column=1)

button_timkiem = tk.Button(window,text = "Tim Kiem",command=tim_kiem)
button_timkiem.grid(row=4,column=2)

button_xoa = tk.Button(window,text = "Xoa",command=xoa)
button_xoa.grid(row=4,column=4)

label3 = tk.Label(window,text="")
label3.grid(row=5,column=0)
window.mainloop()