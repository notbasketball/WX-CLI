import urllib, urllib.request
import json

class WeatherMan:
    base_url = 'http://api.weather.com/'

    def __init__(self):
        self.apikey = None
        self.params = {
            'language': 'en-US',
            'units': 'e'
        }

    def get_request(self, url, params = { } , blacklist = ()):
        # send api key
        params['apiKey'] = self.apikey
        params['language'] = self.params['language']
        params['units'] = self.params['units']
        for x in blacklist:
            params.pop(x, None)

        # add url params
        url_full = self.base_url + url + '?' + urllib.parse.urlencode(params)
        # the http request itself
        req = urllib.request.Request(url_full)

        # open a connection, read data & close
        conn = urllib.request.urlopen(req)
        data = conn.read()
        conn.close()

        return data

    def get_request_json(self, url, params = { }, blacklist = ()):
        return json.loads(self.get_request(url, params, blacklist))

    def set_key(self, key):
        self.apikey = key

    def set_lang(self, lang):
        self.params.lang = lang

    def set_units(self, units):
        self.params.units = units

    def get_currents_on_demand(self, lat, lon):
        return self.get_request_json('v2/turbo/vt1observation', {
            'geocode': str(lat) + ',' + str(lon),
            'format': 'json'
        }, ())
    def get_hourly(self, lat, lon):
        return self.get_request_json('v1/geocode/{0}/{1}/forecast/hourly/6hour.json'.format(lat, lon), { }, ())

    def get_five_day(self, lat, lon):
        return self.get_request_json('v1/geocode/{0}/{1}/forecast/daily/5day.json'.format(lat, lon), { }, ())
    def alerts(self, lat, lon):
        try:
            return self.get_request_json('v3/alerts/headlines'.format(lat, lon), {
                'geocode': str(lat) + ',' + str(lon),
                'format': 'json'
            }, ('units', ))
        except:
            return None