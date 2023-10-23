import gui
from gui import Point   

class Laser:
    def __init__(self):
        self.current_point = Point(gui._WIDTH/2,gui._HEIGTH/2 )

    def __str__(self):
        return f"Laser at x : {self.x} y : {self.y}"
    
    def move(self, x : float, y : float):
        self.x=x
        self.y=y
    

    