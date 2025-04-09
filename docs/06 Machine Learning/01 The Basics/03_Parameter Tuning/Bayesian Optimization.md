#### Definition

A strategy for finding the minimum of a function by building a probabilistic model to predict which input values are most likely to yield the lowest output values.

where, "input values" refer to the hyperparameters being optimized
"output values" refer to loss function or error metric

#### How is loss function related to accuracy?

We often aim to minimize a loss function, not the performance metric like accuracy directly. So, the "lowest output values" typically refer to the lowest values of a loss function or error metric. When we're optimizing for performance, like accuracy, we're actually aiming to minimize the inverse (or a related loss function), as Bayesian optimization inherently looks for minima. So, in the context of improving a model's accuracy, you'd adjust the process to ensure that minimizing the function aligns with maximizing accuracy.

#### How does it build probabilistic model?

Bayesian optimization builds a probabilistic model by using past evaluation results of the function to predict the performance of different hyperparameters. 
This model is then used to:
1. Estimate both the expected performance and 
2. the uncertainty of that estimate, 
guiding the selection of the next set of hyperparameters to evaluate.

#### What is this probabilistic model like in practice?

1. **Generate or Use a Small Dataset**: The dataset is split into training and testing sets.
    
2. **Define the Objective Function**: This function trains a model (e.g., Ridge regression) using a set of hyperparameters (in this example, the regularization strength `alpha`) and returns a performance metric (e.g., mean squared error) on the testing set.
    
3. **Specify the Hyperparameter Space**: This defines the range of values for each hyperparameter that the optimization algorithm will explore.
    
4. **Run Bayesian Optimization**: The algorithm iteratively selects new hyperparameter values to test by predicting which values are most likely to yield an improvement based on the probabilistic model built from previous runs. This model balances exploration of new areas with exploitation of known good areas.
    
5. **Find Optimal Hyperparameters**: After a predefined number of iterations, the algorithm suggests the hyperparameter values that are expected to minimize the objective function, based on the model.

#### Wait, what is Gaussian Process-based optimization?

Gaussian Process-based optimization is a method that uses Gaussian Processes to model the probability distribution of objective functions and efficiently finds the optimum by predicting where the function is likely to have its minimum.

Imagine you're searching for the lowest point in a hilly landscape covered in fog. You can't see far, so you guess where the next low point might be based on where you've stepped before and how the ground felt under your feet. Gaussian Process-based optimization does something similar by making educated guesses on where to step next to find the lowest point, using information from previous steps to predict where the ground might slope down even more.