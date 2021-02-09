import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/shark.jpg', cv2.IMREAD_GRAYSCALE)

plt.hist(img.ravel(),256,[0,256]); plt.show()

