# 2. Intermediate: The "Diamond" Conflict
# The Goal: Understand priority when two parents have the same method.
# Class 1 (Radio): Method play() prints "Playing FM Radio."
class Radio:
    def play(self):
        print("Playing FM Radio.")
# Class 2 (CDPlayer): Method play() prints "Playing CD tracks."

class CDPlayer:
    def play(self):
        print("Playing CD tracks.")

# Class 3 (MultimediaSystem): Inherits from CDPlayer first, then Radio.

class MultimediaSystem(CDPlayer,Radio):
    def smarts(self):
        print("Playing Multimedia system.")
        self.play()

mms=MultimediaSystem()
mms.smarts()

