import unittest
import sys
import math

sys.path.append("..")
from src.models.celestial import CelestialBody
from src.models.external import ExternalBody

class TestOrbitalPhysics(unittest.TestCase):

    def test_earth_surface_gravity(self):
        # Real data using m and kg.
        earth_mass = 5.972e24 
        earth_radius = 6371000
        
        # Earth in origin.
        earth = CelestialBody("Earth", "blue", (0, 0), earth_mass, earth_radius)
        
        # Position a 1kg satellite just at the surface (x-axis)
        satellite = ExternalBody("Satellite", "gray", (earth_radius, 0), 1.0, 1)
        
        # Calculate the acceleration
        acceleration = satellite.calculate_acceleration(earth)
        # Just take two decimal places for the assertion, since we are using approximated values for mass and radius of Earth.
        acceleration = math.floor(acceleration * 100) / 100 # Round to 2 decimal places
        
        # Verify that it is ~9.81 m/s^2 (with a tolerance of 2 decimal places)
        self.assertAlmostEqual(acceleration, 9.81, places=2)

if __name__ == '__main__':
    unittest.main()