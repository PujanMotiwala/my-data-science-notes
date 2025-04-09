> It allows data points to belong to multiple clusters with separate degrees of membership. “Soft” or fuzzy k-means clustering is an example of overlapping clustering. Soft k-means is a variant of the k-means algorithm that uses probabilities to assign data points to clusters, rather than hard assignments. 

- One way to implement soft k-means in Python is to use the Expectation-Maximization (EM) algorithm

## Method

- Expectation-Maximization (EM) algorithm is a powerful tool for fitting models to data when the data is incomplete or has missing values. The algorithm is a iterative method that is used to find the maximum likelihood estimates of the parameters of a statistical model. It can also be used to find the maximum a posteriori estimates in Bayesian statistics.

- The EM algorithm consists of two steps: the expectation step (E-step) and the maximization step (M-step). These steps are repeated until the model converges.

	- The E-step computes the expected value of the complete data log-likelihood, given the current estimates of the parameters. This expected value is used as a surrogate for the true data log-likelihood, which is intractable because of the missing data.

	- The M-step maximizes the expected complete data log-likelihood with respect to the parameters. This step updates the parameter estimates to be more consistent with the observed data and the expected complete data.

- The EM algorithm is guaranteed to increase the likelihood at each iteration. The algorithm will converge to a local maximum of the likelihood function, which may or may not be the global maximum.

## Applications

EM algorithm can be applied in many fields, for example in image processing, computer vision and natural language processing. Gaussian Mixture Model (GMM) is one of the most popular model that uses EM algorithm. In GMM, EM algorithm is used to find the maximum likelihood estimates of the parameters of a mixture of Gaussian distributions.

## TAGS
[[Unsupervised]] [[Clustering]] [[Overlapping Clustering]]