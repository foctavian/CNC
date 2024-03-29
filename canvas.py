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
        

    def draw(event):
        x,y = event.x, event.y

    def draw_interpolated_line(self, list, rapid):
        size = 2
        for x,y in list:
            (x,y) = self._center(x,y)
            self.canvas.create_oval(x,y,x+size, y+size, fill = 'black', width=size)
            
            #fastline or slowline
            if rapid:
                self.canvas.update()
            else:
                self.canvas.update()

                sleep(0.05)
            
    def clear_canvas(self):
        self.canvas.delete("all")
        self._axis()

    ### PRIVATE METHODS ###

    def _axis(self):
        self.canvas.create_line(_WIDTH/2+1,0,_WIDTH/2+1,_HEIGTH ,fill = 'red', width = 1)
        self.canvas.create_line(0,_HEIGTH/2+1,_WIDTH,_HEIGTH/2+1 ,fill = 'red', width = 1)
    

    def _center(self, x, y):
        return (x+_CENTERX, -y+_CENTERY)

 


