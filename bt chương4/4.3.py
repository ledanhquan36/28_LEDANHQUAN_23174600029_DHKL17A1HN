import numpy as np
import pandas as pd
ser1 = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
df = pd.DataFrame({'Letter': ser1, 'Number': ser2})
print("DataFrame từ hai Series:\n", df)