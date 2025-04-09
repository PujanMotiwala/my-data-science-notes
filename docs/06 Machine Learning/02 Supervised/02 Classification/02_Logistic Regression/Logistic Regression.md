### Definitions

- A statistical and machine learning technique used for classification, predicting the probability of a categorical or discrete target field based on the values of input features.
- For modeling binary and multi-class classification problems
- Used to predict the probability of a certain class or event occurring.

#### Other Definitions:
- **Independent Variables** (X): Features used to predict the outcome (e.g., tenure, age, income).
- **Dependent Variable** (Y): The outcome being predicted (e.g., churn), typically binary (e.g., yes/no, true/false).
- **Coefficients** (Parameters): Weights assigned to features in the model. Features with coefficients close to zero have a smaller effect on the prediction.

#### Feature Requirements:
- Independent variables should be continuous or dummy/indicator coded if categorical.
#### What Output do we get?

$0 \leq P(x) \leq 1$
- It returns a probability score between zero and one for a given sample of data.
#### Equations:

##### 1. The basic equation 
The logistic function (also known as the sigmoid function):

$\Huge P(x) = \frac{1}{1 + e^{-z}}$

where:
- $p(x)$ is the probability of the event occurring
- $z$ is the input to the function (also called the log-odds)
- $e$ is the base of the natural logarithm (2.71828)

**Goal**: To find the values of the coefficients $(b_0, b_1, b_2, \ldots, b_n)$ that minimize the error between the predicted probability and the actual outcome. 

##### 2. Error Equation: [[Cost Function]] 
- It is typically the negative log-likelihood of the data.

$\Huge J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(h_\theta(x^{(i)})) + (1 - y^{(i)}) \log(1 - h_\theta(x^{(i)})) \right]$

where:
- $J(\theta)$ is the cost function
- $m$ is the number of training examples
- $y^{(i)}$ is the actual label of the *i*-th training example
- $h_\theta(x^{(i)})$ is the predicted probability of the *i*-th training example
- $x^{(i)}$ represents the input features of the *i*-th training example
##### 3. For Multiple independent variables:

$\Huge p(x) = \frac{1}{1 + e^{-(b_0 + b_1 x_1 + b_2 x_2 + \ldots + b_n x_n)}} \normalsize$

where:
- $x_1, x_2, \ldots, x_n$ are the independent variables
- $b_0, b_1, b_2, \ldots, b_n$ are the coefficients

### How to use logistic regression?

![[Pasted image 20240615204619.png]]

Given that, let's start to formalize the problem.

- **Dataset $X$**:
  - $X \in \mathbb{R}^{m \times n}$ is our dataset in the space of real numbers with dimensions $m \times n$.
	  - $m$ represents the number of features (dimensions).
	  - $n$ represents the number of records.

- **Target $Y$**:
  - $y \in \{0, 1\}$ is the class that we want to predict, which can be either 0 or 1.

- **The Model**:
  - Ideally, it can predict that the class of the customer is 1, given its features $x$.
  $\large \hat{y} = P(y = 1 | x)$  
  - The probability of a customer being in class 0 can be calculated as:
  $\large P(y = 0 | x) = 1 - P(y = 1 | x)$

####


### When to use logistic regression?

When the target field is categorical (binary), when the probability of prediction is needed, when data is linearly separable, and when understanding the impact of features is required.

##### The four cases:
1. When the Target Field is Binary:
	- Applicable for categorical targets like zero/one, yes/no, churn/no churn, positive/negative.
2. When You Need the Probability of Your Prediction:
	- Example: Determining the probability of a customer buying a product.
	- Logistic regression predicts the probability and maps cases to discrete classes based on that probability.
3. When Your Data is Linearly Separable:
	- Decision boundary is a line, plane, or hyperplane.
	- Example: With two features and no polynomial processing, we get a simple inequality (e.g., $\theta_0 + \theta_1 x_1 + \theta_2 x_2 > 0$).
	- Complex [[Decision Boundaries]] can be achieved with polynomial processing.
4. To understand the impact of a feature.
	- Based on statistical significance of logistic regression model coefficients.
	- **Optimum Parameters**:
		- Feature $X$ with coefficient (weight) $\theta_1$ close to zero has less impact.
		- Features with large absolute values of $\theta_1$ have a greater impact.
	- Allows understanding of independent variable impact while controlling for others.

#### Applications:
- Health: Predict heart attack probability, diabetes diagnosis.
- Marketing: Likelihood of product purchase, customer churn.
- System/Finance: Predict process failure, mortgage default.
#### How analogous to Linear Regression?
- Logistic regression is analogous to linear regression but tries to predict a categorical or discrete target field instead of a numeric one. 
- In linear regression, 
	- we might try to predict a continuous value of variables such as the price of a house, blood pressure of a patient, or fuel consumption of a car. 
- But in logistic regression, 
	- we predict a variable which is binary such as yes/no, true/false, successful or not successful, pregnant/not pregnant, and so on, all of which can be coded as zero or one
For more details, visit [[Logistic Regression vs Linear Regression]] 


In python, logistic regression can be implemented using the `LogisticRegression`
## TAGS
[[ML model]] [[Supervised]] [[Classification]] [[Logistic Regression]]