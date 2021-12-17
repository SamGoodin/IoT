import RPi.GPIO as GPIO
from time import sleep
from w1thermsensor import W1ThermSensor
import math

LED = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#LED Green
GPIO.setup(LED, GPIO.OUT)
led = GPIO.PWM(LED, 500)
sensor = W1ThermSensor()

maxTemp = 30
step = None

led.start(0)

while True:
    temp = sensor.get_temperature()
    print("Temp is: " + str(temp))
    if not step:
        step = round(maxTemp - temp, 1)
        print("Step: " + str(step))
    pwm = (1 - ((maxTemp - temp)/step)) * 100
    if pwm > 100:
        pwm = 100.0
    elif pwm < 0:
        pwm = 0.0
    print("PWM: " + str(pwm))
    led.ChangeDutyCycle(pwm)
