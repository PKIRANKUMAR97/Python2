# The Challenge: The Delivery Hierarchy
# Level 1 (Grandparent): Package
# __init__ accepts weight.
# Method calculate_cost() returns weight * 5 (Standard shipping rate).

# Level 2 (Parent): ExpressPackage
# Inherits from Package.
# __init__ accepts weight and speed.
# Overrides calculate_cost() to call the parent's cost and add a flat $10 "express fee."

# Level 3 (Child): InternationalPackage
# Inherits from ExpressPackage.
# __init__ accepts weight, speed, and country.
# Overrides calculate_cost() to call the parent's cost (which already includes the express fee) and multiplies the final result by 1.5 (customs tax).
#
# Your Tasks:
# Use super().__init__ in every child class to pass arguments up.
# Use super().calculate_cost() inside the overrides to "build" the total price layer by layer.
# Create an instance of InternationalPackage with a weight of 10kg, speed of "Fast", and country "Japan".
# Print the final cost.
# Tip for Level 3: It should look something like this: total = super().calculate_cost() * 1.5

class Package:
    def __init__(self, weight):
        self.weight = weight

    def calculate_cost(self):
        return self.weight * 5


class ExpressPackage(Package):
    def __init__(self, weight,speed):
        super().__init__(weight)
        self.speed = speed

    def calculate_cost(self):
        base_cost =super().calculate_cost()
        return base_cost + 10

class InternationalPackage(ExpressPackage):
    def __init__(self,weight,speed,country):
        super().__init__(weight,speed)
        self.country = country

    def calculate_cost(self):
        int_price = super().calculate_cost()
        return int_price * 1.5

ip_japan=InternationalPackage(10,"Fast","Japan")

final_price = ip_japan.calculate_cost()
print(final_price)





