import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
path = "/content/drive/MyDrive/MLT Datasets/income.csv"
df = pd.read_csv(path)
df1 = df.drop("fnlwgt", axis = 1)
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
adb = AdaBoostClassifier()
adb.fit(X_train1, Y_train1)
y_pred_ad = adb.predict(X_test1)
print(classification_report(Y_test1, y_pred_ad))
from sklearn.model_selection import RandomizedSearchCV
ad = AdaBoostClassifier()
params = {
 "n_estimators" : (50, 100, 200),
 "learning_rate" : (1, 0.3, 0.1),
 "algorithm" : ("SAMME", "SAMME.R")
}
rcva = RandomizedSearchCV(ad, params, random_state = 0, scoring='accuracy',
verbose=10)
rcva.fit(X_train1, Y_train1)
y_pred_ad = rcva.predict(X_test1)
print(classification_report(Y_test1, y_pred_ad))
