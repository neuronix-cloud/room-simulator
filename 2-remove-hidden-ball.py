import os
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


files = os.listdir("rotgen/ok")
for i in range(0, len(files)):
  img0 = cv.cvtColor(cv.imread('rotgen/ok/%s'%files[i]), cv.COLOR_BGR2GRAY)
  img1 = cv.cvtColor(cv.imread('rotgen/ko/%s'%files[i]), cv.COLOR_BGR2GRAY)
  n = np.sum(np.bitwise_xor(img0,img1))
  if n == 0: 
    print("rm -v rotgen/ok/%s" % files[i])
