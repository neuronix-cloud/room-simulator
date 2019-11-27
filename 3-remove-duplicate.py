import os
import numpy as np
import cv2 as cv

m = {}
for dir in ["rotgen/ok", "rotgen/ko"]:
    for f in os.listdir(dir):
        file = "%s/%s" %(dir,f)
        img0 = cv.cvtColor(cv.imread(file), cv.COLOR_BGR2GRAY)
        n = np.sum(img0)
        if n in m:
            m[n].append(file)
            print("rm -v %s" % file)
        else:
            m[n] = [file]

#for k in m.keys():
#    if len(m[k]) > 1:
#        print("cd rotgen/ko ; open", " ".join(m[k]), "; cd -")

