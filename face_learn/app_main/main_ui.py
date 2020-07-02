import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk
import os

class AppWindow(tk.Frame):#Frame
    def __init__(self, master=None, size=None, path=None):
        super().__init__(master)
        self.master = master
        self.master.geometry(size)
        self.master.resizable(True, True)
        self.pack()#opencv frame
        self.sub_fr= None#frame
        self.scr = None#tk의 label에 츨력할 영상
        self.frame = None #tk의 label
        self.create_widgets(path)
        self.variable_init()


    def make_img(self, path):
        src= cv2.imread(path)
        src= cv2.resize(src,(400, 300))
        img= cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image = img)

    def create_widgets(self,path):#프레임만
        self.make_img(path)
        self.frame= tk.Label(self.master, image = self.src)
        self.frame.pack()
        self.sub_fr= tk.Frame(self.master)#Frame
        self.sub_fr.pack()

    def change_img(self, res):
        res= cv2.resize(res, (400, 300))
        img = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image = img)
        self.frame['image'] = self.src

    def list_img(self):
        self.test_imgs = os.listdir('img/')
        for idx, f in enumerate(self.test_imgs):
            self.test_imgs[idx] = 'img/'+ f
        print(self.test_imgs)

    def next_img_path(self):
        if self.idx<len(self.test_imgs)-1:
            self.idx += 1
            print(self.idx)
            print(self.test_imgs[self.idx])
            return self.test_imgs[self.idx]
        else:
            self.idx=0
            print(self.idx)
            print(self.test_imgs[self.idx])
            return self.test_imgs[self.idx]

    def path2img(self,img_path):
        return cv2.imread(img_path)


    def variable_init(self):
        self.list_img()
        self.idx=0

