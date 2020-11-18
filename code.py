from scipy.io import wavfile
from scipy.fftpack import fft, ifft
from matplotlib import pyplot as plt
import numpy as np

power = 0.02e7


def string_to_binary_ascii(string):
    binary = []
    for char in string:
        binary.append("{:08b}".format(ord(char)))
    return "".join(binary)


def put_code_in_signal(data, samplerate, songname, lim, length, filename):
    codename = string_to_binary_ascii(songname)
    c = fft(data)
    for i in range(0, len(codename)):
        for j in range(length):
            if codename[i] == "1":
                c[lim + i * length + j] = (power)
            else:
                c[lim + i * length + j] = (-power)
    p = ifft(c).real.astype(np.int16)
    wavfile.write(filename, samplerate, p)
    plt.plot(c)
    plt.show()
