FULLDATA = 24569
SAMPLEDATA = 202

import csv
dataCSV = open('PittAreaRawData.csv')
dataRead = csv.reader(dataCSV)
dataList = list(dataRead)

def howManyRepeats(i, r):
	if dataList[i][2] == dataList[i+r+1][2]:
		r += 1
		howManyRepeats(i, r)
	else:
		return r
		

#geocoding test
#requires pip install geopy from terminal
from geopy.geocoders import Nominatim
geolocator = Nominatim()
jso = open('MckeesportJstring.json', 'w')
McSpread = open('MckeesportSpread.csv', 'w')
jso.write("var addressLocations = \n[\n")
McSpread.write("Account, Owners, Input Address, Output Number, Output Street, Output City, Output County, Output Zipcode, Output Country, Description, CDT, DQT, Interest, Latitude, Longitude, Index, Comments")


for i in range(4500, 5000):
	fullAddress = str(dataList[i][2]) + ", Mckeesport, PA"
	location = geolocator.geocode(fullAddress, timeout=30)
	if location == None:
		tempP = "index " + str(i) + ": " + dataList[i][2] + " not found in Mckeesport, PA"
		print(tempP)
		continue
	if dataList[i][2] != dataList[i-1][2]:
		tempO = "Found! at " + str(location.latitude) + ", " + str(location.longitude) + ", adding to files..."
		r = 0
		repeats = howManyRepeats(i, r)
		print(tempO)
		additionalInfo = "Account Number: " + str(dataList[i][0]) + ", Owners: " + str(dataList[i][1]) + ", Description: " + str(dataList[i][3]) + ", CDT: " + str(dataList[i][4]) + ", DQT: " + ", Interest: " + str(dataList[i][5]) + ", Comments: " + str(dataList[i][7])
		jso.write("\t{ \"address\": \"")
		jso.write(dataList[i][2])
		jso.write("\", ")
		jso.write("\"latitude\": \"")
		jso.write(str(location.latitude))
		jso.write("\", \"longitude\": \"")
		jso.write(str(location.longitude))
		jso.write("\", \"index\": \"")
		jso.write(str(i))
		jso.write("\", \"repeats\": \"")
		jso.write(str(repeats))
		jso.write("\", \"additionalInfo\": \"")
		jso.write(additionalInfo)
		jso.write("\"},\n")
		
		McSpread.write("\n")
		McSpread.write(dataList[i][0])
		McSpread.write(", ")
		McSpread.write(dataList[i][1])
		McSpread.write(", ")
		McSpread.write(dataList[i][2])
		McSpread.write(", ")
		McSpread.write(str(location.address))
		print(str(location.address))
		McSpread.write(", ")
		McSpread.write(dataList[i][3])
		McSpread.write(", ")
		McSpread.write(dataList[i][4])
		McSpread.write(", ")
		McSpread.write(dataList[i][5])
		McSpread.write(", ")
		McSpread.write(dataList[i][6])
		McSpread.write(", ")
		McSpread.write(str(location.latitude))
		McSpread.write(", ")
		McSpread.write(str(location.longitude))
		McSpread.write(", ")
		McSpread.write(str(i))
		McSpread.write(", ")
		McSpread.write(dataList[i][7])
jso.write("]")
jso.close()
McSpread.close()
