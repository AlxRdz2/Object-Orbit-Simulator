from src.models.body import Body

class ExternalBody(Body):
    def __init__(self, name, color, position, mass, radius, velocity=(0, 0)):
        super().__init__(name, color, position, mass, radius, velocity)

    def __str__(self):
        return f"External Body: {self.name}, Position: {self.position}, Mass: {self.mass}, Radius: {self.radius}, Velocity: {self.velocity}"