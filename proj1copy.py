import RPi.GPIO as GPIO
from time import sleep


buttonA = 12
buttonB = 16

LED_A = 18
LED_B = 22

FLAG_A = False #
FLAG_B = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#Button A - Controls LED action
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Button B - Controls functionality of button A
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#LED A - PWM
GPIO.setup(18, GPIO.OUT)
#LED B - Frequency
GPIO.setup(22, GPIO.OUT)

#GPIO.add_event_detect(12, GPIO.RISING, callback=button_callback)
#GPIO.add_event_detect(16, GPIO.RISING, callback=button_callback)
led = GPIO.PWM(18, 500)

def pwm():
    led.ChangeDutyCycle(num%100)
    
GPIO.output(LED_A,False)
GPIO.output(LED_B,False)

currentDC = 0
currentBlink = 0

def runA(dc):
    #PWM
    led.start(0)
    #FLAG_A = True
    led.ChangeDutyCycle(dc % 100)
    #print(dc)
    
    if (GPIO.input(buttonA) == 0):
        print("Button A pressed while runA running")
        currentDC += 20
        return True
    elif (GPIO.input(buttonB) == 0):
        print("Button B pressed while runA running")
        GPIO.output(LED_A, False)
        return False
    else:
        return True

def runB():
    #Blinking
    GPIO.output(LED_B, 1)
    sleep(0.3)
    GPIO.output(LED_B, GPIO.LOW)
    sleep(0.3)
    if (GPIO.input(buttonA) == 0):
        print("Button A pressed while blink running runB" )
        #currentBlink += 20
        sleep(0.2)
        return True
    elif (GPIO.input(buttonB) == 0):
        print("Button B pressed while blink running runB")
        GPIO.output(LED_B, False)
        sleep(0.2)
        return False
    else:
        return True

def changeAtoB():
    GPIO.output(LED_A, False)
    while True:
        status = runB()
        if not status:
            break
        if (GPIO.input(buttonA) == 0):
            print("Button A pressed while blink running changeAtoB")
            #currentBlink += 20
            sleep(0.2)
        elif (GPIO.input(buttonB) == 0):
            print("Button B pressed while blink running changeAtoB")
            GPIO.output(LED_B, False)
            break
    
def changeBtoA():
    GPIO.output(LED_B, False)
    while True:
        status = runA(currentDC)
        if not status:
            break
        if (GPIO.input(buttonA) == 0):
            print("Button A pressed while blink running changeBtoA")
            #currentBlink += 20
            sleep(0.2)
        elif (GPIO.input(buttonB) == 0):
            print("Button B pressed while blink running changeBtoA")
            GPIO.output(LED_A, False)
            break

while True:
    
    if (GPIO.input(buttonA) == 0):
        #PWM LED
        """
        print("Button A pressed")
        led.start(0)
        FLAG_A = True
        for dc in range(0, 101, 5):
            led.ChangeDutyCycle(dc)
            sleep(0.1)
        for dc in range (100, -1, -5):
            led.ChangeDutyCycle(dc)
            sleep(0.1)
        FLAG_A = False
        """
        print("Flag A: " + str(FLAG_A) + " Flag B: " + str(FLAG_B))
        if FLAG_A == True and FLAG_B == False:
            #PWM
            changeBtoA()
            #GPIO.output(LED_A,True)
        elif FLAG_A == False and FLAG_B == True:
            #Blinking
            changeAtoB()
        elif FLAG_A == False and FLAG_B == False:
            pass
        else:
            #Blinking
            GPIO.output(LED_A,False)
            GPIO.output(LED_B,True)
        
        sleep(0.2)
        
        
    if (GPIO.input(buttonB) == 0):
        print("Button B pressed")
             
        if FLAG_A == True and FLAG_B == False:
            FLAG_B = True
            FLAG_A = False
            changeAtoB()
            sleep(0.5)
        elif FLAG_A == False and FLAG_B == True:
            FLAG_B = False
            FLAG_A = True
            changeBtoA()
            sleep(0.5)
        elif FLAG_A == False and FLAG_B == False:
            FLAG_B = True
            FLAG_A = False
            changeAtoB()
            sleep(0.5)
        else:
            FLAG_A = False
            FLAG_B = True
            changeAtoB()
            sleep(0.5)
        
    """
    if (GPIO.input(buttonB) == 0):
        print("Button B pressed")
             
        if FLAG_B == False:
            GPIO.output(LED_B,True)
            FLAG_B = True
            sleep(0.5)
        else:
            GPIO.output(LED_B,False)
            FLAG_B = False
            sleep(0.5)
      """  
    
        
GPIO.cleanup()
