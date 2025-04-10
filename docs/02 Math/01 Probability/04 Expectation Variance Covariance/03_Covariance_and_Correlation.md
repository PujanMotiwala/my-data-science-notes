# Covariance and Correlation

## Definition / Introduction
*   While [[02_Variance_and_Standard_Deviation|Variance]] measures the spread of a single random variable, **Covariance** and **Correlation** measure the degree to which **two random variables move together**.
*   **Covariance** indicates the direction of the linear relationship (positive or negative). A positive covariance suggests that as one variable tends to be above its mean, the other also tends to be above its mean. A negative covariance suggests they move in opposite directions relative to their means.
*   **Correlation** (specifically, Pearson correlation coefficient $\rho$) standardizes covariance to a unitless value between -1 and +1, making it easier to interpret the *strength* and direction of the *linear* relationship, regardless of the variables' scales.
*   Notation: Covariance $Cov(X, Y)$ or $\sigma_{XY}$. Correlation $Corr(X, Y)$, $\rho$, or $\rho_{XY}$.

## Key Concepts

### 1. Covariance
*   **Definition:** The [[01_Expected_Value|expected value]] of the product of the deviations of two random variables $X$ and $Y$ from their respective means ($\mu_X = E[X]$, $\mu_Y = E[Y]$):
    $$ Cov(X, Y) = \sigma_{XY} = E[(X - \mu_X)(Y - \mu_Y)] $$
*   **Computational Formula:** Derived using linearity of expectation:
    $$ Cov(X, Y) = E[XY] - E[X]E[Y] = E[XY] - \mu_X \mu_Y $$
    Requires calculating $E[X]$, $E[Y]$, and $E[XY]$ (the expected value of the product, found using the [[05_Joint_Marginal_Conditional_Distributions|joint distribution]]).
*   **Interpretation of Sign:**
    *   $Cov(X, Y) > 0$: Indicates a positive linear relationship (X and Y tend to move in the same direction relative to their means).
    *   $Cov(X, Y) < 0$: Indicates a negative linear relationship (X and Y tend to move in opposite directions relative to their means).
    *   $Cov(X, Y) = 0$: Suggests no *linear* relationship. (Important: Could still have a non-linear relationship).
*   **Units:** The units of covariance are the units of X multiplied by the units of Y, making it hard to compare across different pairs of variables.

### 2. Correlation (Pearson Correlation Coefficient)
*   **Definition:** Covariance scaled by the product of the [[02_Variance_and_Standard_Deviation|standard deviations]] of the two variables ($\sigma_X = SD(X)$, $\sigma_Y = SD(Y)$):
    $$ Corr(X, Y) = \rho_{XY} = \frac{Cov(X, Y)}{\sigma_X \sigma_Y} $$
    $$ \rho_{XY} = \frac{E[(X - \mu_X)(Y - \mu_Y)]}{\sigma_X \sigma_Y} $$
    Requires $\sigma_X > 0$ and $\sigma_Y > 0$.
*   **Properties & Interpretation:**
    *   **Range:** $-1 \le \rho \le +1$.
    *   $\rho = +1$: Perfect positive *linear* relationship.
    *   $\rho = -1$: Perfect negative *linear* relationship.
    *   $\rho = 0$: No *linear* relationship.
    *   Values closer to +1 or -1 indicate stronger linear relationships. Values closer to 0 indicate weaker linear relationships.
    *   **Unitless:** Allows comparison of relationship strength across different pairs of variables.

### 3. Properties of Covariance
*   $Cov(X, X) = Var(X)$
*   $Cov(X, Y) = Cov(Y, X)$ (Symmetric)
*   $Cov(aX + b, cY + d) = ac Cov(X, Y)$ for constants $a, b, c, d$.
*   $Cov(X + Z, Y) = Cov(X, Y) + Cov(Z, Y)$ (Linearity/Bilnearity)
*   $Var(X+Y) = Var(X) + Var(Y) + 2 Cov(X, Y)$

### 4. Independence vs. Zero Correlation
*   If $X$ and $Y$ are **[[05_Independence|independent]]**, then $Cov(X, Y) = 0$ and $Corr(X, Y) = 0$.
    *   *Proof Sketch:* If independent, $E[XY] = E[X]E[Y]$, so $Cov(X, Y) = E[XY] - E[X]E[Y] = 0$.
*   **Important:** The converse is **not** generally true. $Cov(X, Y) = 0$ (or $\rho = 0$) **does not** imply independence. It only implies the absence of a *linear* relationship. Variables can have a strong non-linear relationship (e.g., $Y = X^2$ for $X \sim N(0,1)$) and still have zero covariance/correlation.
    *   (Exception: If X and Y are jointly Normally distributed, then zero correlation *does* imply independence).

### 5. Correlation vs. Causation
*   **Critical Distinction:** Correlation measures the statistical association between two variables. It **does not** imply that one variable *causes* the other. A correlation might arise due to:
    *   Causation (X causes Y, or Y causes X)
    *   A third, unobserved confounding variable affecting both X and Y.
    *   Coincidence (spurious correlation).

## Connections to Other Topics & Relevance
*   **Feature Selection & Engineering:** Correlation analysis helps identify redundant features (high correlation) or features strongly related to a target variable. Used in understanding feature interactions.
*   **[[../../06 Machine Learning/02 Supervised/01 Regression/01_Simple Linear Regression/Assumptions/03 No or little multicollinearity|Multicollinearity]] in Regression:** High correlation between predictor variables is problematic for interpreting linear models.
*   **Portfolio Theory (Finance):** Covariance and correlation are essential for calculating portfolio risk and diversification benefits. Combining assets with low or negative correlation can reduce overall portfolio variance.
*   **[[02_Variance_and_Standard_Deviation|Variance of Sums]]:** Covariance appears in the formula $Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X, Y)$.
*   **Dimensionality Reduction:** Techniques like Principal Component Analysis (PCA) rely heavily on the covariance matrix of the data.

## Summary
*   **Covariance $Cov(X, Y)$** measures the direction of the linear relationship between $X$ and $Y$. Units depend on X and Y. $E[(X-\mu_X)(Y-\mu_Y)] = E[XY] - E[X]E[Y]$.
*   **Correlation $Corr(X, Y)$ or $\rho$** standardizes covariance ($\frac{Cov(X,Y)}{\sigma_X \sigma_Y}$) to be between -1 and +1, measuring the strength and direction of the *linear* relationship. It is unitless.
*   $\rho = +1$: Perfect positive linear relation. $\rho = -1$: Perfect negative linear relation. $\rho = 0$: No linear relation.
*   **[[05_Independence|Independence]] implies zero correlation**, but zero correlation **does not** imply independence (unless jointly Normal).
*   **Correlation $\neq$ Causation**.

## Sources
*   [Wikipedia: Covariance](https://en.wikipedia.org/wiki/Covariance), [Wikipedia: Correlation](https://en.wikipedia.org/wiki/Correlation)
*   [Khan Academy: Covariance and Correlation](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/correlation-coefficient-r/v/correlation-and-causality) (Focuses on sample correlation, but concepts overlap)
*   [PennState STAT 414: Covariance & Correlation](https://online.stat.psu.edu/stat414/lesson/21/21.1)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross; DeGroot & Schervish) - Consult relevant chapters.

## TAGS
[[Probability]] [[Random Variable]] [[Covariance]] [[Correlation]] [[Pearson Correlation]] [[Linear Relationship]] [[Dependence]] [[Independence]] [[02 Math/02 Inferential statistics/Tradeoffs/Variance]] [[02 Math/index]] [[Statistics]] [[Feature Selection]] [[Multicollinearity]]