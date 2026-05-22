from src.models.body import Body

class ExternalBody(Body):
    def __init__(self, name, position, mass, radius, velocityX, velocityY, direction):
        super().__init__(name, position, mass, radius)
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.direction = direction

    def __str__(self):
        return f"External Body: {self.name}, Position: {self.position}, Mass: {self.mass}, Radius: {self.radius}, Velocity: ({self.velocityX}, {self.velocityY}), Direction: {self.direction}"