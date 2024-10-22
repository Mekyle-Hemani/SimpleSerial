import serial #Required library for sending data to an Arduino
import serial.tools.list_ports #Required librray for checking all available Arduinos
import time as delaycode #Required library for delaying the code


#Data is the text that will be sent to the Arduino
#Rate is the rate of the information being sent (This is different for all types of Arduinos however the Arduino Uno uses 9600)

def senddata(data, rate=9600, delay=0):
    #This section is for finding and initializing your Arduino

    ports = serial.tools.list_ports.comports() #These are all the found ports that are active
    comports = [port.device for port in ports] #For each COM port in the list of active ports

    if not comports: #If there are no found ports
        print("Please ensure that the Arduino is connected") #Send an error message
        return False #Close the code as False to show negative
    
    port = comports[0] #If there was no problem finding ports, pick the first one

    #Surrounded in a try catch to catch errors during communication
    try:
        ser = serial.Serial(port, baudrate=rate, timeout=1) #Start the communication at the supplied port and at the given

        delaycode.sleep(2) #Delays the code for 2 seconds
        print(f"Connected to {port}") #Tells the user that they have conncected to the Arduino
        ser.write(data.encode('utf-8')) #This is the type of data encoding that will be used. Arduinos require UTF8. This sends the data in UTF8 to the device
        print(f"Sent '{data}' successfully") #Display a success message

        return True #Return a positive element
    
    except serial.SerialException as error:
        #If the library finds an error
        print(f"Failed to connect to {port}: {error}") #Say an error was found and on what COM port it occorred on
        return False #Return a negative element
    
    except KeyboardInterrupt:
        #If the user uses a keyboard to quit the code
        print("Stopping communication due to key handle") #Tells the user why the code stopped
        return False #Return a negative element
    finally:
        #If any error occurred
        if ser.is_open: #And the port is still open
            ser.close() #Close the port so that the Arduino can reconnect

if __name__ == "__main__":
    #The first field is the text you want to send
    #The second field is the baudrate (Optional)
    #The second field is the debug function (Optional) 0-1
    print(senddata("123456", 9600, 1))