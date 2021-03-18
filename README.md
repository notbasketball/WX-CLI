# WX-CLI
Welcome to WX-CLI... a command line based weather.com API parser. 

## Features
When executed with `python3 weather.py`, after it asks you for your longitude and latitude, WX-CLI will give you weather data. Such as Current Conditions, the 36 Hour Forecast, and the Extended Forecast. An expected output may look like the following:

```Enter latitude: 37.77392
Enter longitude: -122.431297
Current Weather Conditions:
  Cloudy
  Temp: 64°F
  Wind: SSE @ 8 MPH
  Wind Gust: None
  Humidity: 65%
  Feels Like: 63°F

36 Hour Forecast:
Tonight: Showers and thundershowers early, then overcast overnight with occasional rain. A few storms may be severe. Low around 35F. Winds N at 10 to 15 mph. Chance of rain 90%.
Tomorrow: Sunshine along with some cloudy intervals. High around 50F. Winds NNE at 10 to 15 mph.
Tomorrow night: Mainly clear. Low 26F. Winds ENE at 5 to 10 mph.

 5 Day Forecast:
Tomorrow: More sun than clouds | 50°F
Saturday: Abundant sunshine | 60°F
Sunday: Sunshine | 63°F
Monday: Abundant sunshine | 65°F
Tuesday: Mostly cloudy | 66°F
```

## Download/Installation

### Download
How do I download and use this?
Before you download the source code, please download the latest version of Python.
 
Windows: https://www.python.org/downloads/windows/
macOS: https://www.python.org/downloads/mac-osx/
Linux/UNIX: https://www.python.org/downloads/source/
* If you are using a Debian-based Distro just type `sudo apt install python3`
* On Arch, the command would be `sudo pacman -S python3`

### Installation
Now, at the top of this page you should see a green `Code` button. Click that, download the zip, extract wherever. Populate the .ini file as such that it is an object containing one property entitled `weathercom` (see example below). Open a terminal window in the WX-CLI folder. Type in `python3 weather.py`, enter your latitude and longitude, and you should be getting data! 

### Example config.ini
```
[WeatherCom]
API_KEY=<Your API-Key here>
```
