import RPi.GPIO as GPIO
from time import sleep


buttonA = 12
buttonB = 16

LED_A = 18
LED_B = 22

FLAG_A = False
FLAG_B = True

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

while True:
    
    if (GPIO.input(buttonA) == 0):
        #PWM LED
        print("Button A pressed in main")
        print("Flag A: " + str(FLAG_A) + " Flag B: " + str(FLAG_B))
        if FLAG_A == True and FLAG_B == False:
            #PWM
            GPIO.output(LED_B,False)
            led.start(0)
            #FLAG_A = True
            while True:
                led.ChangeDutyCycle(currentDC % 100)
                #print(dc)
                
                if (GPIO.input(buttonA) == 0):
                    print("Button A - PWM Changed")
                    currentDC += 20
                    sleep(0.2)
                elif (GPIO.input(buttonB) == 0):
                    print("Button B - Switching from PWM to Blinking")
                    led.stop()
                    GPIO.output(LED_A, False)
                    FLAG_A = False
                    FLAG_B = True
                    break
            #GPIO.output(LED_A,True)
        elif FLAG_A == False and FLAG_B == True:
            #Blinking
            GPIO.output(LED_A,False)
            #GPIO.output(LED_B,True)
            
            sleepArr = [1, .5, .25, .1]
            sleepVar = sleepArr[0]
            endBlinking = False
            keepBlinking = False
            
            
            while endBlinking == False:
                print("endBlinking Running")
                #blinking once every second
                if sleepVar == sleepArr[0]:
            
                    for x in range(2):
                        print("Blinking " + str(sleepVar) + " " + str(x))
                        GPIO.output(LED_B, 1)
                        sleep(sleepVar)
                        GPIO.output(LED_B, 0)
                        sleep(sleepVar)
                        
                        if (GPIO.input(buttonA) == 0):
                            print("Button A pressed while full second blinking at step " + str(x))
                            keepBlinking = True
                            
                            while keepBlinking == True:
                                print("keepBlinking running in full " + str(x))
                                GPIO.output(LED_B, 1)
                                sleep(sleepVar)
                                GPIO.output(LED_B, 0)
                                sleep(sleepVar)
                                
                                if (GPIO.input(buttonA) == 0):
                                    keepBlinking = False
                                    
                        elif (GPIO.input(buttonB) == 0):
                            print("Button B pressed while blinking in 1 second")
                            endBlinking = True
                            GPIO.output(LED_A, False)
                            FLAG_A = False
                            FLAG_B = True
                            break
                            
                    #changing speed
                    sleepVar = sleepArr[1]
                
                
                #blinking once every half second
                elif sleepVar == sleepArr[1]:
            
                    for x in range(4):
                        print("Blinking " + str(sleepVar) + " " + str(x))
                        GPIO.output(LED_B, 1)
                        sleep(sleepVar)
                        GPIO.output(LED_B, 0)
                        sleep(sleepVar)
                        
                        if (GPIO.input(buttonA) == 0):
                            print("Button A pressed while half second blinking at step " + str(x))
                            keepBlinking = True
                            
                            while keepBlinking == True:
                                print("keepBlinking running in half " + str(x))
                                GPIO.output(LED_B, 1)
                                sleep(sleepVar)
                                GPIO.output(LED_B, 0)
                                sleep(sleepVar)
                                
                                if (GPIO.input(buttonA) == 0):
                                    keepBlinking = False
                                    
                        elif (GPIO.input(buttonB) == 0):
                            print("Button B pressed while blinking in 0.5 second")
                            endBlinking = True
                            GPIO.output(LED_A, False)
                            FLAG_A = False
                            FLAG_B = True
                            break

                    #changing speed
                    sleepVar = sleepArr[2]
                        
                
                    
                #blinking once every quarter second
                elif sleepVar == sleepArr[2]:
            
                    for x in range(8):
                        print("Blinking " + str(sleepVar) + " " + str(x))
                        GPIO.output(LED_B, 1)
                        sleep(sleepVar)
                        GPIO.output(LED_B, 0)
                        sleep(sleepVar)
                        
                        if (GPIO.input(buttonA) == 0):
                            print("Button A pressed while quarter second blinking at step " + str(x))
                            keepBlinking = True
                            
                            while keepBlinking == True:
                                print("keepBlinking running in quarter " + str(x))
                                GPIO.output(LED_B, 1)
                                sleep(sleepVar)
                                GPIO.output(LED_B, 0)
                                sleep(sleepVar)
                                
                                if (GPIO.input(buttonA) == 0):
                                    keepBlinking = False
                                    
                        elif (GPIO.input(buttonB) == 0):
                            print("Button B pressed while blinking in 0.25 second")
                            endBlinking = True
                            GPIO.output(LED_A, False)
                            FLAG_A = False
                            FLAG_B = True
                            break
                            
                    #changing speed
                    sleepVar = sleepArr[0]
            

            
        elif FLAG_A == False and FLAG_B == False:
            pass
        else:
            #Blinking
            GPIO.output(LED_A,False)
            GPIO.output(LED_B,True)
        
        sleep(0.2)
        
        
    if (GPIO.input(buttonB) == 0):
        print("Button B pressed in main")
              
        if FLAG_A == True and FLAG_B == False:
            FLAG_B = True
            FLAG_A = False
            sleep(0.5)
            GPIO.output(LED_A,False)
            GPIO.output(LED_B,True)
        elif FLAG_A == False and FLAG_B == True:
            FLAG_B = False
            FLAG_A = True
            sleep(0.5)
            GPIO.output(LED_B,False)
            #GPIO.output(LED_A,True)
        elif FLAG_A == False and FLAG_B == False:
            FLAG_B = True
            FLAG_A = False
            sleep(0.5)
            GPIO.output(LED_A,False)
            GPIO.output(LED_B,True)
        else:
            FLAG_A = False
            FLAG_B = True
            sleep(0.5)
            GPIO.output(LED_A,False)
            GPIO.output(LED_B,True)
        print("Flag A: " + str(FLAG_A) + " Flag B: " + str(FLAG_B)) 
    
        
GPIO.cleanup()
