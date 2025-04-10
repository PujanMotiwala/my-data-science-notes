# Beta Distribution

## Simple Idea
*   The Beta distribution is a [[../02 Random Variables/01_Definition|continuous probability distribution]] defined on the interval **(0, 1)**.
*   Think of it as representing a **probability distribution *of probabilities***. It's often used to model uncertainty about a parameter that itself represents a probability, like the bias of a coin (`p`) or the conversion rate of a webpage.
*   Its shape is very flexible, controlled by two positive shape parameters, allowing it to model various forms of belief about a probability.

## Formal Definition
*   A continuous random variable $X$ follows a Beta distribution with positive shape parameters $\alpha$ and $\beta$, if its [[../02 Random Variables/03_Probability_Density_Function_PDF|Probability Density Function (PDF)]] is defined on the interval $(0, 1)$ as:
    $$ f(x | \alpha, \beta) = \frac{1}{B(\alpha, \beta)} x^{\alpha-1} (1-x)^{\beta-1} \quad \text{for } 0 < x < 1 $$
*   Where:
    *   $x$ is a value between 0 and 1 (representing a probability or proportion).
    *   $\alpha > 0$ is the first shape parameter.
    *   $\beta > 0$ is the second shape parameter.
    *   $B(\alpha, \beta)$ is the **Beta function**, which acts as the normalization constant.

## Key Concepts

### 1. The Beta Function $B(\alpha, \beta)$
*   A function related to the [[10_Gamma_Distribution|Gamma function]] $\Gamma$:
    $$ B(\alpha, \beta) = \frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha + \beta)} $$
*   It ensures that the total area under the Beta PDF integrates to 1.

### 2. Parameters $\alpha$ and $\beta$ (Shape Parameters)
*   These parameters control the shape of the distribution:
    *   $\alpha = \beta = 1$: Reduces to the [[04_Uniform_Distribution|Uniform(0, 1)]] distribution (all probabilities equally likely).
    *   $\alpha > 1, \beta > 1$: Unimodal distribution (single peak between 0 and 1). If $\alpha=\beta$, the peak is at $0.5$. If $\alpha > \beta$, peak is closer to 1. If $\beta > \alpha$, peak is closer to 0.
    *   $\alpha < 1, \beta < 1$: U-shaped distribution (probabilities near 0 and 1 are more likely).
    *   $\alpha = 1, \beta > 1$: Strictly decreasing shape.
    *   $\alpha > 1, \beta = 1$: Strictly increasing shape.
    *(Visual Idea: Excalidraw showing different Beta PDF shapes for various $\alpha, \beta$ values - uniform, bell-shaped, U-shaped, skewed).*

### 3. Expected Value (Mean)
*   The expected value (average probability) is:
    $$ E[X] = \frac{\alpha}{\alpha + \beta} $$
*   *Intuition:* $\alpha$ can be thought of as related to the count of "successes" and $\beta$ to the count of "failures". The mean is like the proportion of successes.

### 4. Variance
*   The variance is:
    $$ Var(X) = \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)} $$

### 5. Bayesian Inference (Key Application)
*   The Beta distribution is the **conjugate prior** for the [[01_Bernoulli_Distribution|Bernoulli]], [[02_Binomial_Distribution|Binomial]], and [[08_Geometric_Distribution|Geometric]] distributions (in terms of the success probability parameter $p$).
*   **What this means:** If your prior belief about a probability parameter $p$ can be represented by a Beta($\alpha_{prior}, \beta_{prior}$) distribution, and you observe new data (e.g., $k$ successes in $n$ Binomial trials), then your updated belief (the **posterior distribution**) for $p$ is *also* a Beta distribution:
    $$ p | \text{data} \sim \text{Beta}(\alpha_{prior} + k, \beta_{prior} + n - k) $$
*   This makes Bayesian updates mathematically convenient. $\alpha$ acts like a "prior count of successes + 1", $\beta$ like a "prior count of failures + 1".

## Connections to Other Topics
*   Related to the [[10_Gamma_Distribution|Gamma distribution]] via the Beta function definition.
*   Special case is the [[04_Uniform_Distribution|Uniform(0, 1)]] distribution when $\alpha=\beta=1$.
*   Crucial in **[[../02 Inferential statistics/Parametric tests/Bayesian Inference|Bayesian Statistics]]** for modeling uncertainty about probability parameters.
*   Used in A/B testing analysis from a Bayesian perspective.

## Summary
*   The **Beta($\alpha, \beta$) distribution** models probabilities or proportions, defined on **(0, 1)**.
*   Parameters $\alpha, \beta > 0$ control the shape (uniform, bell, U-shaped, skewed).
*   PDF involves the Beta function $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$.
*   Mean: $E[X] = \frac{\alpha}{\alpha+\beta}$.
*   Variance: $Var(X) = \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}$.
*   Key application as a **conjugate prior** in Bayesian inference for probability parameters $p$.

## Sources
*   [Wikipedia: Beta distribution](https://en.wikipedia.org/wiki/Beta_distribution)
*   [PennState STAT 414: Beta Distribution](https://online.stat.psu.edu/stat414/lesson/18/18.3)
*   [Cross Validated discussion on Beta distribution intuition](https://stats.stackexchange.com/questions/47771/what-is-the-intuition-behind-beta-distribution)
*   Bayesian statistics textbooks (e.g., "Doing Bayesian Data Analysis" by Kruschke; "Bayesian Data Analysis" by Gelman et al.)

## TAGS
[[Probability]] [[Probability Distribution]] [[Continuous Distribution]] [[Beta Distribution]] [[PDF]] [[Expected Value]] [[Variance]] [[Beta Function]] [[Gamma Function]] [[Bayesian Statistics]] [[Conjugate Prior]] [[02 Math/index]] [[Statistics]] [[Foundations]]