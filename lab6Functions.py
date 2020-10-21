"""
CSM 2170: Lab 6
Support functions for Lab 7

Submitted by: Christobel Nweke
"""

import turtle
import csv


def skipAmount(maximumValue):
    """
    Determines an appropriate skip amounts for a bar chart

    Args:
        maximumValue: the largest frequency which appears on a bar chart

    Returns:
        A "skip" amount for drawing equally spaced intermediate lines along
        the y axis.  If the maximum value appears is M, then this skip value
        is as follows:
            max value                 skip
            ------------------------------
                     M <= 10             1
                10 < M <= 50             5
                50 < M <= 100           10
               100 < M <= 500           50
               500 < M <= 1,000        100
             1,000 < M <= 5,000        500
             5,000 < M <= 10,000     1,000
            10,000 < M <= 100,000   10,000
    """
    skip = 0

    if maximumValue <= 10:
        skip = skip + 1
    elif 10 < maximumValue <= 50:
        skip = skip + 5
    elif 50 < maximumValue <= 100:
        skip = skip + 10
    elif 100 < maximumValue <= 500:
        skip = skip + 50
    elif 500 < maximumValue <= 1000:
        skip = skip + 100
    elif 1000 < maximumValue <= 5000:
        skip = skip + 500
    elif 5000 < maximumValue <= 10000:
        skip = skip + 1000
    elif 10000 < maximumValue <= 100000:
        skip = skip + 10000

    return skip

    pass  # NOT IMPLEMENTED YET
    
    
def makeMapping(filename):
    """
    Creates a mapping based on a file of ordered pairs.

    Args:
        filename: the name of a file with ordered pairs, in CSV format.

    Returns:
        A dictionary d with d[a] = b for every ordered pair a,b which appears
        in the specified file.
    """
    # Dictionary for each line read
    lineDict = {}
    # iterates over each line in the opened file
    for aline in filename:
        # zeroes the dictionary out and store into it everything in that line starting from the first index
        lineDict[aline[0]] = aline[1]

    return lineDict


def displayMapping(d):
    """
    Display the contents of a dictionary.

    Args:
        d: a dictionary

    Returns:
        None
    """
    # Loop that for each iteration prints out the iteration number and the indexed line at the Ith position.
    for aline in d:
       print("%s -> %s" % (aline,d[aline]))


def makeInverseMapping(m):
    """
    Create the inverse of a given map.

    Args:
        m: a dictionary

    Returns:
        A dictionary d which gives the inverse mapping.  More precisely,
        if there are p key values, k_1, k_2, ..., k_p, which map to v,
        then d[v] = [k_1, k_2, ..., k_p].
    """
    inverse = {}
    for aline in m:
        inverse[m[aline]] = inverse.get(m[aline], [])
        inverse[m[aline]].append(aline)

    return inverse


def offerMenuItems(choices):
    """
    Offer a menu of items and offer a choice to be selected

    Args:
        choices: a list of menu choices

    Returns:
        For valid input, the option number is returned.  If an incorrect
        response is given, the value None is returned.
    """

    print("Choose From The Following Options: ")
    # prints out a numbered list of choices
    for i in range(len(choices)):
        print(('%s, %s' %(i, choices[i])))

    # prompts the user to select a number from the menu list
    enter = int(input("Enter your desired choice number: "))
    choice = ("You entered %d (for %s)" % (enter, choices[enter]))
    #print(choices)

    # returns choice which prints out the number you chose and the associated menu item
    return choices[enter]

    
def state(s, stateDict):
    """
    Find a 2-letter state abbreviation within space-separated string s

    Args:
        s: a string
        stateDict: a dictionary with the states as keys

    Returns:
        If the string has a two-letter state abbreviation (e.g., IL)
        somewhere within it, then it returns this state;
        otherwise it returns None.
    """
    a = s.split()
    for i in range(len(a)):
        if a[i] in stateDict:
            return s


def drawBar(myTurtle,LLx,LLy,URx,URy,color):
    """
    Draws a filled rectangle, in a specified color,
    given coordinates of the lower left and upper right
    points of a rectangle

    Args:
        myTurtle: a turtle
        LLx, LLy: coordinates of lower left corner of the bar
        URx, URy: coordinates of upper right corner of the bar
        color: desired fill color for this bar

    Returns:
        None
    """
    myTurtle.color(color)
    myTurtle.up()
    myTurtle.goto(LLx, LLy)
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(LLx, URy)
    myTurtle.goto(URx, URy)
    myTurtle.goto(URx, LLy)
    myTurtle.end_fill()
    myTurtle.up()
    myTurtle.goto(0, 0)

    return None


def computeFrequencies(aList):
    """
    Compute a frequency distribution of a given data set

    Args:
        aList: a list of data values

    Returns:
        A dictionary consisting of (item, frequency) pairs
    """

    # dictionary of data items and their frequencies
    countDict = {}

    # determine how many times each data item appears in the list
    for item in aList:
        if item in countDict:
            # item has been seen before; boost its count
            countDict[item] = countDict[item] + 1
        else:
            # first time this item has been seen
            countDict[item] = 1

    return countDict


def tabulateFrequencies(aList):
    countDict = (computeFrequencies(aList))
    # Produce a sorted list of the unique data items
    itemList = list((countDict.keys()))
    itemList.sort()

    # Tabulate the items and their associated frequencies
    print("ITEM", "FREQUENCY")
    for item in itemList:
        print(item, "     ", countDict[item])



def drawLine(myTurtle, Px, Py, Qx, Qy, color):
    """
    Draws a line segment from one point to another

    Args:
        myTurtle: a turtle
        Px, Py: coordinates of one endpoint
        Qx, Qy: coordinates of the other endpoint

    Returns:
        None
    """

    # Draw a line segment from point (Px, Py) to point (Qx, Qy)
    myTurtle.up()
    myTurtle.goto(Px, Py)
    myTurtle.down()
    myTurtle.goto(Qx, Qy)
    myTurtle.up()
    myTurtle.color(color)


def frequencyChart(aList):
    """
    Draw a histogram for a given data set

    Args:
        aList: a list of data values

    Returns:
        None
    """

    # Size of labels
    fontSize = 12

    # dictionary of data items and their frequencies
    countDict = computeFrequencies(aList)

    # Produce a sorted list of the unique data items
    itemList = list(countDict.keys())
    itemList.sort()

    # Number of histogram bars needed, one for each item
    numItems = len(itemList)

    # Create a list of frequencies and find the largest one
    countList = countDict.values()
    maxFrequency = max(countList)

    # Establish graphics window, create turtle and turn off animation
    window = turtle.Screen()
    chartT = turtle.Turtle()
    turtle.tracer(0)



    # Set up the window coordinate system, leaving a 10% margin on all sides
    window.setworldcoordinates(-0.1*numItems, -0.1*maxFrequency,
                               1.1*numItems, maxFrequency*1.1)

    # Ensure the chart does not include an image of the turtle
    chartT.hideturtle()

    # horizontal offset for each bar
    offset = 0.5


    # specify how close labels should be to histogram bars
    xLabelOffset = 0.05*numItems       # for vertical axis labels
    yLabelOffset = 0.05*maxFrequency   # for horizontal axis labels

    # Draw a horizontal axis
    drawLine(chartT, 0, 0, numItems, 0, 'red')
    drawLine(chartT, 0, skipAmount(maxFrequency), numItems, skipAmount(maxFrequency), "blue")
    drawLine(chartT, 0, 2 * skipAmount(maxFrequency), numItems, 2 * skipAmount(maxFrequency), "blue")
    drawLine(chartT, 0, 3 * skipAmount(maxFrequency), numItems, 3 * skipAmount(maxFrequency), "blue")

    #drawBar(chartT, 0, 0, numItems, 0, 'blue')

    # Add labels for vertical min and max (the frequency range)
    chartT.goto(-xLabelOffset, 0)
    chartT.write("0", font=("Helvetica", fontSize))
    chartT.goto(-xLabelOffset, maxFrequency)
    chartT.write(str(maxFrequency), font=("Helvetica", fontSize))
    chartT.goto(-xLabelOffset, skipAmount(maxFrequency))
    chartT.write(str(skipAmount(maxFrequency)), font=("Helvetica", fontSize))
    chartT.goto(-xLabelOffset, 2 * skipAmount(maxFrequency))
    chartT.write(str(2 * skipAmount(maxFrequency)), font=("Helvetica", fontSize))
    chartT.goto(-xLabelOffset, 3 * skipAmount(maxFrequency))
    chartT.write(str(3 * skipAmount(maxFrequency)), font=("Helvetica", fontSize))


    # For each item, draw a bar of appropriate height
    for index in range(len(itemList)):
        # Move turtle to the current index for that item's bar, and label it
        chartT.goto(index + offset, -yLabelOffset)
        chartT.write(str(itemList[index]), align="center",
                     font=("Helvetica", fontSize))

        # Determine the current item's frequency
        barHeight = countDict[itemList[index]]

        # Draw a bar of the appropriate height
        drawLine(chartT, index + offset, 0, index + offset, barHeight, 'red')
        drawBar(chartT, index + 1 / 2 * offset, 0, index + 1.5 * offset, barHeight, 'red')


    turtle.update()
    chartT.hideturtle()

    # Keep graphics window open until user dismisses it
    window.exitonclick()










