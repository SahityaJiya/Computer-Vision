import cv2 as cv
import numpy as np

myImage = np.zeros((500,500),dtype = 'uint8')
cv.imshow('black',myImage)


myImage = np.zeros((500,500,3),dtype = 'uint8') 
myImage[:] = 0,0,255 
cv.imshow('red',myImage)

myImage = np.zeros((500,500,3),dtype = 'uint8') 
myImage[200:300,300:400] = 0,0,255
cv.imshow('blue',myImage)

cv.rectangle(myImage,(100,100),(400,400),(127,80,56),thickness=-1)
cv.imshow('rectangle',myImage)
cv.rectangle(myImage,(100,100),(400,400),(45,87,78),thickness= 5)
cv.imshow('rectangle2',myImage)

cv.circle(myImage,(myImage.shape[1] // 2, myImage.shape[0] // 2),40,(45,98,35),thickness = -1)
cv.imshow('circle',myImage)





myImage = np.zeros((500,500),dtype = 'uint8')
cv.imshow('black',myImage)
myImage = np.zeros((500,500),dtype = 'uint8')
cv.imshow('black',myImage)




img = cv.imread('./prof_pic.jpg')

cv.waitKey()