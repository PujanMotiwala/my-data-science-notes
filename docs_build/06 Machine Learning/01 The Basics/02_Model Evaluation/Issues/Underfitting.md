[[Underfitting]]

![[underfitting.excalidraw.svg]]

##### Definition
- A model is yet failing to capture the underlying trend of the data
- i.e. Performs well on training data but poorly on testing data. 
- It’s just like trying to fit undersized pants!
##### When it happens ?
	- Underfitting destroys the accuracy of our machine learning model. Its occurrence simply means that our model or the algorithm does not fit the data well enough. It usually happens when we have fewer data to build an accurate model and also when we try to build a linear model with fewer non-linear data.
	- In such cases, the rules of the machine learning model are too easy and flexible to be applied to such minimal data and therefore the model will probably make a lot of wrong predictions.
##### Why is it happening ?
	1.  High bias and low variance 
	2.  The size of the training dataset used is not enough.
	3.  The model is too simple.
	4.  Training data is not cleaned and also contains noise in it.
##### How to solve it ?
**Cure**
- Use more data.
- Reduction in the features by feature selection.
**Techniques used**
1.  Increase model complexity
2.  Increase the number of features, performing feature engineering
3.  Remove noise from the data.
4.  Increase the number of epochs or increase the duration of training to get better results.


##### Example