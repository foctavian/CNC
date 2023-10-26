import tkinter as tk
from numerical_control import Interpolation 
import math

_HEIGTH = 640
_WIDTH = 640
_CENTERX = _WIDTH/2
_CENTERY = _HEIGTH/2

class Canvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root,width = _WIDTH,height=_HEIGTH,bg = "white")
        self.clear_button = tk.Button(root, text = "Clear", command = self.clear_canvas)
        self.canvas.pack(side = tk.RIGHT)
        self._axis()
        #self.draw_interpolated_line(Interpolation().liniar_interpolation(152.5,65.7, 5.67,1))
        #self.draw_sinusoidal_wave(50,1, 1000000)
        #self.draw_circle(200,200,100)
        #self.draw_cos_wave(50,1,10000)


    def draw(event):
        x,y = event.x, event.y

    def draw_interpolated_line(self, list):
        size = 2
        for x,y in list:
            self.canvas.create_oval(x,y,x+size, y+size, fill = 'black', width=size)

    
    def draw_sinusoidal_wave(self, amplitude, frequency, num_points):
        points = []

        for i in range(num_points):
            x = (i / num_points) * _WIDTH
            y = _HEIGTH / 2 - amplitude * math.sin(2 * math.pi * frequency * (x / _WIDTH))
            points.append((x, y))

        self.canvas.create_line(points, fill="blue")



    def draw_cos_wave(self, amplitude, frequency, num_points):
        points = []

        for i in range(num_points):
            x = (i/num_points) * _WIDTH
            y = _HEIGTH / 2 - amplitude * math.cos(2*math.pi*frequency*(x/_WIDTH))
            points.append((x,y))
        self.canvas.create_line(points, fill = 'blue')



    def draw_circle(self,x,y,radius, num_points=360):
        angle_inc = 360 / num_points

        points = []

        for i in range (num_points):
            angle = math.radians(i * angle_inc)
            x_point = x+ radius * math.cos(angle)
            y_point = y + radius * math.sin(angle)
            points.append((x_point, y_point))

        self.canvas.create_polygon(points, outline='green', fill='')   


    def clear_canvas(canvas):
        canvas.delete('all')


    ### PRIVATE METHODS ###

    def _axis(self):
        self.canvas.create_line(_WIDTH/2+1,0,_WIDTH/2+1,_HEIGTH ,fill = 'red', width = 1)
        self.canvas.create_line(0,_HEIGTH/2+1,_WIDTH,_HEIGTH/2+1 ,fill = 'red', width = 1)
    

    def _center(self, x, y):
        return (x+_CENTERX, y+_CENTERY)

 


