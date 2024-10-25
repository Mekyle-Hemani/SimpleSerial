#First thing to do is type this in terminal
'''

pip install SimpleWine

'''

import SimpleSerial.SimpleSerialMain #Library

while True:
    #When the arduino sends "buttonpressed"
    if "buttonpressed" in SimpleSerial.SimpleSerialMain.readDataOnce(debug=1):
        #Have the code do something HERE
        break