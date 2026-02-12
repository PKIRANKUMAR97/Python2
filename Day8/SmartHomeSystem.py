#
# The Task: The Smart Home System
# Level 1 (Grandparent): Create a class Electronics with an attribute brand and a method set_brand().
# Level 2 (Parent): Create a class SmartDevice that inherits from Electronics.
# Add an attribute connected_to_wifi (default it to False) and a method connect().
# Level 3 (Child): Create a class SmartCamera that inherits from SmartDevice.
# Add a method record() that only works if connected_to_wifi is True.

# Constraints:
#
# You must use super() in the SmartCamera constructor to pass the brand all the way up to Electronics.
# If record() is called while offline, print a warning message.


class Electronics:
    def __init__(self,brand):
        self.brand=brand


class SmartDevice(Electronics):
    def __init__(self,brand):
        super().__init__(brand)
        self.connected_to_wifi=False

    def connect(self):
        self.connected_to_wifi = True
        print("Connecting to wifi.....")

class SmartCamera(SmartDevice):
    def __init__(self,brand):
        super().__init__(brand)

    def record(self):

        if self.connected_to_wifi == True:
            print(" Smart camera is connected to wifi")
        else:
            print("Smart camera is working..............")

sc1=SmartCamera("Samsung")
sc1.record()
sc1.connect()
sc1.record()




