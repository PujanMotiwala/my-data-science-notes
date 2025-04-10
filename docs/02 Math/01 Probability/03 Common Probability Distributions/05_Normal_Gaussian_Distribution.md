# Normal (Gaussian) Distribution

## Definition / Introduction
*   The Normal distribution, also known as the Gaussian distribution or the "bell curve," is arguably the most important [[02 Math/01 Probability/02 Random Variables/01_Definition|Continuous Probability Distribution]] in statistics and many scientific fields.
*   It describes data that cluster around a central mean value ($\mu$), with probabilities tapering off symmetrically as values move further away from the mean.
*   Many natural phenomena (e.g., heights, blood pressure), measurement errors, and sums/averages of random variables (due to the [[02_Central_Limit_Theorem_CLT|Central Limit Theorem]]) tend to follow a Normal distribution.

## Key Concepts

### 1. The Normal Random Variable
*   A continuous random variable $X$ follows a Normal distribution with mean $\mu$ and variance $\sigma^2$.
*   Notation: $X \sim \text{Normal}(\mu, \sigma^2)$ or $X \sim N(\mu, \sigma^2)$.

### 2. Probability Density Function (PDF)
*   The [[03_Probability_Density_Function_PDF|PDF]] formula defines the characteristic symmetrical bell shape:
    $$ f(x | \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( - \frac{(x-\mu)^2}{2\sigma^2} \right) $$
*   Where:
    *   $x$ is the value of the random variable ($x \in \mathbb{R}$).
    *   $\mu$ (mu) is the mean (center) of the distribution ($\mu \in \mathbb{R}$).
    *   $\sigma^2$ (sigma-squared) is the variance (spread) of the distribution ($\sigma^2 > 0$). $\sigma = \sqrt{\sigma^2}$ is the standard deviation.
    *   $\pi$ (pi) is the mathematical constant ($\pi \approx 3.14159...$).
    *   $e$ is Euler's number ($e \approx 2.71828...$). `exp(y)` is equivalent to $e^y$.
*   The curve is symmetric around $x = \mu$.
*   The total area under the curve is 1: $\int_{-\infty}^{\infty} f(x | \mu, \sigma^2) \, dx = 1$.

### 3. Parameters
*   The Normal distribution is completely defined by **two parameters**:
    *   $\mu$ (Mean): Determines the location (center) of the peak.
    *   $\sigma^2$ (Variance): Determines the spread or width of the bell. ($\sigma$ is Standard Deviation).

### 4. Cumulative Distribution Function (CDF)
*   The [[04_Cumulative_Distribution_Function_CDF|CDF]] $F(x) = P(X \le x)$ is the integral of the PDF from $-\infty$ to $x$:
    $$ F(x | \mu, \sigma^2) = \int_{-\infty}^{x} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( - \frac{(t-\mu)^2}{2\sigma^2} \right) \, dt $$
*   There is no simple closed-form expression for this integral in terms of elementary functions. Probabilities are typically found using:
    *   Statistical software or calculators (using error function `erf` or standard normal CDF $\Phi$).
    *   Standard Normal (Z) tables after standardizing the variable.

### 5. The Standard Normal Distribution (Z-distribution)
*   A crucial special case where the mean is 0 and the variance (and standard deviation) is 1: $Z \sim N(0, 1)$.
*   Its PDF is often denoted $\phi(z)$:
    $$ \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2} $$
*   Its CDF is often denoted $\Phi(z)$:
    $$ \Phi(z) = \int_{-\infty}^{z} \phi(t) dt $$
*   **Standardization (Z-score):** Any Normal random variable $X \sim N(\mu, \sigma^2)$ can be transformed into a standard normal variable $Z$ using the formula:
    $$ Z = \frac{X - \mu}{\sigma} $$
    The Z-score measures how many standard deviations $\sigma$ the value $X$ is away from its mean $\mu$.
*   This allows us to calculate probabilities for *any* Normal distribution using a single table or function for the Standard Normal distribution: $P(X \le x) = P\left(Z \le \frac{x-\mu}{\sigma}\right) = \Phi\left(\frac{x-\mu}{\sigma}\right)$.

### 6. The Empirical Rule (68-95-99.7 Rule)
For any Normal distribution:
*   Approximately **68%** of the data falls within 1 standard deviation of the mean: $P(\mu-\sigma \le X \le \mu+\sigma) \approx 0.68$.
*   Approximately **95%** of the data falls within 2 standard deviations of the mean: $P(\mu-2\sigma \le X \le \mu+2\sigma) \approx 0.95$.
*   Approximately **99.7%** of the data falls within 3 standard deviations of the mean: $P(\mu-3\sigma \le X \le \mu+3\sigma) \approx 0.997$.

### 7. Expected Value (Mean) & Variance
*   By definition, the parameters directly give the [[01_Expected_Value|mean]] and [[02_Variance_and_Standard_Deviation|variance]]:
    $$ E[X] = \mu $$
    $$ Var(X) = \sigma^2 $$

## Connections to Other Topics
*   **[[02_Central_Limit_Theorem_CLT|Central Limit Theorem (CLT)]]:** States that the sum (or average) of a large number of independent, identically distributed random variables will be approximately Normally distributed, regardless of the original distribution. This is why the Normal distribution appears so often.
*   **Approximation to Binomial:** The Normal distribution approximates the [[02_Binomial_Distribution|Binomial distribution]] $B(n, p)$ for large $n$ (using continuity correction).
*   **Approximation to Poisson:** The Normal distribution approximates the [[03_Poisson_Distribution|Poisson distribution]] $\text{Poi}(\lambda)$ for large $\lambda$.
*   Foundation for many **[[../02 Inferential statistics/001 Inferential Statistics|Inferential Statistics]]** methods: [[../02 Inferential statistics/parametric tests/01 t test/t test|t-tests]], [[../02 Inferential statistics/parametric tests/02 ANOVA/ANOVA|ANOVA]], [[../02 Inferential statistics/Hypothesis testing|Hypothesis testing]] for means, confidence intervals, [[../../06 Machine Learning/02 Supervised/01 Regression/01_Simple Linear Regression/Linear Regression|Linear Regression]] assumptions often involve normality of errors.

## Summary
*   The most common continuous distribution, the "bell curve".
*   Symmetric around the mean $\mu$.
*   Parameters: $\mu$ (mean, location), $\sigma^2$ (variance, spread).
*   PDF: $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$. No simple CDF formula.
*   **Standard Normal (Z):** $N(0, 1)$. Use Z-scores $Z = \frac{X - \mu}{\sigma}$ to find probabilities for any $N(\mu, \sigma^2)$.
*   **Empirical Rule:** 68% within $\mu \pm 1\sigma$, 95% within $\mu \pm 2\sigma$, 99.7% within $\mu \pm 3\sigma$.
*   [[02_Central_Limit_Theorem_CLT|Central Limit Theorem]] explains its prevalence. Foundational for much of statistics.

## Sources
*   [Wikipedia: Normal Distribution](https://en.wikipedia.org/wiki/Normal_distribution)
*   [Khan Academy: Normal Distribution](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/normal-distributions-library/v/introduction-to-the-normal-distribution)
*   [PennState STAT 414: Normal Distribution](https://online.stat.psu.edu/stat414/lesson/17)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross; DeGroot & Schervish "Probability and Statistics") - Consult relevant chapters.

## TAGS
[[Probability]] [[Probability Distribution]] [[Continuous Distribution]] [[Normal Distribution]] [[Gaussian Distribution]] [[Bell Curve]] [[PDF]] [[CDF]] [[Expected Value]] [[02 Math/02 Inferential statistics/Tradeoffs/Variance]] [[Standard Deviation]] [[Z-score]] [[Standard Normal Distribution]] [[Central Limit Theorem]] [[Empirical Rule]] [[02 Math/index]] [[Statistics]]