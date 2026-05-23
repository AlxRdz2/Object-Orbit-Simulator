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
        for obj in self.objects:
            obj.euler_update(self.objects[0], time_step=1)  # Update the position of the object based on the first object (for simplicity)
            obj.draw()

    def clear(self):
        self.ax.clear()
    
    def animate(self, frames=100, interval=100):
        ani = animation.FuncAnimation(self.fig, self.update, frames=frames, interval=interval)
        plt.show()

    def update(self, frame):
        self.clear()
        self.draw()