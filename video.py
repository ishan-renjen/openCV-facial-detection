import cv2 as cv
import numpy as np

def video():
    image = cv.VideoCapture(0)
    if image.isOpened() == False:
        print("cant open")
        exit()
    
    while True:
        retval, frame = image.read()

        if retval is False:
            print("cant recieve")
            break
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('c'):
            break

def draw_square()
