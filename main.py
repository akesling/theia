#!/usr/bin/python

# Initial tutorial turned to (http://www.neuroforge.co.uk/index.php/getting-started-with-python-a-opencv)
import cv

x = 255
y = 255

# Setup
cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
webcam=cv.CaptureFromCAM(0)
font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font

while True:
    image=cv.QueryFrame(webcam)
    cv.PutText(image,"Hello World!!!", (x,y),font, 255) #Draw the text
    cv.ShowImage('a_window', image) #Show the image
    cv.WaitKey(2)
    cv.SaveImage('image.png', image) #Saves the image
