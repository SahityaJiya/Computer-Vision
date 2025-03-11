import cv2 as cv

#video part
capture = cv.VideoCapture('./video.mp4')
while True:
    isTrue,frame = capture.read()
    frameResize = cv.resize(frame,(640,480),interpolation= cv.INTER_AREA)

    
    # cv.imshow('video',frame)
    cv.imshow('video resized',frameResize)
    if cv.waitKey(20) & 0xff == ord('d'):   
        break

capture.release()
cv.destroyAllWindows()