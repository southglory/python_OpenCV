import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pickle

csv = pd.read_csv('heart.csv')
#값의 범위를 0~1로 만들어줌.
csv['age']=csv['age']/100
csv['trestbps']=csv['trestbps']/200
csv['chol']=csv['chol']/500
csv['thalach']=csv['thalach']/200

csv_data = csv[["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]]
csv_label= csv["target"]
print(csv_data)
print(csv_label)

train_data, test_data,train_label, test_label =train_test_split(csv_data,csv_label,test_size=0.01)

clf = svm.SVC()
clf.fit(train_data,train_label)

with open('heart_res.pkl','wb') as f:
    pickle.dump(clf,f)#오픈한 파일에 저장

pre = clf.predict(test_data)
score = metrics.accuracy_score(test_label,pre)
print(pre)
print('score:', score)

