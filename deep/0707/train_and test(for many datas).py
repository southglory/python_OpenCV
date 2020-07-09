import pickle

from sklearn import svm, metrics


def load_csv(fname):
    label = []
    data = []
    with open(fname, 'r') as f:
        for line in f:
            t = line.split(',')
            if t[0] == '\n':
                continue
            label.append(ord(t[0]))
            num_img = []  # 숫자 이미지 1개
            for i in range(1, len(t)):
                num_img.append(int(t[i]))
            data.append(num_img)
    return label, data


train_label, train_data = load_csv('al.csv')

for jj in range(2,8):
    train_label2, train_data2 = load_csv('al'+str(jj)+'.csv')
    train_label=train_label+train_label2
    train_data=train_data+train_data2

test_label, test_data = load_csv('al_test.csv')

clf = svm.SVC()
clf.fit(train_data, train_label)

'''
with open('res.pkl', 'rb') as f:
    clf = pickle.load(f)
'''

pre = clf.predict(test_data)
for ch in pre:
    print(chr(ch))
score = metrics.accuracy_score(test_label, pre)
print(score)

'''
with open('res.pkl','wb') as f:
    pickle.dump(clf,f)#오픈한 파일에 저장


#tmp 변수에 저장하는 방법
pickle.dumps(tmp)
'''
