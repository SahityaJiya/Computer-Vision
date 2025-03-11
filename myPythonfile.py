import cv2 as cv

#image part
# img = cv.imread('./prof_pic.jpg')
# cv.imshow('boglaji',img)

# cv.waitKey(0)

#video part
capture = cv.VideoCapture('./video.mp4')
while True:
    isTrue,frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xff == ord('d'):   
        break

capture.release()
cv.destroyAllWindows()

