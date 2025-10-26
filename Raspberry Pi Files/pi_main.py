#Import python modules
import system_response as sys_res
import sensor_functions as sensor
import pub_functions as pub_func
import sub_functions as sub_func

#Import time module
import time

#Function to start mqtt subscriber for fan control
sub_func.startFanSub()

try:
    while True:

        #Retrieve data received in mqtt message from subscription
        fan_control = sub_func.callData()

        #Check received data and toggle fan
        if(fan_control == "ON"):
            sys_res.fan_on()
        elif(fan_control == "OFF"):
            sys_res.fan_off()

        #Get reading from bme280 sensor
        temperature, humidity, pressure, timestamp = sensor.getReading()

        #Publish readings to mqtt channel
        pub_func.sensorPub(temperature, humidity, pressure, timestamp)

        #System responses start----------------------------------------------
        #Checks if the readings received from the sensor are within range and if not,
        #to respond accordingly

        pressure = float(pressure)
        temperature = float(temperature)
        humidity = float(humidity)

        #Pressure check & response
        if(pressure < 1006.5 or pressure > 1006.95):

            if(pressure < 1006):
                print(f"\n**Warning: Pressure is too low at {pressure:.2f}hPa.")
            elif(pressure > 1006.95):
                print(f"\n**Warning: Pressure is too high at {pressure:.2f}hPa.")
                
            sys_res.pressure_response()
            
        #Temperature check & response
        if(temperature > 29):
            print(f"**Warning: Temperature is too high at {temperature:.2f}°C.")
            sys_res.fan_on()
            sys_res.temperature_response()

        elif(temperature < 24):
            print(f"**Warning: Temperature is too low at {temperature:.2f}°C.")

        elif(27 <= temperature <= 28):
            sys_res.fan_off()

        #Humidity check & response
        if(humidity < 55 or humidity > 65): #Note for demo: Breathing on it raises the level by more than 10%

            if(humidity < 53):
                print(f"**Warning: Humidity is too low at {humidity:.2f}%.")
            elif(humidity > 65):
                print(f"**Warning: Humidity is too high at {humidity:.2f}%.")

            sys_res.humidity_response()

        #System responses end----------------------------------------------

        time.sleep(5) #Delay for 5secs

except KeyboardInterrupt:

    #Upon keyboard interrupt, end mqtt subscription
    sub_func.endFanSub()


    


    
    


