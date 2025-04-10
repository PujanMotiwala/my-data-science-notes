```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Generate sample data
X, y = make_classification(n_features=1, n_redundant=0, random_state=42)

# Create the logistic regression model
model = LogisticRegression()

# Fit the model to the data
model.fit(X, y)

# Get the coefficients
b0 = model.intercept_
b1 = model.coef_

# Print the results
print('Intercept:', b0)
print('Coefficient:', b1)

# Predict the output for a new input
x_new = [[-2]]
y_new = model.predict(x_new)

print("Predicted output :", y_new)
```

>In this example, we first generate some sample data using the `make_classification` method from scikit-learn library. Then we create a LogisticRegression model using the LogisticRegression() function from the scikit-learn library. Next, we fit the model to the data using the fit() method. 
>
>Then, we get the intercept and coefficients of the line by accessing the `intercept_` and `coef_` attributes of the model. Finally, we can use the predict method on the model to predict the output for a new input. 
>
>It's worth mentioning that, In case of multiple independent variables, you can pass the independent variables as a 2D array with shape (n_samples, n_features) and the output will be the predicted probability of the event.