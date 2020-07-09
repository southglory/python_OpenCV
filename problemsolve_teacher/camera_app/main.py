import tkinter as tk
import camera_app.main_ui as win
import camera_app.make_widgets as mkw
import camera_app.camera_service as s

def main():
    img_path = '../img/a.jpg'
    root = tk.Tk()
    app = win.AppWindow(root, '650x500+100+100', img_path)
    service = s.CameraService(app)
    mkw.make(app, service)
    app.mainloop()

main()