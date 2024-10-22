import serial #Required library for sending data to an Arduino
import serial.tools.list_ports #Required librray for checking all available Arduinos
import time as delaycode #Required library for delaying the code


#Data is the text that will be sent to the Arduino
#Rate is the rate of the information being sent (This is different for all types of Arduinos however the Arduino Uno uses 9600)

def sendData(data, rate=9600, debug=0):
    #This section is for finding and initializing your Arduino

    ports = serial.tools.list_ports.comports() #These are all the found ports that are active
    comports = [port.device for port in ports] #For each COM port in the list of active ports

    if not comports: #If there are no found ports
        if debug == 1: #If the debug mode is enabled
            print("Please ensure that the Arduino is connected") #Send an error message
        return False #Close the code as False to show negative
    
    port = comports[0] #If there was no problem finding ports, pick the first one

    #Surrounded in a try catch to catch errors during communication
    try:
        ser = serial.Serial(port, baudrate=rate, timeout=1) #Start the communication at the supplied port and at the given

        delaycode.sleep(2) #Delays the code for 2 seconds
        if debug == 1: #If the debug mode is enabled
            print(f"Connected to {port}") #Tells the user that they have conncected to the Arduino

        ser.write(data.encode('utf-8')) #This is the type of data encoding that will be used. Arduinos require UTF8. This sends the data in UTF8 to the device

        if debug == 1: #If the debug mode is enabled
            print(f"Sent '{data}' successfully") #Display a success message

        return True #Return a positive element
    
    except serial.SerialException as error:
        #If the library finds an error
        if debug == 1: #If the debug mode is enabled
            print(f"Failed to connect to {port}: {error}") #Say an error was found and on what COM port it occorred on
        return False #Return a negative element
    
    except KeyboardInterrupt:
        #If the user uses a keyboard to quit the code
        if debug == 1: #If the debug mode is enabled
            print("Stopping communication due to key handle") #Tells the user why the code stopped
        return False #Return a negative element
    finally:
        #If any error occurred
        if ser.is_open: #And the port is still open
            ser.close() #Close the port so that the Arduino can reconnect

def readData(data=None, rate=9600, debug=0):
    #This section is for finding and initializing your Arduino
    ports = serial.tools.list_ports.comports() #These are all the found ports that are active
    comports = [port.device for port in ports] #For each COM port in the list of active ports

    if not comports: #If there are no found ports
        print("Please ensure that the Arduino is connected") #Send an error message
        return False #Close the code as False to show negative
    
    port = comports[0] #If there was no problem finding ports, pick the first one

    try:
        ser = serial.Serial(port, baudrate=rate, timeout=1) #Start the communication
        delaycode.sleep(2) #Delays the code for 2 seconds
        print(f"Connected to {port}") #Tells the user that they have connected to the Arduino
        
        while True:
            #Constantly check for incoming data from Arduino
            if ser.in_waiting > 0: #If there is data waiting to be read
                received_data = ser.read(ser.in_waiting).decode('utf-8') #Read and decode data
                print(f"Received from Arduino: {received_data}")

                #If there wasnt a specific return that the user is looking for
                if data == None:
                    return data #Return whatever the Arduino sends
                
                #If the user was looking for something specific
                elif received_data == data: #If the found data is what the user is looking for
                    return True #Return succesful
            else:
                print("No data received from Arduino")
    
    except serial.SerialException as error:
        print(f"Failed to connect to {port}: {error}") #Handle errors
        return False
    
    except KeyboardInterrupt:
        print("Stopping communication due to key handle") #Handle keyboard interrupt
        return False
    
    finally:
        if ser.is_open: #Ensure the port is closed after completion
            ser.close()

if __name__ == "__main__":
    #The first field is the text you want to send
    #The second field is the baudrate (Optional)
    #The second field is the debug function (Optional) 0-1
    print(sendData("123456", 9600, 1))