# Negative Binomial Distribution

## Definition / Introduction
*   The Negative Binomial distribution generalizes the [[08_Geometric_Distribution|Geometric distribution]]. It models the number of **[[01_Bernoulli_Distribution|Bernoulli trials]]** required to achieve a **fixed number ($r$) of successes**.
*   Like the Geometric distribution, it involves repeating independent trials with constant success probability $p$, but stops only after $r$ successes have occurred.
*   Examples: Number of times you need to flip a coin to get 5 Heads ($r=5$), number of products to inspect to find 3 defective ones ($r=3$), number of sales calls needed to secure 10 sales ($r=10$).

## Key Concepts

### 1. Setup
*   Sequence of independent Bernoulli trials with constant success probability $p$.
*   Trials continue *until* exactly $r$ successes have occurred. $r$ is a fixed positive integer.

### 2. Two Versions of the Negative Binomial Random Variable
Similar to the Geometric case, there are two common definitions:
*   **Version 1 (Number of Trials):** $X$ is the total number of trials *up to and including* the $r$-th success. Possible values: $k \in \{r, r+1, r+2, ...\}$. (Must have at least $r$ trials).
*   **Version 2 (Number of Failures):** $Y$ is the number of failures *before* the $r$-th success. Possible values: $k \in \{0, 1, 2, ...\}$. Note that $Y = X - r$.

*We will primarily use **Version 1 (Number of Trials)**.*

### 3. Probability Mass Function (PMF) - Version 1 (Trials)
*   Let $X$ be the number of trials until the $r$-th success. For $X$ to equal $k$ (where $k \ge r$), the following must happen:
    1.  The $k$-th trial *must* be a success.
    2.  In the first $k-1$ trials, there must have been exactly $r-1$ successes (and thus $(k-1)-(r-1) = k-r$ failures).
*   The number of ways to arrange the $r-1$ successes within the first $k-1$ trials is given by the [[../01 Basic Probability Theory/03_Combinatorics|binomial coefficient]] $\binom{k-1}{r-1}$.
*   The probability of any specific sequence with $r$ successes and $k-r$ failures is $p^r (1-p)^{k-r}$.
*   Combining these, the [[../02 Random Variables/02_Probability_Mass_Function_PMF|PMF]] is:
    $$ P(X=k) = \binom{k-1}{r-1} p^r (1-p)^{k-r} \quad \text{for } k = r, r+1, r+2, ... $$
*   Where:
    *   $k$ is the number of trials ($k \ge r$).
    *   $r$ is the target number of successes ($r \ge 1$).
    *   $p$ is the probability of success on a single trial ($0 < p \le 1$).

*(PMF for Version 2 (Failures $Y=k$): $P(Y=k) = \binom{k+r-1}{k} p^r (1-p)^k = \binom{k+r-1}{r-1} p^r (1-p)^k$ for $k=0, 1, 2, ...$)*

### 4. Parameters
*   The Negative Binomial distribution has **two parameters**:
    *   $r$: The target number of successes (a positive integer).
    *   $p$: The probability of success on each trial ($0 < p \le 1$).
*   (Note: Some parameterizations allow $r$ to be a real number, involving the Gamma function in the coefficient, but the interpretation as number of successes requires integer $r$).

### 5. Expected Value (Mean) - Version 1 (Trials)
*   The [[../04 Expectation Variance Covariance/01_Expected_Value|expected]] number of trials needed to get $r$ successes is:
    $$ E[X] = \frac{r}{p} $$
*   Intuition: If $r=1$, this reduces to $1/p$, the mean of the Geometric distribution. If $r=5$ and $p=0.5$, you expect $5 / 0.5 = 10$ trials.

*(Expected Value for Version 2 (Failures): $E[Y] = \frac{r(1-p)}{p}$)*

### 6. Variance - Version 1 (Trials)
*   The [[../04 Expectation Variance Covariance/02_Variance_and_Standard_Deviation|variance]] of the number of trials is:
    $$ Var(X) = \frac{r(1-p)}{p^2} $$

*(Variance for Version 2 (Failures): $Var(Y) = \frac{r(1-p)}{p^2}$ - Same variance)*

## Connections to Other Topics
*   The **[[08_Geometric_Distribution|Geometric distribution]]** is a special case of the Negative Binomial distribution where $r=1$.
*   The sum of $r$ independent Geometric random variables (Version 1) with parameter $p$ follows a Negative Binomial distribution (Version 1) with parameters $r$ and $p$.
*   Can be used in modeling count data that exhibits **overdispersion** (where the variance is greater than the mean), as $Var(X) = E[X] \frac{1-p}{p} > E[X]$ if $p < 1/2$ and $r>0$. More generally $Var(X) = E[X] / p$. Since $p \le 1$, $Var(X) \ge E[X]$. Equality only holds if $p=1$. Useful contrast to the [[03_Poisson_Distribution|Poisson distribution]] where $Var(X) = E[X]$.

## Summary
*   Models the number of **trials ($k$)** needed for a **fixed number ($r$) of successes** in independent Bernoulli trials.
*   Generalizes the Geometric distribution (which has $r=1$).
*   Parameters: $r$ (target successes), $p$ (success probability).
*   PMF (Version 1): $P(X=k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}$ for $k \ge r$.
*   Mean (Version 1): $E[X] = r/p$.
*   Variance (Version 1): $Var(X) = \frac{r(1-p)}{p^2}$.
*   Useful for modeling "waiting times" for multiple events and overdispersed count data.

## Sources
*   [Wikipedia: Negative Binomial Distribution](https://en.wikipedia.org/wiki/Negative_binomial_distribution)
*   [PennState STAT 414: Negative Binomial Distribution](https://online.stat.psu.edu/stat414/lesson/10/10.5)
*   [Cut the Knot: Negative Binomial Distribution](https://www.cut-the-knot.org/Probability/NegativeBinomial.shtml)
*   *OpenIntro Statistics* (Free PDF textbook) - Less commonly covered in intro texts, but check index. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross; Casella & Berger) - Consult relevant chapters.

## TAGS
[[Probability]] [[Probability Distribution]] [[Discrete Distribution]] [[Negative Binomial Distribution]] [[Geometric Distribution]] [[Bernoulli Distribution]] [[PMF]] [[Expected Value]] [[Variance]] [[Overdispersion]] [[02 Math/index]] [[Statistics]]