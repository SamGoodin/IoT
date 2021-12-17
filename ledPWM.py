import RPi.GPIO as GPIO
from time import sleep

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

led = GPIO.PWM(8, 500)
led.start(0)

while True:
    for dc in range(0, 101, 5):
        led.ChangeDutyCycle(dc)
        sleep(0.1)
    for dc in range (100, -1, -5):
        led.ChangeDutyCycle(dc)
        sleep(0.1)
        
