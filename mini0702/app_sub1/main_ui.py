import tkinter as tk

class AppWindow(tk.Frame):#frame
    def __init__(self, master=None, size=None, path=None):
        super().__init__(master)

        self.pack()#opencv frame

        self.create_widgets(path)

    def create_widgets(self, path):

        self.sub_fr = tk.Frame(self.master)#frame
        self.sub_fr.pack()



