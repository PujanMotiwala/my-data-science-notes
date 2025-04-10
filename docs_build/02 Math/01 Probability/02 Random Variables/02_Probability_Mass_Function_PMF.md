---
tags:
- Discrete Variable
- PMF
- Probability
- Probability Distribution
- Probability Mass Function
- Random Variable
- Statistics
---

# Probability Mass Function (PMF)

## Definition / Introduction
*   For a [[02 Math/01 Probability/02 Random Variables/01_Definition|Discrete Random Variable]] (RV), we need a way to describe the probability associated with each specific value it can take.
*   The **Probability Mass Function (PMF)** provides this description. It gives the probability that a discrete random variable $X$ is exactly equal to some specific value $x$.
*   It essentially lists all possible numerical values the discrete RV can take and their corresponding probabilities.

## Key Concepts

### 1. Notation and Definition
*   The PMF of a discrete random variable $X$ is denoted by $p(x)$, $p_X(x)$, or $P(X=x)$.
*   **Definition:** $p(x) = P(X = x)$
    *   $p(x)$ is the probability that the random variable $X$ takes on the specific value $x$.

### 2. Properties of a PMF
A function $p(x)$ can be considered a valid PMF if and only if it satisfies these two conditions:
*   **Non-negativity:** The probability for every possible value $x$ must be greater than or equal to zero.
    $$ p(x) \ge 0 \quad \text{for all possible values } x $$
*   **Summation to One:** The sum of the probabilities for all possible values $x$ that the random variable $X$ can take must equal 1. This reflects that one of the possible outcomes must occur.
    $$ \sum_{\text{all } x} p(x) = 1 $$

### 3. Example: Fair Coin Flips
*   **Experiment:** Flip a fair coin twice.
*   **Random Variable (X):** Let X be the number of Heads. Possible values for X are $\{0, 1, 2\}$.
*   **Sample Space (S):** $\{TT, TH, HT, HH\}$ (Each outcome has probability $1/4$).
*   **Calculating the PMF:**
    *   $p(0) = P(X=0) = P(\{TT\}) = 1/4$
    *   $p(1) = P(X=1) = P(\{TH, HT\}) = P(\{TH\}) + P(\{HT\}) = 1/4 + 1/4 = 2/4 = 1/2$
    *   $p(2) = P(X=2) = P(\{HH\}) = 1/4$
*   **PMF Representation:** We can represent this PMF as a table or a function:

    | $x$ (Value of X) | $p(x) = P(X=x)$ |
    |------------------|-----------------|
    | 0                | 1/4             |
    | 1                | 1/2             |
    | 2                | 1/4             |
    | **Total**        | **1**           |

*   **Verification:** Note that $p(x) \ge 0$ for all $x$, and $\frac{1}{4} + \frac{1}{2} + \frac{1}{4} = 1$.

### 4. Visualization
*   A PMF is often visualized using a **bar chart** or a **spike plot**, where the height of the bar/spike at each value $x$ represents the probability $p(x)$.

### 5. Usage
*   The PMF allows us to calculate the probability of the RV falling within a certain range by summing the probabilities of the individual values within that range.
*   Example: Using the coin flip PMF, what is the probability of getting *at least* one Head?
    *   $P(X \ge 1) = P(X=1) + P(X=2) = p(1) + p(2) = \frac{1}{2} + \frac{1}{4} = \frac{3}{4}$.

## Connections to Other Topics
*   The PMF defines the probability distribution for a [[02 Math/01 Probability/02 Random Variables/01_Definition|Discrete Random Variable]]. Common discrete distributions like [[01_Bernoulli_Distribution|Bernoulli]], [[02_Binomial_Distribution|Binomial]], and [[03_Poisson_Distribution|Poisson]] are characterized by their specific PMF formulas.
*   The PMF is used to calculate the [[01_Expected_Value|Expected Value]] ($E[X] = \sum x p(x)$) and [[02_Variance_and_Standard_Deviation|Variance]] ($Var(X) = \sum (x-\mu)^2 p(x)$) of a discrete RV.
*   It is related to the [[04_Cumulative_Distribution_Function_CDF|Cumulative Distribution Function (CDF)]] for discrete variables: $F(x) = P(X \le x) = \sum_{t \le x} p(t)$.

## Summary
*   The **PMF** gives the probability $P(X=x)$ for each possible value $x$ of a **discrete** random variable $X$.
*   Key properties: $p(x) \ge 0$ and $\sum p(x) = 1$.
*   It fully describes the probability distribution of a discrete RV.
*   Often visualized as a bar chart.

## Sources
*   [Wikipedia: Probability Mass Function](https://en.wikipedia.org/wiki/Probability_mass_function)
*   [PennState STAT 414: Probability Mass Functions](https://online.stat.psu.edu/stat414/lesson/9/9.1)
*   [Statistics LibreTexts: Probability Mass Functions (PMF)](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/03%3A_Distributions/3.01%3A_Introduction_to_Distributions) (Check Section 3.1 or similar)
*   (Introductory Probability and Statistics textbooks)