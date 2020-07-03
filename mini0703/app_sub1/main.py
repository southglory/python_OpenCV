import tkinter as tk
import app_sub1.main_ui as win
import app_sub1.make_widgets as mkw
import app_sub1.service_Video as s1
import app_sub1.service_Student_Member as s2

def main():
    root = tk.Tk()
    app = win.AppWindow(root)
    root.geometry('%dx%d+%d+%d' % (500, 200, 410, 10))#위치 설정
    ser1=s1.video_service(app)
    ser2 = s2.StudentMemberDao()
    mkw.make(app,ser1,ser2)
    app.mainloop()


