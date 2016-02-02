import csv
dataCSV = open('MckeesportEdited.csv')
dataRead = csv.reader(dataCSV)
dataList = list(dataRead)

additionalInfoOrder = [10, 11, 12, 13, 17] #forlater


jso = open('MckeesportJstring.json', 'w')

jso.write("McPoints = [\n")
for i in range(0, 122):
	jso.write("\t{\"inputAddress\": \"")
	jso.write(dataList[i][2])
	jso.write("\", \"outputAddress\": \"")
	oA = str(dataList[i][3]) + " " + str(dataList[i][4]) + ", " + str(dataList[i][5]) + ", " + str(dataList[i][6])
	jso.write(oA)
	jso.write("\", \"latitude\": \"")
	jso.write(str(dataList[i][14]))
	jso.write("\", \"longitude\": \"")
	jso.write(str(dataList[i][15]))
	jso.write("\", \"additionalInfo\": \"To be added\"")
	jso.write("}\n")
	
