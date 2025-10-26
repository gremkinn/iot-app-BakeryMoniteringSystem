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

#Global variables
temperature = None
humidity = None
pressure = None
timestamp = None
fan_status = None

#mqtt topics for subscriber
topic_temp = "bakery_sensor/temperature"
topic_humid = "bakery_sensor/humidity"
topic_press = "bakery_sensor/pressure"
topic_time = "bakery_sensor/timestamp"
topic_fan = "bakery/fan_status"

i = 0 #Variable for iteration

#Save received data into relevant variables & display data
def onMessage(client, userdata, message): 
    global i, temperature, pressure, humidity, timestamp, fan_status

    if message.topic == topic_time:
        timestamp = message.payload.decode()
        print("-- Timestamp:", timestamp)
        
    elif message.topic == topic_temp:
        temperature = float(message.payload.decode())
        print(f"-- Temperature:", temperature, "°C")
    
    elif message.topic == topic_humid:
        humidity = float(message.payload.decode())
        print(f"-- Humidity:", humidity, "%")

    elif message.topic == topic_press:
        pressure = float(message.payload.decode())
        print(f"-- Pressure:", pressure, "hPa")

    elif message.topic == topic_fan:
        fan_status = message.payload.decode()
        print(f"-- Fan Status:", fan_status)
    
    i += 1 

    if i == 5:
        print("") #Print new line when one set of data has been received
        i = 0

#Function to call data for use in main
def callData():
    return temperature, humidity, pressure, timestamp, fan_status

#Function to start mqtt subscriber with relevant topics
def startSensorSub():
    mqtt_client.on_message = onMessage
    mqtt_client.connect("172.20.10.9", port=8883)
    mqtt_client.subscribe(topic_temp, qos=1)
    mqtt_client.subscribe(topic_humid, qos=1)
    mqtt_client.subscribe(topic_press, qos=1)
    mqtt_client.subscribe(topic_time, qos=1)
    mqtt_client.subscribe(topic_fan, qos=1)
    mqtt_client.loop_start()
    print("-- Subscribed to topics\n")

#Function to end mqtt subscriber
def endSensorSub():
    print("Exiting...")
    mqtt_client.loop_stop()
    mqtt_client.disconnect()


    

