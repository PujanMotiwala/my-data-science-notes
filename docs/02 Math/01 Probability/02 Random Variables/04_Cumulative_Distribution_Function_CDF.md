# Cumulative Distribution Function (CDF)

## Definition / Introduction
*   The **Cumulative Distribution Function (CDF)** provides a unified way to describe the probability distribution of *any* random variable, whether it's [[01_Definition|Discrete]] or [[01_Definition|Continuous]].
*   The CDF, denoted $F(x)$ or $F_X(x)$, gives the probability that the random variable $X$ takes on a value *less than or equal to* a specific value $x$.
*   It accumulates probability as the value $x$ increases.

## Key Concepts

### 1. Notation and Definition
*   The CDF of a random variable $X$ is defined as:
    $$ F(x) = P(X \le x) $$
*   For any given value $x$, $F(x)$ tells you the total probability accumulated up to that point.

### 2. Properties of a CDF
A function $F(x)$ is a valid CDF if and only if it satisfies these properties:
*   **Non-decreasing:** If $a < b$, then $F(a) \le F(b)$. As $x$ increases, the accumulated probability cannot decrease.
*   **Right-continuous:** The function is continuous from the right: $\lim_{t \to x^+} F(t) = F(x)$. (This is more technical, but important for precise definitions, especially with discrete variables).
*   **Limits:**
    *   The limit as $x$ approaches negative infinity is 0: $\lim_{x \to -\infty} F(x) = 0$ (There's no accumulated probability infinitely far to the left).
    *   The limit as $x$ approaches positive infinity is 1: $\lim_{x \to +\infty} F(x) = 1$ (Eventually, all probability is accumulated).

### 3. CDF for Discrete Random Variables
*   Calculated by summing the [[02_Probability_Mass_Function_PMF|PMF]] values $p(t)$ for all possible outcomes $t$ less than or equal to $x$.
    $$ F(x) = P(X \le x) = \sum_{t \le x} p(t) $$
*   The graph of a discrete CDF is a **step function**. It jumps at each value $x$ where $p(x) > 0$, and the size of the jump is equal to $p(x)$. It's constant between jumps.
*   **Example (Two Coin Flips, X = # Heads):** PMF was $p(0)=1/4, p(1)=1/2, p(2)=1/4$.
    $$
    F(x) = \begin{cases}
    0 & \text{if } x < 0 \\
    1/4 & \text{if } 0 \le x < 1 \\
    3/4 & \text{if } 1 \le x < 2 \\
    1 & \text{if } x \ge 2
    \end{cases}
    $$

### 4. CDF for Continuous Random Variables
*   Calculated by integrating the [[03_Probability_Density_Function_PDF|PDF]] $f(t)$ from negative infinity up to $x$.
    $$ F(x) = P(X \le x) = \int_{-\infty}^{x} f(t) \, dt $$
*   The graph of a continuous CDF is a **continuous, non-decreasing function** that smoothly rises from 0 to 1.
*   The value of the PDF $f(x)$ is the *slope* ([[../01 Foundations/02_Derivatives|derivative]]) of the CDF $F(x)$: $f(x) = \frac{d}{dx} F(x)$.
*   **Example (Uniform Distribution on [0, 2]):** PDF was $f(t) = 1/2$ for $0 \le t \le 2$.
    $$
    F(x) = \begin{cases}
    0 & \text{if } x < 0 \\
    \int_0^x \frac{1}{2} dt = \frac{x}{2} & \text{if } 0 \le x \le 2 \\
    1 & \text{if } x > 2
    \end{cases}
    $$
    *So, $F(x)$ starts at 0, rises linearly to 1 between x=0 and x=2, and stays at 1 thereafter.*

### 5. Usage: Calculating Probabilities from CDF
*   The CDF is very useful for finding the probability that $X$ falls within any interval $(a, b]$:
    $$ P(a < X \le b) = F(b) - F(a) $$
*   This works for both discrete and continuous variables.
*   Other probabilities can also be derived:
    *   $P(X > a) = 1 - P(X \le a) = 1 - F(a)$
    *   $P(X < a)$ is $F(a)$ for continuous RVs, but $F(a) - P(X=a)$ for discrete RVs (or $\lim_{t \to a^-} F(t)$).
    *   $P(X \ge a) = 1 - P(X < a)$.
    *   $P(X=a) = F(a) - \lim_{t \to a^-} F(t)$ (This is zero for continuous RVs, and equal to the jump size $p(a)$ for discrete RVs).

## Connections to Other Topics
*   Directly related to [[02_Probability_Mass_Function_PMF|PMF]] (by summation) and [[03_Probability_Density_Function_PDF|PDF]] (by integration/differentiation).
*   Provides a complete description of a random variable's distribution.
*   Used to find percentiles (quantiles) of a distribution. The median, for example, is the value $m$ such that $F(m) = 0.5$.
*   Used in generating random numbers from specific distributions (Inverse Transform Sampling: if $U \sim \text{Uniform}(0, 1)$, then $X = F^{-1}(U)$ follows the distribution with CDF $F$).

## Summary
*   The **CDF**, $F(x) = P(X \le x)$, gives the cumulative probability up to value $x$.
*   Defined for **both discrete and continuous** random variables.
*   Properties: Non-decreasing, right-continuous, limits 0 and 1.
*   Graph: Step function for discrete RVs, continuous curve for continuous RVs.
*   Useful for calculating probabilities over intervals: $P(a < X \le b) = F(b) - F(a)$.

## Sources
*   [Wikipedia: Cumulative Distribution Function](https://en.wikipedia.org/wiki/Cumulative_distribution_function)
*   [Khan Academy: Cumulative Distribution Functions](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/cumulative-distribution-functions-cdfs/v/cumulative-distribution-functions)
*   [PennState STAT 414: Cumulative Distribution Functions](https://online.stat.psu.edu/stat414/lesson/15/15.1) (Continuous example) & Lesson 10 (Discrete example)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross; DeGroot & Schervish) - Consult relevant chapters.

## TAGS
[[Probability]] [[Random Variable]] [[Cumulative Distribution Function]] [[CDF]] [[PMF]] [[PDF]] [[Probability Distribution]] [[02 Math/index]] [[Statistics]]