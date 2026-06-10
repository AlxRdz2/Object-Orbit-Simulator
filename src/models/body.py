from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import math

class Body(ABC):
    @abstractmethod
    def __init__(self, name, color, position, mass, radius, velocity=(0, 0)):
        self.name = name
        self.color = color
        self.position = position
        self.mass = mass
        self.radius = radius
        self.velocity = velocity

    def draw(self):
        # Uses the radius to determine the size of the circle representing the body
        plt.scatter(self.position[0], self.position[1], s=self.radius, label=self.name, color=self.color)
        # Shows the name of the body next to the point
        # plt.text(self.position[0], self.position[1], self.name, fontsize=9, color=self.color)
        return self

    def update_position(self, new_position):
        # Updates the position of the object.
        self.position = new_position
        return self

    def update_velocity(self, new_velocity):
        # Updates the velocity of the object.
        self.velocity = new_velocity
        return self     

    def calculate_gravity(self, other_body):
        # Parameters for the gravitational force calculation
        # We treat the distances all in km and masses in kg
        G = 6.6743e-11 # Gravitational constant in m^3 kg^-1 s^-2
        m1 = self.mass
        m2 = other_body.mass
        r = self.calculate_distance(other_body)  # Distance between the two bodies in km
        if r == 0:
            return 0  # Avoid division by zero
        force = G * (m1 * m2) / r**2
        return force

    def calculate_acceleration(self, other_body):
        # Calculate the acceleration of self due to the gravitational force from other_body.
        force = self.calculate_gravity(other_body)
        acceleration = force / self.mass  # F = m * a => a = F / m
        return acceleration
    
    def calculate_distance(self, other_body):
        # Calculate the distance between self and other_body.
        distance = math.sqrt((self.position[0] - other_body.position[0])**2 + (self.position[1] - other_body.position[1])**2)
        return distance
    
    def euler_update(self, other_body, time_step):
        # Update the position and velocity of the body using Euler's method.
        # This is a simple numerical method for solving ordinary differential equations.

        # Calculate the acceleration due to gravity from the other body
        acceleration = self.calculate_acceleration(other_body)
        # Update velocity based on acceleration
        r = self.calculate_distance(other_body)
        if r == 0:
            return # Avoid division by zero
        acceleration_x = acceleration * (other_body.position[0] - self.position[0]) / r
        acceleration_y = acceleration * (other_body.position[1] - self.position[1]) / r

        new_velocity_x = self.velocity[0] + acceleration_x * time_step
        new_velocity_y = self.velocity[1] + acceleration_y * time_step
        self.update_velocity((new_velocity_x, new_velocity_y))
        # Update position based on velocity
        new_position_x = self.position[0] + self.velocity[0] * time_step
        new_position_y = self.position[1] + self.velocity[1] * time_step
        self.update_position((new_position_x, new_position_y))
        return self
        
    def __str__(self):
        return f"{self.name}: Position={self.position}, Mass={self.mass}, Radius={self.radius}"
    
# class BodyFactory:
#     @staticmethod
#     def create_body(name, color, position, mass, radius, velocity=(0, 0)):
#         return Body(name, color, position, mass, radius, velocity)
    