#!/usr/bin/python

# Initial tutorial turned to (http://www.neuroforge.co.uk/index.php/getting-started-with-python-a-opencv)
import cv

cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
image=cv.LoadImage('picture.png', cv.CV_LOAD_IMAGE_COLOR) #Load the image
font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font
x = 255
y = 255
cv.PutText(image,"Hello World!!!", (x,y),font, 255) #Draw the text
cv.ShowImage('a_window', image) #Show the image
cv.WaitKey(10000)
cv.SaveImage('image.png', image) #Saves the image
