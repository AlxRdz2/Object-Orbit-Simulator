# Traspass the actual route to the parent directory
import sys
sys.path.append("..")
print(sys.path)

from src.models.celestial import CelestialBody
from src.models.window import Window
import matplotlib.pyplot as plt

# Instance to test the CelestialBody class using real data.
earth = CelestialBody("Earth", (0, 0), 5.972e24, 10)
print(earth)
moon = CelestialBody("Moon", (0, 384400), 7.342e22, 5)
print(moon)

# Calculate the gravitational force between Earth and Moon and print the result.
gravity_force = earth.calculate_gravity(moon)
print(f"Gravitational Force between Earth and Moon: {gravity_force:.2e} N")

# Instance of window object to test the animation of the celestial bodies.
window = Window("Celestial Simulation", limits=(20, 20), objects=[earth, moon])
window.animate(frames=120, interval=120)