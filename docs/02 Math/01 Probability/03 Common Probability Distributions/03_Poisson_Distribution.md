# Poisson Distribution

## Definition / Introduction
*   The Poisson distribution is a [[../02 Random Variables/01_Definition|Discrete Probability Distribution]] that models the probability of a given **number of events occurring in a fixed interval** of time or space.
*   It's used when these events occur independently and with a known constant average rate ($\lambda$).
*   Examples: Number of emails received per hour, number of typos per page, number of cars arriving at a toll booth per minute, number of mutations in a DNA strand.

## Key Concepts

### 1. Conditions for Poisson Distribution
A process can often be modeled by a Poisson distribution if:
*   Events occur independently (occurrence of one event doesn't affect the probability of another).
*   The average rate ($\lambda$) at which events occur is constant for the interval of interest.
*   The probability of an event occurring is proportional to the length of the interval (for small intervals).
*   Two events cannot occur at exactly the same instant (the probability of simultaneous events is negligible).

### 2. The Poisson Random Variable
*   A [[../02 Random Variables/01_Definition|Random Variable]] $X$ follows a Poisson distribution if it represents the count of events occurring in a fixed interval, given the average rate $\lambda$.
*   Possible values for $X$ are non-negative integers $\{0, 1, 2, 3, ...\}$.
*   Notation: $X \sim \text{Poisson}(\lambda)$ or $X \sim \text{Poi}(\lambda)$.

### 3. Probability Mass Function (PMF)
*   The [[../02 Random Variables/02_Probability_Mass_Function_PMF|PMF]] gives the probability of observing exactly $k$ events in the interval:
    $$ P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!} \quad \text{for } k = 0, 1, 2, ... $$
*   Where:
    *   $k$ is the number of events (a non-negative integer).
    *   $\lambda$ (lambda) is the average number of events per interval (the rate parameter). $\lambda > 0$.
    *   $e$ is Euler's number (the base of the natural logarithm, $e \approx 2.71828...$).
    *   $k!$ is the [[../01 Basic Probability Theory/03_Combinatorics|factorial]] of $k$.

### 4. Parameter
*   The Poisson distribution has only **one parameter**:
    *   $\lambda$ (lambda): The average rate or mean number of events in the given interval.

### 5. Expected Value (Mean)
*   The [[../04 Expectation Variance Covariance/01_Expected_Value|expected]] number of events in the interval is simply the rate parameter:
    $$ E[X] = \lambda $$

### 6. Variance
*   A key property of the Poisson distribution is that its [[../04 Expectation Variance Covariance/02_Variance_and_Standard_Deviation|variance]] is equal to its mean:
    $$ Var(X) = \lambda $$
*   If the observed variance in count data is much larger than the mean (overdispersion), a simple Poisson model might not be appropriate (consider [[09_Negative_Binomial_Distribution|Negative Binomial]] instead).

### 7. Adjusting the Rate Parameter $\lambda$
*   If the average rate is given for one interval length, you must adjust $\lambda$ proportionally if you are interested in a different interval length.
*   Example: If a call center receives an average of 10 calls per hour ($\lambda=10$ for 1 hour), the average number of calls in a 3-hour period would be $\lambda = 10 \times 3 = 30$. The average number of calls in a 15-minute (0.25 hour) period would be $\lambda = 10 \times 0.25 = 2.5$.

## Connections to Other Topics
*   **Binomial Approximation:** The Poisson distribution approximates the [[02_Binomial_Distribution|Binomial Distribution]] $B(n, p)$ when $n$ is large and $p$ is small (rare events), such that $\lambda \approx np$. This is useful because the Poisson PMF is often easier to compute than the Binomial PMF under these conditions.
*   **Exponential Distribution:** If the number of events occurring in an interval follows a Poisson distribution with rate $\lambda$, then the time *between* consecutive events follows an [[06_Exponential_Distribution|Exponential Distribution]] with the same rate parameter $\lambda$. They describe different aspects of the same underlying "Poisson process".

## Summary
*   Models the number of events ($k$) in a **fixed interval** of time/space.
*   Assumes events occur independently at a constant average rate ($\lambda$).
*   Parameter: $\lambda$ (average rate/mean number of events).
*   PMF: $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$.
*   Mean: $E[X] = \lambda$.
*   Variance: $Var(X) = \lambda$ (Mean = Variance).
*   Related to Binomial (rare events) and Exponential (time between events) distributions.

## Sources
*   [Wikipedia: Poisson Distribution](https://en.wikipedia.org/wiki/Poisson_distribution)
*   [Khan Academy: Poisson Distribution](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/poisson-distribution/v/poisson-distribution-introduction)
*   [PennState STAT 414: Poisson Distribution](https://online.stat.psu.edu/stat414/lesson/12/12.1)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross) - Consult relevant chapters.

## TAGS
[[Probability]] [[Probability Distribution]] [[Discrete Distribution]] [[Poisson Distribution]] [[PMF]] [[Expected Value]] [[Variance]] [[Rate Parameter]] [[Exponential Distribution]] [[Binomial Distribution]] [[Math]] [[Statistics]]