#Import required libraries/packages for mqtt
import paho.mqtt.client as mqtt
import time

#Create client instance & print status update
sub_client = mqtt.Client()
print("\nMQTT client object created at " + time.strftime("%H:%M:%S") + ".")

#Enable TLS with private cert
sub_client.tls_set(ca_certs="ca.pem")

#Set user account for access to broker
sub_client.username_pw_set("IoTAM_user", "bakery")

#Global variable
fan_control = None

#mqtt topic for subscriber
topic_fan = "bakery/fan_control"

#Save received data into variable & display data
def onMessage(client, userdata, message): 
    global fan_control
    fan_control = message.payload.decode()
    print("-- Received Fan Control:", fan_control)

#Function to call data for use in main
def callData():
    return fan_control

#Function to start mqtt subscriber with relevant topic
def startFanSub():
    sub_client.on_message = onMessage
    sub_client.connect("172.20.10.9", port=8883)
    sub_client.subscribe(topic_fan, qos=1)
    sub_client.loop_start()
    print("-- Subscribed to topic\n")

#Function to end mqtt subscriber
def endFanSub():
    print("Exiting...")
    sub_client.loop_stop()
    sub_client.disconnect()

