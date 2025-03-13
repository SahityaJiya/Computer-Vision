import cv2 as cv
import numpy as np

img = cv.imread('./prof_pic.jpg')
# height = img.shape[1]
# width = img.shape[0]

(height,width) = img.shape[:2] 
img = cv.resize(img,(height // 4,width // 4),interpolation = cv.INTER_AREA)
cv.imshow('my image',img)

#crop
croppedImage = img[50:200,200:400]
cv.imshow('cropped image',croppedImage)

#translate image
def moveImage(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = img.shape[:2]
    return cv.warpAffine(img,transMat,dimension)

for x in range(200):
    img1 = moveImage(img,x,20)
    cv.waitKey(20)
    cv.imshow('moved image',img1)

cv.waitKey()
cv.destroyAllWindows()