import cv2
import copy
import os
import numpy as np

class FaceDetectService:
    def __init__(self, src):
        self.classifiers = []
        self.src = src
        self.img = None
        self.face = None
        self.gray = None
        self.res = None
        self.dataset_path = 'dataset/'
        self.trainer = 'trainer.yml'

    def face_detect(self):
        self.classifiers.clear()
        self.classifiers.append(cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'))
        self.img = cv2.imread(self.src)#얼굴 있는 사진에서 영상 읽음
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)#영상 흑백으로 전환
        #얼굴 분리자로 얼굴 분리
        #self.face는 리스트: [(x, y, w, h),(x, y, w, h),(x, y, w, h)...]
        self.face = self.classifiers[0].detectMultiScale(
            self.gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )
        #원본 이미지 손상 없도록 영상 복사
        img = copy.deepcopy(self.img)
        #얼굴에 박스 그리고 그 결과를 self.res에 저장
        for (x, y, w, h) in self.face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            self.res = img

        if len(self.face) == 0:
            print('no face')
            return False
        #처리결과 리턴
        return True

    def eye_detect(self):
        flag = self.face_detect()#얼굴을 먼저 찾아서 얼굴 영역을 self.face에 저장
        if not flag:
            print('no face, no eyes')
            return False

        #눈을 분리자 로드 및 생성
        self.classifiers.append(cv2.CascadeClassifier('classifier/haarcascade_eye.xml'))
        img = copy.deepcopy(self.img)

        #얼굴영역을 흑백로이와 칼라로이로 생성
        for(x,y,w,h) in self.face:
            roi_gray = self.gray[y:y+h, x:x+w]#눈 판별을 위한 로이
            roi_color = img[y:y+h, x:x+w]#눈에 사각형 그릴 로이

        #학습한 데이터를 기반으로 눈영역 추출해서 반환
        eyes = self.classifiers[1].detectMultiScale(roi_gray,
            scaleFactor=1.2,
            minNeighbors=10,
            minSize=(5, 5)
        )
        for (x,y,w,h) in eyes:
            #눈 영역에 박스 그림
            cv2.rectangle(roi_color, (x,y), (x+w, y+h), (0, 255, 0), 2)
            self.res = img

        return True

    def smile_detect(self):
        flag = self.face_detect()  # 얼굴을 먼저 찾아서 얼굴 영역을 self.face에 저장
        if not flag:
            print('no face, no eyes')
            return False

        # smile 분리자 로드 및 생성
        self.classifiers.append(cv2.CascadeClassifier('classifier/haarcascade_smile.xml'))
        img = copy.deepcopy(self.img)

        # 얼굴영역을 흑백로이와 칼라로이로 생성
        for (x, y, w, h) in self.face:
            roi_gray = self.gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        # 학습한 데이터를 기반으로 눈영역 추출해서 반환
        eyes = self.classifiers[1].detectMultiScale(roi_gray,
                                                    scaleFactor=1.5,
                                                    minNeighbors=15,
                                                    minSize=(25, 25)
                                                    )
        for (x, y, w, h) in eyes:
            cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 0, 255), 2)
            self.res = img

        return True

    def face_recog_train(self):
        dirs = os.listdir(self.dataset_path)#dataset 하위 디렉토리 이름을 리스트에 저장
        persons = []
        for dir in dirs: #각 디렉토리에 저장된 파일명들을 persons에 담음
            if os.path.isdir(self.dataset_path+dir):
                files = os.listdir(self.dataset_path+dir)
                for idx, f in enumerate(files):
                    files[idx] = self.dataset_path+dir+'/'+f
                persons.append(files)
        print(persons)
        self.classifiers.clear()
        self.classifiers.append(cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'))

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        samples = []
        ids = []
        #학습할 얼굴 샘플링
        for id, row in enumerate(persons):
            for p in row:
                img = cv2.imread(p)
                #print(self.dataset_path+dirs[id]+'/'+p)
                self.gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                self.face = self.classifiers[0].detectMultiScale(
                    self.gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(20, 20)
                )
                for (x,y,w,h) in self.face:
                    samples.append(self.gray[y:y+h, x:x+w])
                    ids.append(id)

        recognizer.train(samples, np.array(ids))
        recognizer.write(self.dataset_path+self.trainer)
        print('얼굴 학습 완료')

    def face_recog(self):
        self.classifiers.clear()
        self.classifiers.append(cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'))

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(self.dataset_path+self.trainer)

        names=['IU', '조시']
        self.img = cv2.imread(self.src)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.face = self.classifiers[0].detectMultiScale(
            self.gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )
        res = False
        name = 'no face'
        for (x, y, w, h) in self.face:
            id, confi = recognizer.predict(self.gray[y:y+h, x:x+w])
            if confi < 50:
                name = names[id]
                print(name,'/ confidence:', confi)
                res = True
            else:
                name = 'unknown'
                res = False

        return res, name

