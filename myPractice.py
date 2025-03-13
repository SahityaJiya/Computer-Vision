import cv2 as cv

# Here we add image in this file 
image = cv.imread('./prof_pic.jpg')
# Resize the image
image = cv.resize(image,(image.shape[0] // 3, image.shape[1] // 3), interpolation= cv.INTER_AREA)
cv.imshow('resized image', image)
# Gray Image
GrayImage = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image form', GrayImage)
# Blur Image
blurImage =  cv.GaussianBlur(image,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur image form', blurImage)
# Max Blur Check
MaxblurImage1 =  cv.GaussianBlur(image,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur image form', MaxblurImage1)
# canny image
cannyImage = cv.Canny(blurImage,100,120)
cv.imshow('Blur image form', cannyImage)
# Dilate Image
dilatedImage = cv.dilate(cannyImage,(4,4),iterations=2)
cv.imshow('Dilated Image', dilatedImage)
# Eroded Image
ErodedImage = cv.erode(dilatedImage,(3,3),iterations= 2) 
cv.imshow('Eroded Image',ErodedImage)
# waiting key
cv.waitKey(0)
cv.destroyAllWindowsx
