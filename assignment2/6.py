import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lowContrast.png',0)
plt.hist(img.ravel(),256,[0,256])
plt.savefig('histogram.png')

equ = cv2.equalizeHist(img)
cv2.imwrite('equilizedImage.png',equ)

plt.hist(res.ravel(),256,[0,256])
plt.savefig('equilizedHistogram.png')