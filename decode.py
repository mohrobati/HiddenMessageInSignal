from scipy.fftpack import fft, fftfreq
from matplotlib import pyplot as plt
import numpy as np


def decode_from_signal(data, lim, length, codelength, sr):
    c = fft(data)
    code = []
    binary_name = []
    for i in range(codelength):
        for j in range(8):
            tmp = c[lim + int(length/2) + j*length + i*8*length]
            if tmp > 0:
                binary_name.append("1")
            elif tmp < 0:
                binary_name.append("0")
        code.append("".join(binary_name))
        binary_name.clear()
    final_name = []
    for bn in code:
        final_name.append(chr(int(bn, 2)))
    print("".join(final_name))
    samr = fftfreq(len(c), sr)
    print(len(c))
    print(samr[300000])
    plt.plot(samr, c)
    plt.show()
