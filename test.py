def fileToDict(file):

    file = str(file)

    callFile = open(file, "r")

    dictionary = {}

    for i in callFile:
        if(i in dictionary):
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1
    for key, value in dictionary.items():
        print("% s is repeated % d times" % (key,value))

    callFile.close()


print(fileToDict("testdoc"))







