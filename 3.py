
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

#np.fft.fft(np.exp(2j * np.pi * np.arange(8) / 8))


y = np.load(r'abnormal.npy')
N = y.size
Fs = 150.0
T = N/Fs
x = np.linspace(0.0, N*T, N)

k = np.arange(N)
T = N/Fs
frq = k/T
frq = frq[range(N/2)]

yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()

ax.plot(xf, 2.0/N * np.abs(yf[:N/2]))
ax.set_xlabel('Day')
ax.set_ylabel('Power')

plt.show()
