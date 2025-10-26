#Import required libraries/packages for bme280 sensor
import smbus2
import bme280

#Import required libraries/packages to retrieve current date & time
from datetime import datetime

#Sensor configuration
port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

#Function to retrieve readings from bme280 sensor
def getReading():

    #Retrieve a single real-time reading
    data = bme280.sample(bus, address, calibration_params)

    #Read sensor data
    temperature = data.temperature
    humidity = data.humidity
    pressure = data.pressure

    #Retrieve current date & time
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return temperature, humidity, pressure, timestamp #Return received data