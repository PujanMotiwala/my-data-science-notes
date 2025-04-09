## When we think about how well does the trained model generalize new input data, there are two factors responsible for poor performances of ML algorithms:

#### Overfitting

![[overfitting.excalidraw.svg]]

##### Definition
- A model starts capturing noise in the data which is increasing the error rate
- does not make accurate predictions on testing data
- It’s just like trying to fit oversized pants!
##### When it happens ?
- It happens when learning power of the model is too high or the dataset is too small. 
- An overtrained model start to feeds in noise rather than useful information of the data.
- Testing with test data comes out with high variance. Then the model does not categorize the data correctly, because of too many details and noise.

##### Why is it happening ?
**Cause**: The non-parametric and non-linear methods. These type of ml algorithms have more freedom in building the model based on the dataset, thus building unrealistic models.
	a. High variance and low bias
	b. Too complex model
	c. Oversize training data

##### How to solve it ?
**Cure** 
Use linear algorithm w/ linear data or parameters like maximal depth for decision trees
**Techniques used**
1.  To increase training data.
2.  Reduce model complexity.
3.  Early stopping during the training phase (have an eye over the loss over the training period, as soon as loss begins to increase, stop training).
4.  [[Ridge Regularization]] and [[Lasso Regularization]]
5.  Use dropout for neural networks to tackle overfitting.

##### Example
- In a Regression model, the number of data points are lesser than the number of features 
- Solutions
	- Reduce the model learning power
	- [[Regularization]]
	- Increase training data size
	- [[Hyperparameter tuning]]
 







# TAGS

#ml/basics/overfitting
#ml/basics/underfitting