#!/usr/bin/python
# https://github.com/akesling/facerec/blob/master/py/facedet/detector.py was used as a tutorial on the subject

import cv2
import numpy as np

if __name__ == '__main__':
    # Setup
    cv2.namedWindow('webcam_feed', cv2.CV_WINDOW_AUTOSIZE)
    webcam = cv2.VideoCapture(0)

    success, image = webcam.read()
    if not success:
        webcam.release()
        exit(1)

    width,height,channels = image.shape

    grey = np.zeros((width,height,1), image.dtype)

    while True:
        # Get image from webcam
        success, image = webcam.read()
        if not success:
            webcam.release()
            exit(1)

        # Convert to grescale
        cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, grey)

        cv2.equalizeHist(grey, grey)
        cv2.imshow('webcam_feed', grey) #Show the image

        if 0 < cv2.waitKey(1):
            webcam.release()
            break
