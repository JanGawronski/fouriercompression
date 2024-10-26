from PIL import Image
from scipy.fft import irfft2
import numpy as np
import pickle

array = pickle.load(open("99image", "rb"))
print("Loading file succesful")

result = [np.zeros((array[3][0] * array[3][1]), dtype = np.complex128), np.zeros((array[3][0] * array[3][1]), dtype = np.complex128), np.zeros((array[3][0] * array[3][1]), dtype = np.complex128)]
print("Creating array succesful")

for i in range(3):
    for index, value in zip(array[i][0], array[i][1]):
        result[i][index] = value
    result[i] = np.reshape(result[i], array[3])

print("Filling array succesful")

original = np.transpose(np.array([np.astype(np.ravel(irfft2(result[0])), int, copy = False), np.astype(np.ravel(irfft2(result[1])), int, copy = False), np.astype(np.ravel(irfft2(result[2])), int, copy = False)]))
print("IFFT succesful")

print("Creating image array succesful")

resultimg = Image.new("RGB", array[4])
resultimg.putdata([tuple(x) for x in original])

resultimg.save("result.png")
print("Creating image succesful")