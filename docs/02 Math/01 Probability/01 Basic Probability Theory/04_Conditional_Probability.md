# Conditional Probability

## Definition / Introduction
*   Conditional probability measures the likelihood of an event $A$ occurring *given that* another event $B$ has already occurred or is known to be true.
*   It allows us to update our probability estimates based on new information or conditions.
*   It's a fundamental concept in probability theory with wide applications in inference, machine learning (especially Bayesian methods), and decision making.

## Key Concepts

### 1. Notation
*   The conditional probability of event $A$ occurring given that event $B$ has occurred is denoted by $P(A|B)$.
*   Read as: "The probability of A given B".

### 2. Formula
*   If $P(B) > 0$, the conditional probability $P(A|B)$ is defined as:
    $$ P(A|B) = \frac{P(A \cap B)}{P(B)} $$
*   Where:
    *   $P(A|B)$ is the probability of A given B.
    *   $P(A \cap B)$ (or $P(A \text{ and } B)$) is the probability that *both* event A and event B occur (their intersection).
    *   $P(B)$ is the probability of the conditioning event B occurring.

### 3. Intuition
*   When we know that event $B$ has occurred, we effectively restrict our [[01_Definition_and_Terminology|Sample Space]] to only those outcomes included in $B$.
*   The conditional probability $P(A|B)$ is then the proportion of those outcomes in $B$ that *also* belong to event $A$.
*   The formula divides the probability of both happening ($P(A \cap B)$) by the probability of the condition happening ($P(B)$) to re-normalize the probability within the new, restricted sample space $B$.

### 4. Example: Using a Contingency Table
*   Consider data on 100 patients regarding a disease (D) and a symptom (S):

    |             | Symptom (S) | No Symptom ($\neg S$) | Total |
    |-------------|-------------|-----------------------|-------|
    | Disease (D) | 15          | 5                     | 20    |
    | No Disease ($\neg D$)| 10          | 70                    | 80    |
    | Total       | 25          | 75                    | 100   |

*   Let's find $P(D|S)$: The probability a patient has the disease given they have the symptom.
    *   $P(D \cap S)$ (Disease and Symptom): $\frac{15}{100} = 0.15$
    *   $P(S)$ (Symptom): $\frac{25}{100} = 0.25$
    *   $P(D|S) = \frac{P(D \cap S)}{P(S)} = \frac{0.15}{0.25} = 0.60$ or 60%.
*   Alternatively, using intuition: Restrict the sample space to the 25 patients with the symptom. Within this group, 15 have the disease. So, $P(D|S) = \frac{15}{25} = 0.60$.

### 5. The Multiplication Rule (derived from the formula)
*   Rearranging the conditional probability formula gives a way to calculate the probability of the intersection of two events:
    $$ P(A \cap B) = P(A|B) P(B) $$
    $$ P(A \cap B) = P(B|A) P(A) $$
*   This is useful for calculating the probability of a sequence of events.

### 6. Chain Rule (Generalization of Multiplication Rule)
*   For a sequence of events $A_1, A_2, ..., A_n$:
    $$ P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) P(A_2|A_1) P(A_3|A_1 \cap A_2) \dots P(A_n|A_1 \cap \dots \cap A_{n-1}) $$
*   **Importance:** Crucial in modeling sequences, like in Natural Language Processing (calculating probability of a sentence) or analyzing sequential processes.

## Connections to Other Topics
*   Leads directly to the concept of [[05_Independence|Independence]] (when $P(A|B) = P(A)$).
*   Forms the basis for [[06_Bayes_Theorem|Bayes' Theorem]], which relates $P(A|B)$ to $P(B|A)$.
*   Used extensively in [[../../06 Machine Learning/02 Supervised/02 Classification/Classification|Classification algorithms]] (e.g., Naive Bayes relies on assumptions about conditional probabilities).
*   Fundamental to understanding [[Markov Chains]].

## Summary
*   Conditional probability $P(A|B)$ is the probability of event A happening, given that event B has already happened.
*   Formula: $P(A|B) = \frac{P(A \cap B)}{P(B)}$.
*   It represents updating probability based on new information by restricting the sample space.
*   The Multiplication Rule ($P(A \cap B) = P(A|B)P(B)$) helps find joint probabilities.
*   The Chain Rule extends this to sequences of events.

## Sources
*   [Khan Academy: Conditional Probability](https://www.khanacademy.org/math/statistics-probability/probability-library/conditional-probability-independence/v/conditional-probability-basic-idea)
*   [Wikipedia: Conditional Probability](https://en.wikipedia.org/wiki/Conditional_probability)
*   [Seeing Theory: Conditional Probability (Interactive)](https://seeing-theory.brown.edu/basic-probability/index.html#section2)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross) - Consult relevant chapters.

## TAGS
[[Probability]] [[Conditional Probability]] [[Bayes Theorem]] [[Independence]] [[Multiplication Rule]] [[Chain Rule]] [[02 Math/index]] [[Statistics]] [[Machine Learning]]