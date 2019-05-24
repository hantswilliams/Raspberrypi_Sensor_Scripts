#https://medium.com/hacking-datascience/sqlalchemy-python-tutorial-abcc2ec77b57

import sqlalchemy as db


engine = db.create_engine('mysql+mysqldb://sensoruser:46566656@localhost/sensordata')
connection = engine.connect()
metadata = db.MetaData()

rawdata = db.Table(
   'rawdata4', metadata, 
   db.Column('id', db.Integer(), primary_key = True), 
   db.Column('raw_temp', db.String(255)), 
   db.Column('raw_humidity', db.String(255)),
   #db.Column('rawdatetime', db.String(255)),
   db.Column('raw_datetime', db.DateTime),
)

metadata.create_all(engine) #creates the table in sensordata


print ("DONE")
