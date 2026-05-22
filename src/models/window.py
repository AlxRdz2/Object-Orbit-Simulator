import matplotlib.animation as animation
import matplotlib.pyplot as plt
import math

class Window:
    def __init__(self, title="Window", limits=(800, 600), objects=[]):
        self.title = title
        self.limits = limits
        self.fig, self.ax = plt.subplots()
        self.ax.set_title(self.title)
        self.objects = objects
        self.ax.set_xlim(-self.limits[0], self.limits[0])
        self.ax.set_ylim(-self.limits[1], self.limits[1])

    def draw(self):
        self.ax.set_title(self.title)
        self.ax.set_xlim(-self.limits[0], self.limits[0])
        self.ax.set_ylim(-self.limits[1], self.limits[1])
        self.update_objects()  # Update the positions of objects before drawing
        for obj in self.objects:
            obj.draw()

    def clear(self):
        self.ax.clear()
    
    def animate(self, frames=100, interval=100):
        # Error. Window.update() takes 1 positional argument but 2 were given.
        # print(self.update.__code__.co_varnames[:self.update.__code__.co_argcount])  # Check the argument sent to the update method.
        ani = animation.FuncAnimation(self.fig, self.update, frames=frames, interval=interval)
        plt.show()

    def update(self, frame):
        self.clear()
        self.draw()

    # Temporally, we can add a method to update the position of objects in the window for animation purposes.
    def update_objects(self):
        for obj in self.objects:
            # Circular movement for demonstration purposes.
            new_x = 10 * math.cos(0.1 * obj.position[0])
            new_y = 10 * math.sin(0.1 * obj.position[1])
            obj.update_position((new_x, new_y))