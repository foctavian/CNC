from math import floor
import tkinter as tk
from canvas import Canvas
from numerical_control import Interpolation
from gcode import GCODES, parser
'''
TODO 
implement absolute and relative coords  []
implement interface commands            []
implement gcode file writes             []
refactor classes                        [x]
add config file for project settings    [] 
'''

class Window():
    text_line_cnt = 0
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CNC")
        self.canvas = Canvas(self.root)
        self.text_area = tk.Text(self.root, width = 40, height=40)
        self.text_area.grid(row=0,column=0,columnspan=5,padx=5,pady=5)
        #tags for text area
        self.text_area.tag_config('err', foreground="red")
        self.text_area.tag_config('ok', foreground="green")

        gcode_file = open("./gcode.txt", "w")
        self.entry = tk.Entry(self.root, width = 40)
        self.entry.grid(column=0,columnspan=5,row=1, padx=5, pady=5)
        self.entry.bind("<KeyRelease>", self.key_pressed)
        

        q = []
        #self.canvas.draw_interpolated_line(Interpolation().circular_interpolation(10,-5,50))


    def send_command(self):
        print(self.get_text(self.entry))
        cmd = parser(self.get_text(self.entry))
        print(cmd.get_code())
        if cmd.get_code() == GCODES["error"] : 
            self.text_area.insert('end', str(Window.text_line_cnt) + '>> ')
            Window.text_line_cnt += 1
            self.text_area.insert('end', "Error: Invalid command\n", 'err')
        else:
            self.text_area.insert('end', str(Window.text_line_cnt) + '>> ')
            Window.text_line_cnt += 1
            self.text_area.insert('end', self.get_text(self.entry) + '\n', 'ok')
            

    def key_pressed(self,event):
        if event.keysym == 'Return': #send message key
            self.send_command()
            self.clear(self.entry)
        elif event.keysym == 'Delete': #delete key
            self.text_area.delete('1.0', 'end')
            Window.text_line_cnt = 0
        elif event.keysym == 'F5':
            #start the queue of commands
            pass
        
            

    ### ENTRY METHODS ###

    def clear(self,entry):
        l = len(self.get_text(entry))
        entry.delete(0,l)

    def get_text(self,entry):
        return entry.get()

   



def main():
    window = Window()
    window.root.mainloop()
if __name__=="__main__":
    main()