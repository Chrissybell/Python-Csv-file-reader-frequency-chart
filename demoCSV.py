"""
CSM 2170: Lab 6
Processing a CSV (comma-separated values) file

Submitted by: Christobel Nweke
"""

import csv
import lab6Functions

# Open the states file and prepare to read each of its rows
states = open("states.csv", "r")
csvfile = csv.reader(states)

# Iterate over each row in the file
for row in csvfile:

    town = row[0]
    rainfall = str(row[1])
    state = "States"
    region = "Regions"
    blank = "------"
    blank2 = "------"
    print("%s %+15s" % (state, region))
    print("%s %+15s" % (blank, blank2))
    print("%s %+20s" % (town, rainfall))
    print()


# After processing the file, close it
states.close()

# Open the starbucks file and prepare to read each of its rows
starbucks = open("starbucks-sample.csv", "r")
csvfile = csv.reader(starbucks)

# Iterate over each row in the file
for row in csvfile:

    Latitude = row[0]
    Longitude = row[1]
    Location = row[2]
    Address = row[3]
    blank = "------"
    blank2 = "------"
    print("LATITUDE: ", Latitude )
    print("LONGITUDE: ", Longitude)
    print("LOCATION: ", Location)
    print("ADDRESS: ", Address)
    print()


starbucks.close()
