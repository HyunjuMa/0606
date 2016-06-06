import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

start_date = '2002-01-01'

y = np.load(r'abnormal.npy')
x = pd.date_range(start=start_date, periods=y.size, freq='D')

plt.plot(x,y,'.')
plt.show()
