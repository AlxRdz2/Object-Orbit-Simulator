from .body import Body

class CelestialBody(Body):
    def __init__(self, name, color, position, mass, radius, velocity=(0, 0)):
        super().__init__(name, color, position, mass, radius, velocity)

    def __str__(self):
        return f"CelestialBody(name={self.name}, color={self.color}, position={self.position}, mass={self.mass}, radius={self.radius}), velocity={self.velocity})"