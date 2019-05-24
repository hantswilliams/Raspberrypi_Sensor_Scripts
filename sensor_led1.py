#Note - for running this, we are connecting the PI via GPIO to a GND, and 
#GPIO #18. In addition, utilizing  a 300 ohm resistor 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


print "LED on"

GPIO.output(18,GPIO.HIGH)
time.sleep(1)

print "LED off"
GPIO.output(18,GPIO.LOW)
