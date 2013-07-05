#!/usr/bin/python
# https://github.com/akesling/facerec/blob/master/py/facedet/detector.py was used as a tutorial on the subject

import cv2
import numpy as np

CASCADES_FILE = "/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml"
MIN_NEIGHBORS = 5
SCALE_FACTOR = 1.2
MIN_SIZE = (30, 30)

CLASSIFIER = cv2.CascadeClassifier(CASCADES_FILE)

def detect_faces(image):
    grey = np.zeros((width,height,1), image.dtype)
    cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, grey)
    cv2.equalizeHist(grey, grey)
    rects = CLASSIFIER.detectMultiScale(grey, scaleFactor=SCALE_FACTOR, minNeighbors=MIN_NEIGHBORS, minSize=MIN_SIZE)

    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

if __name__ == '__main__':
    # Setup
    cv2.namedWindow('face_boxes', cv2.CV_WINDOW_AUTOSIZE)
    webcam = cv2.VideoCapture(0)

    success, image = webcam.read()
    if not success:
        webcam.release()
        exit(1)

    width,height,channels = image.shape

    grey = np.zeros((width,height,1), image.dtype)

    while True:
        # Get image from webcam
        success, image = webcam.read(image)
        if not success:
            webcam.release()
            exit(1)

        for i, face in enumerate(detect_faces(image)):
            upper_left = tuple(face[:2])
            lower_right = tuple(face[2:])
            print i, upper_left, lower_right
            cv2.rectangle(image, upper_left, lower_right, (0,0,255), 1, 0)

        cv2.imshow('face_boxes', image) #Show the image

        if 0 < cv2.waitKey(1):
            webcam.release()
            break
