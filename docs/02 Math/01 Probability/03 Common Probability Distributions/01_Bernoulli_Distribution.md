# Bernoulli Distribution

## Definition / Introduction
*   The Bernoulli distribution is the simplest [[02 Math/01 Probability/02 Random Variables/01_Definition|Discrete Probability Distribution]].
*   It models a *single trial* of a random experiment that has exactly **two possible outcomes**, often labeled as "success" (usually encoded as 1) and "failure" (usually encoded as 0).
*   Think of it as a single coin flip (potentially biased).

## Key Concepts

### 1. The Bernoulli Trial
*   A single experiment that meets the following criteria:
    *   There are only two mutually exclusive outcomes (e.g., success/failure, yes/no, heads/tails, click/no-click, defect/no-defect).
    *   The probability of success, denoted by $p$, remains constant for the trial.
    *   The probability of failure is therefore $1 - p$, often denoted by $q$. ($p + q = 1$).

### 2. The Bernoulli Random Variable
*   A [[02 Math/01 Probability/02 Random Variables/01_Definition|Random Variable]] $X$ follows a Bernoulli distribution if it takes the value $1$ (success) with probability $p$, and the value $0$ (failure) with probability $1-p$.
*   Notation: $X \sim \text{Bernoulli}(p)$ (read as "X follows a Bernoulli distribution with parameter p").

### 3. Probability Mass Function (PMF)
*   The [[02_Probability_Mass_Function_PMF|PMF]] gives the probability for each possible outcome ($x=0$ or $x=1$):
    $$ P(X=x) = p^x (1-p)^{1-x} \quad \text{for } x \in \{0, 1\} $$
*   Let's check this formula:
    *   If $x = 1$ (success): $P(X=1) = p^1 (1-p)^{1-1} = p (1-p)^0 = p \times 1 = p$
    *   If $x = 0$ (failure): $P(X=0) = p^0 (1-p)^{1-0} = 1 \times (1-p)^1 = 1-p$
*   The PMF can also be written piecewise:
    $$
    P(X=x) = \begin{cases} p & \text{if } x=1 \\ 1-p & \text{if } x=0 \end{cases}
    $$

### 4. Parameters
*   The Bernoulli distribution has only **one parameter**: $p$, the probability of success (where $0 \le p \le 1$).

### 5. Expected Value (Mean)
*   The [[01_Expected_Value|expected value]] (average outcome over many trials) of a Bernoulli RV is:
    $$ E[X] = \sum x \cdot P(X=x) = (1 \cdot p) + (0 \cdot (1-p)) = p $$
*   Intuition: If you flip a coin with $P(\text{Heads})=0.6$ many times, the average outcome (treating Heads=1, Tails=0) will be close to 0.6.

### 6. Variance
*   The [[02_Variance_and_Standard_Deviation|variance]] (measure of spread) of a Bernoulli RV is:
    $$ Var(X) = E[X^2] - (E[X])^2 $$
    *   $E[X^2] = (1^2 \cdot p) + (0^2 \cdot (1-p)) = p$
    *   $Var(X) = p - p^2 = p(1-p)$
*   The variance is maximized when $p = 0.5$ (most uncertainty) and is 0 when $p=0$ or $p=1$ (certainty).

## Connections to Other Topics
*   The Bernoulli distribution is the fundamental building block for several other more complex discrete distributions:
    *   [[02_Binomial_Distribution|Binomial Distribution]]: Represents the *number of successes* in a *fixed number* ($n$) of independent Bernoulli trials.
    *   [[08_Geometric_Distribution|Geometric Distribution]]: Represents the *number of Bernoulli trials* needed to get the *first* success.
    *   [[09_Negative_Binomial_Distribution|Negative Binomial Distribution]]: Represents the *number of Bernoulli trials* needed to get a *fixed number* ($r$) of successes.
*   Used in [[../../06 Machine Learning/02 Supervised/02 Classification/02_Logistic Regression/Logistic Regression|Logistic Regression]] where the outcome for each data point is often modeled as a Bernoulli variable (e.g., predicting click/no-click).

## Summary
*   Models a **single trial** with **two outcomes** (success/failure).
*   Parameter: $p$ = probability of success (value 1).
*   PMF: $P(X=1) = p$, $P(X=0) = 1-p$. Can be written $p^x(1-p)^{1-x}$.
*   Mean: $E[X] = p$.
*   Variance: $Var(X) = p(1-p)$.
*   Foundation for Binomial, Geometric, and Negative Binomial distributions.

## Sources
*   [Wikipedia: Bernoulli Distribution](https://en.wikipedia.org/wiki/Bernoulli_distribution)
*   [Khan Academy: Bernoulli Distribution](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/bernoulli-distribution/v/bernoulli-distribution)
*   [PennState STAT 414: Bernoulli Distribution](https://online.stat.psu.edu/stat414/lesson/10/10.1)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters on probability distributions. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., "Probability and Statistics for Engineers and Scientists" by Walpole, Myers, Ye; "A First Course in Probability" by Sheldon Ross) - Consult relevant chapters.

## TAGS
[[Probability]] [[Probability Distribution]] [[Discrete Distribution]] [[Bernoulli Distribution]] [[PMF]] [[Expected Value]] [[02 Math/02 Inferential statistics/Tradeoffs/Variance]] [[02 Math/index]] [[Statistics]] [[Binomial Distribution]]