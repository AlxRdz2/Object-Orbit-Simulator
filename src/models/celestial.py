from .body import Body

class CelestialBody(Body):
    def __init__(self, name, color, position, mass, radius):
        super().__init__(name, color, position, mass, radius)