---
tags:
- Bernoulli Distribution
- Beta Distribution
- Binomial Distribution
- Continuous Distribution
- Discrete Distribution
- Exponential Distribution
- Gamma Distribution
- Geometric Distribution
- Negative Binomial Distribution
- Normal Distribution
- Poisson Distribution
- Probability
- Probability Distribution
- Statistics
- Summary
- Uniform Distribution
---

# Overview of Common Probability Distributions

## Introduction
*   This note provides a quick summary and comparison of the fundamental [[02 Math/01 Probability/02 Random Variables/01_Definition|discrete]] and [[02 Math/01 Probability/02 Random Variables/01_Definition|continuous]] probability distributions covered in this section.
*   Understanding the characteristics and typical use cases of these distributions is essential for modeling random phenomena encountered in data science, AI engineering, and statistical analysis.

## Core Distributions Summary

| Distribution                                                      | Type       | Parameters                       | Key Use Case / Interpretation                               | Mean ($E[X]$)                                     | Variance ($Var(X)$)           | Notes                                                  |                        |
| :---------------------------------------------------------------- | :--------- | :------------------------------- | :---------------------------------------------------------- | :------------------------------------------------ | :---------------------------- | :----------------------------------------------------- | ---------------------- |
| [[01_Bernoulli_Distribution\|Bernoulli]]                          | Discrete   | $p$ (success prob)               | Single trial, two outcomes (0/1, success/failure)           | $p$                                               | $p(1-p)$                      | Building block                                         |                        |
| [[02_Binomial_Distribution\|Binomial]]                            | Discrete   | $n$ (trials), $p$                | Number of successes in $n$ independent Bernoulli trials     | $np$                                              | $np(1-p)$                     | Fixed trials                                           |                        |
| [[07_Geometric_Distribution\|Geometric_Distribution]]             | Discrete   | $p$                              | Number of trials until *first* success                      | $1/p$                                             | $\frac{1-p}{p^2}$             | Memoryless                                             |                        |
| [[08_Negative_Binomial_Distribution\|Negative Binomial (Trials)]] | Discrete   | $r$ (successes), $p$             | Number of trials until *$r$-th* success                     | $r/p$                                             | $\frac{r(1-p)}{p^2}$          | Generalizes Geometric ($r=1$)                          |                        |
| [[03_Poisson_Distribution\|Poisson]]                              | Discrete   | $\lambda$ (rate/average)         | Number of events in fixed interval (time/space)             | $\lambda$                                         | $\lambda$                     | Mean = Variance                                        |                        |
| [[04_Uniform_Distribution\|Uniform (Continuous)]]                 | Continuous | $a$ (min), $b$ (max)             | Outcomes equally likely within range $[a, b]$               | $\frac{a+b}{2}$                                   | $\frac{(b-a)^2}{12}$          | Used in simulation                                     |                        |
| [[06_Exponential_Distribution\|Exponential]]                      | Continuous | $\lambda$ (rate)                 | Waiting time until *next* event in Poisson process          | $1/\lambda$                                       | $1/\lambda^2$                 | Memoryless, Mean=SD                                    |                        |
| [[09_Gamma_Distribution\|Gamma]]                                  | Continuous | $\alpha$ (shape), $\beta$ (rate) | Waiting time until *$\alpha$-th* event in Poisson process   | $\alpha/\beta$                                    | $\alpha/\beta^2$              | Generalizes Exponential ($\alpha=1$)                   |                        |
| [[05_Normal_Gaussian_Distribution\|Normal (Gaussian)]]            | Continuous | $\mu$ (mean), $\sigma^2$ (var)   | "Bell curve", sums of vars (CLT), errors, natural phenomena | $\mu$                                             | $\sigma^2$                    | Central Limit Theorem                                  |                        |
| [[10_Beta_Distribution\|Beta_Distribution]]                       | Beta]]     | Continuous                       | $\alpha$ (shape), $\beta$ (shape)                           | Represents a probability (values between 0 and 1) | $\frac{\alpha}{\alpha+\beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | Bayesian prior for $p$ |

## Key Takeaways & Relationships

*   **Discrete vs. Continuous:** Remember the fundamental difference in how probabilities are assigned ([[02_Probability_Mass_Function_PMF|PMF]] for points vs. [[03_Probability_Density_Function_PDF|PDF]] for intervals/areas).
*   **Bernoulli as Building Block:** [[01_Bernoulli_Distribution|Bernoulli]] trials underlie the [[02_Binomial_Distribution|Binomial]], [[08_Geometric_Distribution|Geometric]], and [[09_Negative_Binomial_Distribution|Negative Binomial]] distributions.
*   **Poisson Process:** The [[03_Poisson_Distribution|Poisson distribution]] (counts in interval) and [[06_Exponential_Distribution|Exponential]]/[[10_Gamma_Distribution|Gamma]] distributions (waiting times) describe different aspects of the same underlying random arrival process.
*   **Generalizations:** [[09_Negative_Binomial_Distribution|Negative Binomial]] generalizes [[08_Geometric_Distribution|Geometric]]; [[10_Gamma_Distribution|Gamma]] generalizes [[06_Exponential_Distribution|Exponential]].
*   **Approximations:** [[05_Normal_Gaussian_Distribution|Normal]] approximates [[02_Binomial_Distribution|Binomial]] (large $n$) and [[03_Poisson_Distribution|Poisson]] (large $\lambda$). [[03_Poisson_Distribution|Poisson]] approximates [[02_Binomial_Distribution|Binomial]] (large $n$, small $p$).
*   **Modeling Choices:**
    *   Binary outcome, single trial -> [[01_Bernoulli_Distribution|Bernoulli]]
    *   Number of successes in fixed trials -> [[02_Binomial_Distribution|Binomial]]
    *   Number of trials for fixed successes -> [[08_Geometric_Distribution|Geometric]] ($r=1$) or [[09_Negative_Binomial_Distribution|Negative Binomial]] ($r>1$)
    *   Number of events in fixed interval -> [[03_Poisson_Distribution|Poisson]]
    *   Waiting time for next event -> [[06_Exponential_Distribution|Exponential]]
    *   Waiting time for $\alpha$-th event -> [[10_Gamma_Distribution|Gamma]]
    *   Equally likely continuous outcomes -> [[04_Uniform_Distribution|Uniform]]
    *   Symmetric "bell-shaped" data, sums/averages -> [[05_Normal_Gaussian_Distribution|Normal]]
    *   Modeling a probability itself (value between 0 and 1) -> [[11_Beta_Distribution|Beta]]

## Further Exploration
*   Distributions crucial for **Statistical Inference** (often derived from the Normal) include the **t-distribution**, **Chi-squared ($\chi^2$) distribution**, and **F-distribution**. These will be covered in the context of hypothesis testing and confidence intervals ([[../02 Inferential statistics/parametric tests/Parametric Tests|Parametric Tests]]).
*   Understanding **[[05_Joint_Marginal_Conditional_Distributions|Joint Distributions]]** (e.g., Multivariate Normal) is key for modeling relationships between multiple variables.
*   [[02_Central_Limit_Theorem_CLT|Central Limit Theorem]] and [[01_Law_of_Large_Numbers_LLN|Law of Large Numbers]] are theoretical cornerstones underpinning the relevance of many distributions, especially the Normal distribution.

## Sources
*   Refer to the individual notes for each distribution for specific sources.
*   General Probability & Statistics Textbooks (e.g., *OpenIntro Statistics*, Walpole et al., Ross, DeGroot & Schervish, Casella & Berger) provide comprehensive coverage.