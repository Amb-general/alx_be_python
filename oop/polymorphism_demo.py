import math

class Shape:
    def area(self):
        """Base method that should be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override area() method")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Rectangle class that inherits from Shape."""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculates rectangle area: length * width"""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Circle class that inherits from Shape."""
        self.radius = radius
    
    def area(self):
        """Calculates circle area: π * radius²"""
        return math.pi * self.radius ** 2
