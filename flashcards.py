import random
import os
import sys  # to access the system
import cv2
import mido
import keyboard


def display_image(path_to_image, title):
    '''
    Display image with openCV
    :param path_to_image: Filepath for image to be displayed
    :param title: Title of window (use the same name to refresh)
    :return: None
    '''
    # Display Random Image
    img = cv2.imread(path_to_image, cv2.IMREAD_ANYCOLOR)

    # Resize Image
    imS = cv2.resize(img, (600, 850))

    # draw the re-sized image
    cv2.imshow(title, imS)

    # wait 1ms to allow OpenCV to draw the image
    cv2.waitKey(0)

# Map notes to keyboard letters.
"""keyboard_letter_map = {
    'a': a,
    'b': ,
    'c': ,
    'd': ,
    'e': 
}"""

window_title = "Braille Flash Cards"

available_letters = ['a', 'b', 'c', 'd', 'e']

# begin loop to listen for 10x nanokey presses
counter = 0

old_random_value = random.randint(0, 100) % 5
while counter < 10:

    new_random_value = random.randint(0, 100) % 5

    while old_random_value == new_random_value:
        new_random_value = random.randint(0, 100) % 5

    random_letter = available_letters[new_random_value]

    filepath = "letter_" + random_letter + ".png"

    # display image with openCV given the filepath and window title
    display_image(filepath, window_title)

    # wait for correct key to be press
    received_key = '@'
    correct_key = random_letter

    while received_key != correct_key:
        # read in a key
        received_key = keyboard.read_key()

        # if correct, do something...
        dummy=0

        # if not correct, do something else..."""

counter = counter + 1
old_random_value = new_random_value
