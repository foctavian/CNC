from math import floor
import tkinter as tk
import canvas

class Entry:
    def __init__(self, root):
        self.entry = tk.Entry(root, width = 40)
        self.entry.pack(side=tk.BOTTOM)

class Window():
    def send_command():
        pass

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CNC")

        self.canvas = canvas.Canvas(self.root)
        self.text_area = tk.Text(self.root, width = 40, height=20)
        self.text_area.pack(side = tk.LEFT)
        self.send_button = tk.Button(self.root, text="Send", command=self.send_command)
        self.entry = Entry(self.root)
        self.send_button.pack(side=tk.BOTTOM)



def main():
    window = Window()
    window.root.mainloop()


if __name__=="__main__":
    main()