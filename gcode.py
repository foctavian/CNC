import re

GCODES = {
    "line"                  : "G01",
    "arc clockwise"         : "G02",
    "arc counterclockwise"  : "G03",
    "absolute"              : "G90",
    "relative"              : "G91",
    "home"                  : "G28",
    "error"                 : "G00"
}

class Gcode():
    def __init__(self,code, x=0, y=0) : 
        self.code = code
        self.x = x
        self.y = y


    def __str__(self) -> str:
        return f"{self.code} {self.x} {self.y}"
    

    def get_code(self):
        return self.code

def parser(command : str):

    low = command.split(" ")

    if low[0] == "relative":
        return Gcode(GCODES["relative"])
    elif low[0] == "absolute":
        return Gcode(GCODES["absolute"])
    elif low[0] == "line":
        x=[]
        y=[]
        for i in range(1,len(low)):
            if low[i].startswith("x"):
                try:
                    float(low[i][1:])
                    x.append(float(low[i][1:]))
                except: Gcode(GCODES["error"])
            elif low[i].startswith("x"):
                try:
                    float(low[i][1:])
                    y.append(float(low[i][1:]))
                except: Gcode(GCODES["error"])
        return Gcode(GCODES["line"], x, y)
    elif low[0] == "home":
        return Gcode("home")
    else:
        return Gcode(GCODES["error"])

