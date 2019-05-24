#!/usr/bin/python
import sys
import Adafruit_DHT

#http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
#the 11 in the code below stands for dht11, versus if using dht22 it would be 22 instead;
#the 4 stands for GPIO 4 / on the circuit board 
#on the DHT11 chip: left side (+) = 3v; middle = GPIO4; right side (-) = ground 

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
