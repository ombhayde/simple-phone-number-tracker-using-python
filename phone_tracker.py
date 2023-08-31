import phonenumbers
import opencage
import folium
number=str(input("Enter your phone number with country code: "))
from phonenumbers import geocoder

pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))


from opencage.geocoder import OpenCageGeocode

key='e980f8ada6054100ac05636e16a4f375'

geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)


lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")