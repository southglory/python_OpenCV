import tkinter as tk
import app_sub1.main_ui as win
import app_sub1.make_widgets as mkw
import app_sub1.service as s

def main():
    root = tk.Tk()
    app = win.AppWindow(root)
    root.geometry('%dx%d+%d+%d' % (500, 200, 410, 10))#위치 설정
    ser=s.video_service(app)
    mkw.make(app,ser)
    app.mainloop()


