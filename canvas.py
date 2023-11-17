import time
import tkinter as tk
from numerical_control import Interpolation 
import math
from time import sleep

_HEIGTH = 640
_WIDTH = 640
_CENTERX = _WIDTH/2
_CENTERY = _HEIGTH/2


class Canvas:
    def __init__(self,root):
        self.canvas = tk.Canvas(root,width = _WIDTH,height=_HEIGTH,bg = "white")
        self.clear_button = tk.Button(root, text = "Clear", command = self.clear_canvas)
        self.canvas.grid(column=5, columnspan=5)
        self._axis()
        #self.draw_interpolated_line(Interpolation().liniar_interpolation(-50,125,55, -100))
        #self.draw_interpolated_line(Interpolation().circular_interpolation(-100,50,40))

    def draw(event):
        x,y = event.x, event.y

    def draw_interpolated_line(self, list):
        size = 2
        for x,y in list:
            (x,y) = self._center(x,y)
            #print(f"{x}  {y}")
            time.sleep(0.05)
            self.canvas.create_oval(x,y,x+size, y+size, fill = 'black', width=size)
            self.canvas.update()
        
            
    def clear_canvas(canvas):
        canvas.delete('all')


    ### PRIVATE METHODS ###

    def _axis(self):
        self.canvas.create_line(_WIDTH/2+1,0,_WIDTH/2+1,_HEIGTH ,fill = 'red', width = 1)
        self.canvas.create_line(0,_HEIGTH/2+1,_WIDTH,_HEIGTH/2+1 ,fill = 'red', width = 1)
    

    def _center(self, x, y):
        return (x+_CENTERX, -y+_CENTERY)

 


