import threading
import cv2


def preview_th(stop, app):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 400)
    while stop():
        ret, frame = cam.read()
        if ret:
            app.change_img(frame)
        cv2.waitKey(100)
    cam.release()

def write_avi_th(stop, app):
    cam = cv2.VideoCapture(0)  # 카메라 오픈
    #이걸로 크기 지정하면 동영상 잘 안만들어짐. cv2.resize()사용권고
    #cam.set(3, 640)
    #cam.set(4, 400)
    codec = cv2.VideoWriter_fourcc(*"mp4v")  # 사용할 코덱 생성
    # 동영상 작성자 객체 생성
    out = cv2.VideoWriter('../img/a.mp4', codec, 25.0, (640, 400), True)
    while stop():  # 카메라 정상 오픈일 때 동작
        ret, frame = cam.read()  # 카메라 영상 읽기
        if ret:  # 읽기가 정상이면
            frame = cv2.resize(frame,(640,400))
            out.write(frame)  # 동영상 작성
            app.change_img(frame)
        else:
            break
    cam.release()
def view_video_th(stop, app):
    path = 'C:\\Users\\Playdata\\Desktop\\mydata\\opencv\\yolo-object-detection\\yolo-object-detection\\videos\\airport.mp4'
    #path = '../img/a.mp4'
    cam = cv2.VideoCapture(path)

    while stop():
        ret, frame = cam.read()
        if ret:  # 정상 읽기일 때만
            app.change_img(frame)
        else:
            break
        cv2.waitKey(100)
    cam.release()

class CameraService:
    def __init__(self, app):
        self.cam = None
        self.app = app
        self.flag = True

    def stop(self):
        self.flag = False

    def preview(self):
        self.flag = True
        cam_th = threading.Thread(target=preview_th, args=(lambda:self.flag, self.app))
        cam_th.start()

    def capture(self):
        self.stop()
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 640)
        self.cam.set(4, 400)
        ret, frame = self.cam.read()
        self.app.change_img(frame)
        cv2.imwrite('../img/img1.jpg', frame)
        self.cam.release()

    def write_avi(self):
        self.flag = True
        avi_th = threading.Thread(target=write_avi_th, args=(lambda: self.flag, self.app))
        avi_th.start()

    def view_img(self):
        src = cv2.imread('../img/img1.jpg')
        self.app.change_img(src)

    def view_video(self):
        self.flag = True
        avi_read_th = threading.Thread(target=view_video_th, args=(lambda: self.flag, self.app))
        avi_read_th.start()