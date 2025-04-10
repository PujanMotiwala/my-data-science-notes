# Exponential Distribution

## Definition / Introduction
*   The Exponential distribution is a [[02 Math/01 Probability/02 Random Variables/01_Definition|Continuous Probability Distribution]] that models the **time until an event occurs** in a [[03_Poisson_Distribution|Poisson process]].
*   A Poisson process is one where events occur continuously and independently at a constant average rate ($\lambda$). The Exponential distribution describes the waiting time for the *next* event.
*   Examples: Time until the next customer arrives, time until a radioactive particle decays, time until a component fails (assuming constant failure rate), duration of telephone calls.

## Key Concepts

### 1. The Exponential Random Variable
*   A continuous random variable $X$ follows an Exponential distribution if it represents the waiting time for an event in a process where events occur at a constant average rate $\lambda$.
*   Possible values for $X$ are non-negative real numbers ($X \ge 0$).
*   Notation: $X \sim \text{Exponential}(\lambda)$ or $X \sim \text{Exp}(\lambda)$. (Sometimes parameterized by the mean $\beta = 1/\lambda$, as $\text{Exp}(\beta)$). We'll use the rate parameter $\lambda$.

### 2. Probability Density Function (PDF)
*   The [[03_Probability_Density_Function_PDF|PDF]] shows that shorter waiting times are more likely, with the probability decreasing exponentially as the waiting time $x$ increases:
    $$
    f(x | \lambda) = \begin{cases} \lambda e^{-\lambda x} & \text{if } x \ge 0 \\ 0 & \text{if } x < 0 \end{cases}
    $$
*   Where:
    *   $x$ is the waiting time ($x \ge 0$).
    *   $\lambda$ (lambda) is the rate parameter (average number of events per unit of time), $\lambda > 0$.
    *   $e$ is Euler's number ($e \approx 2.71828...$).

### 3. Parameter
*   The Exponential distribution (when parameterized by rate) has **one parameter**:
    *   $\lambda$ (Rate): The average number of events per unit interval (same $\lambda$ as in the related [[03_Poisson_Distribution|Poisson distribution]]).

### 4. Cumulative Distribution Function (CDF)
*   The [[04_Cumulative_Distribution_Function_CDF|CDF]] $F(x) = P(X \le x)$ gives the probability that the event occurs *within* time $x$:
    $$
    F(x) = P(X \le x) = \begin{cases} 1 - e^{-\lambda x} & \text{if } x \ge 0 \\ 0 & \text{if } x < 0 \end{cases}
    $$
*   This is derived by integrating the PDF: $\int_0^x \lambda e^{-\lambda t} dt$.

### 5. Expected Value (Mean)
*   The [[01_Expected_Value|expected]] (average) waiting time until the next event is the reciprocal of the rate:
    $$ E[X] = \frac{1}{\lambda} $$
*   Intuition: If events occur at a high rate ($\lambda$ is large), the average waiting time between them ($1/\lambda$) is short.

### 6. Variance
*   The [[02_Variance_and_Standard_Deviation|variance]] of the waiting time is:
    $$ Var(X) = \frac{1}{\lambda^2} $$
*   Note: The standard deviation is $\sigma = \sqrt{Var(X)} = 1/\lambda$, which is equal to the mean.

### 7. Memorylessness Property
*   The Exponential distribution has a unique property among continuous distributions called **memorylessness**.
*   Mathematically: $P(X > s + t | X > s) = P(X > t)$ for all $s, t \ge 0$.
*   **Intuition:** If you've already waited $s$ units of time for an event without it occurring, the probability that you'll have to wait an *additional* $t$ units of time is exactly the same as the probability you would have had to wait $t$ units from the very beginning. The process "doesn't remember" how long you've already waited.
*   Example: If component lifetime follows an Exponential distribution, knowing it has already survived for 100 hours doesn't change the probability distribution of its *remaining* lifetime. This is often unrealistic for mechanical components (which wear out) but can be applicable to certain electronic components or radioactive decay.

## Connections to Other Topics
*   **[[03_Poisson_Distribution|Poisson Distribution]]:** Describes the *number* of events in a fixed interval, while Exponential describes the *time between* those events. They are intrinsically linked through the Poisson process.
*   **[[10_Gamma_Distribution|Gamma Distribution]]:** The Exponential distribution is a special case of the Gamma distribution where the shape parameter $\alpha=1$ ($Exp(\lambda) = Gamma(1, \lambda)$). The Gamma distribution models the waiting time until the $\alpha$-th event.
*   **[[08_Geometric_Distribution|Geometric Distribution]]:** The discrete analogue of the Exponential distribution. It models the number of [[01_Bernoulli_Distribution|Bernoulli trials]] needed until the *first* success and also possesses a discrete version of the memorylessness property.
*   Used heavily in **Reliability Engineering** and **Survival Analysis** to model lifetimes or time-to-failure (though often more complex distributions like Weibull are needed if the failure rate isn't constant).
*   Used in **Queueing Theory** to model inter-arrival times and service times.

## Summary
*   Models the **waiting time ($x$)** until an event occurs in a **Poisson process** (constant average rate $\lambda$).
*   Parameter: $\lambda$ (rate of events).
*   PDF: $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$. Decreasing curve. Uses `\begin{cases}`.
*   CDF: $F(x) = 1 - e^{-\lambda x}$ for $x \ge 0$. Uses `\begin{cases}`.
*   Mean: $E[X] = 1/\lambda$ (average waiting time).
*   Variance: $Var(X) = 1/\lambda^2$ (Mean = Standard Deviation).
*   Key Property: **Memorylessness**.
*   Related to Poisson (counts), Gamma ($\alpha=1$), and Geometric (discrete waiting time) distributions.

## Sources
*   [Wikipedia: Exponential Distribution](https://en.wikipedia.org/wiki/Exponential_distribution)
*   [Khan Academy: Exponential Distribution](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/continuous-random-variables-library/v/exponential-distribution-probability-density-function)
*   [PennState STAT 414: Exponential Distribution](https://online.stat.psu.edu/stat414/lesson/16/16.3)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross) - Consult relevant chapters.

## TAGS
[[Probability]] [[Probability Distribution]] [[Continuous Distribution]] [[Exponential Distribution]] [[PDF]] [[CDF]] [[Expected Value]] [[02 Math/02 Inferential statistics/Tradeoffs/Variance]] [[Rate Parameter]] [[Memorylessness]] [[Poisson Distribution]] [[Poisson Process]] [[Gamma Distribution]] [[Geometric Distribution]] [[Survival Analysis]] [[Queueing Theory]] [[02 Math/index]] [[Statistics]]