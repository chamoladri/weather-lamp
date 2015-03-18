import pywapi
import pprint

pp = pprint.PrettyPrinter(indent=4)


class webTempweather_com:
    def __init__(self, locationId):
        self.locationId = locationId


    def getTemp(self):
        self.query = pywapi.get_weather_from_weather_com(self.locationId)
        return self.query['current_conditions']['temperature']

    def feels_like(self):
        self.query = pywapi.get_weather_from_weather_com(self.locationId)
        return self.query['current_conditions']['feels_like']

    def getAllinfo(self):
        self.a = pp.pprint(self.query)
        return self.a


if __name__ == '__main__':
    # incializando la clase
    temp = webTempweather_com('ARBA0009:1:AR')
    print temp.getTemp()
    print temp.feels_like()
    print temp.getAllinfo()
