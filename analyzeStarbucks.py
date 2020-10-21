"""
CSM 2170: Lab 6
Analyze a CSV file giving information about location of Starbucks stores

Submitted by: Christobel Nweke
"""

import lab6Functions
import csv



# Get the state/region information
statesFile = open("states.csv", "r")
csvfile1 = csv.reader(statesFile)
srInfo = lab6Functions.makeMapping(csvfile1)


# Present a list of options -- which region to analyze
statefile = open("states.csv", "r")
csvfile1 = csv.reader(statefile)
stateList = []
for row in csvfile1:
    if row[1] not in stateList:
        stateList.append(row[1])
sChoice = lab6Functions.offerMenuItems(stateList)
print("You entered %s" %sChoice)


# Create a list of states in this region
sList = lab6Functions.makeInverseMapping(srInfo)
print("The list of states here are: ", sList[sChoice])

f = open("starbucks.csv")
# Process the Starbucks data file. For each line of the file, determine if
# it appears in one of the desired states.  If so, append the state
# to the list of states; otherwise ignore it
csv1 = csv.reader(f)
starbucks = []
for row in csv1:
    latitude = row[0]
    longitude = (row[1])
    location = row[2]
    address = row[3]
    word = address.split()
    for i in range(len(word)):
        if word[i] in sList[sChoice]:
            starbucks.append(word[i])


f.close()

# Produce a histogram showing the frequency of stores by state
lab6Functions.frequencyChart(starbucks)