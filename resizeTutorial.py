import cv2 as cv

def resizebogla(img,scale):
    height = img.shape[0] * scale
    width = img.shape[1] * scale
    dimension = (width,height)

    return cv.resize(img,dimension,interpolation= cv.INTER_AREA)

img = cv.imread('./prof_pic.jpg')
# cv.imshow('dfjskdf',img)

# img1 = cv.resize(img,(640,480),interpolation= cv.INTER_AREA)
# cv.imshow('df',img1)
# cv.waitKey()
# print(img.shape[0])
# print(img.shape[1])

img2 = resizebogla(img,0.3)






