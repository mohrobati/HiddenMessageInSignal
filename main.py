from scipy.io import wavfile
from code import put_code_in_signal
from decode import decode_from_signal
from scipy.fftpack import fft
from matplotlib import style, pyplot as plt
import os



lim = 300000
length = 10
codelength = 8

# # files = os.listdir('test/')
# # for file in files:
# #     samplerate, data = wavfile.read('test/' + file)
# #     songname = file[:len(file) - 4]
# #     put_code_in_signal(data, samplerate, songname, lim, length, "out/"+songname+'_out.wav')
# # #
#
files = os.listdir('out/')
files.remove('.DS_Store')
for file in files:
    samplerate, data = wavfile.read('out/' + file)
    songname = file[:len(file) - 4]
    print(songname)
    decode_from_signal(data, lim, length, codelength, samplerate)

