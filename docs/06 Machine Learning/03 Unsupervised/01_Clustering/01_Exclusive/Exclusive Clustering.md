> A form of grouping that stipulates a data point can exist only in one cluster. This can also be referred to as “hard” clustering. The K-means clustering algorithm is an example of exclusive clustering.


- A common example of an exclusive clustering method: **K-means clustering** 

![[Pasted image 20230115013500.png]]


## Method

- Hard k-means is the standard, traditional version of the k-means algorithm. 
- It assigns each data point to exactly one cluster, based on the Euclidean distance between the data point and the cluster centers. 
- The basic idea of k-means is to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean.
OR
- Data points are assigned into K groups, where K represents the number of clusters based on the distance from each group’s centroid. 
- The data points closest to a given centroid will be clustered under the same category. 
	- A larger K value will be indicative of smaller groupings with more granularity 
	- A smaller K value will have larger groupings and less granularity. 

## Application

- Market segmentation
- Document clustering
- Image segmentation
- Image compression

## TAGS
[[Unsupervised]] [[Clustering]] [[Exclusive Clustering]]