---
tags:
- Linear Regression
- ML model
- Regression
- Supervised
---

### Definition
*An analysis that assesses whether one or more predictor/independent variables explain the dependent variable.*

### 5 key assumptions
[[01 Linear relationship]]
[[02 Multivariate normality]]
[[03 No or little multicollinearity]]
[[04 No auto-correlation]]
[[05 Homoscedasticity]]

- It is sensitive to outlier effects


Linear regression is a statistical method for modelling the relationship between a dependent variable (y) and one or more independent variables (X). 
The basic equation for a simple linear regression model with one independent variable is:

y = b0 + b1X

where:

-   y is the dependent variable
-   x is the independent variable
-   b0 is the y-intercept (the value of y when x = 0)
-   b1 is the slope of the line (the change in y for a unit change in x)

In multiple linear regression, where there are more than one independent variables, the equation becomes:

y = b0 + b1_x1 + b2_x2 + ... + bn*xn

where:

-   x1, x2, ..., xn are the independent variables
-   b0, b1, b2, ..., bn are the coefficients

The values of b0, b1, b2, ..., bn are estimated from the data using a method called least squares. The goal is to find the values of b0, b1, b2, ..., bn that minimize the sum of the squared errors between the predicted values (y hat) and the actual values (y). The equation for the sum of the squared errors (also known as the cost function) is:

J(b0, b1, b2, ..., bn) = 1/2m * ∑(y^ - y)^2

where:

-   y^ is the predicted value of y
-   m is the number of observations
-   ∑ is the sum over all observations

The goal is to find the values of b0, b1, b2, ..., bn that minimize J(b0, b1, b2, ..., bn)