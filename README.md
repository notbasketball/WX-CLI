# WX-CLI
Welcome to WX-CLI... a command line based weather.com API parser. 

## Features
When executed with `python3 weather.py`, after it asks you for your longitude and latitude, WX-CLI will give you weather data. Such as Current Conditions, 6 Hour Forecast, the 36 Hour Forecast, and the Extended Forecast. An expected output may look like the following:

![carbon](https://cdn.discordapp.com/attachments/731261406091018335/826218797961707550/unknown.png)

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
