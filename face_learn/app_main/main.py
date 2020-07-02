import tkinter as tk
import app_main.main_ui as win
import app_main.make_widgets as mkw
import app_main.service as s
import app_main.face_detect_service as fds

def main():

    img_path = 'img/IU.jpg'
    root = tk.Tk()
    fd_service = fds.FaceDetectService(img_path)
    app=win.AppWindow(root, '650x500+100+100',img_path)
    mkw.make(app,fd_service)
    s.service() #ui 이벤트와 상관없이 수행해야 하는 기능(ex.소켓 등등)
    app.mainloop()