from sklearn.preprocessing import LabelEncoder
X = np.array(X)
le = LabelEncoder()
Y_p = le.fit_transform(Y)
print(Y_p)
iris_som = SOM(m=3, n=1, dim=4, random_state = 404)
iris_som.fit(np.array(X))
predictions = iris_som.predict(X)
plt.scatter(X[:,0], X[:,1], c=predictions, cmap='brg_r')
plt.title("Predicted results")
plt.show()
from sklearn.metrics import silhouette_score
silhouette_score(X, predictions)
best_score = -1
best_cluster = 0
scores = []
for m_size in range(2, 6):
 for n_size in range(2, 6):
 iris_som = SOM(m=m_size, n=n_size, dim=4)
 iris_som.fit(X)
 pred = iris_som.predict(X)
 # print(pred)
 scores.append(silhouette_score(X, pred))
 if scores[-1] > best_score:
 best_score = scores[-1]
 best_cluster = (m_size, n_size)
print("Best score :", best_score)
print("Best number of clusters:", best_cluster)
