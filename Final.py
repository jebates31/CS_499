import time
import sys 
import requests
import csv
import grovepi
import math
import json
from grove_rgb_lcd import *
from time import sleep
from datetime import datetime, date, time, timedelta, timezone

#Light Sensor to analog port A0
light_sensor = 0
# Connect the LED to digital port D5 D6 and D7 

blue_led = 6
green_led = 5
red_led = 7

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 4  # The Sensor goes on digital port 4.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

weather_on = False
outputData = 0



# Turn on LED once sensor exceeds threshold resistance
threshold = 20

grovepi.pinMode(light_sensor,"INPUT")
[temp,humidity] = grovepi.dht(sensor,blue)

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K added 1 to stop divsion by 0 error
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value +1

        if resistance > threshold:
            # Send HIGH to switch on LED
            weather_on = True
        else:
            # Send LOW to switch off LED
            weather_on = False 

        print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))
        time.sleep(.5)

    
        # This example uses the blue colored sensor. 
        # The first parameter is the port, the second parameter is the type of sensor.
        
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            
            temp = ((temp/5.0)*9)+32
            
        t = str(temp)
        h = str(humidity)
        time.sleep(.5)
        outputData = {}
        outputData['weather'] = []
        outputData['weather'].append({
                    'temperature': t,
                    'humidity': h
                        })
    
        print(temp)
        print(weather_on)
    
        while weather_on == True: 
                
            if temp > 60.0 and temp < 85.0:
                    grovepi.digitalWrite(green_led,1)
            elif temp > 85.0 and temp < 95.0:
                    grovepi.digitalWrite(blue_led,1)
            elif temp < 95.0:
                    grovepi.digitalWrite(red_led,1)
            elif humidity < 80.0:
                    grovepi.digitalWrite(blue_led,1) and grovepi.digitalWrite(green_led,1)
            else:
                    # Send LOW to switch off LED
                    grovepi.digitalWrite(blue_led,0)
                    grovepi.digitalWrite(red_led,0)
                    grovepi.digitalWrite(green_led,0)
            
            #create and send data to json file 
            with open ('outputData.json', 'w') as outfile: 
                json.dumps(outputData, outfile)

            LOCATION = "40.7608° N, 111.8910° W"
            RAPIDAPI_KEY  = "<6213a469f242743e8d0ca347ef211780>"
            def trigger_api():
             url = "https://dark-sky.p.rapidapi.com/" + LOCATION
            querystring = {"lang":"en","units":"auto"}
            headers = {
                     'x-rapidapi-host': "dark-sky.p.rapidapi.com",
                     'x-rapidapi-key': RAPIDAPI_KEY
                     }
            response = requests.request("GET", url, headers=headers, params=querystring)
            if(200 == response.status_code):
                return json.loads(response.text)
            else:
                return None
                if __name__ == "__main__":
                    try: 
                        api_response = trigger_api()
                        current_date = datetime.fromtimestamp(api_response["currently"]["time"])
                        with open('Weather_Data-' + current_date.strftime("%m-%d-%Y") +  '.csv', 'w',newline='') as csv_file:
                         csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(["Parameter","Time", "Value"])  
                        for record in api_response["daily"]["data"]:
                            try: 
                                time     = record["time"]
                                tempH     = record["temperatureHigh"]
                                tempL     = record["temperatureLow"]
                                humidity = int(record["humidity"] * 100)
                                cloud    = int(record["cloudCover"] * 100)
                              
                                time_of_day = datetime.fromtimestamp(time).strftime("%Y%m%d")
                                print("Adding Record for " + time_of_day)
                                csv_writer.writerow(["Temp High",time_of_day,tempH])
                                csv_writer.writerow(["Temp Low",time_of_day,tempL])
                                csv_writer.writerow(["Humidity",time_of_day,humidity])
                                csv_writer.writerow(["Cloud Cover",time_of_day,cloud])  
                              
                            except TypeError as e:
                              print(e)
                              print("Type Error...Ignoring")
                              
                            except csv.Error as e:
                              
                              print(e)
                              print("CSV Error...Ignoring")
          
                            csv_file.close()
                    except Exception as e:
                        sys.exit(e)
               
 