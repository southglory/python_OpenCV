import random
import time
import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk
import numpy as np
import omok.app.main as om


class AppWindow(tk.Frame):#frame
    def __init__(self, master=None):
        super().__init__(master)
        self.AI_loop_flag = None
        self.master = master
        self.master.geometry('1000x700+50+50')
        self.master.resizable(True, True)
        self.pack()#opencv frame
        self.sub_fr = None#frame
        self.frame = None #tk의 보드를 놓을 캔버스
        self.create_widgets()

    def create_widgets(self):#한번만
        self.frame = tk.Canvas(self.master, width = 540, height = 540, background = "white")
        self.frame.pack()
        #보드 게임 생성
        self.make_board_game()
        # 보드 그래픽 생성
        self.make_board_Graphic()

        self.sub_fr = tk.Frame(self.master)#frame
        self.sub_fr.pack()

    def make_board_game(self):#한번만.#보드 게임 생성
        #보드 배열 생성
        self.board_arr=np.zeros((19,19))
        #print(self.board_mem)
        #플레이어 순서 결정
        self.player=["black","gray","white"]
        self.turn_plus=(-1)#gray 모드는 0
        self.make_turn()
        self.Flag = False #게임 끝나면 True

    def make_board_Graphic(self):#한번만# 보드 그래픽 생성
        self.board_img = self.make_img('img/go_play.png')
        self.frame.create_image(270, 270, image=self.board_img)
        self.frame.bind("<Button-1>", self.make_hansu)

    def make_turn(self):#턴 교체 함수
        self.turn = 1 + self.turn_plus #0:black, 2: white
        self.turn_plus*=(-1)


    def make_hansu(self,event=None,AI=None,Ax=None, Ay=None):#한수 유효성 검사 후, 돌 놓고, 승리조건 판단.
        if AI==None:
            x=event.x
            y=event.y
        else:
            x=int(Ax*30)
            y=int(Ay*30)

        self.hansu_x=int(round(x * 0.1) * 10)
        self.hansu_y=int(round(y * 0.1) * 10)
        self.hansu_x_arr= int(self.hansu_x/30)
        self.hansu_y_arr= int(self.hansu_y/30)
        if self.test_availability()==True:
            print(self.hansu_x_arr,self.hansu_y_arr)
            self.put_doll(self.player[self.turn])#돌 놓기
            self.check_Five(self.player[self.turn])
            self.make_turn()


    def test_availability(self):
        x=self.hansu_x
        y=self.hansu_y
        for i in range(0,19+1):#위치 유효성
            if (x>4+30*i and x<26+30*i) or (y>4+30*i and y<26+30*i):
                print("어디에 두세요? 다시 두세요.")
                return False
        if self.board_arr[self.hansu_y_arr, self.hansu_x_arr] in [1,2]:#중복 유효성
            print("어디에 두세요? 다시 두세요.")
            return False
        return True

    def put_doll(self,color):#돌 그려주고 메모리 저장.
        doll_size=10
        self.frame.create_oval(self.hansu_x-doll_size,self.hansu_y-doll_size,self.hansu_x+doll_size,self.hansu_y+doll_size, fill=color)
        self.board_arr[self.hansu_y_arr,self.hansu_x_arr]=self.turn+1#black:1, gray:2, white:3
        #print(self.board_mem)

    def check_Five(self,color):
        x = self.hansu_x_arr
        y = self.hansu_y_arr
        c=self.turn+1 #color number
        cntL=self.check_doll_hor1(x,y,c,0)
        cntR=self.check_doll_hor2(x,y,c,0)
        cntU=self.check_doll_ver1(x, y,c,0)
        cntB=self.check_doll_ver2(x, y,c,0)
        cntUR1=self.check_doll_UR1(x,y,c,0)
        cntUR2=self.check_doll_UR2(x,y,c,0)
        cntBR1=self.check_doll_BR1(x,y,c,0)
        cntBR2=self.check_doll_BR2(x,y,c,0)
        if (cntL+cntR==5) or (cntU+cntB==5) or (cntUR1+cntUR2==5) or (cntBR1+cntBR2==5):
            print(color+": six!")
        if (cntL+cntR==4) or (cntU+cntB==4) or (cntUR1+cntUR2==4) or (cntBR1+cntBR2==4):
            print(color+": win")
            self.Flag=True
            #승리 지점 표시
            doll_size = 15
            self.frame.create_oval(self.hansu_x - doll_size, self.hansu_y - doll_size, self.hansu_x + doll_size,
                                   self.hansu_y + doll_size, fill="red")
            doll_size = 10
            self.frame.create_oval(self.hansu_x - doll_size, self.hansu_y - doll_size, self.hansu_x + doll_size,
                                   self.hansu_y + doll_size, fill=color)

        elif (cntL+cntR==2) or (cntU+cntB==2) or (cntUR1+cntUR2==2) or (cntBR1+cntBR2==2):
            print(color+": three!")


############ AI 모드 ###################################
    def AI_mode(self):
        positions=[]
        #[[1,2],[1,3]..]
        app=om.app
        if self.AI_loop_flag==-1:#not loop
            for i in range(0,18+1):
                for j in range(0,18+1):
                    positions.append([i,j])
            print(positions)
            print("3")
            time.sleep(0.5)
            print("2")
            time.sleep(0.5)
            print("1")
            time.sleep(0.5)
            print("start!")
            while self.Flag==False:
                self.AI_choice=random.sample(positions,1)
                #print(self.AI_choice)
                positions.remove(self.AI_choice[0])
                #print(len(positions))
                self.make_hansu(AI=True, Ax=self.AI_choice[0][0], Ay=self.AI_choice[0][1])
            time.sleep(1)
        else:
            while self.AI_loop_flag==1:#loop
                for i in range(0,18+1):
                    for j in range(0,18+1):
                        positions.append([i,j])
                print(positions)
                print("3")
                time.sleep(0.5)
                print("2")
                time.sleep(0.5)
                print("1")
                time.sleep(0.5)
                print("start!")
                while self.Flag==False:
                    self.AI_choice=random.sample(positions,1)
                    #print(self.AI_choice)
                    positions.remove(self.AI_choice[0])
                    #print(len(positions))
                    self.make_hansu(AI=True, Ax=self.AI_choice[0][0], Ay=self.AI_choice[0][1])
                print("AI again")

                time.sleep(1)
                app.make_board_Graphic()
                app.make_board_game()
                print("AI")
                if app.lbl1['text'] == "gray mode":
                    app.turn_plus = 0
                elif app.lbl1['text'] == "black vs. white":
                    app.turn_plus = -1
                app.lbl2['text'] = "AI"
                app.make_turn()
        print("AI quit")






############ 4방위 체크돌 ############################
    def check_doll_hor1(self,x,y,c,cnt):#x-1에 돌이 있는지 판단.
        x-=1
        if x>=0 and x<=18:
            if self.board_arr[y, x] == c:
                cnt+=1
                #print("again",x)
                cnt=self.check_doll_hor1(x, y,c,cnt)
        return cnt

    def check_doll_hor2(self, x, y,c,cnt):
        x += 1
        if x >= 0 and x <= 18:
            if self.board_arr[y, x] == c:
                cnt += 1
                #print("again",x)
                cnt=self.check_doll_hor2(x, y,c,cnt)
        return cnt

    def check_doll_ver1(self, x, y,c,cnt):
        y -= 1
        if y >= 0 and y <= 18:
            if self.board_arr[y, x] == c:
                cnt+=1
                #print("again")
                cnt=self.check_doll_ver1(x, y,c,cnt)
        return cnt

    def check_doll_ver2(self, x, y,c,cnt):
        y += 1
        if y >= 0 and y <= 18:
            if self.board_arr[y, x] == c:
                cnt+=1
                #print("again")
                cnt=self.check_doll_ver2(x, y,c,cnt)
        return cnt

    def check_doll_UR1(self,x,y,c,cnt):
        x -=1
        y -= 1
        if x>=0 and x<=18 and y >= 0 and y <= 18:
            if self.board_arr[y, x] == c:
                cnt += 1
                #print("again")
                cnt = self.check_doll_UR1(x, y,c, cnt)
        return cnt

    def check_doll_UR2(self,x,y,c,cnt):
        x +=1
        y += 1
        if x>=0 and x<=18 and y >= 0 and y <= 18:
            if self.board_arr[y, x] == c:
                cnt += 1
                #print("again")
                cnt = self.check_doll_UR2(x, y,c, cnt)
        return cnt

    def check_doll_BR1(self, x, y,c, cnt):
        x += 1
        y -= 1
        if x >= 0 and x <= 18 and y >= 0 and y <= 18:
            if self.board_arr[y, x] == c:
                cnt += 1
                #print("again")
                cnt = self.check_doll_BR1(x, y,c, cnt)
        return cnt

    def check_doll_BR2(self, x, y,c, cnt):
        x -= 1
        y += 1
        if x >= 0 and x <= 18 and y >= 0 and y <= 18:
            if self.board_arr[y, x] == c:
                cnt += 1
                #print("again")
                cnt = self.check_doll_BR2(x, y,c, cnt)
        return cnt

#############기타 편의 함수####################
    def make_img(self, path):
        src = cv2.imread(path)
        src = cv2.resize(src, (540, 540))
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        src = ImageTk.PhotoImage(image=img)
        return src