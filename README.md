SimpleSerial is a small package that can help anyone who needs quick and simple functions for communication with micro controllers. You can do things like read incoming data constantly, check the incoming data, as well as send through multiple very simple functions.

Some simple functions included with the package:


SimpleSerialMain.readDataOnce(data, rate=9600, debug=0)
This returns the data of the broadcasted information of the microcontroller once.

You can change the data argument to a string that contains what you want to check the broadcasted information of the microcontroller to.
If you have data equal to "Hello, World" in the function and the microcontroller is broadcasting "Hello, World"; The function will return True.
Otherwise it will return False. (Optional)

Rate can be changed to your baudrate of the microcontroller (Normally 9600).

Debug can be set to 1 to have coloured progress checks (Optional).



SimpleSerialMain.writeDataOnce(data, rate=9600, debug=0)
This writes the variable "data" to the microcontroller.

Rate can be changed to your baudrate of the microcontroller (Normally 9600).

Debug can be set to 1 to have coloured progress checks (Optional).



SimpleSerialMain.readDataForMultipleItemsOnce(data, rate=9600, debug=0)
This will check data of the broadcasted information of the microcontroller once for multiple items (data).

You can change the data argument to a list that contains what you want to check the broadcasted information of the microcontroller to.
If you have data contain "Hello, World" in the function and the microcontroller is broadcasting "Hello, World"; The function will return True.
Otherwise it will keep checking for another item in the list.

Rate can be changed to your baudrate of the microcontroller (Normally 9600).

Debug can be set to 1 to have coloured progress checks (Optional).



SimpleSerialMain.readDataForMultipleItemsConstantly(data, rate=9600, debug=0)
This will check data of the broadcasted information of the microcontroller until it finds a wanted item (data).

You can change the data argument to a list that contains what you want to check the broadcasted information of the microcontroller to.
If you have data contain "Hello, World" in the function and the microcontroller is broadcasting "Hello, World"; The function will return True.
Otherwise it will return False unless it references another item in the list.

Rate can be changed to your baudrate of the microcontroller (Normally 9600).

Debug can be set to 1 to have coloured progress checks (Optional).



SimpleSerialMain.readDataForOneItemConstantly(data, rate=9600, debug=0)
This will check data of the broadcasted information of the microcontroller until it finds an item (data).

You can change the data argument to a string that contains what you want to check the broadcasted information of the microcontroller to.
If you have data equal to "Hello, World" in the function and the microcontroller is broadcasting "Hello, World"; The function will return True.
Otherwise it will keep checking. (Optional)

Rate can be changed to your baudrate of the microcontroller (Normally 9600).