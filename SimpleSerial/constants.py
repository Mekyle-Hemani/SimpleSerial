from . import communication #Imports the file that has all the basic communication
from . import colourprint #A function that can print colours

#Creates a new function that can search for items in the "searching" list
#Searching list must have only string items
def readForMulti(searching, rate=9600, debug=0):
    while True: #While the micro controller returned items are not the wanted items
        result = communication.readData(rate=rate, debug=debug) #Grab the given result from the micro controller
        if result in searching: #If the result is in the wanted items list
            if debug == 1: #If debug mode is on
                colourprint.print_colored(f"Microcontroller returned {result}", colourprint.GREEN) #Display that the user found the item form the micro controller
            return result #Return what result was found

#Creates a new function that can constantly search for one item "searching" variable
def readFor(searching, rate=9600, debug=0):
    while True: #While the micro controller returned items are not the wanted items
        result = communication.readData(rate=rate, debug=debug) #Grab the given result from the micro controller
        if result == searching: #If the result is in the wanted items list
            if debug == 1: #If debug mode is on
                print(f"Microcontroller returned {result}", colourprint.GREEN) #Display that the user found the item form the micro controller
            return result #Return what result was found