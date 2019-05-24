#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#consumer 
#https://github.com/akbarpn136/temphum/tree/master/temphum
#https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

#####IMPORTANT NOTE
#Be sure that zookeeper and kafak are running before running this producer script 
#and then that the PRODUCER script is also running, DUH 


import json
from kafka import KafkaConsumer

#Step 1: Load the consumer / e.g., kafka stream called 'sensordata1'
consumer = KafkaConsumer('sensordata1', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('ascii')))

#Step 2: Print out the data for testing purposes 
for message in consumer:
	print (message.temp)
	print (message.hum)
	print (message.wkt)

#Step 3: Send the data to mysql / postgresql / mongodb, etc.... 