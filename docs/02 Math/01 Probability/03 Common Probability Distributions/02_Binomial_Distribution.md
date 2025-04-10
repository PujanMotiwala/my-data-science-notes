# Binomial Distribution

## Definition / Introduction
*   The Binomial distribution models the number of "successes" in a **fixed number ($n$) of independent [[01_Bernoulli_Distribution|Bernoulli trials]]**, where each trial has the same probability of success ($p$).
*   It's one of the most important [[02 Math/01 Probability/02 Random Variables/01_Definition|Discrete Probability Distributions]], used extensively in quality control, polling, genetics, and any scenario counting successes in repeated independent trials.
*   Think of it as counting the number of Heads in $n$ coin flips.

## Key Concepts

### 1. Conditions for Binomial Distribution (The "BINS" mnemonic)
An experiment can be modeled by a Binomial distribution if it meets these criteria:
*   **B**inary Outcomes: Each trial results in one of two mutually exclusive outcomes (success/failure).
*   **I**ndependent Trials: The outcome of one trial does not affect the outcome of any other trial.
*   **N**umber of Trials Fixed: The total number of trials, $n$, is determined in advance.
*   **S**ame Probability of Success: The probability of success, $p$, is constant for every trial.

### 2. The Binomial Random Variable
*   A [[02 Math/01 Probability/02 Random Variables/01_Definition|Random Variable]] $X$ follows a Binomial distribution if it represents the count of successes in $n$ independent Bernoulli trials, each with success probability $p$.
*   Possible values for $X$ are integers from 0 to $n$, i.e., $X \in \{0, 1, 2, ..., n\}$.
*   Notation: $X \sim \text{Binomial}(n, p)$ or $X \sim B(n, p)$.

### 3. Probability Mass Function (PMF)
*   The [[02_Probability_Mass_Function_PMF|PMF]] gives the probability of obtaining exactly $k$ successes in $n$ trials:
    $$ P(X=k) = \binom{n}{k} p^k (1-p)^{n-k} \quad \text{for } k = 0, 1, 2, ..., n $$
*   Where:
    *   $n$ is the number of trials.
    *   $k$ is the number of successes.
    *   $p$ is the probability of success on a single trial.
    *   $(1-p)$ is the probability of failure on a single trial.
    *   $\binom{n}{k} = C(n, k) = \frac{n!}{k!(n-k)!}$ is the [[03_Combinatorics|Binomial Coefficient]], representing the number of ways to choose $k$ successes from $n$ trials.

### 4. Parameters
*   The Binomial distribution has **two parameters**:
    *   $n$: The number of trials (a positive integer).
    *   $p$: The probability of success on each trial (where $0 \le p \le 1$).

### 5. Expected Value (Mean)
*   The [[01_Expected_Value|expected]] number of successes in $n$ trials is:
    $$ E[X] = np $$
*   Intuition: If you flip a fair coin ($p=0.5$) 10 times ($n=10$), you expect $10 \times 0.5 = 5$ Heads on average.

### 6. Variance
*   The [[02_Variance_and_Standard_Deviation|variance]] (measure of spread) of the number of successes is:
    $$ Var(X) = np(1-p) $$
*   Note: The variance is the sum of variances of $n$ independent Bernoulli(p) variables.

### 7. Shape of the Distribution
*   If $p = 0.5$, the distribution is symmetric around the mean $np/2$. *(Self-correction: mean is np)* If $p = 0.5$, the distribution is symmetric around the mean $n/2$.
*   If $p < 0.5$, the distribution is skewed to the right.
*   If $p > 0.5$, the distribution is skewed to the left.
*   As $n$ increases, the distribution becomes more symmetric and bell-shaped (approaching a [[05_Normal_Gaussian_Distribution|Normal distribution]]).

## Connections to Other Topics
*   A [[01_Bernoulli_Distribution|Bernoulli Distribution]] is a special case of the Binomial distribution where $n=1$.
*   For large $n$ and moderate $p$ (specifically, when $np \ge 5$ and $n(1-p) \ge 5$ is a common rule of thumb), the Binomial distribution can be approximated by the [[05_Normal_Gaussian_Distribution|Normal Distribution]] with mean $\mu = np$ and variance $\sigma^2 = np(1-p)$.
*   If $n$ is large and $p$ is very small (making $np$ moderate), the Binomial distribution can be approximated by the [[03_Poisson_Distribution|Poisson Distribution]] with parameter $\lambda = np$.

## Summary
*   Models the number of successes ($k$) in a **fixed number ($n$)** of **independent trials**.
*   Parameters: $n$ (trials), $p$ (success probability).
*   PMF: $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$.
*   Mean: $E[X] = np$.
*   Variance: $Var(X) = np(1-p)$.
*   Foundation for understanding repeated experiments with binary outcomes.

## Sources
*   [Wikipedia: Binomial Distribution](https://en.wikipedia.org/wiki/Binomial_distribution)
*   [Khan Academy: Binomial Distribution](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/binomial-distribution/v/binomial-distribution)
*   [PennState STAT 414: Binomial Distribution](https://online.stat.psu.edu/stat414/lesson/10/10.3)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross) - Consult relevant chapters.

## TAGS
[[Probability]] [[Probability Distribution]] [[Discrete Distribution]] [[Binomial Distribution]] [[Bernoulli Distribution]] [[PMF]] [[Expected Value]] [[02 Math/02 Inferential statistics/Tradeoffs/Variance]] [[02 Math/index]] [[Statistics]]