import pickle

with open('heart_res.pkl', 'rb') as f:
    clf = pickle.load(f)

your_data = [[64/100,1,3,110/200,211/500,0,0,144/200,1,1.8,1,0,2]] #pre:1

pre = clf.predict(your_data)
if pre==1:
    print('심장이 위험함')
else:
    print('good')