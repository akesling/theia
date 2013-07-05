#!/usr/bin/python

# Initial tutorial turned to (http://www.neuroforge.co.uk/index.php/getting-started-with-python-a-opencv)
import cv
import random

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
    cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
    webcam = cv.CaptureFromCAM(0)
    font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8)

    image = cv.QueryFrame(webcam)

    height = image.height
    width = image.width
    current_ul = (1,1)
    current_lr = (1,1)
    target_ul = (1,1)
    target_lr = (1,1)

    grey = cv.CreateImage((width,height), 8, 1)

    while True:
        next_ul = drift(current_ul, target_ul)
        next_lr = drift(current_lr, target_lr)

        # Get image from webcam
        image = cv.QueryFrame(webcam)

        # Convert to grescale
        cv.CvtColor(image, grey, cv.CV_BGR2GRAY)

        cv.EqualizeHist(grey, grey)
        cv.Rectangle(grey, next_ul, next_lr, (0,0,255), 1, 0)
        cv.ShowImage('a_window', grey) #Show the image

        if 0 < cv.WaitKey(2):
            break

        if next_ul == current_ul:
            target_ul = new_target(width, height)
        if next_lr == current_lr:
            target_lr = new_target(width, height)

        current_ul = next_ul
        current_lr = next_lr
