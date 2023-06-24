import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
path = "/content/drive/MyDrive/MLT Datasets/income.csv"
df = pd.read_csv(path)
df1 = df.drop("fnlwgt", axis = 1)
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]
rf1 = RandomForestClassifier(class_weight = "balanced_subsample")
rf2 = RandomForestClassifier(n_estimators = 50, criterion = "entropy")
rf3 = RandomForestClassifier(min_samples_split = 3, min_samples_leaf=3)
rf4 = RandomForestClassifier(ccp_alpha = 0.1, n_estimators = 150, bootstrap
= False)
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
rf1.fit(X_train, Y_train)
y_pred1 = rf1.predict(X_test)
print(classification_report(Y_test, y_pred1))
rf2.fit(X_train, Y_train)
y_pred2 = rf2.predict(X_test)
print(classification_report(Y_test, y_pred2))
print(classification_report(Y_train, rf2.predict(X_train)))
rf3.fit(X_train, Y_train)
y_pred3 = rf3.predict(X_test)
print(classification_report(Y_test, y_pred3))
rf4.fit(X_train, Y_train)
y_pred4 = rf4.predict(X_test)
print(classification_report(Y_test, y_pred4))
