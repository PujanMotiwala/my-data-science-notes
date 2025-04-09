[[ML model]]
#### What is a model ?
- A model is simply a system for mapping inputs to outputs.
- A model learns relationships between the inputs, called features, and outputs, called labels, from a training dataset.
- Models are useful because we can use them to predict the values of outputs for new data points given the inputs (test data).

#### What is training a model ?
- A model learns relationships between the inputs, called features, and outputs, called labels, from a *training dataset*.
- During training, the model is given both the features and the labels and learns how to map the former to the latter.

#### How to evaluate a model ?
- A trained model is evaluated on a *testing dataset*, where we only give it the features and it makes predictions. 
- We compare the predictions with the known labels for the testing set to calculate accuracy.

#### What are the two prediction errors for a model ?
- Performance
- Accuracy

#### What is Model Validation ?
- We need some sort of pre-test to use for model optimization and evaluate. This pre-test is known as a *validation dataset*.
- A basic approach would be to use a validation set in addition to the training and testing set. This presents a few problems though: we could just end up overfitting to the validation set, and we would have less training data. A smarter implementation of the validation concept is **k-fold cross-validation**.
- *What is k-fold cross-validation ?*
	- The idea is straightforward: rather than using a separate validation set, we split the training set into a number of subsets, called *folds*.
	- Example: 
		- Let’s use five folds
		- We perform a series of train and evaluate cycles where each time we train on 4 of the folds and test on the 5th, called the *hold-out dataset*.
		- We repeat this cycle 5 times, each time using a different fold for evaluation.
		- At the end, we average the scores for each of the folds to determine the overall performance of a given model.
		- This allows us to optimize the model before deployment without having to use additional data.
		
		![[Pasted image 20230205032829.png]]

 


