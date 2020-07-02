import tkinter as tk
import app_sub1.main as sub1
from functools import partial


def btn1_clicked():
    print('btn1 clicked')

def btn2_clicked(app,event):
    print('btn2 clicked, 관리 창 오픈')
    sub1.main()


def make(app, service):
    app.label1= tk.Label(app.sub_fr, text = "학번:",font=60)
    app.label2 = tk.Label(app.sub_fr, text="이름:",font=60)
    app.ent1 = tk.Entry(app.sub_fr, width=30)
    app.ent2 = tk.Entry(app.sub_fr, width=30)

    app.btn1 = tk.Button(app.sub_fr, width=10, font=60, text='btn1')
    app.btn2 = tk.Button(app.sub_fr, width=10, font=60, text='관리')


    app.label1.grid(row=0, column=0)
    app.label2.grid(row=1, column=0)
    app.ent1.grid(row=0, column=1)
    app.ent2.grid(row=1, column=1)

    app.btn1.grid(row=2, column=1)
    app.btn2.grid(row=3, column=1)


    app.btn1['command'] = btn1_clicked
    #app.btn1.bind('<Button-1>', partial(btn1_clicked, app))
    app.btn2.bind('<Button-1>', partial(btn2_clicked, app))

