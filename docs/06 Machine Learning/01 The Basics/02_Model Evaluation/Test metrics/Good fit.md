[[Good fit]]
## What is a good fit in a statistical model?

![[goodfit.excalidraw.svg]]

- Ideally, the case when the model makes the predictions with 0 error, is said to have a _good fit_ on the data. 
- This situation is achievable at a spot between overfitting and underfitting. 
- In order to understand it, we will have to look at the performance of our model with the passage of time, while it is learning from the training dataset.
	1. With the passage of time, our model will keep on learning, and thus the error for the model on the training and testing data will keep on decreasing. 
	2. If it learns for too long, the model will become more prone to overfitting due to the presence of noise and less useful details. Hence, the performance of our model will decrease. 
	3. In order to get a good fit, we will stop at a point just before where the error starts increasing. At this point, the model is said to have good skills in training datasets as well as our unseen testing dataset.