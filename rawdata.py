# -*- coding: utf-8 -*-
import  serial
import numpy as np
import numpy as np
import matplotlib.pyplot as pl
import matplotlib
import math
import random

ser  = serial.Serial('COM4',57600)

while True:
    arr = []
    #f = open('data1.txt', mode='a+')
    for i in range(512):
        a = ser.read(36)
        if a[0] == 170 and a[1] == 170 and a[2] == 4 and a[3] == 128 and a[4] == 2:
             high = a[5]
             low = a[6]
             rawdata1 = (high << 8) | low
             if rawdata1 > 32768:
                    rawdata1 = rawdata1 - 65536
             sum = ((0x80 + 0x02 + high + low) ^ 0xffffffff) & 0xff
             if sum == a[7]:
                 arr.append(rawdata1)
             #f.write(str(rawdata1))
    N = len(arr)
    fs = N  # 采样频率
    df = fs / (N - 1)  # 分辨率
    #f = [df * n for n in range(0, N)]
    Y = np.fft.fft(arr) * 2 / N  # *2/N
    absY = [np.abs(x) for x in Y]
    i = 0
    # while i < len(absY):
    #      if absY[i] > 0.01:
    #         print("freq:M, Y: %5.2f + %5.2f j, A:%3.2f, phi: %6.1f" % (i, Y[i].real, Y[i].imag, absY[i], math.atan2(Y[i].imag, Y[i].real) * 180 / math.pi))
    #         i += 1
    pl.plot(f, absY)
    pl.show()
    #trans =  np.fft.fft(arr)
    #xf_abs = np.fft.fftshift(abs())
    # axis_xf = np.linspace(-N / 2, N / 2 - 1, num=N)
    # pl.subplot(223)
    # pl.title(u'频率为5Hz的正弦频谱图')
    # pl.plot(axis_xf, absY)
    # pl.axis('tight')
    f.close()

