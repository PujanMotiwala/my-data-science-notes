# Variance and Standard Deviation

## Definition / Introduction
*   While [[01_Expected_Value|Expected Value]] $E[X]$ describes the center of a random variable's distribution, **Variance** $Var(X)$ measures its **spread or dispersion**.
*   It quantifies how much the values of the random variable $X$ tend to deviate from their mean $\mu = E[X]$ on average. A higher variance means values are more spread out; lower variance means they are more clustered around the mean.
*   **Standard Deviation** $SD(X)$ or $\sigma_X$ is simply the **square root of the variance**. It's often preferred for interpretation because it's in the *same units* as the random variable $X$.
*   Notation: Variance $Var(X)$, $\sigma^2$, or $\sigma_X^2$. Standard Deviation $SD(X)$, $\sigma$, or $\sigma_X$.

## Key Concepts

### 1. Definition based on Expected Squared Deviation
*   The variance is defined as the expected value of the *squared difference* between the random variable $X$ and its mean $\mu = E[X]$:
    $$ Var(X) = E[(X - \mu)^2] $$
*   **Calculation (Discrete):** $Var(X) = \sum_{\text{all } x} (x - \mu)^2 p(x)$
*   **Calculation (Continuous):** $Var(X) = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) \, dx$

### 2. Computational Formula (Often Easier)
*   A more convenient formula for calculating variance is derived from the definition using [[01_Expected_Value|linearity of expectation]]:
    $$ Var(X) = E[X^2] - (E[X])^2 $$
    $$ Var(X) = E[X^2] - \mu^2 $$
*   This requires calculating two expected values: $E[X]$ (the mean) and $E[X^2]$ (the expected value of X squared, calculated using [[01_Expected_Value|LOTUS]] as $\sum x^2 p(x)$ or $\int x^2 f(x) dx$).

### 3. Standard Deviation
*   The standard deviation is the positive square root of the variance:
    $$ SD(X) = \sigma = \sqrt{Var(X)} = \sqrt{E[(X - \mu)^2]} $$
*   **Interpretation:** $\sigma$ measures the typical or average distance of the values of $X$ from their mean $\mu$. A smaller $\sigma$ means data points are typically close to the mean; a larger $\sigma$ means they are typically far from the mean.

### 4. Properties of Variance
*   **Non-negativity:** $Var(X) \ge 0$. Variance is zero if and only if $X$ is a constant (no spread).
*   **Constants:** $Var(b) = 0$ for any constant $b$.
*   **Linear Transformation:** For constants $a$ and $b$:
    $$ Var(aX + b) = a^2 Var(X) $$
    *Note:* Adding a constant $b$ shifts the distribution but doesn't change its spread, so $b$ disappears. Multiplying by $a$ scales the deviations, and squaring $a$ reflects the squaring in the variance definition.
    *   Consequently: $SD(aX + b) = |a| SD(X)$.

### 5. Variance of a Sum of Random Variables
*   For any random variables $X$ and $Y$:
    $$ Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X, Y) $$
    where $Cov(X, Y)$ is the [[03_Covariance_and_Correlation|Covariance]] between X and Y.
*   **If X and Y are [[../01 Basic Probability Theory/05_Independence|Independent]]:** Then $Cov(X, Y) = 0$, and the formula simplifies significantly:
    $$ Var(X + Y) = Var(X) + Var(Y) \quad (\text{if X, Y independent}) $$
    $$ Var(X - Y) = Var(X) + Var(Y) \quad (\text{if X, Y independent}) $$
    *Note:* Variance ADDS even when subtracting independent variables because subtraction can still increase the range of outcomes.

## Connections to Other Topics & Relevance
*   **Risk Assessment:** In finance and business, variance and standard deviation are key measures of risk or volatility (e.g., of investment returns).
*   **Data Analysis & Feature Scaling:** Standard deviation is used in standardization (calculating [[../03 Common Probability Distributions/05_Normal_Gaussian_Distribution|Z-scores]]: $Z = (X - \mu) / \sigma$) which is essential for many machine learning algorithms. Understanding variance helps interpret feature importance and variability.
*   **Confidence Intervals & Hypothesis Testing:** Standard deviation (often estimated from samples as the standard error) is crucial for constructing confidence intervals and performing hypothesis tests about population means.
*   **[[../03 Common Probability Distributions/05_Normal_Gaussian_Distribution|Normal Distribution]] & Empirical Rule:** Standard deviation defines the intervals ($\mu \pm k\sigma$) containing specific percentages of data (68%, 95%, 99.7%).
*   **Process Control:** Used to monitor the stability and consistency of processes (e.g., manufacturing).

## Summary
*   **Variance $Var(X)$** measures the expected squared deviation from the mean $E[X]$, quantifying spread. $\sigma^2 = E[(X - \mu)^2]$.
*   **Standard Deviation $SD(X) = \sigma = \sqrt{Var(X)}$** measures the typical deviation from the mean, in the original units.
*   Calculation: $Var(X) = E[X^2] - (E[X])^2$.
*   Properties: $Var(aX + b) = a^2 Var(X)$. For independent RVs, $Var(X + Y) = Var(X) + Var(Y)$.
*   Fundamental for understanding risk, variability, and for many statistical procedures.

## Sources
*   [Wikipedia: Variance](https://en.wikipedia.org/wiki/Variance)
*   [Khan Academy: Variance and Standard Deviation](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/v/variance-of-a-discrete-random-variable)
*   [PennState STAT 414: Variance](https://online.stat.psu.edu/stat414/lesson/19/19.3) (Continuous) & Lesson 11 (Discrete)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross; DeGroot & Schervish) - Consult relevant chapters.

## TAGS
[[Probability]] [[Random Variable]] [[Variance]] [[Standard Deviation]] [[Dispersion]] [[Spread]] [[Risk]] [[Expected Value]] [[PMF]] [[PDF]] [[Math]] [[Statistics]] [[Feature Scaling]]