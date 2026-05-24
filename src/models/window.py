import matplotlib.animation as animation
import matplotlib.pyplot as plt
import math

class Window:
    def __init__(self, limits=(800, 600), objects=[]):
        self.limits = limits
        self.fig, self.ax = plt.subplots()
        self.objects = objects
        self.ax.set_xlim(-self.limits[0], self.limits[0])
        self.ax.set_ylim(-self.limits[1], self.limits[1])
        plt.axis("off")  # Hide axes for better visualization

    def draw(self):
        self.ax.set_xlim(-self.limits[0], self.limits[0])
        self.ax.set_ylim(-self.limits[1], self.limits[1])
        plt.axis("off")  # Hide axes for better visualization
        # For each object in the window, we will call the euler update to update their positions
        # and then we will call the draw method to draw them on the window.
        for obj in self.objects:
            # For each object we compare all the other objects to calculate the gravitational force and update the position accordingly.
            for other_obj in self.objects:
                if obj != other_obj:
                    obj.euler_update(other_obj, time_step=1)
            obj.draw()
        return self

    def clear(self):
        self.ax.clear()
    
    def animate(self, frames=200, interval=10):
        ani = animation.FuncAnimation(self.fig, self.update, frames=frames, interval=interval)
        plt.show()

    def update(self, frame):
        self.clear()
        self.draw()