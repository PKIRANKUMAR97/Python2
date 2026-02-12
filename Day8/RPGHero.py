# 4. Advanced: The "RPG Hero" (The MRO Challenge)
# The Goal: Create a complex character that inherits from multiple combat styles.
# Parent 1 (Archer): Method attack() prints "Firing an arrow!" and a method range_check() prints "Checking distance..."
# Parent 2 (Knight): Method attack() prints "Swinging a sword!" and a method shield_up() prints "Blocking..."
# Child (Paladin): Inherits from Knight then Archer.
# Task:
# Override attack() in Paladin to first call super().attack(), then print "Casting a holy spell!"
# In your main code, call Paladin.mro() and explain why the "sword" or "arrow" appeared first.

class Archer:
    def attack(self):
        print("Firing an arrow!")

    def range_check(self):
        print("Checking distance...")

class Knight:
    def attack(self):
        print("Swinging a sword!")

    def shield_up(self):
        print("Blocking...")

class Paladin(Knight, Archer):
    def attack(self):
        super().attack()
        print("Casting a holy spell!")

p1=Paladin()
p1.attack()
