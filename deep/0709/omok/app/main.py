import tkinter as tk
import omok.app.main_ui as win
import omok.app.make_widgets as mkw
import omok.app.service as s

def main():
    root = tk.Tk()
    app = win.AppWindow(root)

    mkw.make(app)
    s.service() #ui 이벤트와 상관없이 수행해야하는 기능
    app.mainloop()
