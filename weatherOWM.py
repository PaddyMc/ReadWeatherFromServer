#! python3

# weatherOWM.py - Finds the weather for certain areas
# reads from a file specified by the user

# website the information is scraped from: http://openweathermap.org/find?q=Dublin%2Cirl
# to run correctly pip install pyowm then run from the command line specifing a filename

import pyowm,sys

owm = pyowm.OWM('b60b126a78724caf12607df35fde3f51')

def weatherConditions(city):
    weather = owm.weather_at_place(city)
    weatherInfo = weather.get_weather()
    
    temp = weatherInfo.get_temperature('celsius')
    tempMin = temp['temp_min']
    skyConditions = weatherInfo.get_status()
    humidity = weatherInfo.get_humidity()

    return(tempMin,skyConditions,humidity)

if __name__ == '__main__':
    try:
        print('File being used: '+ sys.argv[1]+ '\n')
        with open(sys.argv[1]) as cities:
            for city in cities:
                weather = weatherConditions(city)                
                print(city)
                print('~Temperature: ' + str(weather[0]) + " celcius")
                print('~Sky Conditions: ' + str(weather[1]))
                print('~Humidity: ' + str(weather[2])+ '%' + '\n\n')
                
        cities.close()
    except:
        print("Please specify a filename")
