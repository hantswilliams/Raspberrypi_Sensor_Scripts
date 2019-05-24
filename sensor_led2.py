#NOTE - for this we are utilizing PI GPIO - GND along with GPIO #18 
#ALONG WITH A 300 OHM RESISTOR 

import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(18, GPIO.OUT) ## Setup GPIO Pin 18 to OUT

##Define a function named Blink()
def Blink(numTimes,speed):
    for i in range(0,numTimes):## Run loop numTimes
        print "Iteration " + str(i+1)## Print current loop
	GPIO.output(18,1)## Switch on pin 18
	time.sleep(speed)## Wait
	GPIO.output(18,0)## Switch off pin 18
	time.sleep(speed)## Wait
    print "Done" ## When loop is complete, print "Done"
    GPIO.cleanup()

## Ask user for total number of blinks and length of each blink
iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink(seconds): ")

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(int(iterations),float(speed))
