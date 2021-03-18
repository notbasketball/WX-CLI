import configparser
from wman import WeatherMan

# Load API Keys and initialize configparser
config = configparser.ConfigParser()
config.read('config.ini')

weatherman = WeatherMan()
weatherman.set_key(config["WeatherCom"]["API_KEY"])

lat, lon = input("Enter latitude: "), input("Enter longitude: ")
print("")
cod = weatherman.get_currents_on_demand(lat, lon)["vt1observation"]

five_day = weatherman.get_five_day(lat, lon)["forecasts"]
twelve_hour = five_day[0]
twenty_four_hour = five_day[1]
thirty_six_hour = five_day[2]

print("Current Weather Conditions:")
print("\t" + str(cod["phrase"]))
print("\t" + "Temp: ".ljust(12) + str(cod["temperature"]) + "°F") 
print("\t" + "Wind: ".ljust(12) + str(cod["windDirCompass"]) + " @ " + str(cod["windSpeed"]) + " MPH")

if "gust" in cod: 
    print("\t" + "Wind Gust: ".ljust(12) + str(cod["gust"]))

print("\t" + "Humidity: ".ljust(12) + str(cod["humidity"]) + "%")
print("\t" + "Feels Like: ".ljust(12) + str(cod["feelsLike"]) + "°F")
print("")
print("36 Hour Forecast:")

# forecasts.0.day = only in day time
# forecasts.0.night = always

if "daypart_name" in twelve_hour:
    print("\t" + str(twelve_hour["daypart_name"]))

if "day" in twelve_hour:
    print("\t" + str(twelve_hour["day"]["daypart_name"]) + ": " + str(twelve_hour["day"]["narrative"]))

print("\t" + str(twelve_hour["night"]["daypart_name"]) + ": " + str(twelve_hour["night"]["narrative"]))
# twelvehour = today or tonight depending on the day, twentyFourhour = tonight or tomorrow depending on the day
if "day" in twenty_four_hour: 
    if "day" not in twelve_hour:
        print("\t" + str(twenty_four_hour["day"]["daypart_name"]) + ": " + str(twenty_four_hour["day"]["narrative"]))
    print("\t" + str(twenty_four_hour["night"]["daypart_name"]) + ": " + str(twenty_four_hour["night"]["narrative"]))
else:
    print(str(twenty_four_hour["day"]["daypart_name"]) + ": " + str(twenty_four_hour["day"]["narrative"]))
    print(str(twenty_four_hour["night"]["daypart_name"]) + ": " + str(twenty_four_hour["night"]["narrative"]))
# 4pm tonight, tomorrow, tomorrowNight 
# line 45 = 8am today, tonight, Tomorrow
print("")
print("5 Day Forecast:")
for days in range(0, 6):
    if (days < len(five_day)) and ("day" in five_day[days]):
        print("\t" + 
            str(five_day[days]["day"]["daypart_name"] + ": ").ljust(15) +
            str(five_day[days]["day"]["shortcast"] + " | ").rjust(30)   + 
            str(five_day[days]["day"]["temp"])          + "°F"
        )