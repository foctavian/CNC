from math import floor
import tkinter as tk
from canvas import Canvas
'''
TODO 
implement absolute and relative coords  []
implement interface commands            []
implement gcode file writes             []
refactor classes                        []
'''

class TextArea():
    def __init__(self,root):
        text_area = tk.Text(root, width = 40, height=40)
        text_area.grid(row=0,column=0,columnspan=5,padx=5,pady=5)
        gcode_file = open("./gcode.txt", "w")


class Entry():
    def __init__(self, root):
        self.entry = tk.Entry(root, width = 40)
        self.entry.grid(column=0,columnspan=5,row=1, padx=5, pady=5)

    def get_text(self):
        return self.entry.get()
    
    def clear(self):
        l = len(self.get_text())
        self.entry.delete(0,l)


class Window():
    def send_command(self):
        print(self.entry.get_text())
        self.text_area.text_area.insert('end',self.entry.get_text() + '\n')
        
    def key_pressed(self,event):
        if event.keysym == 'Return': #send message key
            self.send_command()
            self.entry.clear()
        elif event.keysym == 'Delete': #delete key
            self.text_area.text_area.delete('1.0', 'end')

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CNC")
        self.canvas = Canvas(self.root)
        self.text_area = TextArea(self.root)
        entry = Entry(self.root)
        entry.entry.bind("<KeyRelease>", self.key_pressed)



def main():
    window = Window()
    window.root.mainloop()

if __name__=="__main__":
    main()