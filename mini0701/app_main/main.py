import tkinter as tk
import app_main.main_ui as win
import app_main.make_widgets as mkw
import app_main.service as s

def main():
    root = tk.Tk()
    app = win.AppWindow(root)
    root.geometry('%dx%d+%d+%d' % (400, 200, 10, 10))
    mkw.make(app,s.service)
    s.service() #ui 이벤트와 상관없이 수행해야하는 기능
    app.mainloop()
