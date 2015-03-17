
import pywapi
import pprint

pp = pprint.PrettyPrinter(indent=4)

buneosAires = pywapi.get_weather_from_weather_com('ARBA0009:1:AR')

#pp.pprint(buneosAires)
#print buneosAires

print buneosAires['current_conditions']['temperature']
print buneosAires['current_conditions']['temperature']
print buneosAires['current_conditions']['temperature']
print buneosAires['current_conditions']['temperature']