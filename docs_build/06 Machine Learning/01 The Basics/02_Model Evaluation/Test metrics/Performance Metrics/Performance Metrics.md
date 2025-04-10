[[Performance Metrics]]
When we think about how well does the trained model generalize new input data, there are two factors responsible for poor performances of ML algorithms:
- [[Overfitting]]
- [[Underfitting]]



### How to measure accuracy of classification models?

Three types of performance metrics are used:
1. [[Precision]]
2. [[Recall]]
3. [[F1 Score]]

- For example, we are classifying 🍎 and 🍌. 
	- If a model avoids a lot of mistakes in predicting 🍌 as 🍎 class, then the model is high in precision.  (Other example, Attackers or TP) $$precision = \frac{TP}{TP + FP}$$
	- Likewise, if a model avoids a lot of mistakes in predicting 🍎 as 🍌, then the model is high in recall. (Other example, Users or FP)
$$recall = \frac{TP}{TP + FN}$$
- You want high precision and high recalls while predicting. But what if the model aces in predicting one class, but fails for the other class ?
- This is where F1 score comes in, it takes into account both precision and recall. A balance of the two is what F1 scores on. If your model does a good job at accurately predicting both, then the score will be high. 

$$F1 = 2* \frac{precision*recall}{precision+recall}$$

Precision and recall are ways of monitoring the power of machine learning implementation. But they often used at the same time.

Precision answers the question, “Out of the items that the classifier predicted to be relevant, how many are truly relevant?”

Whereas, recall answers the question, “Out of all the items that are truly relevant, how many are found by the classifier?

In general, the meaning of precision is the fact of being exact and accurate. So the same will go in our machine learning model as well. If you have a set of items that your model needs to predict to be relevant. How many items are truly relevant?

The below figure shows the Venn diagram that precision and recall.

![[Pasted image 20230206144943.png]]

Mathematically, precision and recall can be defined as the following:

precision = # happy correct answers/# total items returned by ranker

recall = # happy correct answers/# total relevant answers