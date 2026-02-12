# 3. Electronic Devices
# The Goal: Create a parent class Device with a method power_on() that prints "System is booting...".
# Create a child class Laptop.
# In Laptop, override power_on() so it first calls the parent's power_on() using super(),
# and then prints "Laptop screen is glowing."
# Key concept: Extending parent functionality instead of just replacing it.

class Device:
    def power_on(self):
        print("System is booting...")

class Laptop(Device):
    def power_on(self):
        super().power_on()
        print("Laptop screen is glowing.")

l1 = Laptop()
l1.power_on()