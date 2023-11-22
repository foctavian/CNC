import re

GCODES = {
    "fastline"              : "G00",
    "line"                  : "G01",
    "arc clockwise"         : "G02",
    "arc counterclockwise"  : "G03",
    "absolute"              : "G90",
    "relative"              : "G91",
    "home"                  : "G28",
    "error"                 : "G99"
}

class Gcode():
    def __init__(self,code, x=0, y=0, i=0, j=0) : 
        self.code = code
        self.x = x
        self.y = y
        self.i=i
        self.j=j
        #self.command = f"{self.code} {self.x} {self.y} {self.i} {self.j}"


    def __str__(self) -> str:
        return f"{self.code} {self.x} {self.y}"
    

    def get_code(self):
        return self.code

def parser(command : str): # TODO REFACTOR THIS

    low = command.split(" ")

    if low[0] == "relative":
        return Gcode(GCODES["relative"])
    elif low[0] == "absolute":
        return Gcode(GCODES["absolute"])
    elif low[0] == "line":
        x=0
        y=0
        for i in range(1,len(low)):
            if low[i].startswith("x"):
                try:
                    x = (float(low[i][1:]))
                except: Gcode(GCODES["error"])
            elif low[i].startswith("y"):
                try:
                    y = (float(low[i][1:]))
                except: Gcode(GCODES["error"])
        return Gcode(GCODES["line"], x, y)
    elif low[0] == "home":
        return Gcode("home")
    elif low[0] == "arc":
        x=0
        y=0
        k=0 #instead of i because i was already in the existing code
        j=0
        if low[1] == "clockwise":
            for i in range(1,len(low)):
                if low[i].startswith("x"):
                    try:
                        x = (float(low[i][1:]))
                    except: Gcode(GCODES["error"])
                elif low[i].startswith("y"):
                    try:
                        y = (float(low[i][1:]))
                    except: Gcode(GCODES["error"])
                elif low[i].startswith("i"):
                    try:
                        k = (float(low[i][1:]))
                    except: Gcode(GCODES["error"])
                elif low[i].startswith("j"):
                    try:
                        j = (float(low[i][1:]))
                    except: Gcode(GCODES["error"])
            return Gcode(GCODES["arc clockwise"], x, y,k,j) 
        elif low[1] == "counterclockwise":
            
            for i in range(1,len(low)):
                if low[i].startswith("x"):
                    try:
                        x = (float(low[i][1:]))
                    except: Gcode(GCODES["error"])
                elif low[i].startswith("y"):
                    try:
                        y = (float(low[i][1:]))
                    except: Gcode(GCODES["error"])
                elif low[i].startswith("i"):
                    try:
                        k = (float(low[i][1:]))
                    except: Gcode(GCODES["error"])
                elif low[i].startswith("j"):
                    try:
                        j = (float(low[i][1:]))
                    except: Gcode(GCODES["error"])
            return Gcode(GCODES["arc counterclockwise"], x, y,k,j)
             
    elif low[0] == "fastline":
        x=0
        y=0
        
        for i in range(1,len(low)): # TODO : BEAUTIFY THIS
            if low[i].startswith("x"):
                try:
                    x = (float(low[i][1:]))
                except: Gcode(GCODES["error"])
            elif low[i].startswith("y"):
                try:
                    y = (float(low[i][1:]))
                except: Gcode(GCODES["error"])
            
        return Gcode(GCODES["fastline"], x, y)
    else:
        return Gcode(GCODES["error"])

