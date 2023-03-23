# 24. Write a class that represents a circle.The circle should have a radius, a diameter, and an area. 
# It should also have a nice string representation.

import math

class circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * self.radius
        self.area = math.pi * (self.radius**2) 

    def __str__(self):
        return f"Circle with radius {self.radius} has a diameter of {self.diameter} and total area of circle is {self.area: .2f}"

r = float(input('Enter the radius :'))    
c1 = circle(r)
print(c1)