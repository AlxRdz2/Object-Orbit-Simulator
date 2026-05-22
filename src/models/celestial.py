from .body import Body

class CelestialBody(Body):
    def __init__(self, name, position, mass, radius):
        super().__init__(name, position, mass, radius)