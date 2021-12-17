import RPi.GPIO as GPIO
from time import sleep

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(8, 1)
    sleep(0.5)
    GPIO.output(8, GPIO.LOW)
    sleep(0.5)