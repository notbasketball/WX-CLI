import urllib, urllib.request
import json

class WeatherMan:
    base_url = 'https://api.weather.com/'

    def __init__(self):
        self.apikey = None
        self.params = {
            'lang': 'en-US',
            'units': 'e'
        }

    def get_request(self, url, params = { }):
        # send api key
        params['apiKey'] = self.apikey

        # add url params
        url_full = self.base_url + url + '?' + urllib.parse.urlencode(params)

        # the http request itself
        req = urllib.request.Request(url_full, headers = {
            'User-Agent': 'Mozilla/5.0 (Mac OS X 11.2.1)'
        })

        # open a connection, read data & close
        conn = urllib.request.urlopen(req)
        data = conn.read()
        conn.close()

        return data

    def get_request_json(self, url, params = { }):
        return json.loads(self.get_request(url, params))

    def set_key(self, key):
        self.apikey = key

    def set_lang(self, lang):
        self.params.lang = lang

    def set_units(self, units):
        self.params.units = units

    def get_currents_on_demand(self, lat, lon, params = { }):
        return self.get_request_json('v2/turbo/vt1observation', {
            'apiKey': self.apikey,
            'geocode': str(lat) + ',' + str(lon),
            'language': self.params['lang'],
            'units': self.params['units'],
            'format': 'json'
        })

    def get_five_day(self, lat, lon, params = { }):
        return self.get_request_json('v1/geocode/{0}/{1}/forecast/daily/5day.json'.format(lat, lon), {
            'apiKey': self.apikey,
            'language': self.params['lang'],
            'units': self.params['units']
        })
