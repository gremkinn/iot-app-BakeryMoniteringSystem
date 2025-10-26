#Import required libraries/packages for RESTful api
from flask import Flask

#Import required libraries/packages for mqtt
import time
import paho.mqtt.client as mqtt

#Create client instance & print status update
mqtt_client = mqtt.Client() 
print("\nMQTT client object creted at " + time.strftime("%H:%M:%S") + ".")

#Enable TLS with private cert
mqtt_client.tls_set(ca_certs="ca.pem")

#Set user account for access to broker
mqtt_client.username_pw_set("IoTAM_user", "bakery")

#mqtt topic for publisher
topic_fan = "bakery/fan_control"

#Function to start mqtt publisher and send a message
def fanPub(payload):

    #Connect to broker
    mqtt_client.connect("172.20.10.9", port=8883)
    print("\n-- Connected to MQTT broker")

    #Start network loop
    mqtt_client.loop_start()

    try:
        #Publish messages
        mqtt_client.publish(topic_fan, payload)
        
        #Print result
        print("-- Published Fan Control:", payload)
    
    except:
        print("-- Error publishing!")
    
    else:
        #Stop network loop
        mqtt_client.loop_stop()
        mqtt_client.disconnect()
        print("-- Disconnected from broker")  

#Create new flask instance
app = Flask(__name__) 

@app.route('/fan_off') #Publish relevant message when this HTTP url is accessed
def fan_off():
    fanPub("OFF")
    return "-- Published Fan Control: OFF"
    
@app.route('/fan_on') #Publish relevant message when this HTTP url is accessed
def fan_on():
    fanPub("ON")
    return "-- Published Fan Control: ON"

app.run(host='0.0.0.0', port=5000, debug=True) #Start flask server

