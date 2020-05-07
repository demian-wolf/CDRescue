import tkinter as tk
import tkinter.ttk as ttk


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CDRescue")
        self.resizable(False, False)

        self.create_wgts()
        
    def create_wgts(self):
        pass

if __name__ == "__main__":
    Main().mainloop()
