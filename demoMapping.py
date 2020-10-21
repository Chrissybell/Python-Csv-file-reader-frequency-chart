import lab6Functions
import csv
"Submitted by: Christobel Nweke"

statefile = open("states.csv", "r")
rainfile = open("rainfall.csv", "r")
csvfile1 = csv.reader(statefile)
csvfile2 = csv.reader(rainfile)


make1 = lab6Functions.makeMapping(csvfile1)
print(make1)
lab6Functions.displayMapping(make1)
print("")
make2 = lab6Functions.makeMapping(csvfile2)
lab6Functions.displayMapping(make2)

inverse = lab6Functions.makeInverseMapping(make1)
print("")
print(inverse)
lab6Functions.displayMapping(inverse)

