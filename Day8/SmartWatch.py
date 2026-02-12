# The Task: The Smart Watch
# Create a class Clock with a method show_time().
# Create a class Phone with a method Phone().
# Create a child class SmartWatch that inherits from both.
# Add a method track_steps() to SmartWatch.

class Clock:
    def show_time(self):
        print("this shows time")

class Phone:
    def Phone(self):
        print("this shows phone features")

class SmartWatch(Phone,Clock):
    def track_steps(self):
        print("this shows track steps and everything ....")

sw = SmartWatch()
sw.show_time()
sw.Phone()
sw.track_steps()