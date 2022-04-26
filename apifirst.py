import requests
import json

class Places:
    placeslist = []
    def __init__(self, long, lat, name):
        self.longitude = long
        self.latitude = lat
        self.name = name
        Places.placeslist.append(self)
        
lo = ''
la = ''
status = input("Press enter to add a place or type Done: ")
while status != "Done":
    lo = input('Give a longitude: ')
    la = input('Give a latitude: ')
    name = input('Give this places name: ')
    status = input("Press enter to add a place or type Done: ")
    Places(lo, la, name)

outdict = {}

for place in Places.placeslist:
    params = {
    "lat": place.latitude, 
    "lon": place.longitude,
    "appid": '60ef62c7f8d9b245d9bc66b691f0712c'
    }
    response = requests.get(
        'https://api.openweathermap.org/data/2.5/weather', params= params)  
    outdict[str(place.name)] = response.json()['main']['temp']
    
    
for key in outdict:
    temp = int(outdict[key]-273)
    print(key + " has temperature " + str(temp))

