#### Linear relationship
- Linear regression needs the relationship between the independent and dependent variables to be linear.
- The linearity assumption can best be tested with scatter plots, the following two examples depict two cases, where no and little linearity is present.
- In [linear regression](https://vitalflux.com/linear-regression-real-life-example/), the [[t test]] is a [statistical hypothesis testing](https://vitalflux.com/data-science-how-to-formulate-hypothesis-for-hypothesis-testing/) technique that is used to test the linearity of the relationship between the response variable and different predictor variables.
- -   As part of a **linear regression machine learning model**, it is claimed that there is a relationship between the response variables and predictor variables? Can this hypothesis or claim be taken as truth? Let’s say, the hypothesis is that the housing price depends upon the average income of people already staying in the locality. How true is this hypothesis or claim? The relationship between the response variable and each of the predictor variables can be evaluated using [T-test and T-statistics](https://vitalflux.com/linear-regression-t-test-formula-example/).
#### Why is a t-test used in the linear regression model?

The linearity of the linear relationship can be determined by calculating the t-test statistic. The t-test statistic helps to determine how linear, or nonlinear, this linear relationship is. The linear regression model is used to predict the value of a continuous variable, based on the value of another continuous variable. In most cases, linear regression is an excellent tool for prediction. However, in some instances, the linearity of the linear relationship may not be appropriate. This can be determined by examining the [t-test](https://en.wikipedia.org/wiki/Student%27s_t-test) statistic.

In a simple linear regression model such as Y = mX + b, the t-test statistics are used to determine the following hypothesis:

-   **H0: m = 0**
-   **Ha: m ≠ 0**

The slope or the coefficient of the predictor variable, m = 0 represents the hypothesis that there is no relationship between the predictor variable and the response variable. Assuming that the null hypothesis is true, the linear regression line will be parallel to X-axis such as the following, given Y-axis represents the response variable and the X-axis represent the predictor variable. The following diagram represents the null hypothesis:

A [one-sample t-test](https://vitalflux.com/one-sample-t-test-formula-examples/) will be used in linear regression to test the null hypothesis that the slope or the coefficients of the predictor variables is equal to zero. This test is used when the linear regression line is a straight line.

The formula for the one-sample t-test statistic in linear regression is as follows:

**t = (m – m0) / SE**

Where:

**t** is the t-test statistic

**m** is the linear slope or the coefficient value obtained using the least square method

**m0** is the hypothesized value of linear slope or the coefficient of the predictor variable. The value of m0 = 0.

**SE** represents the standard error of estimation which can be estimated using the following formula:

**SE = S / √N**

Where S represents the standard deviation and N represents the total number of data points

#### Summary
Linear regression is a linear relationship between the response variable and predictor variables. It can be used to predict the value of a continuous variable, based on the value of another continuous variable. The t-test statistic helps to determine the correlation between the response and the predictor variables. A one-sample t-test will be used in linear regression to test the null hypothesis that the slope or the coefficient is equal to zero. In the case of the multiple regression model, the null hypothesis is that the coefficient of each of the predictor variables is equal to zero.