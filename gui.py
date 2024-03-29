from genericpath import isfile
from math import floor
import tkinter as tk
from tkinter import Toplevel, messagebox,Listbox
from tkinter.filedialog import *
from canvas import Canvas
from numerical_control import Interpolation, _RELATIVE, _ABSOLUTE
from gcode import GCODES, Gcode, parser
import queue
import os

'''
TODO 
implement absolute and relative coords  [x]
implement interface commands            []
implement gcode file writes             [x]
refactor classes                        [x]
add config file for project settings    []  optional
last location update method             [x]
'''

interp = Interpolation()
dir_name = "./gcode_files"
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
        self.save_to_file_button = tk.Button(self.root,text = "Save to file", command=self.save_to_file)
        self.save_to_file_button.grid(row=1,column=3,columnspan=5,padx=5,pady=5)
        self.run_file_button = tk.Button(self.root, text= "Run file", command=self.run_file)
        self.run_file_button.grid(row=1,column=4,columnspan=5,padx=5,pady=5)
        self.entry = tk.Entry(self.root, width = 40)
        self.entry.grid(column=0,columnspan=5,row=1, padx=5, pady=5)
        self.entry.bind("<KeyRelease>", self.key_pressed)

        self.q = queue.Queue()


    def send_command(self):
        cmd = parser(self.get_text(self.entry))
        # print(cmd)
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
        try :
            if pop.focus_get() is not None:
                if event.keysym == 'Return':
                    file_name = pop_entry.get()
                    if file_name == "":
                        messagebox.showerror("Error", "Please enter a valid file name")
                    else:
                        self.save_to_file_helper(file_name, self.text_area)
                        pop.destroy()
        except NameError: 
            pass
        
        if event.keysym == 'Return': #send message key
            self.send_command()
            self.clear(self.entry)
        elif event.keysym == 'Delete': #delete key
            self.text_area.delete('1.0', 'end')
            Window.text_line_cnt = 0
        elif event.keysym == 'F5': #execute queue
            execute_queue(self.q, self.canvas)
        elif event.keysym == 'F1':
            self.canvas.clear_canvas()
            self.canvas._axis()
    
    def run_file(self):
        file_name = askopenfile(initialdir=dir_name, filetypes=[("Text files", "*.txt")])
        content = file_name.read()
        self.text_area.delete('1.0', 'end')
        self.canvas.clear_canvas()
        self.text_area.insert('end', "Running file: " + file_name.name + '\n', 'ok')
        insert_into_q_from_file(self.q,content)
        execute_queue(self.q, self.canvas)
    
 
     
    def save_to_file(self):
        global pop
        pop = Toplevel(self.root)
        pop.title("Save to file")
        pop.geometry("350x100")
        pop.config(bg="white")

        label = tk.Label(pop, text="Enter file name:")
        label.grid(row=0,column=0,columnspan=5,padx=5,pady=5)
        global pop_entry
        pop_entry = tk.Entry(pop, width = 40)
        pop_entry.grid(row=1,column=0,columnspan=4, padx=5, pady=5)
        pop_entry.bind("<KeyRelease>", self.key_pressed)

    def save_to_file_helper(self,file_name, text_area):
        
        #init dir
        try:
            os.mkdir(dir_name)
        except:
            print("directory already exists")

        #init file
        file_name = dir_name+"/"+file_name + ".txt"

        with open(file_name,"w") as gcode_file:
            tbr =text_area.get('1.0', 'end-1c')  #  '-1c' means the last line -> to be written
            tbr = tbr.split("\n")
            for line in tbr:
                if line[4::] == "Error: Invalid command":
                    continue
                gcode_file.write((str(parser(line[4::])))+"\n")

        messagebox.showinfo("Success", f"File saved successfully at {file_name}")

    def get_files(self):
        files = [f for f in os.listdir(dir_name) if isfile(dir_name+"/"+f)]
        return files
        
        
    def get_text_area(self):
        return self.text_area

    ### ENTRY METHODS ###

    def clear(self,entry):
        l = len(self.get_text(entry))
        entry.delete(0,l)

    def get_text(self,entry):
        return entry.get()

   
def execute_queue(q, canvas):
    while not q.empty():
        cmd = q.get(0)
        print(str(cmd))
        if cmd.get_code() == GCODES["line"]:
            canvas.draw_interpolated_line(interp.liniar_interpolation(cmd.x, cmd.y), False)
        elif cmd.get_code() == GCODES["arc counterclockwise"]:
            canvas.draw_interpolated_line(interp.arc_interpolation(cmd.x,cmd.y,cmd.i,cmd.j, -1), False)
        elif cmd.get_code() == GCODES["arc clockwise"]:
            canvas.draw_interpolated_line(interp.arc_interpolation(cmd.x,cmd.y,cmd.i,cmd.j, 1), False)
        elif cmd.get_code() == GCODES["absolute"]:
            interp._set_addressing(_ABSOLUTE)
        elif cmd.get_code() == GCODES["relative"]:
            interp._set_addressing(_RELATIVE)
        elif cmd.get_code() == GCODES["home"]:
            interp.home()
        elif cmd.get_code() == GCODES["fastline"]:
            canvas.draw_interpolated_line(interp.liniar_interpolation(cmd.x, cmd.y), True)


def insert_into_q_from_file(q, content):
        for line in content.split('\n'):
            words = line.split(' ')
            if words[0] in GCODES.values():
                for param in words[1::]:
                    if param[0] == 'x':
                        x = float(param[1::])
                        print(x)
                    if param[0] == 'y':
                        y = float(param[1::])  
                    if param[0] == 'i':
                        i = float(param[1::])
                    if param[0] == 'j':
                        j = float(param[1::])
                if words[0] == 'G02' or words[0] == 'G03':
                    cmd  = Gcode(words[0],x,y,i,j)
                    q.put(cmd)
                elif words[0] == 'G00' or words[0] == 'G01':
                    cmd = Gcode(words[0],x,y)
                    q.put(cmd)
                else:
                    q.put(Gcode(words[0]))


def main():
    window = Window()
    window.root.mainloop()
if __name__=="__main__":
    main()