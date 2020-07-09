import cv2 as cv
import csv

als=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
imgs=[]
for al in als:
    img_color = cv.imread('dataset/test/'+al+'.png', cv.IMREAD_COLOR)
    img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
    ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
    imgs.append(img_binary)

    height,width = img_binary.shape[:2]
    for h in range(height):
        for x in range(0,28):
            print("%3d"%img_binary[h,x], end=",")
        print("")

    cv.imshow("Binary", img_binary)
    cv.waitKey(0)

idx = 0
csv_f = open('al_test.csv', 'w', encoding='utf-8')
for x in imgs:
    fdata = x.ravel()
    img_data = list(map(lambda n: str(n), fdata))
    csv_f.write(als[idx] + ',')
    csv_f.write(','.join(img_data) + '\r\n')
    idx += 1
csv_f.close()