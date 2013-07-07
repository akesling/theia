#!/usr/bin/env python
# https://github.com/akesling/facerec/blob/master/py/facedet/detector.py was used as a tutorial on the subject

import cv2
import numpy as np

FACE_CASCADES_FILE = "/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml"
EYE_CASCADES_FILE = "/usr/share/OpenCV/haarcascades/haarcascade_eye.xml"
MIN_NEIGHBORS = 5
SCALE_FACTOR = 1.2
MIN_SIZE = (20, 20)

FACE_CLASSIFIER = cv2.CascadeClassifier(FACE_CASCADES_FILE)
EYE_CLASSIFIER = cv2.CascadeClassifier(EYE_CASCADES_FILE)

def detect_things(image, classifier):
    width, height, channels = image.shape
    grey = np.zeros((width,height,1), image.dtype)
    cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, grey)
    cv2.equalizeHist(grey, grey)
    rects = classifier.detectMultiScale(grey, scaleFactor=SCALE_FACTOR, minNeighbors=MIN_NEIGHBORS, minSize=MIN_SIZE)

    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

if __name__ == '__main__':
    cv2.namedWindow('boxed_image', cv2.CV_WINDOW_AUTOSIZE)
    cv2.namedWindow('faces', cv2.CV_WINDOW_AUTOSIZE)
    cv2.namedWindow('eyes', cv2.CV_WINDOW_AUTOSIZE)
    webcam = cv2.VideoCapture(0)

    success, image = webcam.read()
    if not success:
        webcam.release()
        exit(1)

    while True:
        success, image = webcam.read(image)
        if not success:
            webcam.release()
            exit(1)

        for i, face in enumerate(detect_things(image, FACE_CLASSIFIER)):
            fx_0,fy_0,fx_1,fy_1 = face
            face_image = image[fy_0:fy_1,fx_0:fx_1]
            cv2.imshow('faces', face_image)

            eye_offset = np.array((fx_0,fy_0,fx_0,fy_0), face.dtype)
            for j, eye in enumerate(detect_things(face_image, EYE_CLASSIFIER)):
                ex_0,ey_0,ex_1,ey_1 = eye+eye_offset
                eye_image = image[ey_0:ey_1,ex_0:ex_1]
                scaled = cv2.resize(eye_image, (500,500), interpolation=cv2.INTER_NEAREST)
                cv2.imshow('eyes', scaled)
                cv2.rectangle(image, (ex_0,ey_0), (ex_1,ey_1), (0,255,0), 1, 0)

            cv2.rectangle(image, (fx_0,fy_0), (fx_1,fy_1), (0,0,255), 1, 0)

        cv2.imshow('boxed_image', image) #Show the image

        if 0 < cv2.waitKey(1):
            webcam.release()
            break
