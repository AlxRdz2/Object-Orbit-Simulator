# Traspass the actual route to the parent directory
import sys
sys.path.append("..")
print(sys.path)

from src.models.celestial import CelestialBody
from src.models.window import Window
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


# Instance to test the CelestialBody class using specific data.
earth = CelestialBody("Earth", (0, 0), 100, 10)
print(earth)
moon = CelestialBody("Moon", (5, 5), 50, 5)
print(moon)

# Show the planet using the draw method [Static]
# earth.draw()
# plt.title("Planet Visualization")
# plt.xlabel("X Position")
# plt.ylabel("Y Position")
# plt.show() 

# Show the planet using the draw method [Animated]
# fig, ax = plt.subplots() # Create a figure and axis for the animation

# # Set limits and labels for the plot
# ax.set_xlim(-20, 20)
# ax.set_ylim(-20, 20)

# # Set title and labels for the plot
# ax.set_title("Planet Visualization")
# ax.set_xlabel("X Position")
# ax.set_ylabel("Y Position")

# # Constraints the view to a specific range to better visualize the movement
# ax.set_xlim(-20, 20)
# ax.set_ylim(-20, 20)

# def animate(i):
#     # Simulate movement by updating the position of the Earth
    
#     # Linearly movement.
#     # new_x = earth.position[0] + 0.01 * i
#     # new_y = earth.position[1] + 0.1 * i
#     # earth.update_position((new_x, new_y))

#     # Circular movement.
#     new_x = 10 * math.cos(0.1 * i)
#     new_y = 10 * math.sin(0.1 * i)
#     earth.update_position((new_x, new_y))
    
#     # Clear the previous frame and redraw the object and other plot parameters at its new position
#     ax.clear()
#     earth.draw()
#     ax.set_title("Planet Visualization")
#     ax.set_xlabel("X Position")
#     ax.set_ylabel("Y Position")
#     ax.set_xlim(-20, 20)
#     ax.set_ylim(-20, 20)

# ani = animation.FuncAnimation(fig, animate, frames=120, interval=120)
# plt.show()

window = Window("Celestial Simulation", limits=(20, 20), objects=[earth, moon])
window.animate(frames=120, interval=120)