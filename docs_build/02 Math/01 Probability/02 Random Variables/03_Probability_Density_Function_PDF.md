---
tags:
- Calculus
- Continuous Variable
- Integration
- PDF
- Probability
- Probability Density Function
- Probability Distribution
- Random Variable
- Statistics
---

# Probability Density Function (PDF)

## Definition / Introduction
*   For a [[02 Math/01 Probability/02 Random Variables/01_Definition|Continuous Random Variable]], the probability of it taking on any *single specific* value is essentially zero (because there are infinitely many possible values in any interval).
*   Instead of assigning probabilities to specific points like a [[02_Probability_Mass_Function_PMF|PMF]] does for discrete variables, we use a **Probability Density Function (PDF)** to describe the *relative likelihood* of a continuous random variable $X$ falling within a given range or interval.
*   The PDF $f(x)$ itself does *not* give probability directly; probability is represented by the **area under the PDF curve** over an interval.

## Key Concepts

### 1. Notation and Definition
*   The PDF of a continuous random variable $X$ is denoted by $f(x)$ or $f_X(x)$.
*   It's a function such that the probability of $X$ falling within an interval $[a, b]$ is given by the [[../04 Calculus/05 Integrals/01_Definite_and_Indefinite_Integrals|integral]] (area under the curve) of $f(x)$ from $a$ to $b$:
    $$ P(a \le X \le b) = \int_a^b f(x) \, dx $$

### 2. Properties of a PDF
A function $f(x)$ can be considered a valid PDF if and only if it satisfies these two conditions:
*   **Non-negativity:** The density value must be greater than or equal to zero for all possible values $x$. (Note: $f(x)$ can be greater than 1, unlike a probability).
    $$ f(x) \ge 0 \quad \text{for all } x $$
*   **Total Area Equals One:** The total area under the entire curve of the PDF must equal 1. This represents the certainty that the random variable will take *some* value within its possible range.
    $$ \int_{-\infty}^{\infty} f(x) \, dx = 1 $$

### 3. Key Difference from PMF
*   **PMF (Discrete):** $p(x) = P(X=x)$. Gives direct probability at a point. Values are probabilities ($0 \le p(x) \le 1$). Summation $\sum p(x) = 1$.
*   **PDF (Continuous):** $f(x)$ is *not* $P(X=x)$. $P(X=x) = 0$. Gives probability *density*. Values $f(x) \ge 0$ (can exceed 1). Integration $\int f(x) dx = 1$. Probability is found by integrating $f(x)$ over an interval $[a, b]$.

### 4. Example: Uniform Distribution
*   Consider a continuous random variable $X$ uniformly distributed between 0 and 2, $X \sim \text{Uniform}(0, 2)$. This means $X$ is equally likely to fall anywhere in this interval.
*   **PDF:**
    $$
    f(x) = \begin{cases} \frac{1}{2} & \text{if } 0 \le x \le 2 \\ 0 & \text{otherwise} \end{cases}
    $$
*   **Verification:**
    *   $f(x) = 1/2 \ge 0$ within the range $[0, 2]$.
    *   Total Area: $\int_{-\infty}^{\infty} f(x) dx = \int_0^2 \frac{1}{2} \, dx = \left[ \frac{x}{2} \right]_0^2 = \frac{2}{2} - \frac{0}{2} = 1$.
*   **Calculating Probability:** What is the probability that X falls between 0.5 and 1.5?
    *   $P(0.5 \le X \le 1.5) = \int_{0.5}^{1.5} \frac{1}{2} \, dx = \left[ \frac{x}{2} \right]_{0.5}^{1.5} = \frac{1.5}{2} - \frac{0.5}{2} = \frac{1}{2} = 0.5$.
    *   Visually, this is the area of a rectangle with width $(1.5 - 0.5) = 1$ and height $1/2$.

### 5. Visualization
*   A PDF is visualized as a **curve** on a graph where the x-axis represents the values of the random variable and the y-axis represents the probability density $f(x)$.
*   The **area under the curve** between two points represents the probability of the variable falling within that range.

## Connections to Other Topics
*   The PDF defines the probability distribution for a [[02 Math/01 Probability/02 Random Variables/01_Definition|Continuous Random Variable]]. Common continuous distributions like [[04_Uniform_Distribution|Uniform]], [[05_Normal_Gaussian_Distribution|Normal (Gaussian)]], and [[06_Exponential_Distribution|Exponential]] are characterized by their specific PDF formulas.
*   Requires concepts from [[../04 Calculus/05 Integrals/01_Definite_and_Indefinite_Integrals|Calculus (Integration)]] to calculate probabilities.
*   Used to calculate the [[01_Expected_Value|Expected Value]] ($E[X] = \int x f(x) dx$) and [[02_Variance_and_Standard_Deviation|Variance]] ($Var(X) = \int (x-\mu)^2 f(x) dx$) of a continuous RV using integration.
*   Related to the [[04_Cumulative_Distribution_Function_CDF|Cumulative Distribution Function (CDF)]] for continuous variables: $F(x) = P(X \le x) = \int_{-\infty}^{x} f(t) dt$, and conversely, $f(x) = \frac{d}{dx} F(x)$.

## Summary
*   The **PDF** describes the relative likelihood of values for a **continuous** random variable $X$.
*   $f(x)$ itself is **not** probability; **area** under the PDF curve represents probability. $P(a \le X \le b) = \int_a^b f(x) dx$.
*   $P(X=x) = 0$ for any specific $x$ in a continuous distribution.
*   Key properties: $f(x) \ge 0$ and $\int_{-\infty}^{\infty} f(x) dx = 1$.
*   It fully describes the probability distribution of a continuous RV.

## Sources
*   [Wikipedia: Probability Density Function](https://en.wikipedia.org/wiki/Probability_density_function)
*   [Khan Academy: Probability Density Functions](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/random-variables-continuous/v/probability-density-functions)
*   [PennState STAT 414: Probability Density Functions](https://online.stat.psu.edu/stat414/lesson/14/14.1)
*   (Introductory Probability and Statistics textbooks, Calculus textbooks)