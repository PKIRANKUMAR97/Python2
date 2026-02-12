# 1. Beginner: The "Smart Clock" (Feature Combination)
# The Goal: Create a device that functions as both a clock and a calendar.
# Class 1 (Clock): Method show_time() that prints "Current time is 12:00 PM."

class Clock:
    def show_time(self):
        print("Current time is 12:00 PM.")

# Class 2 (Calendar): Method show_date() that prints "Today is January 1st."

class Calendar:
    def show_date(self):
        print("Today is January 1st.")

# Class 3 (SmartWatch): Inherits from both. Add a method show_all() that calls both parent methods.

class SmartWatch(Clock,Calendar):
    def show_all(self):
        super().show_time()
        super().show_date()

sw=SmartWatch()
sw.show_all()
