X = np.array(df_1041[['total sulfur dioxide', 'volatile acidity']])
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
print(optimal_clusters)
fcm = FCM(n_clusters=2)
fcm.fit(X)
fig2, ax2 = plt.subplots()
ax2.set_title('FCM Clustering')
labels = fcm.predict(X)
ncenters = 2
for i in range(ncenters):
 ax2.scatter(X[labels == i, 0], X[labels == i, 1], label=f'Cluster {i+1}
')
ax2.scatter(fcm.centers[:, 0], fcm.centers[:, 1], marker='*', s=200, c='r')
ax2.legend()
print("Optimal number of clusters:", optimal_clusters)
centroids = fcm.centers
print("Cluster centroids:", centroids)
fig, ax = plt.subplots()
ax.scatter(X[:,0], X[:,1], c=np.argmax(best_partition, axis=1))
plt.show()
