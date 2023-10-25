import tkinter as tk
from numerical_control import Interpolation 

_HEIGTH = 640
_WIDTH = 640

class Canvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root,width = _WIDTH,height=_HEIGTH,bg = "white")
        self.clear_button = tk.Button(root, text = "Clear", command = self.clear_canvas)
        self.canvas.pack(side = tk.RIGHT)
        self._axis()
        self.draw_interpolated_line(Interpolation().liniar_interpolation(152.5,65.7, 5.67,1))

    def draw(event):
        x,y = event.x, event.y

    def draw_interpolated_line(self, list):
        size = 2
        for x,y in list:
            self.canvas.create_oval(x,y,x+size, y+size, fill = 'black', width=size)

  
    def _axis(self):
        self.canvas.create_line(_WIDTH/2+1,0,_WIDTH/2+1,_HEIGTH ,fill = 'red', width = 1)
        self.canvas.create_line(0,_HEIGTH/2+1,_WIDTH,_HEIGTH/2+1 ,fill = 'red', width = 1)
    

    def clear_canvas(canvas):
        canvas.delete('all')


