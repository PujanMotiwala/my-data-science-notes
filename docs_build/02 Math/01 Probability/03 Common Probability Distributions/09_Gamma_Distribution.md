---
tags:
- Bayesian Statistics
- CDF
- Chi-squared Distribution
- Continuous Distribution
- Expected Value
- Exponential Distribution
- Gamma Distribution
- Gamma Function
- PDF
- Poisson Process
- Probability
- Probability Distribution
- Statistics
---

# Gamma Distribution

## Definition / Introduction
*   The Gamma distribution is a flexible [[02 Math/01 Probability/02 Random Variables/01_Definition|Continuous Probability Distribution]] defined for positive real numbers ($x > 0$).
*   It arises naturally as the distribution of the **waiting time until a specified number ($\alpha$) of events occur** in a [[03_Poisson_Distribution|Poisson process]] with rate $\beta$.
*   It generalizes both the [[06_Exponential_Distribution|Exponential distribution]] (waiting time for the 1st event) and the Chi-squared distribution (related to sum of squared Normal variables).
*   Used extensively in reliability, queueing theory, climate modeling, and Bayesian statistics (as a conjugate prior for parameters like the Poisson rate or the precision of a Normal distribution).

## Key Concepts

### 1. Parameters
The Gamma distribution is typically parameterized in two main ways:
*   **Parameterization 1 (Shape $\alpha$ and Rate $\beta$):** This is common in probability and Bayesian statistics.
    *   $\alpha$ (alpha): Shape parameter ($\alpha > 0$). Controls the shape of the curve.
    *   $\beta$ (beta): Rate parameter ($\beta > 0$). Inverse scale; $1/\beta$ is the scale. Corresponds to the rate $\lambda$ in the underlying Poisson process.
*   **Parameterization 2 (Shape $k$ and Scale $\theta$):** Common in some fields and software.
    *   $k$: Shape parameter ($k = \alpha$).
    *   $\theta$ (theta): Scale parameter ($\theta = 1/\beta$).

*We will use **Parameterization 1 (Shape $\alpha$, Rate $\beta$)**.*
*Notation: $X \sim \text{Gamma}(\alpha, \beta)$ or $X \sim \Gamma(\alpha, \beta)$ .*

### 2. Probability Density Function (PDF)
*   The [[03_Probability_Density_Function_PDF|PDF]] for $X \sim \text{Gamma}(\alpha, \beta)$ is:
    $$ f(x | \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} \quad \text{for } x > 0 $$
*   Where:
    *   $x$ is the value of the random variable (waiting time, etc.).
    *   $\alpha > 0$ is the shape parameter.
    *   $\beta > 0$ is the rate parameter.
    *   $e$ is Euler's number.
    *   $\Gamma(\alpha)$ is the **Gamma Function**.

### 3. The Gamma Function $\Gamma(\alpha)$
*   A generalization of the factorial function to real (and complex) numbers.
*   Definition: $\Gamma(\alpha) = \int_0^{\infty} t^{\alpha-1} e^{-t} dt$ for $\alpha > 0$.
*   Key Properties:
    *   $\Gamma(\alpha) = (\alpha - 1) \Gamma(\alpha - 1)$ (Recursive property).
    *   If $n$ is a positive integer, $\Gamma(n) = (n - 1)!$.
    *   $\Gamma(1/2) = \sqrt{\pi}$.
*   It acts as the normalization constant in the Gamma PDF, ensuring the total area integrates to 1.

### 4. Cumulative Distribution Function (CDF)
*   The [[04_Cumulative_Distribution_Function_CDF|CDF]] $F(x) = P(X \le x)$ involves the **lower incomplete Gamma function** $\gamma(s, x) = \int_0^x t^{s-1}e^{-t} dt$:
    $$ F(x | \alpha, \beta) = \frac{\gamma(\alpha, \beta x)}{\Gamma(\alpha)} = P(\alpha, \beta x) \quad \text{for } x > 0 $$
    where $P(s, x)$ is the regularized lower incomplete Gamma function.
*   There's no simple closed-form expression; probabilities are typically found using statistical software.

### 5. Expected Value (Mean)
*   The [[01_Expected_Value|expected value]] is:
    $$ E[X] = \frac{\alpha}{\beta} $$
*   If $\alpha$ is the number of events and $\beta$ is the rate, this makes sense: average rate per event is $1/\beta$, so time for $\alpha$ events is $\alpha \times (1/\beta)$.

### 6. Variance
*   The [[02_Variance_and_Standard_Deviation|variance]] is:
    $$ Var(X) = \frac{\alpha}{\beta^2} $$

### 7. Shape of the Distribution
*   The shape parameter $\alpha$ significantly influences the distribution's form:
    *   $\alpha = 1$: Reduces to the [[06_Exponential_Distribution|Exponential distribution]] $\text{Exp}(\beta)$. PDF starts high at $x=0$ and decays.
    *   $\alpha > 1$: PDF starts at 0, increases to a peak (mode at $(\alpha-1)/\beta$), and then decreases. As $\alpha$ increases, the distribution becomes more symmetric and bell-shaped (approaching Normal due to CLT on sum of Exponentials).
    *   $0 < \alpha < 1$: PDF starts infinitely high near $x=0$ and decreases steeply.

## Connections to Other Topics
*   **[[06_Exponential_Distribution|Exponential Distribution]]:** Special case of Gamma when $\alpha=1$.
*   **Chi-squared Distribution ($\chi^2$):** A Chi-squared distribution with $\nu$ degrees of freedom is a special case of the Gamma distribution: $\chi^2(\nu) \sim \text{Gamma}(\alpha = \nu/2, \beta = 1/2)$. Used heavily in hypothesis testing (covered in [[../02 Inferential statistics/Hypothesis testing]]).
*   **[[03_Poisson_Distribution|Poisson Process]]:** Gamma describes the waiting time for the $\alpha$-th event in a Poisson process with rate $\beta$.
*   **Sum of Independent Exponentials:** The sum of $\alpha$ independent Exponential random variables, each with rate $\beta$, follows a $\text{Gamma}(\alpha, \beta)$ distribution (when $\alpha$ is an integer).
*   **Bayesian Statistics:** Often used as a conjugate prior for the rate parameter $\lambda$ of Poisson/Exponential distributions or the precision ($\tau = 1/\sigma^2$) of a [[05_Normal_Gaussian_Distribution|Normal distribution]].

## Summary
*   Models the **waiting time ($x$)** until the **$\alpha$-th event** occurs in a **Poisson process** with rate $\beta$.
*   Flexible continuous distribution for positive values ($x>0$).
*   Parameters: $\alpha$ (shape, $\alpha>0$), $\beta$ (rate, $\beta>0$).
*   PDF involves the Gamma function $\Gamma(\alpha)$. $f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}$.
*   Mean: $E[X] = \alpha/\beta$.
*   Variance: $Var(X) = \alpha/\beta^2$.
*   Generalizes Exponential ($\alpha=1$) and related to Chi-squared distributions.
*   Important in reliability, queueing, and Bayesian inference.

## Sources
*   [Wikipedia: Gamma Distribution](https://en.wikipedia.org/wiki/Gamma_distribution)
*   [PennState STAT 414: Gamma Distribution](https://online.stat.psu.edu/stat414/lesson/18/18.1)
*   [Stat Trek: Gamma Distribution](https://stattrek.com/probability-distributions/gamma)
*   *OpenIntro Statistics* (Free PDF textbook) - Less likely to be covered in detail. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Casella & Berger; Hogg, McKean, Craig "Introduction to Mathematical Statistics") - Consult relevant chapters.