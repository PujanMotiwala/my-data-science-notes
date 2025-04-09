## What is #Regression Analysis?

> #Regression analysis is a predictive modelling technique that analyzes the relation between the target or dependent variable and independent variable in a dataset.

## When to use it?

> It get used when the target and independent variables show a linear or non-linear relationship between each other, and the target variable contains #Continuous values. The regression technique gets used mainly to determine the predictor strength, forecast trend, time series, and in case of cause & effect relation.

## Types

>There are many types of regression analysis techniques, and the use of each method depends upon the number of factors. These factors include the type of target variable, shape of the regression line, and the number of independent variables. 

**Below are the different regression techniques:**

1.  [[Linear Regression]]: It is used when the relationship between the dependent variable and the independent variable is linear. It is represented by an equation of the form 
   y = b0 + b1*x.
2. Multiple Linear Regression: It is used when there are more than one independent variable. It is represented by an equation of the form y = b0 + b1_x1 + b2_x2 + ... + bn*xn.
3. [[Logistic Regression]]: It is used for binary classification problems and it is represented by the logistic function.
4. [[Ridge Regression]]: It is a variation of linear regression that penalizes large coefficients. It is used to prevent overfitting.
5.  [[Lasso Regression]]: It is also a variation of linear regression that penalizes large coefficients but it tends to shrink some coefficients to zero.
6.  [[Polynomial Regression]]: It is used when the relationship between the dependent variable and the independent variable is non-linear. It is represented by an equation of the form y = b0 + b1_x + b2_x^2 + ... + bn*x^n.
7.  [[Bayesian Linear Regression]]: It is a variation of linear regression that uses Bayesian inference to estimate the coefficients.
8. ElasticNet Regression: It is a combination of Ridge and Lasso regression.
9. Support Vector Regression (SVR): It is a variation of SVM algorithm which is used for regression problems.
10. Decision Tree Regression: It is a non-parametric algorithm that can be used for both linear and non-linear regression problems.
11. Random Forest Regression: It is an ensemble of decision tree regression models which is used for both linear and non-linear regression problems.
12. Neural Network Regression: It is a variation of neural networks that can be used for both linear and non-linear regression problems.
13. Gradient Boosting Regression: It is an ensemble technique that combines multiple weak regression models to create a strong model.
14. K-Nearest Neighbors (KNN) Regression: It is a non-parametric algorithm that uses the values of the k nearest points to make predictions.
15. Generalized Additive Models (GAMs): It is a flexible framework that allows for non-linear relationships between the independent and dependent variables.
16. Gaussian Process Regression (GPR): It is a Bayesian non-parametric technique that can model complex and non-linear relationships between variables.
17. Regression Splines: It allows to fit a non-linear function using linear functions, it's a flexible way of modeling non-linear regression problems
18. Least Absolute Shrinkage and Selection Operator (LASSO): It is a technique that can be used for variable selection and regularization.
19. Principal Component Regression (PCR): It is a technique that uses principal component analysis (PCA) to reduce the dimensionality of the data and then performs linear regression on the transformed data.
20. Partial Least Squares Regression (PLSR): It is a technique that uses principal component analysis (PCA) to reduce the dimensionality of the data and then performs linear regression on the transformed data, it's similar to PCR but it's used when the number of independent variables is larger than the number of observations.
21. Quantile Regression Forest: it's an extension of random forest that allows to estimate different quantiles of the conditional distribution of the response variable given the predictor variables.
22. Additive models: it's a technique that allow to model the relationship between variables with a linear combination of smooth non-linear functions.
23. Bayesian Additive Regression Trees (BART): it's a Bayesian non-parametric technique that combines decision trees and Bayesian inference.
25. Ensemble methods: it's a technique that combine multiple models to improve the performance of the predictions.
26. Recurrent Neural Network (RNN) based regression: it's a variation of RNN that can be used for time series prediction and other sequential data.
27. Extreme Gradient Boosting (XGBoost) based regression: it's an extension of gradient boosting that uses a more regularized model formalization to control over-fitting, which often results in improved performance.
28. LightGBM based regression: it's another extension of gradient boosting that uses histograms to speed up training and reduce memory usage.
29. CatBoost based regression: it's an extension of gradient boosting that uses categorical features without the need to preprocess them, it's particularly useful when working with large datasets with many categorical features.
30. Regularization methods: it's a technique that helps to prevent overfitting by adding a penalty term to the cost function.
31. Adaptive Boosting (AdaBoost) based regression: it's an extension of boosting that adjusts the weight of the observations at each iteration of the algorithm.
32. Multi-Layer Perceptron (MLP) based regression: it's a variation of neural networks that uses multiple layers of perceptrons to model the relationship between variables.
33. Stochastic Gradient Descent (SGD) based regression: it's an optimization technique that can be used to train linear and logistic regression models.
34. Kernel Ridge Regression: it's a variation of Ridge Regression that uses kernel functions to model non-linear relationships.
35. Recursive Feature Elimination (RFE) based regression: it's a technique that recursively eliminates features by removing the ones that have the lowest coefficient values.
36. L1-Regularized Logistic Regression: it's a variation of logistic regression that uses L1 regularization to shrink some coefficients to zero.
37. L2-Regularized Logistic Regression: it's a variation of logistic regression that uses L2 regularization to shrink some coefficients.
38. Weighted Least Squares (WLS) based regression: it's a variation of least squares regression that allows to handle heteroscedasticity by assigning different weights to the observations.
39. Generalized Linear Model (GLM) based regression: it's a technique that allows to model different types of response variables such as binomial, Poisson, and exponential distributions.
40. Non-Linear Least Squares (NLLS) based regression: it's a technique that can be used to estimate the parameters of non-linear functions.
41. Gaussian Process (GP) based regression: it's a technique that uses Bayesian inference to estimate the posterior distribution of the parameters of the model.
42. Locally Weighted Scatterplot Smoothing (LOWESS) based regression: it's a non-parametric technique that uses a moving window to smooth the data and estimate the relationship between variables.
43. Bagging based regression: it's a technique that uses bootstrapped samples to improve the predictions of a base estimator.
44. Boosted Regression Trees (BRT) based regression: it's a technique that combines decision trees and boosting to model non-linear relationships.
45. Artificial Neural Network (ANN) based regression: it's a technique that uses neural networks to model complex relationships between variables.
46. Non-Parametric Bayesian Regression: it's a technique that uses Bayesian inference to estimate the posterior distribution of the parameters of the model without making assumptions about the prior distribution.
47. Neural Networks with Adaptive Activation Function: it's a technique that uses neural networks with adaptive activation functions to model non-linear relationships between variables.
48. Deep Belief Networks (DBN) based regression: it's a variation of neural networks that uses unsupervised pre-training to improve the predictions.
49. Restricted Boltzmann Machines (RBM) based regression: it's a variation of neural networks that uses unsupervised pre-training to improve the predictions.
50. Extreme Learning Machine (ELM) based regression: it's a technique that uses a single hidden layer neural network to model non-linear relationships between variables.
51. Deep Autoencoder based regression: it's a technique that uses deep autoencoder to model non-linear relationships between variables.
52. Self-Organizing Map (SOM) based regression: it's a technique that uses Self-Organizing Map to model non-linear relationships between variables.
53. Deep Reinforcement Learning based regression: it's a technique that uses deep reinforcement learning to model non-linear relationships between variables.
54. Fuzzy Logic based regression: it's a technique that uses fuzzy logic to model non-linear relationships between variables.
55. Ensemble techniques based on different models: it's a technique that combines different models to improve the predictions, like Random Forest of Linear Regression, XGBoost of Logistic Regression and so on.
56. Non-linear Principal Component Analysis (NLPCA) based regression: it's a technique that uses non-linear principal component analysis to model non-linear relationships between variables.
57. Gaussian Mixture Model (GMM) based regression: it's a technique that uses Gaussian mixture models to model non-linear relationships between variables. 
58. Hidden Markov Model (HMM) based regression: it's a technique that uses hidden markov models to model time series data.
59. Conditional Random Fields (CRF) based regression: it's a technique that uses conditional random fields to model relationships between variables in structured data. 
60. Genetic Programming (GP) based regression: it's a technique that uses genetic programming to optimize the parameters of a model for a specific problem. 
61. Deep Generative Model (DGM) based regression: it's a technique that uses deep generative models to model complex relationships between variables.
62. Deep Residual Network (ResNet) based regression: it's a technique that uses deep residual networks to model non-linear relationships between variables.
63. Deep Convolutional Neural Network (CNN) based regression: it's a technique that uses deep convolutional neural networks to model non-linear relationships between variables.

These are some of the other regression techniques that are available but keep in mind that depending on the complexity of the problem, the sample size, the number of features, and the complexity of the relationship between variables, some techniques might perform better than others.

Regenerate response

In addition to the above regression methods, there are many other types of regression in machine learning, including **JackKnife Regression**, and **Ecological Regression**.
