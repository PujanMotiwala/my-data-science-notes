```Python
from sklearn.linear_model import LinearRegression
import numpy as np

# Generate sample data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])

# Create the linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Get the coefficients
b0 = model.intercept_
b1 = model.coef_[0]

# Print the results
print('Intercept:', b0)
print('Coefficient:', b1)

# Predict the output for a new input
x_new = np.array([6]).reshape(-1, 1)
y_new = model.predict(x_new)

print("Predicted output :", y_new)
```

>In this example, we first generate some sample data in the form of two NumPy arrays, one for the independent variable x and one for the dependent variable y. Then we create a Linear Regression model using the *LinearRegression()* function from the Scikit-learn library. Next, we fit the model to the data using the fit() method. Then, we get the intercept and coefficient of the line by accessing the `intercept_` and `coef_` attributes of the model. Finally, we can use the predict method on the model to predict the output for a new input.

>It's worth mentioning that, in case of multiple independent variables, you can pass the independent variables as a 2D array with shape (n_samples, n_features) and the output will be the coefficients of the independent variables.


$$1/N \ from i=1 to n  2(x_i(y - y_i)$$