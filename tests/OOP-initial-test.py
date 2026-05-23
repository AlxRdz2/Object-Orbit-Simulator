# Traspass the actual route to the parent directory
import sys
sys.path.append("..")
print(sys.path)

from src.models.celestial import CelestialBody
from src.models.window import Window

# Instance to test the CelestialBody class using real data.
earth = CelestialBody("Earth", (0, 0), 5.97e24, 6371) # Position in km, mass in kg, radius in km
print(earth)

moon = CelestialBody("Moon", (384400, 0), 7.35e22, 1737) # Position in km (average distance from Earth), mass in kg, radius in km
print(moon)

# Calculate the gravitational force between Earth and Moon and print the result.
# gravity_force = moon.calculate_gravity(earth)
# print(f"Gravitational Force between Earth and Moon: {gravity_force:.2e} N")
# acceleration = moon.calculate_aceleration(earth)
# print(f"Acceleration of the Moon due to Earth's gravity: {acceleration:.2e} m/s^2")

# Instance of window object to test the animation of the celestial bodies.
window = Window(limits=(5e5, 5e5), objects=[earth, moon])
window.animate(frames=120, interval=120)