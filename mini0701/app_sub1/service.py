#이 함수 안에 기능을 구현하시오
#기능구현 클래스를 따로 만들고 그 객체를 생성하여 실행하는 코드를 넣으면 ok
import copy
import os
from tkinter import messagebox
from datetime import datetime, time
import cv2
import tkinter as tk
frame_kept = None#저장을 위해 킵 하는 화면

class video_service():
    #영상 window와 GUI window가 구분됨. 영상 window는 thread로 구현
    def __init__(self,master):
        self.app=master
        print('비디오 서비스 초기화.')
        # CascadeClassifier xml 파일의 경로 #haarcascade_frontalface_alt2.xml
        cascade_file = 'classifier/haarcascade_frontalface_default.xml'
        self.cascade = cv2.CascadeClassifier(cascade_file)


    def video_show(self):
        global frame_kept
        print("show")
        cap = cv2.VideoCapture(0)
        mask=cv2.imread('img/mask.png')

        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                # 이미지 반전,  0:상하, 1 : 좌우
                frame = cv2.flip(frame, 1)
                frame_small=cv2.add(frame,mask)

                gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

                # 얼굴 인식
                face_list = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(170, 170),maxSize=(245,245))

                color = (0, 0, 255)
                cx = 320
                cy = 240
                cw = 250
                ch = 250
                cv2.rectangle(frame, (cx - int(cw / 2), cy - int(ch / 2)), (cx + int(cw / 2), cy + int(ch / 2)), color,thickness=8)
                #roi=img1[vpos:rows+vpos, hpos:cols+hpos]
                if len(face_list) > 0:
                    print(face_list)
                    if len(face_list)>1:
                        alertMsg="Alert ! : Too many people. Please only one person."
                        cv2.putText(frame, alertMsg, (25, 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))
                        frame_kept=None
                    else:
                        dst=frame_small.copy()#잘라내서 보여주기
                        dst=frame_small[cy - int(ch / 2):cy + int(ch / 2), cx - int(cw / 2): cx + int(cw / 2)]
                        frame_kept= copy.deepcopy(dst)
                        cv2.imshow('img', frame_kept)
                    for face in face_list:
                        x, y, w, h = face
                        cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness=8)
                else:
                    # print("no face")
                    frame_kept = None
                    pass

                # 영상 화면 띄우기
                cv2.imshow('frame', cv2.resize(frame, (int(640 * 1.5), int(480 * 1.5))))

                if cv2.waitKey(1) & 0xFF == ord('q'):  # 추가 종료 조건. q 누르기
                    break
        cap.release()
        cv2.destroyAllWindows()
        self.btn2_clicked()#학습창 종료버튼 눌림
        print('\nth exiting.')

    def video_GUI(self,ID):
        print("video GUI 시작.")
        self.ID=ID
        self.newWindow = tk.Toplevel(self.app)
        self.newWindow.geometry('%dx%d+%d+%d' % (500,400, 10, 220))
        self.cnt_learn=0
        self.create_mini_widgets()


    def create_mini_widgets(self):

        self.btn1 = tk.Button(self.newWindow, width=30, font=100, text='5회 학습')
        self.btn1.grid(row=0, column=0, columnspan=2)
        self.label1 = tk.Label(self.newWindow, font=100, text="0회 학습")
        self.label1.grid(row=1, column=0, columnspan=2)
        self.label2 = tk.Label(self.newWindow, font=100, text=" ")
        self.label2.grid(row=2, column=0, columnspan=2)
        self.btn2 = tk.Button(self.newWindow, width=30, font=100, text='닫기')
        self.btn2.grid(row=3, column=0, columnspan=2)


        # app.btn1['command'] = btn1_clicked
        self.btn1['command'] = self.btn1_clicked
        self.btn2['command'] = self.btn2_clicked

    def btn1_clicked(self):
        print("mini_btn1_clicked")
        print("학습 저장")
        if self.write_frame(self.ID)==True:
            self.cnt_learn+=1
            cnt_l="학습 "+str(self.cnt_learn)+"회"
            self.label1['text']=cnt_l
        if self.cnt_learn>4:#5회 이상 학습할 경우 종료하라고 안내함
            self.label2['text'] ="학습이 충분합니다. 영상을 누르고 종료 버튼 : q "

    def btn2_clicked(self):
        print("mini_btn2_clicked")
        print("학습창 닫기")
        self.newWindow.destroy()

    def write_frame(self,ID):
        global frame_kept
        if frame_kept is None:
            messagebox.showerror("error", "not captured")
            return False
        else:
            pngDir='dataset/' + 'person_'+ID
            print(pngDir)
            if not os.path.isdir(pngDir):
                os.mkdir(pngDir)
            cv2.imwrite(pngDir+'/At'+datetime.now().strftime('%Y%m%d_%H%M%S')+'.png', frame_kept)
            return True


