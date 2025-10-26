#Import required libraries/packages for GPIO pin control
import RPi.GPIO as GPIO
import time

#Import mqtt publisher module
import pub_functions as pub

#GPIO pin assignment
led_pin = 17
buzzer_pin = 27
relay_pin = 21

#Configure GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(buzzer_pin,GPIO.OUT)
GPIO.setup(relay_pin,GPIO.OUT)

#Function to run buzzer & LED light when pressure is out of range
def pressure_response():
    #Light & buzzer turn on & off 3 times to signal that pressure level is out of range
    for i in range(0,6): 
        GPIO.output(led_pin,GPIO.HIGH)
        GPIO.output(buzzer_pin,GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(led_pin,GPIO.LOW)
        GPIO.output(buzzer_pin,GPIO.LOW)
        time.sleep(0.25)

#Function to run buzzer & LED light when temperature is out of range
def temperature_response():
    #Light & buzzer turn on & off 5 times to signal that temperature level is out of range
    for temp in range(0,5):
        GPIO.output(led_pin,GPIO.HIGH)
        GPIO.output(buzzer_pin,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_pin,GPIO.LOW)
        GPIO.output(buzzer_pin,GPIO.LOW)
        time.sleep(0.5)
    
#Function to turn on fan
def fan_on():
    GPIO.output(relay_pin,GPIO.HIGH)
    print("-- Fan is turned on.")
    pub.fanStatusPub("ON")

#Function to turn off fan
def fan_off():
    GPIO.output(relay_pin,GPIO.LOW)
    print("-- Fan is turned off.")
    pub.fanStatusPub("OFF")

#Function to run buzzer & LED light when humidity is out of range
def humidity_response(): 
    #Light & buzzer turn oh & off 6 times to signal that humidity level is out of range
    for i in range(0,3): 
        GPIO.output(led_pin,GPIO.HIGH)
        GPIO.output(buzzer_pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_pin,GPIO.LOW)
        GPIO.output(buzzer_pin,GPIO.LOW)
        time.sleep(1)
