#Import required libraries/packages for mqtt
import paho.mqtt.client as mqtt
import time

#Create client instance & print status update
pub_client = mqtt.Client()
print("\nMQTT client object created at " + time.strftime("%H:%M:%S") + ".")

#Enable TLS with private cert
pub_client.tls_set(ca_certs="ca.pem")

#Set user account for access to broker
pub_client.username_pw_set("IoTAM_user", "bakery")

#mqtt topics for publisher
topic_temp = "bakery_sensor/temperature"
topic_humid = "bakery_sensor/humidity"
topic_press = "bakery_sensor/pressure"
topic_time = "bakery_sensor/timestamp"
topic_fan = "bakery/fan_status"

#Function to start mqtt publisher and send messages for sensor readings
def sensorPub(temperature, humidity, pressure, timestamp):

    #Format payloads
    payload_temp = "%.2f" % temperature
    payload_humid = "%.2f" % humidity
    payload_press = "%.2f" % pressure
    payload_time = timestamp

    #Connect to broker
    pub_client.connect("172.20.10.9", port=8883)
    print("\n-- Connected to MQTT broker")

    #Start network loop
    pub_client.loop_start()
   
    try:
        #Publish messages
        pub_client.publish(topic_temp, payload_temp)
        pub_client.publish(topic_humid, payload_humid)
        pub_client.publish(topic_press, payload_press)
        pub_client.publish(topic_time, payload_time)

        #Print results
        print("-- Published")
        print("-- Timestamp:", str(timestamp))
        print("-- Temperature:", payload_temp,"°C")
        print("-- Humidity:", payload_humid, "%")
        print("-- Pressure:", payload_press,"hPa")

    except:
        print("-- Error publishing!")

    else:

        #Stop network loop
        pub_client.loop_stop()
        pub_client.disconnect()
        print("-- Disconnected from broker") 


#Function to start mqtt publisher and send messages for fan status
def fanStatusPub(status):

    #Assign payload
    payload_fan = status

    #Connect to broker
    pub_client.connect("172.20.10.9", port=8883)
    print("\n-- Connected to MQTT broker")

    #Start network loop
    pub_client.loop_start()
   
    try:
        #Publish message
        pub_client.publish(topic_fan, payload_fan)

        #Print results
        print("-- Published Fan Status:", status)

    except:
        print("-- Error publishing!")

    else:

        #Stop network loop
        pub_client.loop_stop()
        pub_client.disconnect()
        print("-- Disconnected from broker") 