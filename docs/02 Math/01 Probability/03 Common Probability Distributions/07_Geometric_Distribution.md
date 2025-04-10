# Geometric Distribution

## Definition / Introduction
*   The Geometric distribution is a [[../02 Random Variables/01_Definition|Discrete Probability Distribution]] that models the number of **[[01_Bernoulli_Distribution|Bernoulli trials]]** needed to achieve the **first success**.
*   It's closely related to the [[02_Binomial_Distribution|Binomial distribution]], but instead of fixing the number of trials and counting successes, we fix the number of successes (at 1) and count the trials.
*   Examples: Number of coin flips until the first Head appears, number of items inspected until the first defective one is found, number of times you attempt a task until you succeed for the first time.

## Key Concepts

### 1. Setup
*   We assume a sequence of independent Bernoulli trials, each with the same probability of success $p$.
*   Trials continue *until* the first success occurs.

### 2. Two Versions of the Geometric Random Variable
There are two common definitions for the Geometric random variable $X$:
*   **Version 1 (Number of Trials):** $X$ is the total number of trials *up to and including* the first success. Possible values: $k \in \{1, 2, 3, ...\}$.
*   **Version 2 (Number of Failures):** $Y$ is the number of failures *before* the first success. Possible values: $k \in \{0, 1, 2, ...\}$. Note that $Y = X - 1$.

*We will primarily use **Version 1 (Number of Trials)** in this note, as it's slightly more common, but be aware of both when consulting other sources.*

### 3. Probability Mass Function (PMF) - Version 1 (Trials)
*   Let $X$ be the number of trials until the first success. For $X$ to equal $k$ (where $k \ge 1$), we must have $k-1$ failures followed by one success.
*   The [[../02 Random Variables/02_Probability_Mass_Function_PMF|PMF]] is:
    $$ P(X=k) = (1-p)^{k-1} p \quad \text{for } k = 1, 2, 3, ... $$
*   Where:
    *   $k$ is the number of trials ($k \ge 1$).
    *   $p$ is the probability of success on a single trial ($0 < p \le 1$).
    *   $(1-p)$ is the probability of failure.

*(PMF for Version 2 (Failures $Y=k$): $P(Y=k) = (1-p)^k p$ for $k=0, 1, 2, ...$)*

### 4. Parameter
*   The Geometric distribution has **one parameter**:
    *   $p$: The probability of success on each trial ($0 < p \le 1$).

### 5. Expected Value (Mean) - Version 1 (Trials)
*   The [[../04 Expectation Variance Covariance/01_Expected_Value|expected]] number of trials needed to get the first success is:
    $$ E[X] = \frac{1}{p} $$
*   Intuition: If the probability of success is $p=0.1$ (10%), you expect to need $1/0.1 = 10$ trials on average to get the first success.

*(Expected Value for Version 2 (Failures): $E[Y] = \frac{1-p}{p}$)*

### 6. Variance - Version 1 (Trials)
*   The [[../04 Expectation Variance Covariance/02_Variance_and_Standard_Deviation|variance]] of the number of trials is:
    $$ Var(X) = \frac{1-p}{p^2} $$

*(Variance for Version 2 (Failures): $Var(Y) = \frac{1-p}{p^2}$ - Same variance)*

### 7. Memorylessness Property (Discrete Analogue)
*   The Geometric distribution is the *only* discrete distribution with the **memorylessness property**.
*   Mathematically (for Version 1): $P(X > k + j | X > k) = P(X > j)$ for integers $j, k \ge 0$.
*   **Intuition:** If you've already performed $k$ trials without success, the probability distribution for the *additional* number of trials needed to get the first success is exactly the same as the original distribution starting from scratch. The process "doesn't remember" the past failures.
*   Example: If flipping a coin until Heads, knowing you've already flipped 5 Tails doesn't change the probability distribution of how many *more* flips you'll need.

## Connections to Other Topics
*   Related to the [[01_Bernoulli_Distribution|Bernoulli distribution]] (models each individual trial).
*   The [[09_Negative_Binomial_Distribution|Negative Binomial distribution]] generalizes the Geometric by modeling the number of trials needed for $r$ successes (Geometric is Negative Binomial with $r=1$).
*   The [[06_Exponential_Distribution|Exponential distribution]] is the continuous analogue of the Geometric distribution, modeling waiting time instead of number of trials, and also possessing the memorylessness property.

## Summary
*   Models the number of **trials ($k$)** needed for the **first success** in independent Bernoulli trials.
*   Parameter: $p$ (success probability).
*   PMF (Version 1): $P(X=k) = (1-p)^{k-1} p$ for $k \ge 1$.
*   Mean (Version 1): $E[X] = 1/p$.
*   Variance (Version 1): $Var(X) = (1-p)/p^2$.
*   Key Property: **Memorylessness** (discrete version).
*   Related to Negative Binomial (r=1) and Exponential (continuous analogue).

## Sources
*   [Wikipedia: Geometric Distribution](https://en.wikipedia.org/wiki/Geometric_distribution)
*   [Khan Academy: Geometric Random Variables](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/geometric-random-variables/v/geometric-random-variable-definition)
*   [PennState STAT 414: Geometric Distribution](https://online.stat.psu.edu/stat414/lesson/10/10.4)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross) - Consult relevant chapters.

## TAGS
[[Probability]] [[Probability Distribution]] [[Discrete Distribution]] [[Geometric Distribution]] [[Bernoulli Distribution]] [[Negative Binomial Distribution]] [[Exponential Distribution]] [[PMF]] [[Expected Value]] [[Variance]] [[Memorylessness]] [[Math]] [[Statistics]]