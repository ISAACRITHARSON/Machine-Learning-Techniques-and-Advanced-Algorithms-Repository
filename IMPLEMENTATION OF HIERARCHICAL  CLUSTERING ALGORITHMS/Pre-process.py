import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_1041 = pd.read_csv("/content/drive/MyDrive/MLT Datasets/CC GENERAL.csv")
df_1041.fillna(method='ffill', inplace=True)
df_1041.isnull().sum()

from sklearn.preprocessing import StandardScaler, normalize
scaler = StandardScaler()
df_scaled_1041 = scaler.fit_transform(df_1041)
df_normalized_1041 = normalize(df_scaled_1041)
df_normalized_1041 = pd.DataFrame(df_normalized_1041)
