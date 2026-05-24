from src.models.body import Body

class ExternalBody(Body):
    def __init__(self, name, color, position, mass, radius, velocity, direction):
        super().__init__(name, color, position, mass, radius)
        self.velocity = velocity # Tuple (velocityX, velocityY)
        self.direction = direction # Direction in degrees (0-360)
    
    def euler_update(self, other_body, time_step):
        return super().euler_update(other_body, time_step, velocity=self.velocity, direction=self.direction)

    def __str__(self):
        return f"External Body: {self.name}, Position: {self.position}, Mass: {self.mass}, Radius: {self.radius}, Velocity: ({self.velocity[0]}, {self.velocity[1]}), Direction: {self.direction}"