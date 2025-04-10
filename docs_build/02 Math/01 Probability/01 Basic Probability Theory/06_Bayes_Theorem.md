---
tags:
- Bayes Theorem
- Bayesian Inference
- Conditional Probability
- Likelihood
- Machine Learning
- Posterior
- Prior
- Probability
- Statistics
---

# Bayes' Theorem

## Definition / Introduction
*   Bayes' Theorem (or Bayes' Rule) is a fundamental theorem in probability theory that describes how to update the probability of a hypothesis ($H$) based on new evidence ($E$).
*   It mathematically formalizes the process of learning from experience, relating the [[04_Conditional_Probability|Conditional Probability]] $P(H|E)$ to $P(E|H)$.
*   It's named after Reverend Thomas Bayes and is the cornerstone of [[../02 Inferential statistics/Parametric tests/Bayesian Inference|Bayesian inference]] and many machine learning algorithms (e.g., Naive Bayes classifiers, Bayesian networks).

## Key Concepts

### 1. The Formula
*   Bayes' Theorem relates $P(H|E)$ (the probability of hypothesis H given evidence E) to $P(E|H)$ (the probability of evidence E given hypothesis H). The most common form is:

    $$ P(H|E) = \frac{P(E|H) P(H)}{P(E)} $$

*   **Terminology:**
    *   $P(H|E)$: **Posterior Probability**. The updated probability of the hypothesis $H$ being true *after* observing the evidence $E$. This is what we often want to find.
    *   $P(E|H)$: **Likelihood**. The probability of observing the evidence $E$ *given* that the hypothesis $H$ is true. This is often derived from our model or understanding of the process.
    *   $P(H)$: **Prior Probability**. The initial probability or belief in the hypothesis $H$ being true *before* observing the evidence $E$.
    *   $P(E)$: **Evidence Probability (Marginal Likelihood)**. The overall probability of observing the evidence $E$, regardless of the hypothesis. It acts as a normalization constant.

### 2. Calculating $P(E)$ (The Denominator)
*   The probability of the evidence $P(E)$ can often be calculated using the Law of Total Probability. If $H$ and $\neg H$ (not H) are mutually exclusive and exhaustive hypotheses:
    $$ P(E) = P(E|H) P(H) + P(E|\neg H) P(\neg H) $$
*   Substituting this into the main formula gives an alternative form:
    $$ P(H|E) = \frac{P(E|H) P(H)}{P(E|H) P(H) + P(E|\neg H) P(\neg H)} $$

### 3. Intuition: Updating Beliefs
*   Bayes' Theorem provides a rational way to update our beliefs (Prior) in light of new data (Evidence) to arrive at a revised belief (Posterior).
*   If the observed evidence $E$ is more likely under hypothesis $H$ (i.e., $P(E|H)$ is high) than under alternative hypotheses (i.e., $P(E|\neg H)$ is low), then observing $E$ increases our belief in $H$ ($P(H|E) > P(H)$).
*   The strength of the prior belief $P(H)$ also influences the final posterior probability.

### 4. Example: Medical Diagnosis
*   Suppose a disease (D) affects 1% of the population ($P(D) = 0.01$). So, $P(\neg D) = 0.99$. (Prior)
*   There's a test (T) for the disease. Let $T^+$ denote a positive test result.
    *   If a person has the disease, the test is positive 95% of the time (Sensitivity): $P(T^+|D) = 0.95$. (Likelihood)
    *   If a person does *not* have the disease, the test is positive 5% of the time (False Positive Rate): $P(T^+|\neg D) = 0.05$.
*   **Question:** If a person tests positive ($T^+$), what is the probability they actually have the disease, $P(D|T^+)$? (Posterior)

*   **Calculation:**
    1.  Find $P(T^+)$ (Probability of a positive test) using the Law of Total Probability:
        $P(T^+) = P(T^+|D) P(D) + P(T^+|\neg D) P(\neg D)$
        $P(T^+) = (0.95 \times 0.01) + (0.05 \times 0.99)$
        $P(T^+) = 0.0095 + 0.0495 = 0.0590$
    2.  Apply Bayes' Theorem:
        $P(D|T^+) = \frac{P(T^+|D) P(D)}{P(T^+)}$
        $P(D|T^+) = \frac{0.95 \times 0.01}{0.0590}$
        $P(D|T^+) = \frac{0.0095}{0.0590} \approx 0.161$ or 16.1%

*   **Interpretation:** Even with a positive test result, the probability of actually having this rare disease is only about 16%. This highlights the importance of considering the base rate (prior probability) of the disease.

## Connections to Other Topics
*   Directly built upon [[04_Conditional_Probability|Conditional Probability]].
*   The foundation of [[../02 Inferential statistics/Parametric tests/Bayesian Inference|Bayesian Statistics]] and Bayesian methods in [[../../06 Machine Learning/ML model|Machine Learning]].
*   [[../../06 Machine Learning/02 Supervised/02 Classification/Naive Bayes|Naive Bayes classifiers]] use Bayes' theorem with a strong assumption of feature [[05_Independence|Independence]].
*   Used in spam filters, recommendation systems, and updating parameters in models.

## Summary
*   Bayes' Theorem updates the probability of a hypothesis ($H$) given evidence ($E$).
*   Formula: $P(H|E) = \frac{P(E|H) P(H)}{P(E)}$.
*   Relates Posterior ($P(H|E)$) to Prior ($P(H)$) and Likelihood ($P(E|H)$).
*   The denominator $P(E)$ ensures the posterior probabilities sum correctly.
*   It's a powerful tool for reasoning under uncertainty and updating beliefs.

## Sources
*   [Wikipedia: Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem)
*   [Khan Academy: Bayes' Theorem](https://www.khanacademy.org/math/statistics-probability/probability-library/bayes-theorem/v/bayes-theorem)
*   [BetterExplained: A Short Guide to Bayes' Theorem](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/)
*   [Stanford Encyclopedia of Philosophy: Bayes' Theorem](https://plato.stanford.edu/entries/bayes-theorem/)
*   [Arbital: Bayes' Rule Guide](https://arbital.com/p/bayes_rule_guide/)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross; Gelman et al. "Bayesian Data Analysis") - Consult relevant chapters.