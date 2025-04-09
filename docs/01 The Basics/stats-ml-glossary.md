# Comprehensive Statistics and Machine Learning Glossary

Welcome to this comprehensive glossary of terms commonly encountered in the fields of statistics and machine learning. This guide aims to provide clear definitions and context for various concepts, from fundamental data types to advanced modeling techniques.

## Data Types

Understanding the type of data you are working with is the first step in any analysis. Data can be broadly classified into categorical and numeric types, each with its own subtypes.

### Categorical (Qualitative Data)

Data that represents groupings or categories. It can be expressed using numbers or text strings.

#### Binary Data
A specific type of nominal data that has only two distinct categories.
*   **Examples:** Yes/No, Male/Female, Heads/Tails, Win/Lose

#### Nominal Data
Categorical data where the categories have no inherent order or ranking.
*   **Examples:** Colors (Red, Blue, Green), Gender (Male, Female, Other), Types of Cuisine (Italian, Mexican, Indian)

#### Ordinal Data
Categorical data where the categories have a meaningful order or ranking, but the distances between categories are not necessarily equal or defined.
*   **Examples:** Satisfaction Level (Very Unsatisfied, Unsatisfied, Neutral, Satisfied, Very Satisfied), Education Level (High School, Bachelor's, Master's, PhD)

### Numeric (Quantitative Data)

Data that represents amounts or quantities, typically expressed as numbers.

#### Discrete Data
Numeric data that can only take specific, distinct values, often integers. There are finite or countably infinite values.
*   **Examples:** Number of students in a class, Number of cars in a parking lot

#### Continuous Data
Numeric data that can take any value within a given range. Measurements can theoretically be broken down into infinitely smaller parts.
*   **Examples:** Height (175.5 cm), Weight (68.2 kg), Temperature (20.1°C, 20.11°C, 20.111°C)

#### Interval Data
Numeric data where the differences between values are meaningful and consistent, but there is no true zero point. Ratios between values are not meaningful.
*   **Characteristics:** Meaningful distances, No true zero.
*   **Examples:** Temperature in Celsius or Fahrenheit (difference between 20°C and 30°C is the same as between 30°C and 40°C, but 40°C is not "twice as hot" as 20°C), Calendar Years (difference between 2000 and 2010 is 10 years, but year 0 doesn't signify the absence of time).

#### Ratio Data
Numeric data that has all the properties of interval data, but also includes a true zero point. This means ratios between values are meaningful.
*   **Characteristics:** Meaningful distances, True zero point.
*   **Examples:** Age, Income, Distance, Height, Weight (A person weighing 100 kg is twice as heavy as someone weighing 50 kg).

---

## Statistics

Statistics provides the tools and methods to collect, analyze, interpret, and draw conclusions from data.

### Descriptive Statistics

Summarizing and describing the main features of a dataset.

#### Mean
The arithmetic average of a dataset, calculated by summing all values and dividing by the count of values. It provides a measure of central tendency but is sensitive to outliers.

#### Median
The middle value in a dataset that has been sorted in ascending order. It divides the data into two equal halves. It is a robust measure of central tendency, less affected by outliers and skewed data.

#### Mode
The value that appears most frequently in a dataset. A dataset can have one mode (unimodal), two modes (bimodal), or more (multimodal).

#### Variance
A measure of the spread or dispersion of data points around the mean. It quantifies the average squared deviation from the mean.

#### Standard Deviation
The square root of the variance. It measures the average distance of data points from the mean, expressed in the same units as the data, making it more interpretable than variance.

#### Skewness
A measure of the asymmetry of a probability distribution or dataset.
*   **Positive Skewness:** The tail on the right side is longer or fatter than the left side; the bulk of the values lie to the left of the mean.
*   **Negative Skewness:** The tail on the left side is longer or fatter than the right side; the bulk of the values lie to the right of the mean.

#### Kurtosis
A measure of the "tailedness" or "peakedness" of a probability distribution compared to a normal distribution.
*   **High Kurtosis (Leptokurtic):** Heavier tails and a sharper peak; indicates more outliers.
*   **Low Kurtosis (Platykurtic):** Lighter tails and a flatter peak; indicates fewer outliers.

#### Central Tendency
A measure that represents the center or typical value of a dataset. Common measures include the mean, median, and mode.

#### Interquartile Range (IQR)
A measure of statistical dispersion, representing the range between the first quartile (25th percentile) and the third quartile (75th percentile). It describes the spread of the middle 50% of the data and is robust to outliers.

### Correlation and Covariance

Measuring the relationship and dependency between variables.

#### Correlation
A statistical measure indicating the extent to which two variables change together linearly. The correlation coefficient (typically Pearson's r) ranges from -1 (perfect negative linear correlation) to +1 (perfect positive linear correlation), with 0 indicating no linear correlation.

#### Covariance
A measure of the degree to which two random variables change together. It indicates the direction of the linear relationship (positive or negative). However, its magnitude is not standardized, making it difficult to compare across different datasets or scales.

#### Pearson Correlation Coefficient
A measure of the linear relationship between two *continuous* variables. It ranges from -1 to 1, quantifying both the strength and direction of the linear association.

#### Spearman Correlation Coefficient
A non-parametric measure of the strength and direction of the *monotonic* relationship between two variables (whether ranked or continuous). It assesses how well the relationship between two variables can be described using a monotonic function. Based on ranked values.

### Inferential Statistics & Hypothesis Testing

Making inferences and conclusions about a population based on sample data.

#### Hypothesis Testing
A formal statistical method used to make decisions or inferences about a population parameter based on sample data. It involves formulating hypotheses, collecting data, and using statistical tests to evaluate the evidence.

#### Null Hypothesis (H₀)
A statement of no effect, no difference, or no relationship between variables. It's the default assumption that researchers aim to test against. Statistical tests determine if there is enough evidence to reject H₀.

#### Alternative Hypothesis (H₁ or Hₐ)
A statement that contradicts the null hypothesis, suggesting there *is* an effect, difference, or relationship. This is typically the hypothesis the researcher is trying to support.

#### p-value
The probability of observing the sample results (or results more extreme) if the null hypothesis (H₀) were actually true. A small p-value (typically < 0.05) suggests that the observed data is unlikely under the null hypothesis, leading to its rejection.

#### Confidence Interval
A range of values, calculated from sample data, that is likely to contain the true population parameter with a certain level of confidence (e.g., 95%). It provides a measure of the uncertainty and precision of an estimate.

#### Statistical Significance
A determination that an observed effect or difference in a study is unlikely to have occurred due to random chance alone. It is typically concluded when the p-value is less than a predetermined significance level (alpha, usually 0.05). Statistical significance does not necessarily imply practical significance.

#### Type I Error (False Positive)
The error of incorrectly rejecting a true null hypothesis (H₀). Concluding there is an effect when there isn't one. The probability of a Type I error is denoted by alpha (α), the significance level.

#### Type II Error (False Negative)
The error of incorrectly failing to reject a false null hypothesis (H₀). Concluding there is no effect when there actually is one. The probability of a Type II error is denoted by beta (β).

### Common Statistical Tests

Specific procedures used to perform hypothesis testing.

#### ANOVA (Analysis of Variance)
A statistical test used to compare the means of two or more groups to determine if there are statistically significant differences between them. It analyzes variance within and between groups.

#### Chi-squared Test (χ²)
A statistical test used primarily to examine differences between categorical variables. It compares observed frequencies to expected frequencies under a null hypothesis (e.g., independence or goodness-of-fit).

#### T-test
A statistical test used to compare the means of two groups to determine if they are significantly different from each other. Assumes data is approximately normally distributed and variances are similar (though variations exist).

#### F-test
A statistical test used generally to compare the variances of two or more groups or to assess the overall significance of a regression model (comparing model variance to residual variance).

#### One-sample t-test
A statistical test used to determine if the mean of a single sample is statistically different from a known or hypothesized population mean.

#### Two-sample t-test
A statistical test used to compare the means of two independent groups to determine if there is a statistically significant difference between them.

### Non-parametric Tests

Statistical tests that do not rely on assumptions about the data's distribution (e.g., normality). Used when parametric assumptions are violated or with ordinal data.

#### Mann-Whitney U test (Wilcoxon Rank-Sum test)
A non-parametric test used to compare distributions between two independent groups. It's an alternative to the independent two-sample t-test.

#### Kruskal-Wallis test
A non-parametric test used to compare distributions among three or more independent groups. It's an alternative to ANOVA.

#### Wilcoxon signed-rank test
A non-parametric test used to compare two related samples, matched samples, or repeated measurements on a single sample to assess whether their population mean ranks differ. It's an alternative to the paired t-test.

### Regression Analysis Concepts

Modeling the relationship between a dependent variable and one or more independent variables.

#### Regression Analysis
A set of statistical processes for estimating the relationships between a dependent variable (target) and one or more independent variables (predictors). Aims to understand how the dependent variable changes when independent variables are varied.

#### Linear Regression
A type of regression analysis where the relationship between the dependent variable and independent variable(s) is modeled using a linear equation. It fits a straight line through the data points.

#### Logistic Regression
A regression analysis used when the dependent variable is binary (e.g., 0/1, Yes/No). It models the probability of the outcome occurring using a logistic (sigmoid) function.

#### Residuals
The differences between the observed values of the dependent variable and the values predicted by the regression model. They represent the unexplained variance or error of the model.

#### Multicollinearity
A phenomenon in multiple regression where two or more predictor variables are highly correlated with each other. This can inflate the variance of coefficient estimates and make them unstable and difficult to interpret.

### Regularization Techniques

Methods used to prevent overfitting in regression models by adding a penalty term to the loss function, shrinking coefficient estimates.

#### Ridge Regression
A regularization technique (L2 penalty) that adds a penalty equal to the square of the magnitude of coefficients. It shrinks coefficients towards zero but doesn't typically set them exactly to zero.

#### Lasso Regression (Least Absolute Shrinkage and Selection Operator)
A regularization technique (L1 penalty) that adds a penalty equal to the absolute value of the magnitude of coefficients. It can shrink some coefficients exactly to zero, effectively performing feature selection.

#### Elastic Net Regression
A hybrid regularization technique that combines both L1 (Lasso) and L2 (Ridge) penalties. It aims to get the benefits of both, useful when there are multiple correlated features.

### Bayesian Statistics

An approach to statistics based on Bayes' theorem, incorporating prior beliefs with observed data to update probabilities.

#### Bayesian Statistics
A framework for statistical inference that uses Bayes' theorem to update prior beliefs about parameters based on observed data, resulting in posterior probabilities.

#### Bayesian Inference
The process of using Bayesian methods to update knowledge or beliefs about unknown parameters or hypotheses based on evidence from data.

#### Maximum Likelihood Estimation (MLE)
A method for estimating the parameters of a statistical model by finding the parameter values that maximize the likelihood function, which represents the probability of observing the given data under the assumed model. (Often contrasted with Bayesian estimation).

### Probability Distributions

Mathematical functions describing the likelihood of different outcomes for a random variable.

#### Normal Distribution (Gaussian Distribution)
A continuous, symmetric, bell-shaped probability distribution defined by its mean (μ) and standard deviation (σ). Many natural phenomena approximate this distribution, partly due to the Central Limit Theorem.

#### Central Limit Theorem (CLT)
A fundamental theorem stating that the sampling distribution of the sample mean (or sum) from a sufficiently large number of independent, identically distributed random variables will be approximately normally distributed, regardless of the original variable's distribution.

#### Probability Distribution
A mathematical function that defines the probabilities of occurrence of different possible outcomes for an experiment or random variable.

#### Probability Density Function (PDF)
A function associated with a *continuous* random variable, where the area under the curve between two points represents the probability that the variable falls within that interval.

#### Cumulative Distribution Function (CDF)
A function giving the probability that a random variable X is less than or equal to a specific value x (P(X ≤ x)). It applies to both discrete and continuous variables.

#### Binomial Distribution
A *discrete* probability distribution describing the number of successes in a fixed number of independent Bernoulli trials (experiments with two outcomes, success/failure), with a constant probability of success (p) on each trial.

#### Poisson Distribution
A *discrete* probability distribution describing the number of events occurring within a fixed interval of time or space, given a constant average rate of occurrence (λ) and independence between events.

#### Exponential Distribution
A *continuous* probability distribution describing the time *between* events in a Poisson process (where events occur continuously and independently at a constant average rate).

### Data Characteristics & Issues

Properties and potential problems within datasets.

#### Outliers
Data points that significantly differ from other observations in a dataset. They can be due to measurement errors, data entry mistakes, or genuinely unusual values. Outliers can heavily influence statistical analyses and models.

#### Autocorrelation (Serial Correlation)
The correlation of a signal (like a time series) with a delayed copy of itself as a function of the delay (lag). It measures the relationship between current observations and past observations.

### Time Series Basics

Concepts specific to data collected over time.

#### Stationarity
A property of a time series where its statistical properties (mean, variance, autocorrelation) remain constant over time. Many time series models assume stationarity.

#### ARIMA (Autoregressive Integrated Moving Average)
A class of statistical models for analyzing and forecasting time series data. It combines autoregressive (AR) components, differencing (I) to achieve stationarity, and moving average (MA) components. (See Time Series Analysis section for more detail).

#### Seasonality
Patterns in time series data that repeat over a fixed period (e.g., daily, weekly, yearly). Examples include retail sales peaking before holidays or temperature fluctuations throughout the year.

### Multivariate Analysis & Dimensionality Reduction

Analyzing data with multiple variables simultaneously.

#### Multivariate Analysis
Statistical methods used to analyze data involving more than one variable at a time, focusing on understanding the relationships and patterns among them.

#### Factor Analysis
A statistical method used to describe variability among observed, correlated variables in terms of a potentially lower number of unobserved variables called factors (latent variables). Aims to identify underlying structures.

#### Principal Component Analysis (PCA)
A dimensionality reduction technique that transforms a dataset with many variables into a smaller set of variables (principal components) while retaining most of the original information (variance). (See Dimensionality Reduction section for more detail).

#### Cluster Analysis
A set of techniques used to group objects or data points into clusters such that objects within the same cluster are more similar to each other than to those in other clusters.

#### K-means Clustering
An iterative partitioning algorithm that assigns each data point to one of K predefined clusters based on the distance to the cluster's centroid (mean). Aims to minimize within-cluster variance.

#### Hierarchical Clustering
A clustering technique that builds a hierarchy of clusters either agglomeratively (bottom-up: starting with individual points and merging clusters) or divisively (top-down: starting with one cluster and splitting). Results are often visualized as a dendrogram.

---

## Data Preprocessing

Preparing raw data for analysis and modeling.

### Categorical Data Encoding

Converting categorical data into a numerical format suitable for machine learning algorithms.

| Method            | What is it                                                                                                                                                           | When to Use                                                                                                                          | Pros                                                                                  | Cons                                                                                                       |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------- |
| **One-Hot Encoding** | Creates a new binary (0/1) column for each unique category level. An observation gets a '1' in the column corresponding to its category and '0's elsewhere.          | Ideal for nominal data (no order). Best when the number of categories is relatively small to avoid excessive dimensionality.          | Preserves category information without implying order. Easy to understand and implement. | Can drastically increase dimensionality ("curse of dimensionality") with many categories. Creates sparsity. |
| **Label Encoding**  | Assigns a unique integer to each category level (e.g., 0, 1, 2...).                                                                                                  | Suitable for ordinal data where the integer reflects the ranking. Can be used for nominal data with tree-based models, but use cautiously. | Simple, efficient, does not increase feature space dimensionality.                    | Can mislead models into assuming an ordinal relationship or magnitude difference between categories.         |
| **Embedding**     | Represents categories as dense, low-dimensional vectors. These vectors are often learned during the training of a neural network model.                               | Best for high-cardinality categorical features, especially within deep learning models (e.g., NLP, tabular data with neural networks). | Captures complex relationships and similarities between categories. Space-efficient.      | Requires more computational resources. Embeddings are learned, adding complexity. Less interpretable.   |

**Comparison Summary:**

*   **Dimensionality:** One-Hot increases significantly, Label Encoding keeps it unchanged, Embedding provides compact representation.
*   **Data Type Suitability:** One-Hot for nominal, Label Encoding for ordinal (or carefully for nominal), Embedding for high cardinality/complex patterns (often in deep learning).
*   **Model Compatibility:** One-Hot and Label Encoding work with most ML models. Embeddings are primarily used with neural networks.
*   **Performance Consideration:** One-Hot is simple but can be inefficient. Label Encoding risks introducing false order. Embeddings capture richness but are computationally intensive.

### Feature Scaling

Adjusting the range or distribution of numeric features. Essential for algorithms sensitive to feature scales (e.g., distance-based algorithms like KNN, SVM, PCA, gradient descent-based algorithms).

#### Normalization (Min-Max Scaling)
Transforms features to a fixed range, typically [0, 1]. Calculated as: `(X - X_min) / (X_max - X_min)`. Useful when the data distribution is unknown or not Gaussian.

#### Standardization (Z-score Scaling)
Transforms features to have a mean of 0 and a standard deviation of 1. Calculated as: `(X - mean) / std_dev`. Useful when features follow a Gaussian distribution. Less affected by outliers compared to normalization.

#### Z-score
A standardized score indicating how many standard deviations a data point is away from the mean of its distribution. `Z = (X - μ) / σ`. Used in standardization and outlier detection.

---

## Core Machine Learning Terminology

Fundamental concepts in machine learning projects.

#### Predictor (Feature)
An independent variable used as input to a machine learning model to predict the target variable. Corresponds to a column in a dataset used for prediction.

#### Target (Label)
The dependent variable or output that the machine learning model aims to predict. In supervised learning, this is the known outcome in the training data.

#### Feature
An individual measurable property or characteristic of an observation. These are the inputs (usually columns in a dataset) used by a model.

#### Control Variable
In experimental design (including some ML contexts like causal inference), a variable that is kept constant or accounted for statistically to prevent it from influencing the relationship between the independent (predictor) and dependent (target) variables.

#### Explanatory Variable
Often used interchangeably with "independent variable" or "predictor," especially in statistical modeling contexts where the goal is to explain variation in the dependent variable rather than just predict it.

---

## A/B Testing

A method for comparing two versions (A and B) of something (e.g., webpage, app feature, email subject line) to determine which one performs better based on a specific metric (e.g., conversion rate, click-through rate). It's a form of randomized controlled experiment.

### Key A/B Testing Concepts

#### Null Hypothesis (in A/B Testing)
The hypothesis that there is no difference in the performance metric between version A (Control) and version B (Treatment). Any observed difference is assumed to be due to random chance.

#### Alternative Hypothesis (in A/B Testing)
The hypothesis that there *is* a statistically significant difference in the performance metric between version A and version B.

#### Type I Error (in A/B Testing)
Incorrectly concluding that version B is better than version A (rejecting the null hypothesis) when there is actually no difference. A false positive.

#### Type II Error (in A/B Testing)
Incorrectly concluding that there is no difference between version A and version B (failing to reject the null hypothesis) when version B actually performs differently. A false negative.

#### p-value (in A/B Testing)
The probability of observing the difference in performance (or a larger difference) between version A and version B, assuming the null hypothesis (no difference) is true. A low p-value suggests the observed difference is unlikely to be random chance.

#### A/B Testing
The overall methodology of comparing two versions (Control vs. Treatment) by randomly assigning users to experience one version and measuring their behavior against a key metric.

#### Control Group
The group of users exposed to the existing or baseline version (Version A).

#### Treatment Group (Variant Group)
The group of users exposed to the new or modified version being tested (Version B).

#### Variation
The alternative version (Version B or Treatment) being tested against the Control.

#### Hypothesis (in A/B Testing)
A specific, testable prediction about the expected outcome (e.g., "Changing the button color from blue to green will increase click-through rate by 10%").

#### Randomization
The process of randomly assigning users to either the Control or Treatment group to ensure unbiased comparison and minimize confounding factors.

#### Sample Size
The number of users or observations included in each group (Control and Treatment). Needs to be sufficiently large to detect a meaningful difference with statistical confidence (power).

#### Statistical Significance
The likelihood that the observed difference between the Control and Treatment groups is not due to random chance. Often determined by comparing the p-value to a predetermined threshold (alpha, e.g., 0.05).

#### Confidence Interval (in A/B Testing)
A range of values estimated from the sample data that likely contains the true difference in the metric between the two versions in the overall population.

#### Conversion Rate
A common metric in A/B testing: the percentage of users who complete a desired action (e.g., purchase, sign-up, click) out of the total users in that group.

#### Segmentation
Analyzing A/B test results within specific subgroups of users (e.g., by device, location, new vs. returning users) to understand if the impact varies across different segments.

#### Multivariate Testing (MVT)
Testing multiple variations of multiple elements simultaneously to understand the impact of each element and their interactions (e.g., testing 2 headlines x 3 images = 6 combinations). Contrasts with A/B testing, which typically tests one change at a time.

#### Sequential Testing
An A/B testing approach where results are monitored continuously, allowing the test to be stopped early if a statistically significant result is reached, potentially saving time and resources. Requires specific statistical methods (e.g., SPRT).

#### Effect Size
Quantifies the magnitude of the difference observed between the groups (e.g., the absolute or relative difference in conversion rates). Indicates the practical significance of the result.

#### Post-test Analysis
Further analysis conducted after the main A/B test concludes, such as examining secondary metrics, looking at long-term effects, or investigating potential biases.

#### Contextual Effects
Differences in user behavior or responses influenced by external factors present during the test (e.g., time of day, day of week, device type, ongoing marketing campaigns).

#### Order Effects
Occurs if the order in which users are exposed to variations influences their behavior (less common in standard A/B tests but relevant in within-subject designs).

#### Duration Effects (Novelty/Learning Effects)
Changes in user behavior over the duration of the test. Users might initially react strongly to a change (novelty effect) or take time to adapt (learning effect).

#### Interaction Effects
In MVT, when the effect of changing one element depends on the variation of another element.

##### Potential Biases in A/B Testing

#### Sampling Bias
Occurs if the sample of users included in the test is not representative of the target population, leading to results that don't generalize.

#### Selection Bias
Bias introduced if the random assignment isn't truly random, or if certain user types are more likely to end up in one group than the other (e.g., due to technical glitches).

#### Confirmation Bias
The tendency for experimenters to interpret results in a way that confirms their pre-existing beliefs or hypotheses.

#### Experimenter Bias
Subtle influences from the experimenter's expectations on how the test is conducted or analyzed.

#### Volunteer Bias
If participation in the test is voluntary, users who opt-in might differ systematically from those who don't.

#### Cohort Effects
Differences in behavior between groups of users who started using the product/service at different times, which might confound results if not accounted for.

#### Temporal Bias (Time-Related Bias)
Bias resulting from external events or changes occurring during the test period that affect one group differently or invalidate the comparison (e.g., a holiday affecting only part of the test run).

#### Response Bias
Systematic differences in how users respond based on factors unrelated to the variations being tested (e.g., survey fatigue if feedback is requested).

---

## Model Evaluation

Assessing the performance and reliability of machine learning models.

### General Concepts

#### Overfitting
A modeling error where the model learns the training data too well, including its noise and random fluctuations. This leads to excellent performance on the training data but poor performance (generalization) on new, unseen data.

#### Underfitting
A modeling error where the model is too simple to capture the underlying patterns in the data. This leads to poor performance on both the training data and new data.

#### Cross-Validation
A resampling technique used to evaluate a model's performance and generalization ability. The data is split into multiple folds (subsets); the model is trained on some folds and tested on the remaining fold, repeated multiple times. Common types include K-Fold Cross-Validation and Leave-One-Out Cross-Validation. Helps provide a more robust estimate of model performance than a single train-test split.

#### Train-Test Split
A common practice where the dataset is divided into two subsets: a training set (used to train the model) and a test set (used to evaluate the final model's performance on unseen data). Provides an unbiased estimate of generalization performance.

#### P-value (in Model Evaluation)
While primarily from hypothesis testing, p-values can appear in model evaluation, particularly in regression output (testing significance of coefficients) or comparing models. Context is key.

---

## Regression Analysis

Modeling relationships between variables, specifically focusing on predicting a continuous target variable.

### Regression Assumptions

Conditions that should ideally be met for standard linear regression models (like OLS - Ordinary Least Squares) to produce reliable and unbiased results. Violations can impact coefficient estimates, standard errors, and p-values.

#### Linearity
*   **Definition:** The relationship between the independent variables and the *mean* of the dependent variable is linear.
*   **Validation:** Scatter plots of dependent variable vs. independent variables; plot of residuals vs. predicted values (should show no pattern).
*   **Strategy if Violated:** Apply transformations (e.g., log, square root, polynomial) to independent or dependent variables; add polynomial terms; use non-linear models.

#### Independence of Observations
*   **Definition:** The observations (and their errors) are independent of each other. One observation's value/error doesn't influence another's.
*   **Validation:** Primarily based on study design and data collection process. Check Durbin-Watson statistic for autocorrelation in residuals (especially for time-ordered data).
*   **Strategy if Violated:** Ensure proper sampling/experimental design; use models designed for dependent data (e.g., time series models, mixed-effects models for hierarchical data).

#### Homoscedasticity (Constant Variance)
*   **Definition:** The variance of the residuals (errors) is constant across all levels of the independent variables.
*   **Validation:** Plot residuals vs. predicted values (look for funnel shapes or changing spread); statistical tests like Breusch-Pagan or White test.
*   **Strategy if Violated:** Transform the dependent variable (e.g., log, Box-Cox); use weighted least squares (WLS) regression; use robust standard errors.

#### Normality of Residuals
*   **Definition:** The residuals of the model are approximately normally distributed. Important for the validity of confidence intervals and hypothesis tests on coefficients, especially with small sample sizes.
*   **Validation:** Q-Q (Quantile-Quantile) plot of residuals (should follow a straight line); histogram of residuals; statistical tests like Shapiro-Wilk or Kolmogorov-Smirnov test.
*   **Strategy if Violated:** Often acceptable with large sample sizes due to CLT. Transformations might help. If severely non-normal, consider generalized linear models (GLMs) or non-parametric regression.

#### No Multicollinearity (or Low Multicollinearity)
*   **Definition:** Independent variables are not highly correlated with each other. High multicollinearity makes it difficult to estimate the individual effect of predictors.
*   **Validation:** Examine correlation matrix of predictors; calculate Variance Inflation Factor (VIF) for each predictor (VIF > 5 or 10 often indicates problematic multicollinearity).
*   **Strategy if Violated:** Remove one of the highly correlated variables; combine correlated variables (e.g., create an index); use dimensionality reduction (PCA); use regularization techniques (Ridge, Lasso).

#### No Auto-correlation (Independence of Errors)
*   **Definition:** Residuals are uncorrelated with each other. This is a specific type of dependence, particularly relevant for time series data.
*   **Validation:** Durbin-Watson statistic (values near 2 suggest no autocorrelation, near 0 suggests positive, near 4 suggests negative); plot residuals vs. time; ACF plot of residuals.
*   **Strategy if Violated:** Use time series models (ARIMA, etc.) that explicitly model the autocorrelation; include lagged variables; adjust standard errors (e.g., Newey-West).

### Regression Metrics

Quantifying the performance of regression models.

#### RMSE (Root Mean Square Error)
The square root of the average of the squared differences between predicted and actual values. Measures the standard deviation of the residuals. Expressed in the same units as the target variable. Sensitive to large errors.
*   `RMSE = sqrt(mean((y_actual - y_predicted)^2))`

#### MAE (Mean Absolute Error)
The average of the absolute differences between predicted and actual values. Measures the average magnitude of errors. Less sensitive to outliers than RMSE. Expressed in the same units as the target variable.
*   `MAE = mean(|y_actual - y_predicted|)`

#### R-squared (Coefficient of Determination)
The proportion of the variance in the dependent variable that is predictable from the independent variables. Ranges from 0 to 1 (or 0% to 100%). Higher values indicate a better fit. Can be misleadingly high if many predictors are added.
*   `R² = 1 - (Sum of Squared Residuals / Total Sum of Squares)`

#### Adjusted R-squared
A modified version of R-squared that adjusts for the number of predictors in the model. It penalizes the addition of irrelevant predictors. Provides a more comparable measure across models with different numbers of predictors. Usually lower than R-squared.

#### MSE (Mean Squared Error)
The average of the squared differences between predicted and actual values. It's the variance of the residuals. Similar to RMSE but not square-rooted, so units are squared. Heavily penalizes large errors.
*   `MSE = mean((y_actual - y_predicted)^2)`

---

## Classification Analysis

Modeling relationships between variables, specifically focusing on predicting a categorical target variable.

### Classification Assumptions

Assumptions vary significantly depending on the algorithm used.

#### Feature Independence (Naive Bayes specific)
*   **Definition:** Assumes that predictors (features) are conditionally independent of each other, given the class label. This is a "naive" assumption but allows for efficient computation.
*   **Validation:** Difficult to fully validate. Correlation matrices can give insights. Despite violations, Naive Bayes often performs surprisingly well.
*   **Strategy if Violated:** Feature selection to remove redundant features; dimensionality reduction (PCA); use other algorithms if independence is strongly violated.

#### Linearity (Logistic Regression specific)
*   **Definition:** Assumes a linear relationship between the independent variables and the *log-odds* of the dependent variable.
*   **Validation:** Box-Tidwell test; visually inspect plots of predictors vs. log-odds (requires binning continuous predictors).
*   **Strategy if Violated:** Include interaction terms or polynomial terms; transformations of predictors; use non-linear classifiers (e.g., trees, SVM with non-linear kernel).

#### Class Balance
*   **Definition:** Many algorithms implicitly perform better or are easier to evaluate when classes are roughly balanced in size. Imbalance can bias models towards the majority class. This is more of a data characteristic than a strict model assumption, but crucial for performance.
*   **Validation:** Examine the frequency distribution of the target variable.
*   **Strategy if Violated:** Use appropriate evaluation metrics (Precision, Recall, F1, AUC, AUPRC); resampling techniques (oversampling minority, undersampling majority, SMOTE); adjust class weights in the algorithm; use anomaly detection approaches.

#### Feature Scaling (for distance-based/gradient-based algorithms)
*   **Definition:** Algorithms like SVM, KNN, Logistic Regression (with gradient descent), and Neural Networks assume features are on a similar scale. Features with larger ranges can dominate distance calculations or slow down/destabilize gradient descent.
*   **Validation:** Check the ranges and variances of numeric features.
*   **Strategy if Violated:** Apply feature scaling (Standardization or Normalization) before training the model.

### Classification Metrics

Quantifying the performance of classification models. Often derived from the Confusion Matrix.

#### Accuracy
The ratio of correctly predicted instances (True Positives + True Negatives) to the total number of instances. Simple but can be misleading, especially with imbalanced classes.
*   `Accuracy = (TP + TN) / (TP + TN + FP + FN)`

#### Precision (Positive Predictive Value)
Of all instances predicted as positive, what proportion were actually positive? Measures the accuracy of positive predictions. Important when the cost of False Positives is high.
*   `Precision = TP / (TP + FP)`

#### Recall (Sensitivity, True Positive Rate, Hit Rate)
Of all actual positive instances, what proportion were correctly predicted as positive? Measures the model's ability to find all positive instances. Important when the cost of False Negatives is high.
*   `Recall = TP / (TP + FN)`

#### F1 Score
The harmonic mean of Precision and Recall. Provides a single score that balances both concerns. Useful for imbalanced classes.
*   `F1 = 2 * (Precision * Recall) / (Precision + Recall)`

#### Specificity (True Negative Rate)
Of all actual negative instances, what proportion were correctly predicted as negative? Measures the model's ability to identify negative instances.
*   `Specificity = TN / (TN + FP)`
*   Note: `Specificity = 1 - False Positive Rate`

#### Balanced Accuracy
The average of Recall (Sensitivity) and Specificity. A good metric for imbalanced datasets as it considers performance on both classes equally.
*   `Balanced Accuracy = (Sensitivity + Specificity) / 2`

#### Area Under the ROC Curve (AUC-ROC)
The ROC curve plots the True Positive Rate (Recall) against the False Positive Rate (1 - Specificity) at various classification thresholds. AUC represents the probability that the model ranks a randomly chosen positive instance higher than a randomly chosen negative instance. Ranges from 0.5 (random) to 1 (perfect). Good overall measure of separability.

#### Area Under the Precision-Recall Curve (AUPRC)
The Precision-Recall curve plots Precision against Recall at various classification thresholds. AUPRC is the area under this curve. More informative than AUC-ROC for highly imbalanced datasets where the focus is on the minority (positive) class.

#### Log Loss (Logarithmic Loss or Cross-Entropy Loss)
Measures the performance of a classification model where the prediction input is a probability value between 0 and 1. Penalizes confident incorrect predictions more heavily. Lower values are better (0 is perfect).

#### Matthews Correlation Coefficient (MCC)
A correlation coefficient between the observed and predicted binary classifications. Ranges from -1 (total disagreement) to +1 (perfect agreement), with 0 indicating random prediction. Considered a balanced measure, robust to class imbalance.
*   `MCC = (TP*TN - FP*FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN))`

---

## Ensemble Methods

Techniques that combine predictions from multiple individual models (base learners) to produce a final prediction that is often more accurate and robust than any single model.

| Method                            | What is it                                                                                                                                                           | When to Use                                                                                                 | Pros                                                                                                    | Cons                                                                                                    |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------ |
| **Bagging (Bootstrap Aggregating)** | Trains multiple instances of the *same* base model (e.g., decision tree) on different random subsets of the training data (sampled *with replacement*). Predictions are aggregated (e.g., averaging for regression, voting for classification). | Effective for reducing variance in high-variance models (like complex decision trees). Helps prevent overfitting. | Reduces variance, improves stability, parallelizable.                                                    | Less effective if base models are simple (low variance). Can reduce interpretability.                      |
| **Random Forest**                 | An extension of Bagging specifically for decision trees. In addition to sampling data, it also samples a random subset of *features* at each split when building trees. | Versatile for classification and regression. Good default choice. Handles high dimensions and non-linearities well. | High accuracy, robust to outliers, handles missing values, provides feature importance scores.          | Can be computationally intensive. Less interpretable than a single tree. May not perform well on very sparse data. |
| **Boosting**                      | Builds models sequentially, with each new model focusing on correcting the errors made by the previous ones. Predictions are combined, often with weights favoring better models. | When seeking maximum accuracy, especially from weak learners (models slightly better than random guessing). | Often achieves state-of-the-art accuracy. Can handle mixed data types.                                | Sensitive to noisy data and outliers. Prone to overfitting if not carefully tuned. Sequential, so less parallelizable. |
| **AdaBoost (Adaptive Boosting)**    | A popular boosting algorithm. Iteratively trains weak learners, increasing the weight of misclassified instances so subsequent learners focus more on them.          | Effective for binary classification, especially with decision stumps (simple trees). Good starting point for boosting. | Relatively simple, often high accuracy, less prone to overfitting than some boosting methods if learners are weak. | Sensitive to noise/outliers. Performance depends heavily on the weak learner chosen.                   |
| **Gradient Boosting Machines (GBM)** | A general boosting framework. Sequentially adds models that predict the *residuals* (errors) of the previous ensemble. Uses gradient descent to minimize a loss function. | Highly effective for regression and classification on structured/tabular data. Flexible loss functions.     | Very high accuracy. Flexible (can optimize various loss functions). Can incorporate regularization.   | Can be slow to train. Prone to overfitting without proper tuning/regularization. More parameters to tune. |
| **XGBoost (Extreme Gradient Boosting)** | An optimized and scalable implementation of Gradient Boosting. Includes features like regularization (L1/L2), handling missing values, tree pruning, parallel processing. | When performance (speed and accuracy) is critical. Widely used in competitions and industry.             | Faster and more efficient than standard GBM. Built-in regularization prevents overfitting. Handles missing values. | Can still overfit on small datasets. More complex parameters to tune than simpler models.                  |
| **Stacking (Stacked Generalization)** | Trains multiple *different* base models. Then, trains a "meta-model" that takes the predictions of the base models as input features to make the final prediction. | When you have several well-performing but different models and want to combine their strengths.         | Can potentially achieve higher accuracy than any single base model. Leverages diverse model strengths. | Increases complexity significantly. Risk of overfitting the meta-model. Can be computationally expensive. |

---

## Clustering Analysis

Unsupervised learning techniques used to group similar data points together based on their features, without prior knowledge of the groups.

### Clustering Assumptions

Assumptions vary greatly depending on the algorithm. Understanding them helps choose the right method.

#### Cluster Shape & Size (K-means specific)
*   **Definition:** K-means assumes clusters are spherical, equally sized, and have similar densities.
*   **Validation:** Visualize data (e.g., using PCA/t-SNE). Check silhouette scores (lower scores for non-spherical might indicate poor fit).
*   **Strategy if Violated:** Use algorithms that handle arbitrary shapes (DBSCAN), different densities (DBSCAN), or model clusters probabilistically (Gaussian Mixture Models - GMM).

#### Number of Clusters (K-means, GMM specific)
*   **Definition:** Algorithms like K-means require the number of clusters (K) to be specified beforehand.
*   **Validation:** Use methods like the Elbow Method (plotting WCSS vs. K), Silhouette Analysis (plotting silhouette scores vs. K), or Gap Statistic to estimate an optimal K. Domain knowledge is often crucial.
*   **Strategy if Violated:** Use methods that don't require pre-specifying K (DBSCAN, Hierarchical Clustering - though a cut-off point is needed). Iterate with different K values using validation metrics.

#### Density & Separation (DBSCAN specific)
*   **Definition:** DBSCAN assumes clusters are dense regions separated by areas of lower density. It identifies core points, border points, and noise.
*   **Validation:** Visual inspection. Sensitivity analysis on DBSCAN parameters (`eps`, `min_samples`). Silhouette scores can sometimes help but are less ideal for density-based clusters.
*   **Strategy if Violated:** Adjust `eps` and `min_samples` parameters carefully. Consider other algorithms if density assumptions don't match the data structure (e.g., K-means if density is uniform, Hierarchical if structure is nested).

#### Feature Scale (Distance-based algorithms like K-means, DBSCAN, Hierarchical)
*   **Definition:** Assumes features contribute equally to distance calculations. Features with larger ranges can dominate the clustering process.
*   **Validation:** Compare feature ranges/variances. Evaluate cluster quality before and after scaling.
*   **Strategy if Violated:** Apply feature scaling (Standardization or Normalization) before clustering.

#### Noise & Outliers
*   **Definition:** Some algorithms are sensitive to noise and outliers, which can distort cluster centroids (K-means) or merge distinct clusters.
*   **Validation:** Pre-identify outliers using statistical methods (Z-score, IQR) or visualization. Observe clustering results for points assigned far from cluster centers.
*   **Strategy if Violated:** Remove or cap outliers before clustering. Use robust algorithms like DBSCAN (which explicitly identifies noise) or use robust versions of K-means (like K-medians).

### Clustering Metrics

Evaluating the quality of clustering results (often challenging due to the unsupervised nature).

#### Silhouette Coefficient
*   **Definition:** Measures how similar a data point is to its own cluster compared to other clusters. Ranges from -1 (poorly clustered) to +1 (well-clustered), with 0 indicating overlapping clusters. Values averaged across all points give an overall score.
*   **Calculation:** For each point `i`: `a =` average distance to points in its own cluster; `b =` average distance to points in the *nearest* other cluster. Silhouette score = `(b - a) / max(a, b)`.

#### Davies-Bouldin Index
*   **Definition:** Measures the average similarity ratio of each cluster with its most similar cluster. Similarity is based on the ratio of within-cluster distances to between-cluster distances. *Lower* values indicate better clustering (clusters are compact and well-separated).
*   **Calculation:** Involves calculating cluster diameters (within-cluster dispersion) and distances between cluster centroids. The index is the average of the maximum similarity ratios for each cluster.

#### Calinski-Harabasz Index (Variance Ratio Criterion)
*   **Definition:** Measures the ratio of the sum of between-cluster dispersion to the sum of within-cluster dispersion. *Higher* values indicate better clustering (clusters are dense and well-separated).
*   **Calculation:** Calculated using the sums of squares between clusters (SSB) and within clusters (SSW), adjusted by degrees of freedom: `(SSB / (K-1)) / (SSW / (N-K))`, where N is total points, K is number of clusters.

#### Dunn Index
*   **Definition:** Aims to identify dense and well-separated clusters. Defined as the ratio of the minimum inter-cluster distance (distance between the closest points in different clusters) to the maximum intra-cluster distance (diameter of the largest cluster). *Higher* values indicate better clustering.
*   **Calculation:** `min(inter-cluster distance) / max(intra-cluster distance)`. Can be sensitive to outliers.

**Considerations for Metric Choice:**

*   **Data Nature:** Metrics relying on centroids (like Davies-Bouldin, Calinski-Harabasz) may work less well for non-spherical clusters. Silhouette is generally more versatile.
*   **Interpretability:** Silhouette score is often considered more intuitive.
*   **Scalability:** Computation complexity varies; some metrics are faster to compute on large datasets than others.

---

## Probabilistic Models and Bayesian Methods

Modeling uncertainty and updating beliefs using probability theory, particularly Bayes' theorem.

| Method                     | Definitions                                                                                                                                        | When to Use                                                                                                                            | Pros                                                                                            | Cons                                                                                                       |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| **Bayesian Inference**     | A method of statistical inference using Bayes' theorem to update the probability of a hypothesis (or parameter value) based on new evidence (data). | When prior knowledge is available and should be incorporated. When quantifying uncertainty in predictions/parameters is crucial.          | Incorporates prior knowledge. Provides full posterior distributions (quantifies uncertainty). Flexible. | Can be computationally intensive (e.g., MCMC). Choice of prior can be subjective and influential.           |
| **Markov Chains**          | A stochastic model describing a sequence of possible events where the probability of transitioning to the next state depends *only* on the current state (Markov property or memorylessness). | Modeling systems that change states over time randomly, where the future depends only on the present state (e.g., random walks, some queueing systems). | Simplifies modeling of complex processes. Mathematically tractable. Widely applicable.            | The memoryless assumption might not hold for all real-world processes.                                     |
| **Hidden Markov Models (HMM)** | A statistical Markov model where the system being modeled is assumed to be a Markov process with *unobservable* (hidden) states. We only observe outputs or emissions dependent on the hidden state. | Modeling systems with underlying hidden states that generate observable sequences (e.g., speech recognition, bioinformatics, financial modeling). | Effective for sequential data with latent structures. Can infer hidden states from observations. | Training can be complex (e.g., Baum-Welch algorithm). Assumes Markov property for hidden states. Computationally demanding. |

---

## Dimensionality Reduction Techniques

Reducing the number of features (dimensions) in a dataset while preserving important information. Used for visualization, noise reduction, computational efficiency, and mitigating the curse of dimensionality.

| Technique                                        | Definitions                                                                                                                                                                                                                                                                    | When to Use                                                                                                                                                                           | Strategy / Considerations                                                                                                                                                                                                                                                              |
| :----------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Principal Component Analysis (PCA)**           | A linear technique that transforms data into a new coordinate system where axes (principal components) are orthogonal and capture the maximum variance in the data. Components are ordered by the amount of variance they explain.                                                  | For linear dimensionality reduction. When the goal is to retain maximum variance. Data preprocessing for other ML algorithms. Noise reduction.                                             | Requires scaling data first (e.g., Standardization). Choose the number of components based on cumulative explained variance (e.g., 80-95%) using a scree plot. Assumes linearity. Components can be hard to interpret.                                                              |
| **t-Distributed Stochastic Neighbor Embedding (t-SNE)** | A non-linear technique primarily used for *visualization*. It models high-dimensional data points based on similarity (neighbor relationships) and finds a low-dimensional embedding that preserves these similarities (local structure).                                | Primarily for visualizing high-dimensional data in 2D or 3D to explore clusters or structure. Not typically used for preprocessing before other ML tasks.                               | Computationally expensive, especially for large datasets (often preceded by PCA). Results depend heavily on the `perplexity` parameter. Distances between clusters in the t-SNE plot are not always meaningful. Does not preserve global structure well. Run multiple times for stability. |
| **Uniform Manifold Approximation and Projection (UMAP)** | A non-linear technique similar to t-SNE but often faster and better at preserving both local and global data structure. Based on manifold learning and topological data analysis.                                                                                       | For visualization (often preferred over t-SNE now) and general non-linear dimensionality reduction. Can be used as a preprocessing step. Handles larger datasets better than t-SNE.      | Generally faster than t-SNE. Performance depends on parameters like `n_neighbors` and `min_dist`. Tends to preserve global structure better than t-SNE. Still non-deterministic to some extent.                                                                                      |
| **Linear Discriminant Analysis (LDA)**           | A *supervised* linear technique used for both classification and dimensionality reduction. It finds feature combinations (linear discriminants) that *maximize the separability between known classes*.                                                                   | For dimensionality reduction specifically when class labels are known and the goal is to improve class separation (often as preprocessing for classification).                            | Requires labeled data. Assumes normality of data within classes and equal covariance matrices between classes. The number of components is limited to (number of classes - 1). Sensitive to outliers.                                                                                 |

**Validation or Application Considerations:**

*   **Preservation of Data Structure:** Evaluate how well the reduced data retains the original structure (e.g., using reconstruction error for PCA, visual inspection for t-SNE/UMAP, or downstream task performance).
*   **Computational Efficiency:** PCA and LDA are generally faster than t-SNE and UMAP.
*   **Suitability for Downstream Tasks:** LDA is designed for classification preprocessing. PCA is general-purpose. t-SNE is mainly for visualization. UMAP can be used for both visualization and preprocessing.

---

## Time Series Analysis

Analyzing sequential data points collected over time to identify patterns, trends, seasonality, and make forecasts.

### Time Series Analysis Methods

| Method                                           | Definitions                                                                                                                                                                                                                                                                                                                         | When to Use                                                                                                                                                            | Pros                                                                                                                                        | Cons                                                                                                                                                                    |
| :----------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ARIMA (Autoregressive Integrated Moving Average)** | A class of models that captures temporal dependencies using autoregression (AR - dependency on past values), integration (I - differencing to achieve stationarity), and moving averages (MA - dependency on past forecast errors). Defined by orders (p, d, q).                                                                     | For univariate time series that are stationary or can be made stationary by differencing. Captures linear relationships and autocorrelation. Widely used baseline.      | Flexible, well-understood statistical properties. Can model many types of time series.                                                     | Requires stationarity. Parameter selection (p, d, q) can be subjective (using ACF/PACF plots, AIC/BIC). Assumes linear relationships. Doesn't handle seasonality directly. |
| **Seasonal ARIMA (SARIMA)**                      | An extension of ARIMA that includes additional seasonal terms (P, D, Q) and a seasonal period parameter (s) to explicitly model seasonality along with trends and autocorrelation. Defined by orders (p, d, q)(P, D, Q)s.                                                                                                           | For univariate time series with clear seasonal patterns, in addition to potential trends and autocorrelation.                                                          | Explicitly models seasonality. Extends the flexibility of ARIMA.                                                                            | More complex with more parameters to estimate (p, d, q, P, D, Q, s). Parameter selection is more challenging. Still assumes linearity.                               |
| **Exponential Smoothing (ETS)**                  | A family of forecasting methods where predictions are weighted averages of past observations, with weights decreasing exponentially as observations get older. Variants include Simple ETS (level only), Holt's (level and trend), and Holt-Winters (level, trend, and seasonality).                                               | Good for data with clear trends and/or seasonality but potentially less complex autocorrelation structures than ARIMA might handle. Often performs well automatically. | Simple, intuitive, computationally efficient. State-space framework provides statistical grounding and confidence intervals. Robust.         | Can be less flexible than ARIMA for complex autocorrelation. Parameter fitting might be automatic but understanding the underlying model is important.                    |
| **Prophet**                                      | A forecasting procedure developed by Facebook, based on an additive model fitting non-linear trends (piecewise linear or logistic growth) with yearly, weekly, and daily seasonality, plus holiday effects. Designed to be easy to use and robust to missing data and outliers.                                                     | For time series with strong seasonal effects (multiple periods), holidays, trends with changepoints. Good for business forecasting with human-interpretable components. | Easy to use, handles multiple seasonalities and holidays well. Robust to outliers and missing data. Tunable changepoints for trends.      | Can be less accurate than complex models like ARIMA or LSTMs on some datasets. Primarily designed for specific types of business time series. Less flexible for complex dynamics. |
| **Long Short-Term Memory Networks (LSTMs)**      | A type of Recurrent Neural Network (RNN) capable of learning long-term dependencies in sequential data. Uses gating mechanisms (input, forget, output gates) to control information flow.                                                                                                                                       | For complex time series with non-linear relationships, long-term dependencies, or when incorporating multivariate inputs. Large datasets are often required.        | Can model complex non-linear patterns. Captures long-range dependencies effectively. Can handle multivariate time series.                   | Requires significant data and computational resources for training. Complex architecture, harder to interpret ("black box"). Prone to overfitting without careful tuning. |

### Time Series Analysis Assumptions

Assumptions underlying common time series models. Violations can lead to poor model fit and inaccurate forecasts.

| Assumption          | Definition                                                                           | Steps to Check/Ensure                                                                                                                                                                                                     |
| :------------------ | :----------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Stationarity**    | Statistical properties (mean, variance, autocorrelation) do not change over time.    | **Check:** Visual inspection (plot data), Augmented Dickey-Fuller (ADF) test, KPSS test. **Ensure:** Apply differencing (subtract previous value) until stationary. Log or Box-Cox transforms can stabilize variance. |
| **No Autocorrelation (of Residuals)** | Residuals (errors) from a fitted model should be uncorrelated (white noise). | **Check:** Plot ACF/PACF of residuals (should be within confidence bounds after lag 0), Ljung-Box test on residuals. **Ensure:** Adjust model order (p, q, P, Q) if significant autocorrelation remains in residuals.    |
| **Homoscedasticity (of Residuals)** | Variance of the residuals is constant over time.                             | **Check:** Plot residuals vs. time, plot residuals vs. fitted values. Look for changing spread. **Ensure:** Transformations (log, Box-Cox) on original data might help. Consider GARCH models if variance changes predictably. |
| **Normality of Residuals** | Residuals are normally distributed (important for confidence intervals/prediction intervals). | **Check:** Histogram of residuals, Q-Q plot of residuals, Shapiro-Wilk test. **Ensure:** Often less critical than other assumptions, especially with large samples. Transformations might help.                     |

##### Model-Specific Assumptions Highlights

*   **ARIMA/SARIMA:** Primarily Stationarity and Linearity. Assumes relationships between lagged values/errors are linear. `d`/`D` parameter handles non-stationarity via differencing. `s` parameter in SARIMA assumes a *fixed* seasonal period.
*   **ETS:** Assumes data can be decomposed into additive or multiplicative components (Error, Trend, Seasonality). Assumes patterns will continue. State-space versions often assume normally distributed errors for interval calculation.
*   **Prophet:** Assumes additive components (trend, seasonality, holidays). Flexible non-linear trends but assumes specific seasonal forms (Fourier series).
*   **LSTMs:** Assumes dependencies exist in the sequence. Requires sufficient data and proper scaling/normalization for stable training. The choice of sequence length (window size) is crucial.

##### General Time Series Assumptions

*   **Sufficient Data:** Need enough historical data to identify patterns (especially seasonality) and train models reliably.
*   **No Perfect Collinearity:** If using external regressors (e.g., in ARIMAX), they shouldn't be perfectly correlated.

##### General Steps for Handling Time Series Data

1.  **Visualize:** Plot the data to identify trends, seasonality, outliers, and potential changepoints.
2.  **Decompose:** Separate the series into trend, seasonal, and residual components.
3.  **Stationarize:** Check for stationarity and apply transformations/differencing if needed.
4.  **Model Selection:** Choose appropriate models based on data characteristics (e.g., ARIMA for autocorrelation, ETS for trend/seasonality, Prophet for holidays/multiple seasons, LSTMs for complex non-linearity).
5.  **Parameter Estimation:** Fit the model(s) to the training data. Select orders/parameters (e.g., using ACF/PACF, AIC/BIC, grid search).
6.  **Diagnostic Checking:** Evaluate model fit by analyzing residuals (check for autocorrelation, normality, constant variance).
7.  **Forecasting:** Generate forecasts on a hold-out test set or for future periods. Evaluate forecast accuracy using metrics like MAE, RMSE, MAPE.
8.  **Iteration:** Refine the model based on diagnostics and evaluation.

---

## Recommender Systems

Algorithms designed to suggest relevant items (e.g., movies, products, articles) to users based on various factors like past behavior, user profiles, or item attributes.

| Method                             | Definitions                                                                                                                                                                                                                                                                                                 | When to Use                                                                                                                                                                                             | Pros                                                                                                                                                                                                      | Cons                                                                                                                                                                                                                                                                        |
| :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Collaborative Filtering (CF)**   | Recommends items based on the preferences and behavior of *similar users* (User-based CF) or by finding items *similar* to those the user has liked (Item-based CF). Relies on the user-item interaction matrix (e.g., ratings, clicks, purchases). Assumption: Users who agreed in the past will agree in the future. | Widely used when sufficient user interaction data is available (e.g., e-commerce, streaming). Good for discovering new items based on collective behavior (serendipity).                               | Can find diverse and unexpected items. Doesn't require item content analysis. Captures latent user tastes.                                                                                                | Suffers from the "cold start" problem (new users/items have little data). Data sparsity (most users interact with few items). Scalability challenges with very large datasets. Popularity bias (tends to recommend popular items).                                               |
| **Content-Based Filtering**        | Recommends items similar to those a user has liked *in the past*, based on the *features* or *content* of the items (e.g., genre, keywords, product attributes) and a profile of the user's preferences derived from their past interactions.                                                                | Useful when item metadata is rich and available. Good for recommending niche items or to users with unique tastes. Helps address the cold start problem for new items (if they have descriptive features). | User independence (recommendations for one user don't affect others). Can recommend new and unpopular items. Provides transparency (can explain *why* an item is recommended based on features).         | Limited by the quality and availability of feature extraction/metadata. Tends to recommend items very similar to past preferences ("filter bubble"), limiting discovery. Cold start for users (needs user interaction history to build profile).                                 |
| **Hybrid Recommender Systems**     | Combines techniques from collaborative filtering, content-based filtering, and potentially other approaches (e.g., demographic, knowledge-based) to leverage their strengths and mitigate weaknesses. Strategies include weighting, switching, mixing, or feature combination.                                | Often used in practice to achieve better overall performance, balancing accuracy, diversity, and addressing issues like cold start and sparsity.                                                  | Can provide more accurate and robust recommendations. Overcomes limitations of individual methods (e.g., combining CF's serendipity with Content's specificity). Improved handling of cold start/sparsity. | Increased complexity in design, implementation, and tuning. Finding the optimal combination strategy can be challenging.                                                                                                                                                         |
| **Matrix Factorization Techniques (e.g., SVD, ALS, NMF)** | Decomposes the sparse user-item interaction matrix into lower-dimensional latent factor matrices for users and items. These factors represent underlying characteristics. Predictions are made by reconstructing the matrix from these factors. Often used within CF.                   | A core technique for collaborative filtering, especially effective with explicit feedback (ratings). Good at handling sparsity and scaling compared to basic neighborhood methods.                       | Captures latent features/preferences. Handles sparse data well. Scalable algorithms exist (e.g., ALS). Good prediction accuracy.                                                                          | Latent factors can be hard to interpret. Less effective with purely implicit feedback unless adapted. Can still suffer from cold start. Requires careful tuning of dimensionality and regularization.                                                                       |
| **Deep Learning Methods (e.g., NCF, CNNs, RNNs)** | Utilizes neural networks to model complex patterns in user-item interactions. Can be applied to CF (e.g., Neural Collaborative Filtering - NCF), content analysis (e.g., CNNs for images/text), or sequential behavior (e.g., RNNs/LSTMs for session-based recommendations).                  | For modeling complex, non-linear relationships. When large datasets are available. For incorporating diverse data types (images, text, sequences) into recommendations. Achieving state-of-the-art accuracy. | Can model highly complex patterns. Can integrate various data sources seamlessly. Effective for sequential/session-based recommendations.                                                               | Requires significant data and computational power. "Black box" nature makes interpretation difficult. Prone to overfitting. Design and tuning complexity.                                                                                                                  |
| **Knowledge-Based Systems**        | Recommends items based on explicit knowledge about item properties, user requirements, and recommendation rules (constraints). Doesn't primarily rely on past user behavior. Examples include constraint-based and case-based reasoning.                                                                | Useful in domains where purchases are infrequent or items are complex (e.g., financial services, cars, real estate). When detailed user preferences can be elicited directly. Addresses cold start well.   | Handles cold start effectively. Recommendations can be highly customized based on explicit user needs. Justification for recommendations is clear.                                                     | Requires significant effort to build and maintain the knowledge base (rules, constraints). Less adaptive to changing user tastes unless profile is updated. Can feel less personalized than behavioral methods.                                                               |
| **Association Rule Mining (e.g., Apriori)** | Identifies items that frequently co-occur in user transactions or interactions (e.g., "users who bought X also bought Y"). Based on concepts like support, confidence, and lift.                                                                                                            | Often used for Market Basket Analysis to find product associations. Can supplement other recommendation methods ("related items"). Simple form of item-based recommendation.                         | Simple, interpretable rules. Useful for discovering relationships between items.                                                                                                                    | Doesn't consider user preferences directly. Can generate many trivial or obvious rules. Doesn't typically provide personalized rankings. Performance can degrade with very large item sets.                                                                          |
| **Ranking-based Methods**          | Focuses explicitly on generating an *ordered* list of recommendations rather than just predicting ratings or relevance scores. Uses techniques like Learning to Rank (LTR) or pairwise comparison models to optimize the order of recommended items based on user preferences or business goals.               | When the order of presented items is crucial (e.g., top-N recommendations, search results). Optimizing for ranking-specific metrics (e.g., NDCG, MAP).                                            | Directly optimizes the ranking quality. Can incorporate various features into the ranking function. Aligns well with how users often consume recommendations (top of the list matters most).          | Can be more complex to implement and train than simple scoring methods. Requires relevance judgments or interaction data suitable for learning ranking preferences.                                                                                                    |