import configparser
import time
from wman import WeatherMan

# Load API Keys and initialize configparser
config = configparser.ConfigParser()
config.read('config.ini')

weatherman = WeatherMan()
weatherman.set_key(config["WeatherCom"]["API_KEY"])
hour = time.localtime()
lat, lon = input("Enter latitude: "), input("Enter longitude: ")
print("")
alert = weatherman.alerts(lat, lon)
cod = weatherman.get_currents_on_demand(lat, lon)["vt1observation"]
hourly = weatherman.get_hourly(lat, lon)["forecasts"]
five_day = weatherman.get_five_day(lat, lon)["forecasts"]
twelve_hour = five_day[0]
twenty_four_hour = five_day[1]
thirty_six_hour = five_day[2]


print("Updated at: " + str(hour.tm_year) + "-" + str(hour.tm_mon).zfill(2) + "-" + str(hour.tm_mday).zfill(2) + " // " + str(hour.tm_hour).zfill(2) + ":" + str(hour.tm_min).zfill(2))
print("WX-CLI v1.5.1")
if alert != None:
    print("")
    print("Alerts:")
    for x in alert["alerts"]:
        print("\t" + x["headlineText"])
    print("")
print("Current Weather Conditions:")
print("\t" + str(cod["phrase"]))
print("\t" + "Temp: ".ljust(12) + str(cod["temperature"]) + "°F") 
print("\t" + "Wind: ".ljust(12) + cod["windDirCompass"] + " @ " + str(cod["windSpeed"]) + " MPH")

if "gust" in cod: 
    print("\t" + "Wind Gust: ".ljust(12) + str(cod["gust"]))

print("\t" + "Humidity: ".ljust(12) + str(cod["humidity"]) + "%")
print("\t" + "Feels Like: ".ljust(12) + str(cod["feelsLike"]) + "°F")
print("")
print("6 Hour Forecast:")
for getHourly in range(0, 6):
    if (getHourly < len(hourly)) and (hourly[getHourly]["pop"] > 30):
        print("\t" + "Hour " + (str((hour.tm_hour + getHourly + 1) % 24) + ": ").ljust(10) + 
            (hourly[getHourly]["phrase_32char"] + " | ").rjust(20) +
            str(hourly[getHourly]["temp"]) + "°F" + " | " + "Chance of " + (hourly[getHourly]["precip_type"]) + ": " + str(hourly[getHourly]["pop"]) + "%"
        )
    else: 
        print("\t" + "Hour " + (str((hour.tm_hour + getHourly + 1) % 24) + ": ").ljust(10) + 
            (hourly[getHourly]["phrase_32char"] + " | ").rjust(20) +
            str(hourly[getHourly]["temp"]) + "°F"
        )
print("")
print("36 Hour Forecast:")

# forecasts.0.day = only in day time
# forecasts.0.night = always
if "day" in twelve_hour:
    print("\t" + twelve_hour["day"]["daypart_name"] + ": " + twelve_hour["day"]["narrative"])
    print("\t" + twelve_hour["night"]["daypart_name"] + ": " + twelve_hour["night"]["narrative"])
    print("\t" + twenty_four_hour["day"]["daypart_name"] + ": " + twenty_four_hour["day"]["narrative"])
else:
    print("\t" + twelve_hour["night"]["daypart_name"] + ": " + twelve_hour["night"]["narrative"])
    print("\t" + twenty_four_hour["day"]["daypart_name"] + ": " + twenty_four_hour["day"]["narrative"])
    print("\t" + twenty_four_hour["night"]["daypart_name"] + ": " + twenty_four_hour["night"]["narrative"])
print("")
print("5 Day Forecast:")
for days in range(1, 6):
    if (days < len(five_day)) and ("day" in five_day[days]) and (five_day[days]["day"]["pop"] > 30):
        print("\t" + 
            (five_day[days]["day"]["daypart_name"] + ": ").ljust(15) +
            (five_day[days]["day"]["shortcast"] + " | ").rjust(30) + 
            str(five_day[days]["day"]["temp"])          + "°F" + " / " + str(five_day[days]["night"]["temp"]) + "°F" + " | Chance of " + (five_day[days]["day"]["precip_type"]) + ": " + str(five_day[days]["day"]["pop"]) + "%"
        )   
    else: 
        print("\t" + 
        (five_day[days]["day"]["daypart_name"] + ": ").ljust(15) +
        (five_day[days]["day"]["shortcast"] + " | ").rjust(30) + 
        str(five_day[days]["day"]["temp"])          + "°F" + " / " + str(five_day[days]["night"]["temp"]) + "°F"
        )
input("\n" + "Press enter to exit")
