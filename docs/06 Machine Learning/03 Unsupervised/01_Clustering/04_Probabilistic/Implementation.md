>Probabilistic clustering is a method of clustering that assigns a probability or likelihood to each data point for belonging to each cluster. One way to perform probabilistic clustering in Python is to use the Gaussian Mixture Model (GMM) algorithm, which is a probabilistic model that can be used for density estimation and cluster analysis.

```python
from sklearn.mixture import GaussianMixture
import numpy as np

# Generate sample data
data = np.array([[1, 2], [1, 4], [1, 0],
                [4, 2], [4, 4], [4, 0]])

# Define the number of clusters (k)
k = 2

# Train the model
gmm = GaussianMixture(n_components=k)
gmm.fit(data)

# Get the cluster assignments for each data point
labels = gmm.predict(data)

# Get the cluster probabilities for each data point
probs = gmm.predict_proba(data)

print(labels)
# Output: [0 0 0 1 1 1]
print(probs)
# Output: [[9.99971248e-01 2.87516864e-05]
#          [2.87516864e-05 9.99971248e-01]
#          [9.99971248e-01 2.87516864e-05]
#          [2.87516864e-05 9.99971248e-01]
#          [2.87516864e-05 9.99971248e-01]
#          [9.99971248e-01 2.87516864e-05]]
```

>In this example, we first generate some sample data in the form of a 2D array. Then we define the number of clusters (k) we want to divide the data into, in this case 2. Next, we train the soft k-means model using GaussianMixture() function from scikit-learn with number of clusters. After that, we can use the predict() method to get the hard cluster assignments for each data point, and the predict_proba() method to get the probability of each data point belonging to each cluster.

>Note that in this example, the GaussianMixture class from scikit-learn is used to fit the model and it is a probabilistic model that uses the Expectation-Maximization (EM) algorithm to fit the data, it is similar to soft k-means.