### What is F1 score? How would you use it?

Let’s have a look at this table before directly jumping into the F1 score.

	Prediction | Predicted Yes | Predicted No

	Actual Yes |       TP      |      FN

	Actual No  |       FP      |      TN


In #binary_classification we consider the F1 score to be a measure of the model’s accuracy. The F1 score is a weighted average of precision and recall scores.

F1 = 2TP/2TP + FP + FN

We see scores for F1 between 0 and 1, where 0 is the worst score and 1 is the best score.   
The F1 score is typically used in information retrieval to see how well a model retrieves relevant results and our model is performing.

[[F1 Score]]
