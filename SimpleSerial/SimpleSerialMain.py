#All other functions by file
from . import communication
from . import constants
from . import multiRead

#Condensed functions by name

#communication.py
def readDataOnce(data=None, rate=9600, debug=0):
    #Read data once
    return communication.readData(data=data, rate=rate, debug=debug)

def writeDataOnce(data, rate=9600, debug=0):
    #Write data once
    return communication.sendData(data=data, rate=rate, debug=debug)


#multiRead.py
def readDataForMultipleItemsOnce(data, rate=9600, debug=0):
    #Read the data for a specific item (data) until it finds it
    return multiRead.readFor(data=data, rate=rate, debug=debug)


#Constants.py
def readDataForMultipleItemsConstantly(data, rate=9600, debug=0):
    #Read data multiple times for multiple conditions in the data list (data) constantly
    return constants.readForMulti(data=data, rate=rate, debug=debug)

def readDataForOneItemConstantly(data, rate=9600, debug=0):
    #Read multiple times for one conditions in the data variable (data)
    return constants.readFor(data=data, rate=rate, debug=debug)