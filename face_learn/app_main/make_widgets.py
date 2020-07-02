import tkinter as tk
from functools import partial


def btn1_clicked(app, service, event):
    print(event)
    flag= service.face_detect()
    if flag:
        app.change_img(service.res)

def btn2_clicked(app, service, event):
    print(event)
    flag = service.eye_detect()
    if flag:
        app.change_img(service.res)

def btn3_clicked(app, service, event):
    print(event)
    flag = service.smile_detect()
    if flag:
        app.change_img(service.res)

def btn4_clicked(service, event):
    print(event)
    service.face_recog_train()

def btn5_clicked(app, service, event):
    print(event)
    flag, name = service.face_recog()
    app.ent.delete(0,'end')
    app.ent.insert(0,name)

def btn6_clicked(app,service,event):
    print(event)
    img_path=app.next_img_path()
    img=app.path2img(img_path)
    app.change_img(img)
    service.__init__(img_path)



def make(app,service):
    app.ent= tk.Entry(app.sub_fr,width = 60)
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.btn1 = tk.Button(app.sub_fr, width = 10, font = 60, text = '얼굴인식')
    app.btn2 = tk.Button(app.sub_fr, width = 10, font = 60, text= '눈인식')
    app.btn3 = tk.Button(app.sub_fr, width = 10, font= 60, text = '미소인식')
    app.btn4 = tk.Button(app.sub_fr, width=10, font=60, text='얼굴학습')
    app.btn5 = tk.Button(app.sub_fr, width=10, font=60, text='사람인식')
    app.btn6 = tk.Button(app.sub_fr, width=10, font=60, text='Next')

    app.ent.grid(row= 0, column = 0, columnspan = 5)
    app.btn1.grid(row = 1, column = 0)
    app.btn2.grid(row = 1, column = 1)
    app.btn3.grid(row = 1, column = 2)
    app.btn4.grid(row=1, column=3)
    app.btn5.grid(row=1, column=4)
    app.btn6.grid(row=2, column=0, columnspan = 5)

    #app.btn1['command'] = btn1_clicked
    app.btn1.bind('<Button-1>',partial(btn1_clicked, app, service))
    app.btn2.bind('<Button-1>', partial(btn2_clicked, app, service))
    app.btn3.bind('<Button-1>', partial(btn3_clicked, app, service))
    app.btn4.bind('<Button-1>', partial(btn4_clicked, service))
    app.btn5.bind('<Button-1>', partial(btn5_clicked, app, service))
    app.btn6.bind('<Button-1>', partial(btn6_clicked, app, service))
