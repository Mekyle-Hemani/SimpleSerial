import communication #Imports the file that has all the basic communication
import colourprint #A function that can print colours

#Creates a new function that can search for items in the "searching" list
#Searching list must have only string items
def readFor(searching, rate=9600, debug=0):
    result = communication.readData(rate=rate, debug=debug) #Grab the given result from the micro controller
    if result in searching: #If the result is in the wanted items list
        if debug == 1: #If debug mode is on
            colourprint.print_colored(f"Micro controller returned {result}", colourprint.GREEN) #Display that the user found the item form the micro controller
        return result #Return what result was found
    else:
        if debug == 1: #If debug mode is on
            print(f"Micro controller did not find item", colourprint.RED) #Display that the user found the item form the micro controller
        return False #Return a negative item