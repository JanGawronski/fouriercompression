from PIL import Image
from scipy.fft import rfft2
import numpy as np
import pickle

img = Image.open("doge.png", "r")

signal = list(img.getdata())
print("Getting image data succesful")

T = [np.array(i) for i in zip(*signal)]

result = (rfft2(np.reshape(T[0], (img.width, img.height))), rfft2(np.reshape(T[1], (img.width, img.height))), rfft2(np.reshape(T[2], (img.width, img.height))))
print("FFT succesful")

compressed = [[], [], [], (len(result[0]), len(result[0][0])), (img.width, img.height)]

compressionRate = .01

topElements = int(compressionRate * len(result[0]) * len(result[0][0]))

for i in range(3):
    flatFFT = np.ravel(result[i])
    flatabsFFT = [abs(x) for x in flatFFT]
    ind = np.argpartition(flatabsFFT, -topElements)[-topElements:]
    compressed[i] = (ind, flatFFT[ind])


print("Compressing image succesful")


pickle.dump(compressed, open("99image", "wb"))
print("Saving image succesful")