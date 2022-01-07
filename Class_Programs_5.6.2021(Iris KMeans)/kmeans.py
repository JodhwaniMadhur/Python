import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


data=pd.read_csv('iris.csv')
x=data.iloc[:,[0,1,2,3]].values

wcss=[]

for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init='k-means++', max_iter=300,n_init=10, random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)


plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


kmeans=KMeans(n_clusters=3, init='k-means++',max_iter=300, n_init=10, random_state=42)
y_kmeans=kmeans.fit_predict(x)

plt.scatter(x[y_kmeans==0,0],x[y_kmeans==0,1],s=100, c='yellow',label='Iris Setosa')
plt.scatter(x[y_kmeans==1,0],x[y_kmeans==1,1],s=100,c='blue',label='Iris Versicular')
plt.scatter(x[y_kmeans==2,0],x[y_kmeans==2,1],s=100,c='crimson',label='Iris Virginica')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='green',label='Centroids')
plt.legend()
plt.show()