# simple circuitPython program sending out midi notes when captouch breakout board pads are touched

import time
import board
import busio
import adafruit_mpr121
import usb_midi
import adafruit_midi

# NoteOn is the main function we'll be using
from adafruit_midi.note_on import NoteOn

# i2c import is for the capacitive touch board, connected via STEMMA
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

# assign midi channel and port
midi_channel = 1
midi = adafruit_midi.MIDI(midi_out = usb_midi.ports[1], out_channel = midi_channel-1)

while True:
    for i in range(12): # loop through all inputs
       if mpr121[i].value: # if any input is touched (ie. value == True), send out that midi note on
            midi.send(NoteOn(i))

