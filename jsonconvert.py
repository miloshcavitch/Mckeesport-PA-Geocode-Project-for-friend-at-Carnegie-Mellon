FULLDATA = 24569
SAMPLEDATA = 202

import csv
dataCSV = open('PittAreaRawData.csv')
dataRead = csv.reader(dataCSV)
dataList = list(dataRead)

#geocoding test
#requires pip install geopy from terminal
from geopy.geocoders import Nominatim
geolocator = Nominatim()
for l in range(230, 260):
	fullAddress = str(dataList[l][2]) + ", Mckeesport, PA"
	location = geolocator.geocode(fullAddress, timeout=30)
	if location == None:
		print("None")
		continue
	print(location.latitude, location.longitude)
	
	
jso = open('jstring.json', 'w')
jso.write("var addressLocations = \n[\n")
for i in range(1, FULLDATA):
	if dataList[i][2] != dataList[i-1][2]:
		jso.write("\t{ \"address\": \"")
		jso.write(dataList[i][2])
		jso.write("\", ")
		jso.write("\"latitude\": 0, \"longitude\": 0, ")
		jso.write("\"index\": \"")
		jso.write(str(i));
		jso.write("\"},\n")
jso.write("]")
jso.close()
