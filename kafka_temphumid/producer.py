#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#producer.py 
#https://github.com/akbarpn136/temphum/tree/master/temphum
#https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1
#https://www.pythonsheets.com/notes/python-sqlalchemy.html

#####IMPORTANT NOTE
#Be sure that zookeeper and kafak are running before running this producer script 

import time
import json
import datetime
import Adafruit_DHT
from kafka import KafkaProducer
import datetime

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'), request_timeout_ms=10000)


while True:
	#Step 1: Get the data from the sensor 
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    #Step 2: Send the data to a kafka stream called 'sensordata1'
    producer.send('sensordata1', {'temp': temperature, 'hum': humidity, 'wkt': str(datetime.datetime.utcnow())})
    #Step 3: Print to confirm collecting 
    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    #Step 4: Put the sensor to sleep for 60 seconds 
    time.sleep(10)


