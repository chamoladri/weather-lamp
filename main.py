
import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)



#pp.pprint(buneosAires)
#print buneosAires

#print buneosAires['current_conditions']['temperature']


class webTempweather_com:
    
    def __init__(self,locationId):
        self.locationId = locationId
      
    def getTemp(self):
        self.buenos = pywapi.get_weather_from_weather_com(self.locationId)
        return self.buenos['current_conditions']['temperature']
         
    def getAllinfo(self):
        self.a = pp.pprint(self.buenos)
        return self.a     


if __name__ == '__main__':     
    
    #incializando la clase 
    temp=webTempweather_com('ARBA0009:1:AR')
    print temp.getTemp()
    print temp.getAllinfo()