import pandas as pd
import quandl
import math
import numpy as np 
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
import pickle


df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'

df.fillna(-999999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out) #predicts 10 day aage ki value ie how today's scene affected 10 days later ka price

df.dropna(inplace=True)

X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

#X = preprocessing.scale(X)

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, y, test_size=0.2)

# clf = LinearRegression()

# clf.fit(X_train, Y_train)

# with open('linearregression', 'wb') as f:
# 	pickle.dump(clf, f)

pickle_in = open('linearregression', 'rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, Y_test)

print(accuracy)

#######################################################

#testing real values
#Expected = 1187.56 
# t = np.array([1.18756000e+03,0.00000000e+00,2.52625197e-03,1.98147600e+06]).reshape(1,4)
# print (clf.predict(t))

df['label'].plot()
plt.show()