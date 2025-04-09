Here we explore why linear regression cannot be used properly for some binary classification problems. 

### The Difference

| Feature    | Logistic Regression                                                                                          | Linear Regression                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| **Goal**   | Build a model to predict the class of each customer and the probability of each sample belonging to a class. | Used for predicting continuous values (e.g., predicting income based on age). |
| **Model**  | $\hat{y}$ estimates that the class of a customer is 1, given its features $x$.                               | Fits a line through data: $a + b x_1$.                                        |
| **Labels** | $y$ is the labels vector (actual values), and $\hat{y}$ is the vector of predicted values by the model.      | Used to predict continuous value $y$ (e.g., income).                          |
### Let’s try using Linear Regression for Classification
- **Example**: Predicting churn (categorical value) using age (independent variable)

![[Pasted image 20240616050916.png]]
- **Data Representation**: 
	- Data is represented as a scatter plot with two y-values (0 and 1).\
	- Red denotes Class 0 (no churn) and blue denotes Class 1 (churn).
- **Applying Linear Regression**:
	- 
- **Model**:
	- Fit a polynomial through the data: $a + b x$ or traditionally, $\Theta_0 + \Theta_1 x_1$.
	- This line has two parameters which are shown with vector $\Theta$, 
		- where the values of the vector are $\Theta_0$ and $\Theta_1$
	 $\Large\Theta^T = [\Theta_0, \Theta_1]$
	- Equation can be shown formally as Theta transpose $X$
	 $\large\Theta^T X = \Theta_0 + \Theta_1 x_1$
	- Equation for a multidimensional space, as Theta transpose X, 
		- where $\Theta$ is the parameters of the line in two-dimensional space or parameters of a plane in three-dimensional space, and so on.
	 $\large \Theta^T X = \Theta_0 + \Theta_1 x_1 + \Theta_2 x_2 + ..$
	- where, 
		- **Theta ($\Theta$)**: This is a vector that contains the parameters (or weights) of our model.
		- **Multiplication**: We multiply this vector ($\Theta$) by the feature set ($x$), which includes all the input features for a customer.
		- **Transpose**: To make the multiplication work correctly, we use the transpose of $\Theta$, which means we flip it from a row to a column vector (or vice versa).
		- **Weights or Confidences**: The values in $\Theta$ are also known as weights or confidences, and they help determine the importance of each feature in making predictions.
		 $\Theta^T = [\Theta_0, \Theta_1, \Theta_2,..]$
		- **Feature Set** ($x$)**: This is the set of all input features (like age, income, etc.) for a particular customer.
		 $X = \begin{pmatrix}1 \\ x_1 \\ x_2 \\ \vdots \end{pmatrix}$
		
	- Fitting the line: 
		- $\Theta$ parameter can be calculated by optimization algorithm or mathematically, which results in the equation of the fitting line. 
			- For example, if the parameters of this line are $-1$ and $0.1$, and the equation for the line is $-1 + 0.1 x_1$
	![[Pasted image 20240616053617.png]]
	
	 - 
	 - As Theta is a vector of parameters and is supposed to be multiplied by x, it is shown conventionally as transpose Theta. Theta is also called the weights factor or confidences of the equation with both these terms used interchangeably, and x is the feature set, which represents a customer.

### Limitation/Problems with Linear Regression for Classification
- **Value Range**:
	- Linear regression can return values outside [0, 1].
	- Requires a threshold (e.g., 0.5) to classify the data points.
- **Threshold Functions**:
	- Step functions do not provide probabilities.
	- Using a threshold can result in the same output for very different input values (e.g., 1 and 1000 both map to 1).
- **Smooth Transition**:
	- There is a lack of smooth transition between classes.
	- Step functions result in abrupt changes, not capturing the probabilistic nature of classification.

