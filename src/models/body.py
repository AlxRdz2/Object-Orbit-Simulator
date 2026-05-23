from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import math

class Body(ABC):
    @abstractmethod
    def __init__(self, name, position, mass, radius):
        self.name = name
        self.position = position
        self.mass = mass
        self.radius = radius
    
    def draw(self):
        # Uses the radius to determine the size of the circle representing the body
        plt.scatter(self.position[0], self.position[1], s=self.radius, label=self.name)
        # Shows the name of the body next to the point
        plt.text(self.position[0], self.position[1], self.name, fontsize=9)
        return self

    def update_position(self, new_position):
        # Updates the position of the object.
        self.position = new_position
        return self     

    def calculate_gravity(self, other_body):
        # Parameters for the gravitational force calculation
        # We treat the distances all in km and masses in kg
        G = 6.674e-17 # Gravitational constant in km^3 kg^-1 s^-2 and we will get the force in Newtons (N)
        m1 = self.mass
        m2 = other_body.mass
        r = ((self.position[0] - other_body.position[0])**2 + (self.position[1] - other_body.position[1])**2)
        r = math.sqrt(r)
        if r == 0:
            return 0  # Avoid division by zero
        force = G * (m1 * m2) / r**2
        return force

    def calculate_aceleration(self, other_body):
        # Calculate the acceleration of self due to the gravitational force from other_body.
        force = self.calculate_gravity(other_body)
        acceleration = force / self.mass  # F = m * a => a = F / m
        return acceleration
    
    def euler_update(self, other_body, time_step):
        # Update the position and velocity of the body using Euler's method.
        # This is a simple numerical method for solving ordinary differential equations.
        # For simplicity, we will assume that the velocity is updated based on the acceleration due to gravity.
        acceleration = self.calculate_aceleration(other_body)
        # Update velocity (assuming initial velocity is zero for simplicity)
        velocity = acceleration * time_step
        # Update position based on velocity
        new_x = self.position[0] + velocity * time_step
        new_y = self.position[1] + velocity * time_step
        self.update_position((new_x, new_y))
    
    def __str__(self):
        return f"{self.name}: Position={self.position}, Mass={self.mass}, Radius={self.radius}"