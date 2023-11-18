import tkinter as tk
import math

class ArcDrawer:
    def __init__(self, master, center_x, center_y, radius):
        self.master = master
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

    def draw_arc(self, start_point, end_point):
        points = self.calculate_arc_points(start_point, end_point)
        self.canvas.create_line(points, smooth=tk.TRUE, width=2)

    def calculate_arc_points(self, start_point, end_point):
        points = []
        no_points = 100  # Adjust the number of points based on the desired smoothness

        start_angle = math.atan2(start_point[1] - self.center_y, start_point[0] - self.center_x)
        end_angle = math.atan2(end_point[1] - self.center_y, end_point[0] - self.center_x)

        for i in range(no_points + 1):
            angle = start_angle + i * ((end_angle - start_angle) / no_points)
            x = self.center_x + self.radius * math.cos(angle)
            y = self.center_y + self.radius * math.sin(angle)
            points.extend([x, y])

        return points

# Example usage
root = tk.Tk()
drawer = ArcDrawer(root, center_x=200, center_y=200, radius=100)
drawer.draw_arc(start_point=(200, 100), end_point=(300, 300))
root.mainloop()
