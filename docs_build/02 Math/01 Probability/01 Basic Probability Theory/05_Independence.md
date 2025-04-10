---
tags:
- Conditional Independence
- Conditional Probability
- Dependence
- Independence
- Machine Learning
- Multiplication Rule
- Naive Bayes
- Probability
- Statistics
---

# Independence of Events

## Definition / Introduction
*   In probability, two events $A$ and $B$ are **independent** if the occurrence of one event does not affect the probability of the other event occurring.
*   Conversely, events are **dependent** if the occurrence of one *does* change the probability of the other.
*   Understanding independence is crucial as it often allows for significant simplification in calculating joint probabilities and is a key assumption in many statistical models (like Naive Bayes).

## Key Concepts

### 1. Intuitive Definition
*   Events A and B are independent if knowing that B occurred does not give you any new information about the likelihood of A occurring (and vice-versa).

### 2. Mathematical Definitions
There are three equivalent ways to mathematically define independence for events A and B:

*   **Using Conditional Probability:** A and B are independent if and only if:
    $$ P(A|B) = P(A) $$
    (Requires $P(B) > 0$). This directly reflects the intuition: the probability of A remains the same even when we know B happened.
    *   Equivalently: $P(B|A) = P(B)$ (Requires $P(A) > 0$).

*   **Using Joint Probability (Multiplication Rule for Independent Events):** A and B are independent if and only if:
    $$ P(A \cap B) = P(A) P(B) $$
    This is often the most practical way to check for or utilize independence. The probability of both independent events occurring is simply the product of their individual probabilities.

### 3. Contrast with Dependence
*   Events A and B are **dependent** if they are *not* independent. This means:
    *   $P(A|B) \neq P(A)$
    *   $P(B|A) \neq P(B)$
    *   $P(A \cap B) \neq P(A) P(B)$
*   In dependent events, knowing one occurred provides information about the other.

### 4. Examples
*   **Independent Events:**
    *   Experiment: Flipping a fair coin twice.
    *   Event A: Getting Heads on the first flip ($P(A) = 0.5$). Event B: Getting Heads on the second flip ($P(B) = 0.5$).
    *   These are independent. $P(A|B) = 0.5 = P(A)$. The outcome of the first flip doesn't influence the second.
    *   $P(A \cap B)$ (Heads on both) = $P(HH) = 0.25$. Also, $P(A) P(B) = 0.5 \times 0.5 = 0.25$. The multiplication rule holds.
*   **Dependent Events:**
    *   Experiment: Drawing two cards from a standard deck *without* replacement.
    *   Event A: The first card is a King ($P(A) = 4/52$). Event B: The second card is a King.
    *   These are dependent. If the first card *was* a King, then $P(B|A) = 3/51$. If the first card was *not* a King, then $P(B|\neg A) = 4/51$. Since $P(B|A) \neq P(B|\neg A)$, the probability of B depends on the outcome of A.
    *   Here, $P(B)$ is actually $4/52$ (by symmetry), but $P(B|A) = 3/51 \neq 4/52$.
    *   $P(A \cap B)$ (both Kings) = $P(A) P(B|A) = (\frac{4}{52}) \times (\frac{3}{51})$. This is not equal to $P(A) P(B) = (\frac{4}{52}) \times (\frac{4}{52})$.

### 5. Conditional Independence
*   Sometimes, two events A and B might be dependent, but become independent *given* a third event C. This is called conditional independence.
*   Definition: A and B are conditionally independent given C if $P(A \cap B | C) = P(A|C) P(B|C)$. Or equivalently $P(A | B, C) = P(A | C)$.
*   **Importance:** This concept is fundamental in graphical models and Bayesian networks.

### 6. Independence of Multiple Events
*   For more than two events (e.g., A, B, C) to be mutually independent, the multiplication rule must hold for all possible subsets of events:
    *   $P(A \cap B) = P(A)P(B)$
    *   $P(A \cap C) = P(A)P(C)$
    *   $P(B \cap C) = P(B)P(C)$
    *   $P(A \cap B \cap C) = P(A)P(B)P(C)$

## Connections to Other Topics
*   Crucial distinction when applying the [[04_Conditional_Probability|Multiplication Rule]]. Use $P(A \cap B) = P(A)P(B)$ only if independent, otherwise use $P(A \cap B) = P(A|B)P(B)$.
*   The assumption of feature independence (often conditional independence given the class) is the core idea behind the [[../../06 Machine Learning/02 Supervised/02 Classification/Naive Bayes|Naive Bayes classifier]], making computations tractable.
*   Related to the concept of uncorrelated variables in [[03_Covariance_and_Correlation|Covariance and Correlation]], although independence is a stronger condition (independence implies zero correlation, but zero correlation does not always imply independence, except for normally distributed variables).

## Summary
*   **Independent Events:** Occurrence of one does not affect the probability of the other.
*   **Key Tests:** $P(A|B) = P(A)$ or $P(A \cap B) = P(A) P(B)$.
*   **Dependent Events:** Occurrence of one *does* affect the probability of the other.
*   Independence simplifies calculations significantly ($P(A \text{ and } B) = P(A) P(B)$).
*   It's a critical assumption in many statistical models and algorithms.

## Sources
*   [Khan Academy: Independent Events](https://www.khanacademy.org/math/statistics-probability/probability-library/conditional-probability-independence/v/independent-events-examples)
*   [Wikipedia: Independence (probability theory)](https://en.wikipedia.org/wiki/Independence_(probability_theory))
*   [Math is Fun: Independent Events](https://www.mathsisfun.com/data/probability-events-independent.html)
*   [PennState STAT 414: Independence](https://online.stat.psu.edu/stat414/lesson/6/6.1)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross) - Consult relevant chapters.