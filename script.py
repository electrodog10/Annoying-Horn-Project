import webiopi

GPIO = webiopi.GPIO

HORN = 11 # GPIO pin using BCM numbering


# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the horn to output
    GPIO.setFunction(HORN, GPIO.OUT)


# loop function is repeatedly called by WebIOPi 
def loop():

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(HORN, GPIO.LOW)