"""
Streaming data consumer
"""
from datetime import datetime
from kafka import KafkaConsumer
import mysql.connector

TOPIC='toll'
DATABASE = 'tolldata'
USERNAME = 'root'
PASSWORD = '1234'

print("Connecting to the database")
try:
    connection = mysql.connector.connect(host='localhost', database=DATABASE, user=USERNAME, password=PASSWORD)
    print("Connected to database")
    cursor = connection.cursor()

    print("Connecting to Kafka")
    consumer = KafkaConsumer(TOPIC)
    print("Connected to Kafka")
    print(f"Reading messages from the topic {TOPIC}")
    for msg in consumer:

        # Extract information from kafka

        message = msg.value.decode("utf-8")

        # Transform the date format to suit the database schema
        (timestamp, vehicle_id, vehicle_type, plaza_id) = message.split(",")

        dateobj = datetime.strptime(timestamp, '%a %b %d %H:%M:%S %Y')
        timestamp = dateobj.strftime("%Y-%m-%d %H:%M:%S")

        # Loading data into the database table

        sql = "insert into livetolldata values(%s,%s,%s,%s)"
        result = cursor.execute(sql, (timestamp, vehicle_id, vehicle_type, plaza_id))
        print(f"A {vehicle_type} was inserted into the database")
        connection.commit()

except Exception as e:
    print(f"Could not connect to database or error occurred: {e}")

finally:
    if 'connection' in locals():
        connection.close()
