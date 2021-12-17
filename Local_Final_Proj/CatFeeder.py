from GmailWrapper import GmailWrapper
from w1thermsensor import W1ThermSensor
from gpiozero import Button
import RPi.GPIO as GPIO
import time
import email

HOSTNAME = 'imap.gmail.com'
USERNAME = 'samandoskarscatfeeder@gmail.com'
PASSWORD = 'itsalmostover'

gmailWrapper = GmailWrapper()

def buttonPressed():
    if button.is_pressed:
        print("Button pressed")
        feed()

button = Button(21)
button.when_pressed = buttonPressed

def feedByGmail():
    ids = gmailWrapper.getIdsBySubject('feed cats')
    
    if(len(ids) > 0):
        try:
            name = getSender(gmailWrapper)
            print(f"Feed request sent from: {name}")
            feed()
            print("Cat Fed ^-^")
            gmailWrapper.markAsRead(ids)
        except:
            print("Failed to feed cats, they're starvingggg")
    else:
        print("No requests - Feeding")

def feed():
    # let the library know where we've connected our servo to the Pi
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

    try:
        servo = GPIO.PWM(18, 50)
        servo.start(12.5)

        # spin left, right, then left again rather than in a continuous circle
        # to prevent the food from jamming the servo
        for index in range(0, 3):
            dutyCycle = 2.5 if (index % 2 == 0) else 12.5
            servo.ChangeDutyCycle(dutyCycle)
            time.sleep(0.8)
        
    finally:
        # always cleanup after ourselves
        servo.stop()
        # GPIO.cleanup()
        
def getSender(gw):
    gw.setFolder('INBOX')
    messages = gw.server.search(['UNSEEN'])
    print(messages)
    bytes_msg = gw.server.fetch(messages[0], ["RFC822"])
    msg = email.message_from_bytes(bytes_msg[messages[0]][b"RFC822"])
    sender = msg['From'].split('<')
    email_name = sender[1].replace('>', '')
    return(email_name)

def getTemp():
    ids = gmailWrapper.getIdsBySubject('get temp')
    
    
    if(len(ids) > 0):
        print(f"Getting UIDs: {ids}")
        GPIO.setwarnings(False)
        sensor = W1ThermSensor()
        temp = sensor.get_temperature()
        temp = round(temp,2)
        
        name = getSender(gmailWrapper)
        
        print(f"Temperature request sent from: {name}")
        print(f"Temperature reading: {temp}")
        # gmailWrapper.email_back(message, temp, uid)
        gmailWrapper.markAsRead(ids)
        """
        except:
            print("Failed to get temp")
        """
    else:
        print("No requests - Temperature")
            



if __name__ == '__main__':
    feedByGmail()
    # kick off the feeding process (move the servo)
    #feed()
    # we now use our new feedByGmail method to handle the feeding
    #feedByGmail()