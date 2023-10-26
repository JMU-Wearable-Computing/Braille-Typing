#!/usr/bin/env python

import mido

# List all available MIDI devices.
ports = mido.get_input_names()
print(ports)

if len(ports) == 0:
    print("Could not find keyboard!")
    exit(-1)

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

# The display is seven empty squares.
display = "\u25A2" * 7
index = 0

while index >= 0:
    # Keep getting messages until note_on.
    message = inport.receive()
    while message.type != 'note_on':
        message = inport.receive()

    # Only handle certain accidental keys. Show pressed key
    # in display by replacing its empty square with a filled
    # square.
    if message.note in keys:
        index = keys[message.note]
        if index >= 0:
            print('Note is: ', message.note, 'Index is: ', index)
            # status = display[:index] + "\u25A3" + display[index + 1:]
            # print(f"\t{status}", end="\r")
    else:
        print(f'Unknown {message.note}')

inport.close()
