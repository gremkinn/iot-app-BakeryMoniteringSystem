#Import python modules
import mqtt_functions as mqtt_func

#Import required libraries/packages
import influxDB as influx
import time

#Function to start mqtt subscriber
mqtt_func.startSensorSub() 

#Variable to save last written timestamp
saved_timestamp = None

try:
    while True:
        time.sleep(5) #Delay for 5secs

        #Retrieve data received in mqtt messages from subscriptions
        temperature, humidity, pressure, timestamp = mqtt_func.callData()

        #Data validation
        if (None not in (temperature, humidity, pressure, timestamp) and saved_timestamp != timestamp):

            #Write data to influxDB
            influx.writeData(temperature, humidity, pressure, timestamp)

            #Save last written timestamp for validation
            saved_timestamp = timestamp

        else:
            #Status update for data validation failure
            print("Data is empty or has already been written.")
            
        #Data validation before writing fan status to database
        if(fan_status != None):
             influx.writeFanStatus(fan_status)

except KeyboardInterrupt:

    #Upon keyboard interrupt, end mqtt subscriptions
    mqtt_func.endSensorSub()