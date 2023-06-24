import pandas as pd
import numpy as np
from fcmeans import FCM
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

path = "/content/drive/MyDrive/MLT Datasets/winequality_red.csv"
df_1015 = pd.read_csv(path)
df_1015['total sulfur dioxide'].unique()

X = np.array(df_1015['total sulfur dioxide']).reshape(-1, 1)

n_clusters_range = range(2, 6)
best_partition = None
best_silhouette_score = -1

for n_clusters in n_clusters_range:
    fcm = FCM(n_clusters=n_clusters)
    fcm.fit(X)
    u = fcm.u
    silhouette_avg = silhouette_score(X, np.argmax(u, axis=1))
    
    if silhouette_avg > best_silhouette_score:
        best_partition = u
        best_silhouette_score = silhouette_avg

optimal_clusters = best_partition.shape[1]
print("Optimal number of clusters:", optimal_clusters)

# Print the cluster centroids
fcm = FCM(n_clusters=optimal_clusters)
fcm.fit(X)
centroids = fcm.centers
print("Cluster centroids:", centroids)

# Plot the datapoints using scatter plots
fig, ax = plt.subplots()
ax.scatter(X[:, 0], np.zeros_like(X[:, 0]), c=np.argmax(best_partition, axis=1))
plt.show()
