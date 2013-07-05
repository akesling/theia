#!/usr/bin/python

import cv2
import random
import numpy as np

def new_target(width, height):
    return (random.randint(1, width), random.randint(1, height))

def drift(current, target):
    xdiff = target[0] - current[0]
    ydiff = target[1] - current[1]

    next_x = current[0]
    next_y = current[1]

    if abs(xdiff) > 0:
        next_x += xdiff/abs(xdiff)

    if abs(ydiff) > 0:
        next_y += ydiff/abs(ydiff)

    return (next_x, next_y)

if __name__ == '__main__':
    # Setup
    cv2.namedWindow('webcam_feed', cv2.CV_WINDOW_AUTOSIZE)
    webcam = cv2.VideoCapture(0)

    success, image = webcam.read()
    if not success:
        webcam.release()
        exit(1)

    width,height,channels = image.shape
    current_ul = (1,1)
    current_lr = (10,10)
    target_ul = (1,1)
    target_lr = (1,1)

    grey = np.zeros((width,height,1), image.dtype)

    while True:
        next_ul = drift(current_ul, target_ul)
        next_lr = drift(current_lr, target_lr)

        # Get image from webcam
        success, image = webcam.read()
        if not success:
            webcam.release()
            exit(1)

        # Convert to grescale
        cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, grey)

        cv2.equalizeHist(grey, grey)
        cv2.rectangle(grey, next_ul, next_lr, (0,0,255), 1, 0)
        cv2.imshow('webcam_feed', grey) #Show the image

        if 0 < cv2.waitKey(1):
            webcam.release()
            break

        if next_ul == current_ul:
            target_ul = new_target(width, height)
        if next_lr == current_lr:
            target_lr = new_target(width, height)

        current_ul = next_ul
        current_lr = next_lr
