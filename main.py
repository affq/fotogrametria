from fun import *
import tkinter as tk

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Projektant nalotu fotogrametrycznego")
        self.root.geometry("800x600")
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()