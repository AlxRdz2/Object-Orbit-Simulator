from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class Body(ABC):
    @abstractmethod
    def __init__(self, name, position, mass, radius):
        self.name = name
        self.position = position
        self.mass = mass
        self.radius = radius
    
    def draw(self):
        # Uses the radius to determine the size of the circle representing the body
        plt.scatter(self.position[0], self.position[1], s=self.radius*100, label=self.name)
        # Shows the name of the body next to the point
        plt.text(self.position[0], self.position[1], self.name, fontsize=9)
        return self

    def update_position(self, new_position):
        # Updates the position of the object.
        self.position = new_position
        return self     

    def calculate_gravity(self, other_body):
        # Parameters for the gravitational force calculation
        G = 6.67430e-11  # Gravitational constant
        m1 = self.mass
        m2 = other_body.mass
        r = ((self.position[0] - other_body.position[0]) ** 2 + (self.position[1] - other_body.position[1]) ** 2) ** 0.5
        if r == 0:
            return 0  # Avoid division by zero
        force = G * (m1 * m2) / r**2
        return force

    def __str__(self):
        return f"{self.name}: Position={self.position}, Mass={self.mass}, Radius={self.radius}"