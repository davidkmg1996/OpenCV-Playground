import cv2 as cv
import numpy as np
#from matplotlib import pyplot as plt

#Quality loss from incrementing x by 1 from 11 through 19

im = cv.imread('photos/imageNoise.jpg')
cv.imshow('noise', im)
im2 = cv.imread('photos/imageNoise.jpg')

x = 10
y = True

def showBlur(ds):
    ds = cv.fastNlMeansDenoisingColored(im2,None, x, x,7,21)
    cv.imshow('denoised' + str(x), ds)


#Params
    
dst = cv.fastNlMeansDenoisingColored(im2,None, x, x,7,21)
while y is True and x < 20:
    x += 2
    dst = cv.fastNlMeansDenoisingColored(im2,None, x, x,7,21)
    showBlur(dst)
    if x >= 20:
        y = False

#dst = cv.fastNlMeansDenoisingColored(im2, None, fStrengthGrey, fStrengthColor, winSizeOdd, winSizeEven)

cv.waitKey(0)



