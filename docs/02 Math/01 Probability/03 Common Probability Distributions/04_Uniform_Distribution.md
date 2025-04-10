# Uniform Distribution (Continuous)

## Definition / Introduction
*   The Continuous Uniform distribution describes a [[../02 Random Variables/01_Definition|Continuous Random Variable]] where all possible values within a specified range $[a, b]$ are **equally likely**.
*   It represents complete uncertainty within the bounds $a$ and $b$; no single value or sub-interval within the range is favored over another of the same size.
*   Think of it as randomly picking a real number from a fixed interval.

## Key Concepts

### 1. The Uniform Random Variable
*   A continuous random variable $X$ follows a Uniform distribution on the interval $[a, b]$ if its probability is spread evenly across that interval.
*   Notation: $X \sim \text{Uniform}(a, b)$ or $X \sim U(a, b)$.

### 2. Probability Density Function (PDF)
*   The [[../02 Random Variables/03_Probability_Density_Function_PDF|PDF]] is constant within the interval $[a, b]$ and zero elsewhere. The height of the constant value must make the total area under the curve equal to 1.
    $$
    f(x) = \begin{cases} \frac{1}{b-a} & \text{if } a \le x \le b \\ 0 & \text{otherwise} \end{cases}
    $$
*   The width of the interval is $(b-a)$. The height $\frac{1}{b-a}$ ensures the area (width $\times$ height) is $(b-a) \times \frac{1}{b-a} = 1$.

### 3. Parameters
*   The Uniform distribution has **two parameters**:
    *   $a$: The minimum possible value (lower bound).
    *   $b$: The maximum possible value (upper bound), where $b > a$.

### 4. Cumulative Distribution Function (CDF)
*   The [[../02 Random Variables/04_Cumulative_Distribution_Function_CDF|CDF]] $F(x) = P(X \le x)$ represents the accumulated probability up to $x$.
    $$
    F(x) = \begin{cases} 0 & \text{if } x < a \\ \frac{x-a}{b-a} & \text{if } a \le x \le b \\ 1 & \text{if } x > b \end{cases}
    $$
*   Intuition: The CDF increases linearly from 0 at $x=a$ to 1 at $x=b$. The proportion of the interval covered up to $x$ is $\frac{x-a}{b-a}$.

### 5. Expected Value (Mean)
*   The [[../04 Expectation Variance Covariance/01_Expected_Value|expected value]] (average) is the midpoint of the interval:
    $$ E[X] = \frac{a+b}{2} $$

### 6. Variance
*   The [[../04 Expectation Variance Covariance/02_Variance_and_Standard_Deviation|variance]] (measure of spread) is:
    $$ Var(X) = \frac{(b-a)^2}{12} $$
*   The variance depends only on the width of the interval $(b-a)$.

### 7. Calculating Probabilities
*   The probability of $X$ falling within a sub-interval $[c, d]$ (where $a \le c \le d \le b$) is the area under the PDF from $c$ to $d$:
    $$ P(c \le X \le d) = \int_c^d \frac{1}{b-a} \, dx = \frac{d-c}{b-a} $$
*   This is simply the ratio of the length of the sub-interval $(d-c)$ to the length of the total interval $(b-a)$.

## Connections to Other Topics
*   The **Standard Uniform Distribution** is a special case where $a=0$ and $b=1$, denoted $U(0, 1)$. This is fundamental in computer science for generating random numbers. Pseudo-random number generators often produce values that approximate a $U(0, 1)$ distribution.
*   Random variables from *any* continuous distribution can be generated using a $U(0, 1)$ generator and the **Inverse Transform Sampling** method based on the target distribution's CDF. If $U \sim U(0,1)$, then $X = F^{-1}(U)$ has CDF $F$.
*   Used as a non-informative prior distribution in [[../02 Inferential statistics/Parametric tests/Bayesian Inference|Bayesian Statistics]] in some contexts.
*   The [[11_Beta_Distribution|Beta distribution]] with $\alpha=1, \beta=1$ reduces to $U(0,1)$.

## Summary
*   Models outcomes that are **equally likely** within a **fixed range $[a, b]$**.
*   Parameters: $a$ (min value), $b$ (max value).
*   PDF: Constant $\frac{1}{b-a}$ between $a$ and $b$, zero otherwise (rectangular shape). Uses `\begin{cases}`.
*   Mean: $\frac{a+b}{2}$ (midpoint).
*   Variance: $\frac{(b-a)^2}{12}$.
*   Probability over a sub-interval $[c, d]$ is $\frac{d-c}{b-a}$.
*   Crucial for random number generation ($U(0, 1)$).

## Sources
*   [Wikipedia: Uniform Distribution (continuous)](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous))
*   [Khan Academy: Uniform Distributions](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/continuous-random-variables-library/v/uniform-distributions)
*   [PennState STAT 414: Uniform Distribution](https://online.stat.psu.edu/stat414/lesson/16/16.1)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross) - Consult relevant chapters.

## TAGS
[[Probability]] [[Probability Distribution]] [[Continuous Distribution]] [[Uniform Distribution]] [[PDF]] [[CDF]] [[Expected Value]] [[Variance]] [[Random Number Generation]] [[Math]] [[Statistics]]