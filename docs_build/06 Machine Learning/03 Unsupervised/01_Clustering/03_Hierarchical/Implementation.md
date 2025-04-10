> Hierarchical Clustering Analysis (HCA) is a method of clustering that builds a hierarchy of clusters by merging or splitting successively smaller clusters.

### Agglomerative linkage

```python
from scipy.cluster.hierarchy import linkage, dendrogram
import numpy as np

# Generate sample data
data = np.array([[1, 2], [1, 4], [1, 0],
                [4, 2], [4, 4], [4, 0]])

# Compute the linkage matrix
Z = linkage(data, 'ward')

# Plot the dendrogram
import matplotlib.pyplot as plt
dendrogram(Z)
plt.show()
```

> In this example, we first generate some sample data in the form of a 2D array. Next, we use the linkage() function from the scipy library to compute the linkage matrix, which encodes the hierarchical relationships between the data points. The linkage method used here is 'ward' which minimizes the variance of the distances of the linkage. Finally, we use the dendrogram() function to plot the dendrogram, which is a tree-like diagram that shows the hierarchical relationships between the clusters.

>It's important to note that in Hierarchical Clustering there are two types of linkage, Agglomerative and Divisive. The above example uses Agglomerative linkage where each point is considered as a separate cluster and then merge the two closest clusters at each step till we reach the desired number of clusters. On the other hand, Divisive linkage starts with all points in a single cluster and then splits it into two clusters till we reach the desired number of clusters.

### Divisive Hierarchical Clustering

```python
from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Generate sample data
data = np.array([[1, 2], [1, 4], [1, 0],
                [4, 2], [4, 4], [4, 0]])

# Define the number of clusters (k)
k = 2

# Train the model
hca = AgglomerativeClustering(n_clusters=k, linkage='single')
hca.fit(data)

# Get the cluster assignments for each data point
labels = hca.labels_

print(labels)
# Output: [0 0 0 1 1 1]
```


>In this example, we first generate some sample data in the form of a 2D array. Then we define the number of clusters (k) we want to divide the data into, in this case 2. Next, we train the divisive hierarchical clustering model on the data using the AgglomerativeClustering() function from scikit-learn with linkage='single'. After that, we can use the labels_ attribute to get the cluster assignments for each data point.

>It's important to note that in scikit-learn the method used is Agglomerative, the difference is that we set linkage='single' which uses the divisive strategy. In this example, at each step, the single point that is farthest from the centroid of its cluster is selected and is re-assigned to a new cluster. This process is repeated until the desired number of clusters is reached.
