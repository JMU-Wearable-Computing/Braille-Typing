import random
import os
import sys #to access the system
import cv2


counter = 0
while counter < 10:
    window_title_test = "Flash Card Test"

    available_letters = ['A','B','C','D','E']

    random_value = random.randint(0,100)%5

    random_letter = available_letters[random_value]

    filepath = random_letter+".png"

    #Display Random Image
    img = cv2.imread(filepath, cv2.IMREAD_ANYCOLOR)
    #Resize Image
    imS = cv2.resize(img, (400, 550))
    cv2.imshow(window_title_test, imS)
    cv2.waitKey(0)


    counter = counter + 1
