# The Task: The Smart Home Light
# Parent 1: Device (needs a brand)
# Parent 2: Light (needs brightness_level)
# Child: SmartLight (needs both)

class Device:
    def __init__(self,brand):
        self.brand=brand

class Light:
    def __init__(self,brightness_level):
        self.brightness_level=brightness_level

class SmartLight(Device,Light):
    def __init__(self,brand,brightness_level,wifi_name):
        super().__init__(brand=brand, brightness_level=brightness_level)
        self.wifi_name=wifi_name

    def med(self):
        print(self.brand, self.brightness_level, self.wifi_name)

bulb = SmartLight("Philips", "80%", "Home_WiFi")
bulb.med()