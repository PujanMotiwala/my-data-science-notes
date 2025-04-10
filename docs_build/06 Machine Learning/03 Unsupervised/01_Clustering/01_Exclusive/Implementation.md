```python
from sklearn.cluster import KMeans
import numpy as np

# Generate sample data
data = np.array([[1, 2], [1, 4], [1, 0],
                [4, 2], [4, 4], [4, 0]])

# Define the number of clusters (k)
k = 2

# Train the model
kmeans = KMeans(n_clusters=k)
kmeans.fit(data)

# Get the cluster assignments for each data point
labels = kmeans.labels_

# Get the coordinates of the cluster centers
cluster_centers = kmeans.cluster_centers_

print(labels)
# Output: [0 0 0 1 1 1]
print(cluster_centers)
# Output: [[1. 2.]
#          [4. 2.]]

```

> In this example, we first generate some sample data in the form of a 2D array. Then we define the number of clusters (k) we want to divide the data into, in this case 2. Next, we train the k-means model on the data using the KMeans() function from scikit-learn. After that, we can use the labels_ attribute to get the cluster assignments for each data point, and the cluster_centers_ attribute to get the coordinates of the cluster centers.
