from abc import ABC, abstractmethod

class Body(ABC):
    @abstractmethod
    def __init__(self, name, position, mass, radius):
        self.name = name
        self.position = position
        self.mass = mass
        self.radius = radius
    
    def draw(self):
        # Placeholder for drawing the body
        pass

    def update_position(self):
        # Placeholder for updating the position of the body
        pass

    def calculate_gravity(self, other_body):
        # Placeholder for calculating gravitational force between this body and another body
        pass

    def __str__(self):
        return f"{self.name}: Position={self.position}, Mass={self.mass}, Radius={self.radius}"