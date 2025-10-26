#Import required libraries/packages for influxDB
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import time

#InfluxDB credentials
USER = 'root'
PASSWORD = 'root'
DBNAME = 'bakery'
HOST = 'localhost'
PORT = 8086

#InfluxDB client
dbclient = InfluxDBClient(HOST, PORT, USER, PASSWORD, DBNAME)

#Function to retrieve data and write to database
def writeSensorData(temperature, humidity, pressure, timestamp):
    data_point = getSensorData(temperature, humidity, pressure, timestamp)
    dbclient.write_points(data_point)
    print("Sensor data has been successfully written to influxDB.")

#Function to create dictionary with data values
def getSensorData(temperature, humidity, pressure, timestamp):
    now = time.gmtime()

    pointValues = [
        {
            "time": time.strftime("%Y-%m-%d %H:%M:%S", now),
            "measurement": 'bakery_environment',
            "tags": {
                "nodeId": "node_1",
            },
            "fields": {
                "temperature": temperature,
                "humidity": humidity,
                "pressure": pressure
            },
        }
    ]

    return pointValues

def writeFanStatus(status):
    data_point = getFanData(status)
    dbclient.write_points(data_point)
    print("Fan status has been successfully written to influxDB.")

#Function to create dictionary with data values
def getFanData(status):
    fixed_time = "2025-01-01 00:00:00"

    pointValues = [
        {
            "time": fixed_time,
            "measurement": 'fan_status',
            "tags": {
                "nodeId": "node_1",
            },
            "fields": {
                "fan_status": status,
            },
        }
    ]

    return pointValues

