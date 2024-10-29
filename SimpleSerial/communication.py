import serial #Required library for sending data to an micro controller
import serial.tools.list_ports #Required librray for checking all available micro controllers
import time #Required library for delaying the code
from . import colourprint #A function that can print colours

#Data is the text that will be sent to the micro controller
#Rate is the rate of the information being sent (This is different for all types of micro controllers however the micro controller Uno uses 9600)

def sendData(data, rate=9600, debug=0):
    ports = serial.tools.list_ports.comports() #These are all the found ports that are active
    comports = [port.device for port in ports] #For each COM port in the list of active ports

    if not comports: #If there are no found ports
        if debug == 1: #If the debug mode is enabled
            colourprint.print_colored("Please ensure that the micro controller is connected", colourprint.ORANGE) #Send an error message
        return "0" #Close the code as False to show negative
    
    port = comports[0] #If there was no problem finding ports, pick the first one

    ser = serial.Serial(port, rate)
    try:
        ser.write((data + "\n").encode())
        time.sleep(1)
        return True
    except Exception as e:
        if debug == 1: #If the debug mode is enabled
            colourprint.print_colored("Error sending data: "+e, colourprint.RED)
        return False
    finally:
        ser.close()

def readData(data=None, rate=9600, debug=0):
    #This section is for finding and initializing your micro controller
    ports = serial.tools.list_ports.comports() #These are all the found ports that are active
    comports = [port.device for port in ports] #For each COM port in the list of active ports

    if not comports: #If there are no found ports
        if debug == 1: #If the debug mode is enabled
            colourprint.print_colored("Please ensure that the micro controller is connected", colourprint.RED) #Send an error message
        return "0" #Close the code as False to show negative
    
    port = comports[0] #If there was no problem finding ports, pick the first one

    try:
        ser = serial.Serial(port, baudrate=rate, timeout=1) #Start the communication
        time.sleep(2) #Delays the code for 2 seconds
        if debug == 1: #If the debug mode is enabled
            colourprint.print_colored(f"Connected to {port}", colourprint.GREEN) #Tells the user that they have connected to the micro controller
        
        while True:
            #Constantly check for incoming data from micro controller
            if ser.in_waiting > 0: #If there is data waiting to be read
                #received_data = ser.read(ser.in_waiting).decode('utf-8') #Read and decode data
                received_data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore')

                if debug == 1: #If the debug mode is enabled
                    colourprint.print_colored(f"Received from micro controller: {received_data}", colourprint.GREEN)

                #If there wasnt a specific return that the user is looking for
                if data == None:
                    return received_data #Return whatever the micro controller sends
                
                #If the user was looking for something specific
                elif data in received_data: #If the found data is what the user is looking for
                    return True #Return succesful
            else:
                if debug == 1: #If the debug mode is enabled
                    colourprint.print_colored("No data received from micro controller", colourprint.RED)
    
    except serial.SerialException as error:
        if debug == 1: #If the debug mode is enabled
            colourprint.print_colored(f"Failed to connect to {port}: {error}", colourprint.RED) #Handle errors
    
    except KeyboardInterrupt:
        if debug == 1: #If the debug mode is enabled
            colourprint.print_colored("Stopping communication due to key handle", colourprint.RED) #Handle keyboard interrupt
        return False