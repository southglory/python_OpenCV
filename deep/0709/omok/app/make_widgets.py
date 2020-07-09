import tkinter as tk
import threading
from functools import partial


def btn1_clicked(app,event):
    app.make_board_Graphic()
    app.make_board_game()
    print("중립 모드")
    app.turn_plus=0
    app.make_turn()
    app.lbl1['text']="gray mode"

def btn2_clicked(app,event):
    app.make_board_Graphic()
    app.make_board_game()
    print("대전 모드")
    app.turn_plus = -1
    app.make_turn()
    app.lbl1['text'] = "black vs. white"

def btn3_clicked(app,event):
    app.make_board_Graphic()
    app.make_board_game()
    print("AI")
    app.turn_plus = 0
    app.make_turn()
    AI = threading.Thread(target=app.AI_mode, args=())
    AI.start()


def make(app):
    app.ent1 = tk.Entry(app.sub_fr, width=10)
    app.ent1.grid(row=0, column=0)
    app.lbl1=tk.Label(app.sub_fr, text="black vs. white", font = 60)
    app.lbl1.grid(row=0, column=1)
    app.btn1 = tk.Button(app.sub_fr, width = 10, font=60, text="gray")
    app.btn1.grid(row=1, column =0 )
    app.btn2 = tk.Button(app.sub_fr, width=15, font=60, text="black vs. white")
    app.btn2.grid(row=1, column=1)
    app.btn3 = tk.Button(app.sub_fr, width=10, font=60, text="AI")
    app.btn3.grid(row=1, column=2)
    app.btn1.bind('<Button-1>', partial(btn1_clicked, app))
    app.btn2.bind('<Button-1>', partial(btn2_clicked, app))
    app.btn3.bind('<Button-1>', partial(btn3_clicked, app))
