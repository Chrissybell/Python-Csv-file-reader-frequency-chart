"Submitted by: Christobel Nweke"
import lab6Functions
import csv

yourOption = lab6Functions.offerMenuItems(['chocolate', 'vanilla', 'strawberry'])

print(yourOption)

statefile = open("states.csv", "r")
csvfile1 = csv.reader(statefile)

stateList = []

#for loop that goes through each line. If the region is not in the list it adds it to the list
# However, if the region is in the list it stops and moves to the next line
for row in csvfile1:
    if row[1] not in stateList:
        stateList.append(row[1])

print(lab6Functions.offerMenuItems(stateList))