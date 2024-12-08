import numpy as np
import pandas as pd
mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser=pd.Series(mydict)
df=ser.reset_index()
df.columns=['Letter',"Number"]
print("Dataframe từ Series:\n:",df)