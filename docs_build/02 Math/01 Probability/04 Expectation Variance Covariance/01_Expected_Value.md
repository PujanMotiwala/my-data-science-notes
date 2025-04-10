---
tags:
- Central Tendency
- Decision Theory
- Expected Value
- LOTUS
- Linearity of Expectation
- Mean
- PDF
- PMF
- Probability
- Random Variable
- Statistics
---

# Expected Value (Mean of a Random Variable)

## Definition / Introduction
*   The **Expected Value** of a [[02 Math/01 Probability/02 Random Variables/01_Definition|Random Variable]] (RV) $X$ represents its theoretical long-run average value if the underlying random experiment were repeated many times.
*   It's a weighted average of all possible values the RV can take, where the weights are the probabilities (or probability densities) of those values occurring.
*   It's a fundamental concept for summarizing the central tendency of a probability distribution and plays a key role in decision theory and model evaluation.
*   Notation: $E[X]$, $\mu$, or $\mu_X$.

## Key Concepts

### 1. Calculation for Discrete Random Variables
*   For a [[02 Math/01 Probability/02 Random Variables/01_Definition|Discrete RV]] $X$ with possible values $x_1, x_2, ...$ and [[02_Probability_Mass_Function_PMF|PMF]] $p(x)$, the expected value is the sum of each value multiplied by its probability:
    $$ E[X] = \mu = \sum_{\text{all } x} x \cdot p(x) = x_1 p(x_1) + x_2 p(x_2) + \dots $$
*   **Example:** Rolling a fair six-sided die. $X$ = outcome. Values are $\{1, 2, 3, 4, 5, 6\}$, each with $p(x) = 1/6$.
    $E[X] = (1 \cdot \frac{1}{6}) + (2 \cdot \frac{1}{6}) + (3 \cdot \frac{1}{6}) + (4 \cdot \frac{1}{6}) + (5 \cdot \frac{1}{6}) + (6 \cdot \frac{1}{6})$
    $E[X] = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5$
    *Interpretation:* While you can never roll a 3.5, if you rolled the die many times, the average of the outcomes would approach 3.5.

### 2. Calculation for Continuous Random Variables
*   For a [[02 Math/01 Probability/02 Random Variables/01_Definition|Continuous RV]] $X$ with [[03_Probability_Density_Function_PDF|PDF]] $f(x)$, the expected value is found by integrating $x$ times its probability density $f(x)$ over all possible values of $x$:
    $$ E[X] = \mu = \int_{-\infty}^{\infty} x \cdot f(x) \, dx $$
*   **Example:** [[04_Uniform_Distribution|Uniform Distribution]] $X \sim U(a, b)$, where $f(x) = \frac{1}{b-a}$ for $a \le x \le b$.
    $E[X] = \int_a^b x \cdot \frac{1}{b-a} \, dx = \frac{1}{b-a} \left[ \frac{x^2}{2} \right]_a^b$
    $E[X] = \frac{1}{b-a} \left( \frac{b^2}{2} - \frac{a^2}{2} \right) = \frac{1}{b-a} \frac{(b-a)(b+a)}{2} = \frac{a+b}{2}$
    *Interpretation:* The expected value is the midpoint of the interval, as expected due to symmetry.

### 3. Intuition: Center of Mass
*   Think of the probability distribution (PMF or PDF) as describing how mass is distributed along the number line. The expected value $E[X]$ is the "balancing point" or the center of mass of this distribution.

### 4. Linearity of Expectation (Very Important Property)
*   For any random variables $X$ and $Y$ (discrete or continuous, dependent or independent) and any constants $a$ and $b$:
    *   $E[aX + b] = aE[X] + b$
    *   $E[X + Y] = E[X] + E[Y]$ (Expectation of a sum is the sum of expectations)
    *   General form: $E[aX + bY] = aE[X] + bE[Y]$
*   **Significance:** This property greatly simplifies calculations involving sums or linear transformations of random variables, even if they are correlated.

### 5. Expected Value of a Function of an RV
*   If $Y = g(X)$ is a function of a random variable $X$, its expected value can be calculated without finding the distribution of $Y$, using the Law of the Unconscious Statistician (LOTUS):
    *   Discrete: $E[Y] = E[g(X)] = \sum_{\text{all } x} g(x) p(x)$
    *   Continuous: $E[Y] = E[g(X)] = \int_{-\infty}^{\infty} g(x) f(x) dx$

## Connections to Other Topics & Relevance
*   **Decision Making:** Used to compare choices under uncertainty (e.g., calculating expected profit/loss for different business strategies). Choose the option with the best expected outcome.
*   **Model Evaluation:** The mean of errors (e.g., Mean Squared Error involves expected values) is a common way to assess predictive models.
*   **Central Tendency:** $E[X]$ is the primary measure of the center of a probability distribution, analogous to the sample mean for data.
*   [[02_Variance_and_Standard_Deviation|Variance]] calculation uses $E[X]$ and $E[X^2]$.
*   [[01_Law_of_Large_Numbers_LLN|Law of Large Numbers (LLN)]] states that the sample mean converges to the expected value $E[X]$ as sample size increases.

## Summary
*   **Expected Value $E[X]$** is the theoretical long-run average of a random variable $X$.
*   Calculation: Sum $x \cdot p(x)$ (discrete) or Integral $\int x \cdot f(x) dx$ (continuous).
*   Represents the center of mass of the distribution.
*   **Linearity:** $E[aX + bY] = aE[X] + bE[Y]$ holds universally.
*   Crucial for decision theory, model assessment, and defining other statistical measures.

## Sources
*   [Wikipedia: Expected Value](https://en.wikipedia.org/wiki/Expected_value)
*   [Khan Academy: Expected Value](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/expected-value-library/v/expected-value-of-a-discrete-random-variable)
*   [PennState STAT 414: Expected Value](https://online.stat.psu.edu/stat414/lesson/19) (Continuous) & Lesson 11 (Discrete)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross; DeGroot & Schervish) - Consult relevant chapters.