import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

start_date = '2002-01-01'

x = np.load(r'abnormal.npy')

sor_x = np.sort(x)
y= np.arange(sor_x.size)/float(len(sor_x))

plt.plot(sor_x, y)

plt.show()
