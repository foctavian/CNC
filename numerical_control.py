from math import floor

class Interpolation():
    def __init__(self):
        pass

    # def __call__(self,x1,y1,x2,y2,command = 'liniar_interpolation'):
    #     if self.command not in dir(self):
    #         print("FUNCTION IS NOT AVAILABLE")
    #     else:
    #         func = getattr(self,command)

    def liniar_interpolation(self, x1, y1, x2, y2):
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            no_points = floor(max(abs(x2-x1), abs(y2-y1)))
            if no_points > 0:
                x_values = [x1 + (i* (x2-x1)/no_points) for i in range(no_points+1)]
                y_values = [y1 + (i* (y2-y1)/no_points) for i in range(no_points+1)]
                return zip(x_values, y_values)
