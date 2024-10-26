from math import cos, pi
from PIL import Image
from scipy.fft import rfft2, irfft2
import pickle

img = Image.open("doge.png", "r")

signal = list(img.getdata())

T = [signal[i:i + img.height] for i in range(0, len(signal), img.height)]
T = ([[x[0] for x in y] for y in T],[ [x[1] for x in y] for y in T], [[x[2] for x in y] for y in T])


#pickle.dump(T, open("image", "wb"))

twoDimDFT = lambda T: [[sum([sum([T[m][n][0]*cos(2 * pi * (k * m / len(T) + l * n / len(T[0]))) for m in range(len(T))]) for n in range(len(T[0]))])/(len(T)*len(T[0])) for k in range(len(T))] for l in range(len(T[0]))]
"""
def twoDimDFT(T, k, l):
    result = 0
    for m in range(len(T)):
        for n in range(len(T[0])):
            result += T[m][n][0]*e**(-1j * 2 * pi * (k * m / len(T) + l * n / len(T[0])))
    return result / (len(T) * len(T[0]))
"""


#result = twoDimDFT(T)

result = (rfft2(T[0]), rfft2(T[1]), rfft2(T[2]))

for i in range(3):
    numbered = []
    for inder, row in enumerate(result[i]):
        for indev, val in enumerate(row):
            numbered.append((val, inder, indev))

    numbered = sorted(numbered, key=lambda x: abs(x[0]))

    for val, x, y in numbered[:len(numbered)*99//100]:
        result[i][x][y] = 0



"""
scale = max([abs(max(*x, key = lambda v: abs(v.real)).real) for x in result])

resultList = []
for y in result:
    for x in y:
        val = int(abs(x.real)*256/scale)
        resultList.append((val, val, val))



resultimg = Image.new("RGB", (50, 50))
resultimg.putdata(resultList)

resultimg.save("result.jpg")
"""

invTwoDimDFT = lambda T: [[sum([sum([T[m][n]*cos(2 * pi * (k * m / len(T) + l * n / len(T[0]))) for m in range(len(T))]) for n in range(len(T[0]))])/(len(T)*len(T[0])) for k in range(len(T))] for l in range(len(T[0]))]

#original = invTwoDimDFT(result)

original = (irfft2(result[0]), irfft2(result[1]), irfft2(result[2]))

resultList = []
for row in range(img.width):
    for col in range(img.height):
        resultList.append((int(original[0][row][col]), int(original[1][row][col]), int(original[2][row][col])))


resultimg = Image.new("RGB", (img.width, img.height))
resultimg.putdata(resultList)

resultimg.save("result.png")


