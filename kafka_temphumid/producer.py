#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#producer.py 
#https://github.com/akbarpn136/temphum/tree/master/temphum
#https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1


#####IMPORTANT NOTE
#Be sure that zookeeper and kafak are running before running this producer script 

import time
import json
import datetime
import Adafruit_DHT
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'), request_timeout_ms=10000)


while True:
	#Step 1: Get the data from the sensor 
    humidity, temperature = Adafruit_DHT.read_retry(22, 22)
    #Step 2: Send the data to a kafka stream called 'sensordata1'
    producer.send('sensordata1', {'temp': temperature, 'hum': humidity, 'wkt': str(datetime.datetime.now())})
    #Step 3: Put the sensor to sleep for 60 seconds 
    time.sleep(60)
