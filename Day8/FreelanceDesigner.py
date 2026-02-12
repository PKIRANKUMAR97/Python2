# 🧩 Practice Challenge for You:
# Create a system for a Freelance Designer:
# Class Artist: Method draw() prints "Drawing a masterpiece."
class Artist:
    def draw(self):
        print("this shows artist drawing")

# Class Coder: Method write_code() prints "Writing Python scripts."

class Coder:
    def write_code(self):
        print("this shows write code")

# Class Freelancer: Inherits from both.
# Add a method invoice() to Freelancer that calls both draw() and write_code() before printing "Sending the bill!"
class Freelancer(Artist,Coder):
    def invoice(self):
        super().draw()
        super().write_code()
        print("Sending the bill!")

fl=Freelancer()
fl.invoice()

