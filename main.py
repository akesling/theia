#!/usr/bin/python

# Initial tutorial turned to (http://www.neuroforge.co.uk/index.php/getting-started-with-python-a-opencv)
import cv
import random

# Setup
cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
webcam=cv.CaptureFromCAM(0)
font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font

image=cv.QueryFrame(webcam)

height = image.height
width = image.width
current = [1,1]
target = [1,1]

while True:
    xdiff = target[0] - current[0]
    ydiff = target[1] - current[1]

    if abs(xdiff) > 0:
        current[0] += xdiff/abs(xdiff)
    else:
        target[0] = random.randint(1, width)

    if abs(ydiff) > 0:
        current[1] += ydiff/abs(ydiff)
    else:
        target[1] = random.randint(1, height)

    image=cv.QueryFrame(webcam)
    cv.PutText(image,"Hello World!!!", tuple(current),font, 255) #Draw the text
    cv.ShowImage('a_window', image) #Show the image
    cv.WaitKey(2)
    cv.SaveImage('image.png', image) #Saves the image
