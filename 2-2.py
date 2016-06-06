import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

start_date = '2002-01-01'

x = np.load(r'abnormal.npy')
cx = np.cumsum(x)


plt.plot(x,cx, 0.2)
plt.show()
