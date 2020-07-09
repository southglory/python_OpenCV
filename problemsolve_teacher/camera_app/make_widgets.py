import tkinter as tk
from functools import partial

def btn1_clicked(s, event):
    s.capture()

def btn2_clicked(s, event):
   s.view_img()

def btn3_clicked(s, event):
    s.write_avi()

def btn4_clicked(s, event):
   s.view_video()

def btn5_clicked(s, event):
   s.preview()

def btn6_clicked(s, event):
   s.stop()

def make(app, service):
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.btn1 = tk.Button(app.sub_fr, width=10, font=60, text='사진찍기')
    app.btn2 = tk.Button(app.sub_fr, width=10, font=60, text='사진보기')
    app.btn3 = tk.Button(app.sub_fr, width=10, font=60, text='동영상찍기')
    app.btn4 = tk.Button(app.sub_fr, width=10, font=60, text='동영상보기')
    app.btn5 = tk.Button(app.sub_fr, width=10, font=60, text='preview')
    app.btn6 = tk.Button(app.sub_fr, width=10, font=60, text='stop')

    app.ent.grid(row=0, column=0, columnspan=6)
    app.btn1.grid(row=1, column=0)
    app.btn2.grid(row=1, column=1)
    app.btn3.grid(row=1, column=2)
    app.btn4.grid(row=1, column=3)
    app.btn5.grid(row=1, column=4)
    app.btn6.grid(row=1, column=5)

    app.btn1.bind('<Button-1>', partial(btn1_clicked, service))
    app.btn2.bind('<Button-1>', partial(btn2_clicked, service))
    app.btn3.bind('<Button-1>', partial(btn3_clicked, service))
    app.btn4.bind('<Button-1>', partial(btn4_clicked, service))
    app.btn5.bind('<Button-1>', partial(btn5_clicked, service))
    app.btn6.bind('<Button-1>', partial(btn6_clicked, service))