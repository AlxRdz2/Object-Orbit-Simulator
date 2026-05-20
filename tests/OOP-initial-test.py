# Traspass the actual route to the parent directory
import sys
sys.path.append("..")
print(sys.path)

from src.models.planet import Planet

earth = Planet("Earth", (0, 0), 5.972e24, 6371)
print(earth)