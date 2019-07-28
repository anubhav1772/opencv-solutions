# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 09:52:03 2019
@author: anubhav singh
Rotate a text on an image in any direction using opencv
Stackoverflow Link: https://stackoverflow.com/questions/57235217/write-text-on-image-randomly-in-any-direction-e-g-horizontal-vertical-diagon/57237825#57237825

"""

import cv2
import numpy as np
img = cv2.imread('bird.jpeg')

def rotate(src, angle):
    rows,cols = src.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2,rows/2), angle, 1)
    dst = cv2.warpAffine(src, M, (cols,rows))
    return dst
    

x = np.zeros((img.shape), dtype=np.uint8)
cv2.putText(x, 'Stackoverflow Sample Image', (50, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
x = rotate(x, 45)
res = cv2.bitwise_or(img, x)
cv2.imshow('img', x)
cv2.waitKey(0)
cv2.destroyAllWindows()