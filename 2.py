import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start_date = '2003-05-01'
y = np.load(r'c:\python27\abnormal.npy')
x = pd.date_range(start=start_date, periods=len(y), freq='D')


plt.plot(x,y,'.')
plt.show()