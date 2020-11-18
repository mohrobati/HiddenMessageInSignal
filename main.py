from scipy.io import wavfile
from code import put_code_in_signal
import os

lim = 300000
length = 10
codelength = 8

files = os.listdir('test/')
files.remove('.DS_Store')

for file in files:
    samplerate, data = wavfile.read('test/' + file)
    songname = file[:len(file) - 4]
    put_code_in_signal(data, samplerate, songname, lim, length, "out/"+songname+'_out.wav')
