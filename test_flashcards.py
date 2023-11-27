# the goal of this script is to display a random letter and based on an input from keyboard notify the user if they
# incorrect or correct by showing red or green.
import random
import os
import sys  # to access the system
import cv2
import mido
import time
import numpy as np


def display_image(path_to_image, title, wait_time=1):
    '''
    Display image with openCV
    :param path_to_image: Filepath for image to be displayed
    :param title: Title of window (use the same name to refresh)
    :return: None
    '''
    # Display Random Image
    img = cv2.imread(path_to_image, cv2.IMREAD_ANYCOLOR)

    # Resize Image
    imS = cv2.resize(img, (400, 550))

    # draw the re-sized image
    cv2.imshow(title, imS)

    # wait 1ms to allow OpenCV to draw the image
    cv2.waitKey(wait_time)


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
notes_to_cell = {
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
    'A': [1],
    'B': [1, 2],
    'C': [1, 4],
    'D': [1, 4, 5],
    'E': [1, 5],
    'a': [7],
    'b': [7],
    'c': [7],
    'd': [7],
    'e': [7]
}


#press 62 (7) if they got it correct, any other key for false
"""letter_to_cell = {
    'a': [7],
    'b': [7],
    'c': [7],
    'd': [7],
    'e': [7]
}"""

window_title = "Flash Cards Quiz Phase 1"

available_letters = ['A', 'B', 'C', 'D', 'E','a','b','c','d','e']


# begin loop to listen for 10x nanokey presses
num_shown = 0

# num_correct = 0
done = False

accuracy_list = []
current_accuracy = 0
num_trials = 20
window_length = 10
successful_average = 0.9

events = []
old_random_value = random.randint(0, 100) % 5
while not done:

    new_random_value = random.randint(0, 100) % 5

    while old_random_value == new_random_value:
        new_random_value = random.randint(0, 100) % 5

    random_letter = available_letters[new_random_value]

    filepath = "Flashcard_" + random_letter + ".png"

    # given selected letter, set the list of acceptable brailer keys from dictionary
    correct_brailler_keys = letter_to_cell[random_letter]

    # display image with openCV given the filepath and window title
    display_image(filepath, window_title)

    # events.append({'foo': 'sdfas', 'time': None})
    print('The random letter selected is', random_letter, ' at ', time.time())
    # waiting for correct key press, will stay in this loop until correct keys are pressed
    correct_cells_pressed = False
    num_attempts = 0
    while not correct_cells_pressed:

        num_attempts = num_attempts + 1

        received_brailler_keys = []

        first_key_received = False
        while not first_key_received:
            message = inport.receive(block=True)
            if message.type == 'note_on' and message.note in notes_to_cell:
                braille_key = notes_to_cell[message.note]
                received_brailler_keys.append(braille_key)
                first_key_received = True

        # wait for the first note_on message via inport.receive(). Place key in list
        # message = inport.receive()
        # putting key into the list

        key_pressed_times = []
        key_pressed_times.append(time.time())
        # start timer for second key, if there is one
        # stay in a loop for X ms. Collect each note_on message as it arrives. Place in list
        current_time = time.time_ns()
        start_time = time.time_ns()

        # wait for 1s (1E9 ns)
        timeout = 1E8

        while abs(current_time - start_time) < timeout:

            # wait for a message from the keyboard (blocking call)
            second_message = inport.receive(block=False)

            #     # is the message of the correct type?
            if second_message is not None and second_message.type == 'note_on':
                # add second message to list
                braille_key = notes_to_cell[second_message.note]
                received_brailler_keys.append(braille_key)
                key_pressed_times.append(time.time())

            # check the time again
            current_time = time.time_ns()

        #print('It took', [abs(start_time-current_time)],'seconds to receive a key press')
        # timeout loop is complete, compare the set of received keys to those in the dictionary

        print('Keys received ', received_brailler_keys, 'at times ', key_pressed_times)

        # allowing keys to be pressed in any order
        received_brailler_keys.sort()


        # look up correct keys from the dictionary
        # logic to compare keys
        if correct_brailler_keys == received_brailler_keys:
            correct_cells_pressed = True
            # num_correct += 1
            print('Correct in ', num_attempts, ' attempts')
            accuracy_list.append(1)
            display_image("green_check.png", window_title, 500)


        else:
            print('Incorrect. Answer: ', correct_brailler_keys, 'Received: ', received_brailler_keys)
            accuracy_list.append(0)
            display_image("red_x.png", window_title, 500)
            display_image(filepath, window_title)


        # have enough trial occurred for the overall study and have enough trials occurred within the window
        if len(accuracy_list) >= num_trials and len(accuracy_list) >= window_length:
            # current_accuracy = np.mean(accuracy_list[-10:0])
            window = accuracy_list[-window_length:]

            #if len(accuracy_list) == window_length:
            #    window = accuracy_list

            current_accuracy = sum(window) / len(window)
            #print('Your window accuracy is', current_accuracy)

            if current_accuracy >= successful_average:
                done = True
                print('Your window accuracy is', current_accuracy)
                print('Your overall accuracy is', sum(accuracy_list) / len(accuracy_list))
                print('The total number of attempts is', len(accuracy_list))


    num_shown = num_shown + 1
    old_random_value = new_random_value
    # end of main loop for entire experimental trials
