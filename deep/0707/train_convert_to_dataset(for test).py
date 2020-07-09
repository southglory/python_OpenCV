import cv2
gray_img = cv2.imread('img/train/al.png', 0)
h,w= gray_img.shape

al_w= w/26

cut=5

imgs =[]

idx=[]
for i in range(0,26):
    idx.append(i)
als=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i, al in zip(idx,als):
    img = gray_img[int(0+cut):int(h-cut), int(i*al_w+cut):int((i+1)*al_w-cut)]
    img=cv2.resize(img,(28,28))
    img = cv2.bitwise_not(img)
    imgs.append(img)
    cv2.imshow(str(i),img)
    cv2.imwrite('dataset/train/'+al+'.png',img)
cv2.waitKey(0)
cv2.destroyAllwindows()