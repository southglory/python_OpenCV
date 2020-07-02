import tkinter as tk
import threading
from functools import partial

def remove_ent(app):
    app.ent.delete(0, 'end')
    app.ent2.delete(0, 'end')

def btn1_clicked(app,service,event):
    print('sub_btn1 clicked: video_show threading')
    ID=ID_make(app)
    service.video_GUI(ID)
    video_showing=threading.Thread(target=service.video_show,args=())
    video_showing.start()



#def btn2_clicked(app,event):
#    print('sub_btn2 clicked')
    

def make(app, service):
    app.label0 = tk.Label(app.sub_fr, font=60, text="학생 정보 입력")
    app.label1 = tk.Label(app.sub_fr, font=60,  text="학년 : ")
    app.entry1 = tk.Entry(app.sub_fr, width=10)

    app.label2 = tk.Label(app.sub_fr, font=60,  text="반 : ")
    app.entry2 = tk.Entry(app.sub_fr, width=10)
    app.label3 = tk.Label(app.sub_fr, font=60,  text="번호 : ")
    app.entry3 = tk.Entry(app.sub_fr, width=10)
    app.label4 = tk.Label(app.sub_fr, font=60,  text="이름 : ")
    app.entry4 = tk.Entry(app.sub_fr, width=10)

    app.label0.grid(row=0, column=0, columnspan=6)
    app.label1.grid(row=1, column=0)
    app.entry1.grid(row=1, column=1)

    app.label2.grid(row=1, column=2)
    app.entry2.grid(row=1, column=3)

    app.label3.grid(row=1, column=4)
    app.entry3.grid(row=1, column=5)

    app.label4.grid(row=2, column=0)
    app.entry4.grid(row=2, column=1)

    app.btn1 = tk.Button(app.sub_fr, width=15, font=60, text='저장')
    app.btn1.grid(row=3,column=2,columnspan=2)

    app.btn1.bind('<Button-1>', partial(btn1_clicked,app,service))

    #app.btn1['command'] = btn1_clicked
    #app.btn1.bind('<Button-1>', partial(btn1_clicked, app))
    #app.btn2.bind('<Button-1>', partial(btn2_clicked, app))

def ID_make(app):
    ID = app.entry1.get() + app.entry2.get() + app.entry3.get()  # 학번을 줌
    return ID