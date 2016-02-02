FULLDATA = 24569
SAMPLEDATA = 202
import time
import csv
dataCSV = open('PittAreaRawData.csv')
dataRead = csv.reader(dataCSV)
dataList = list(dataRead)

#geocoding test
#requires pip install geopy from terminal
from geopy.geocoders import Nominatim
geolocator = Nominatim()
McSpread = open('MckeesportSpread.csv', 'a')
#McSpread.write("Account, Owners, Input Address, Output Number, Output Street, Output City, Output County, Output Zipcode, Output Country, Description, CDT, DQT, Interest, Latitude, Longitude, Index, Comments")


for i in range(24030, FULLDATA): #skipping first 55 indices because they have no number and will get mixed in with the geocode returns that are wrong
	fullAddress = str(dataList[i][2]) + ", Mckeesport, PA"
	location = geolocator.geocode(fullAddress, timeout=60)
	time.sleep(1)
	if location == None:
		tempP = "index " + str(i) + ": " + dataList[i][2] + " not found in Mckeesport, PA"
		print(tempP)
		continue
	if dataList[i][2] != dataList[i-1][2]:
		tempO = "Found! at " + str(location.latitude) + ", " + str(location.longitude) + ", adding to files..."
		r = 0
		print(tempO)
		
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
McSpread.close()
