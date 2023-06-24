import pandas as pd
import numpy as np
from sklearn_som.som import SOM
import matplotlib.pyplot as plt

path = '/content/drive/MyDrive/MLT Datasets/Iris (1).csv'
df_1041 = pd.read_csv(path)
df_1041.head()

X = df_1041.iloc[:, 1:-1]
Y = df_1041.iloc[:, -1]

X.isnull().sum()

som = SOM(n_columns=10, n_rows=10)
som.fit(X.values)

Y_p = som.predict(X.values)

plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=Y_p, cmap='brg')
plt.title("Actual results")
plt.show()
