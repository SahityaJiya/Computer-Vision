import cv2 as cv

img = cv.imread('./prof_pic.jpg')

#resize kase karte hai
img = cv.resize(img,(img.shape[0] // 4, img.shape[1] // 4),interpolation= cv.INTER_AREA)
cv.imshow('image',img)

#using filter in image
grayImage = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey image',grayImage)

#color mai vapas lana hai
colorImage = cv.cvtColor(grayImage,cv.COLOR_GRAY2BGR)
cv.imshow('color image',colorImage)

# Apply a color map to the grayscale image
colorMappedImage = cv.applyColorMap(grayImage, cv.COLORMAP_JET)
cv.imshow('Color Mapped Image', colorMappedImage)

#blur effect
blurImage = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur image',blurImage)

blurImage = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur image2',blurImage)

cannyImage = cv.Canny(grayImage,125,175)
cv.imshow('canny image', cannyImage)

cannyImage = cv.Canny(img,125,175)
cv.imshow('canny color image', cannyImage)

cannyImage = cv.Canny(blurImage,125,175)
cv.imshow('canny blur image', cannyImage)

dilatedImage = cv.dilate(cannyImage,(5,5),iterations=3)
cv.imshow('dilated image', dilatedImage)

erodedImage = cv.erode(dilatedImage,(5,5),iterations=3)
cv.imshow('eroded image', erodedImage)



cv.waitKey()
cv.destroyAllWindows()