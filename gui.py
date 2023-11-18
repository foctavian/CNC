from math import floor
import tkinter as tk
from canvas import Canvas
from numerical_control import Interpolation, _RELATIVE, _ABSOLUTE
from gcode import GCODES, parser
import queue
'''
TODO 
implement absolute and relative coords  [x]
implement interface commands            []
implement gcode file writes             []
refactor classes                        [x]
add config file for project settings    [] 
last location update method             []
'''

interp = Interpolation()


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
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical",command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        gcode_file = open("./gcode.txt", "w")
        self.entry = tk.Entry(self.root, width = 40)
        self.entry.grid(column=0,columnspan=5,row=1, padx=5, pady=5)
        self.entry.bind("<KeyRelease>", self.key_pressed)
        

        self.q = queue.Queue()
        #self.canvas.draw_interpolated_line(Interpolation().circular_interpolation(10,-5,50))


    def send_command(self):
        print(self.get_text(self.entry))
        cmd = parser(self.get_text(self.entry))
        #print(cmd.get_code())
        if cmd.get_code() == GCODES["error"] : 
            self.text_area.insert('end', str(Window.text_line_cnt) + '>> ')
            Window.text_line_cnt += 1
            self.text_area.insert('end', "Error: Invalid command\n", 'err')
        else:
            self.text_area.insert('end', str(Window.text_line_cnt) + '>> ')
            Window.text_line_cnt += 1
            self.text_area.insert('end', self.get_text(self.entry) + '\n', 'ok')
            self.q.put(cmd)
            

    def key_pressed(self,event):
        if event.keysym == 'Return': #send message key
            self.send_command()
            self.clear(self.entry)
        elif event.keysym == 'Delete': #delete key
            self.text_area.delete('1.0', 'end')
            Window.text_line_cnt = 0
        elif event.keysym == 'F5': #execute queue
            execute_queue(self.q, self.canvas)
        

    ### ENTRY METHODS ###

    def clear(self,entry):
        l = len(self.get_text(entry))
        entry.delete(0,l)

    def get_text(self,entry):
        return entry.get()

   
def execute_queue(q, canvas):
    while not q.empty():
        cmd = q.get(0)
        #print(cmd.get_code())
        if cmd.get_code() == GCODES["line"]:
            canvas.draw_interpolated_line(interp.liniar_interpolation(cmd.x, cmd.y), False)
        elif cmd.get_code() == GCODES["arc counterclockwise"]:
            canvas.draw_interpolated_line(interp.arc_interpolation(cmd.x,cmd.y,cmd.i,cmd.j), True)
        elif cmd.get_code() == GCODES["arc clockwise"]:
            pass
        elif cmd.get_code() == GCODES["absolute"]:
            interp._set_addressing(_ABSOLUTE)
        elif cmd.get_code() == GCODES["relative"]:
            interp._set_addressing(_RELATIVE)
        elif cmd.get_code() == GCODES["home"]:
            interp.home()
        elif cmd.get_code() == GCODES["fastline"]:
            canvas.draw_interpolated_line(interp.liniar_interpolation(cmd.x, cmd.y), True)

def main():
    window = Window()
    window.root.mainloop()
if __name__=="__main__":
    main()