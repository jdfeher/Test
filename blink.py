# s://raspberrypihq.com/making-a-led-blink-using-the-raspberry-pi-and-python/

import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

pin1 = 26
pin2 = 23

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
   GPIO.output(pin1, GPIO.HIGH) # Turn on
   GPIO.output(pin2, GPIO.HIGH) # Turn on
   sleep(1)                  # Sleep for 1 second
   GPIO.output(pin1, GPIO.LOW)  # Turn off
   GPIO.output(pin2, GPIO.LOW)  # Turn off
   sleep(1)                  # Sleep for 1 second
