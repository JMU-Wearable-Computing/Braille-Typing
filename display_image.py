# the goal of this script is to display a random letter and based on an input from keyboard notify the user if they
# incorrect or correct by showing red or green.
import random
import os
import sys #to access the system
import cv2


counter = 0
while counter < 10:
    window_title = "Braille Flash Cards"

    available_letters = ['a','b','c','d','e']

    random_value = random.randint(0,100)%5

    random_letter = available_letters[random_value]

    filepath = "letter_"+random_letter+".png"

    #Display Random Image
    img = cv2.imread(filepath, cv2.IMREAD_ANYCOLOR)
    #Resize Image
    imS = cv2.resize(img, (600, 850))
    cv2.imshow(window_title, imS)
    cv2.waitKey(0)

    counter = counter + 1


''''#Letter A
#load the file letter_a.png into an object called img
img = cv2.imread("letter_a.png", cv2.IMREAD_ANYCOLOR)  #loading an image using imread
#Resize Image
imS = cv2.resize(img, (600, 850))

#use openCV to display the contents in img as the window "letter_a"
cv2.imshow(window_title, imS) #show letter a

# wait key....
cv2.waitKey(0)

#img.close() #close image
#sys.exit() #exiting the image
#cv2.destoryAllWindows() # close all windows


#Letter B
img = cv2.imread("letter_b.png", cv2.IMREAD_ANYCOLOR)
imSize = cv2.resize(img, (600, 850))
cv2.imshow(window_title, imSize) #show letter b
cv2.waitKey(0) #close image

#Letter C
img = cv2.imread("letter_c.png", cv2.IMREAD_ANYCOLOR)
imSize = cv2.resize(img, (600, 850))
cv2.imshow(window_title, imSize) #show letter c
cv2.waitKey(0) #close image

#Letter D
img = cv2.imread("letter_d.png", cv2.IMREAD_ANYCOLOR)
imSize = cv2.resize(img, (600, 850))
cv2.imshow(window_title, imSize) #show letter d
cv2.waitKey(0) #close image

#Letter E
img = cv2.imread("letter_e.png", cv2.IMREAD_ANYCOLOR)
imSize = cv2.resize(img, (600, 850))
cv2.imshow(window_title, imSize) #show letter e
cv2.waitKey(0) #close image'''



