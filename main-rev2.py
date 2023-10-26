# the goal of this script is to display a random letter and based on an input from keyboard notify the user if they
# incorrect or correct by showing red or green.
import random
import os
import sys  # to access the system
import cv2
import mido
import time

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
    cv2.waitKey(1)


# List all available MIDI devices.
ports = mido.get_input_names()
print(ports)

# check if keyboard is present
if len(ports) == 0:
    print("Could not find keyboard!")
    exit(-1)

# get the name of the nano keyboard
my_device_name = ports[0]

# Connect to a particular port. The name should appear in the list above.
inport = mido.open_input(my_device_name)

# Map notes to key indices.
keys = {
    70: 3,
    68: 2,
    66: 1,
    63: 0,
    61: 0,
    58: 4,
    56: 5,
    54: 6,
}

letter_to_cell = {
    'a':[1],
    'b':[1,2],
    'c':[1,4],
    'd':[1,4,5],
    'e':[1,5]
}
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

    # given selected letter, set the list of acceptable brailer keys from dictionary
    correct_keys = []

    # display image with openCV given the filepath and window title
    display_image(filepath, window_title)

    correct_cells_pressed = False
    while not correct_cells_pressed:

        received_keys = []
        # wait for the first note_on message via inport.receive(). Place key in list
        message = inport.receive(block=False)

        # stay in a loop for X ms. Collect each note_on message as it arrives. Place in list
            # poll keyboard with receive(block=False)
            # check the return for this call. If note_on, place in list. Else, ignore
            # check the current system time, if timer has expired, leave loop

    # loop until receive note_on message
    # valid_key_received = False
    # while not valid_key_received:
    #
    #     # wait for a message from the keyboard (blocking call)
    #     message = inport.receive()
    #
    #     # is the message of the correct type?
    #     if message.type != 'note_on':
    #
    #         # if so, check if message/key is in set of allowable keys
    #         if message.note in keys:
    #             index = keys[message.note]
    #             print('Note is: ', message.note, 'Index is: ', index)
    #             valid_key_received = True
    #         else:
    #             valid_key_received = False
    #             print('Invalid Key')

    counter = counter + 1
    old_random_value = new_random_value
