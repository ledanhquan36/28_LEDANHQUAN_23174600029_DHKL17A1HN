import numpy as np
import pandas as pd
mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
series_from_list = pd.Series(mylist)
print("Chuỗi từ danh sách:\n",series_from_list)
series_from_array = pd.Series(myarr)
print("\nChuỗi từ mảng NumPy:\n",series_from_array)
series_from_dict = pd.Series(list(mydict))
print("\nChuỗi từ keys của từ điển:\n",series_from_dict)