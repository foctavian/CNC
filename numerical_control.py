from math import floor
import math

_RELATIVE = 0
_ABSOLUTE = 1

class Interpolation():
    def __init__(self):
        self._LASTX = 0.0  # Declare _LASTX as an instance attribute
        self._LASTY = 0.0  # Declare _LASTY as an instance attribute
        self._MODE = _RELATIVE
        self._set_addressing()  # sets the default addressing to absolute

    def liniar_interpolation(self, x2, y2, x1=None, y1=None):
        #POSITIONING CHECK
        if x1 is None and y1 is None :
            if self._MODE == _RELATIVE:
                x1 = self._LASTX
                y1 = self._LASTY
            else: x1 = 0.0; y1 = 0.0

        self._LASTX = x2  # Update _LASTX
        self._LASTY = y2  # Update _LASTY
        print(f"last loc: {x1, y1}")
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            no_points = floor(max(abs(x2 - x1), abs(y2 - y1)))
            if no_points > 0:
                x_values = [x1 + (i * (x2 - x1) / no_points) for i in range(no_points + 1)]
                y_values = [y1 + (i * (y2 - y1) / no_points) for i in range(no_points + 1)]

                return zip(x_values, y_values)
            
    def circular_interpolation(self,x,y,radius,num_points=360):
        x_values = [x+radius*math.cos(math.radians(i)) for i in range(num_points)]
        y_values = [y+radius*math.sin(math.radians(i)) for i in range(num_points)]
        #_LAST_LOC = (x_values[len(x_values)-1], y_values[len(y_values)-1])
        return zip(x_values, y_values)
    
    def arc_interpolation(self, x, y, radius, start_angle, end_angle):
        no_points = 360
        start_angle_rad = math.radians(start_angle)/no_points
        end_angle_rad = math.radians(end_angle)/no_points

        step_size = (end_angle_rad-start_angle_rad)

        if no_points > 0 : 
            x_values = [x + radius *math.cos(start_angle_rad + i*step_size) for i in range (no_points)]
            y_values = [y + radius *math.sin(start_angle_rad + i*step_size) for i in range (no_points)]
            #_LAST_LOC = (x_values[len(x_values)-1], y_values[len(y_values)-1])
            return zip(x_values, y_values)

    def home(self):
        self._LASTX = 0.0
        self._LASTY = 0.0
    ### PRIVATE METHODS ###

    #changes the default mode of addressing 
    def _set_addressing(self,mode = _RELATIVE):
        _MODE = mode
