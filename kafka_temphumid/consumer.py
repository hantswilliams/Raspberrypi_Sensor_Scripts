#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#consumer 
#https://github.com/akbarpn136/temphum/tree/master/temphum
#https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1
#https://www.pythonsheets.com/notes/python-sqlalchemy.html

#####IMPORTANT NOTE
#Be sure that zookeeper and kafak are running before running this producer script 
#and then that the PRODUCER script is also running, DUH 


import json
from kafka import KafkaConsumer
from datetime import datetime

import sqlalchemy as db 
engine = db.create_engine('mysql+mysqldb://sensoruser:46566656@localhost/sensordata')



#Step 1: Load the consumer / e.g., kafka stream called 'sensordata1'
consumer = KafkaConsumer('sensordata1', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('ascii')))

#Step 2: Print out the data for testing purposes 
for message in consumer:

	values = message.value

	temperature = str(values['temp'])
	humidity = str(values['hum'])
	datetime = str(values['wkt'])
	#now = datetime.now()
	#datetime = now.strftime('%Y-%m-%d %H:%M:%S')

	print (values)
	print (temperature)
	print (humidity)
	print (datetime)

#Step 3: Send the data to mysql / postgresql / mongodb, etc.... 

	#query = db.insert(rawdata).values(raw_temp=temperature, raw_humidity=humidity, rawdatetime=datetime)
	#ResultProxy = connection.execute(query)

	# insert a raw
	
	#engine.execute('INSERT INTO rawdata3 (raw_temp, raw_humidity, rawdatetime) VALUES ('+ temperature
        #        + ',' + humidity + ',' + datetime  + ')')

	engine.execute('INSERT into rawdata(raw_temp, raw_humidity, raw_datetime) values(%s, %s, %s)', (temperature, humidity,datetime))

	print ("succesfully added to mySQL")


