from sklearn.decomposition import PCA
pca = PCA(n_components=2)
df_principal_1041 = pca.fit_transform(df_normalized_1041)
df_principal_1041 = pd.DataFrame(df_principal_1041)
df_principal_1041.columns = ['P1', 'P2']

from sklearn.metrics import silhouette_score
import scipy.cluster.hierarchy as shc

plt.figure(figsize=(8, 8))
plt.title('Dendrogram')
Dendrogram = shc.dendrogram(shc.linkage(df_principal_1041, method='ward'))

plt.figure(figsize=(8, 8))
plt.title('Dendrogram')
Dendrogram = shc.dendrogram(shc.linkage(df_principal_1041, method='complete'))

plt.figure(figsize=(8, 8))
plt.title('Dendrogram')
Dendrogram = shc.dendrogram(shc.linkage(df_principal_1041, method='average'))
plt.figure(figsize=(8, 8))
plt.title('Dendrogram')
Dendrogram = shc.dendrogram(shc.linkage(df_principal_1041, method='single'))

ac2 = AgglomerativeClustering(n_clusters=2)
# Visualizing the clustering
plt.figure(figsize=(6, 6))
plt.scatter(df_principal_1041['P1'], df_principal_1041['P2'], c=ac2.fit_predict(df_principal_1041), cmap='rainbow')
plt.show()

ac3 = AgglomerativeClustering(n_clusters=3)
plt.figure(figsize=(6, 6))
plt.scatter(df_principal_1041['P1'], df_principal_1041['P2'], c=ac3.fit_predict(df_principal_1041), cmap='rainbow')
plt.show()

ac4 = AgglomerativeClustering(n_clusters=4)
plt.figure(figsize=(6, 6))
plt.scatter(df_principal_1041['P1'], df_principal_1041['P2'], c=ac4.fit_predict(df_principal_1041), cmap='rainbow')
plt.show()

ac5 = AgglomerativeClustering(n_clusters=5)
plt.figure(figsize=(6, 6))
plt.scatter(df_principal_1041['P1'], df_principal_1041['P2'], c=ac5.fit_predict(df_principal_1041), cmap='rainbow')
plt.show()

k = [2, 3, 4, 5]
# Appending the silhouette scores of the different models to the list
silhouette_scores = []
silhouette_scores.append(silhouette_score(df_principal_1041, ac2.fit_predict(df_principal_1041)))
silhouette_scores.append(silhouette_score(df_principal_1041, ac3.fit_predict(df_principal_1041)))
silhouette_scores.append(silhouette_score(df_principal_1041, ac4.fit_predict(df_principal_1041)))
silhouette_scores.append(silhouette_score(df_principal_1041, ac5.fit_predict(df_principal_1041)))
# Plotting a bar graph to compare the results
plt.bar(k, silhouette_scores)
plt.xlabel('Number of clusters', fontsize=20)
plt.ylabel('Silhouette Scores', fontsize=20)
plt.show()
print(silhouette_scores)

from sklearn.metrics import davies_bouldin_score, mutual_info_score

k = [2, 3, 4, 5]
davies_bouldin_scores = []
davies_bouldin_scores.append(davies_bouldin_score(df_principal_1041, ac2.fit_predict(df_principal_1041)))
davies_bouldin_scores.append(davies_bouldin_score(df_principal_1041, ac3.fit_predict(df_principal_1041)))
davies_bouldin_scores.append(davies_bouldin_score(df_principal_1041, ac4.fit_predict(df_principal_1041)))
davies_bouldin_scores.append(davies_bouldin_score(df_principal_1041, ac5.fit_predict(df_principal_1041)))
# Plotting a bar graph to compare the results
plt.bar(k, davies_bouldin_scores)
plt.xlabel('Number of clusters', fontsize=20)
plt.ylabel('Davies Bouldin Score', fontsize=20)
plt.show()

ac2 = AgglomerativeClustering(n_clusters=2, linkage='single')
plt.figure(figsize=(6, 6))
plt.scatter(df_principal_1041['P1'], df_principal_1041['P2'], c=ac2.fit_predict(df_principal_1041), cmap='rainbow')
plt.show()

