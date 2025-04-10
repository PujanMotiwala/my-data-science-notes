# Types of Probability

## Definition / Introduction
*   While [[01_Definition_and_Terminology|Probability]] quantifies likelihood, the way we arrive at that quantification can differ based on the information available and the nature of the experiment.
*   Understanding these different interpretations helps clarify the meaning and limitations of a stated probability value.
*   There are three main types or interpretations of probability: Theoretical, Empirical, and Subjective.

## Key Concepts

### 1. Theoretical (Classical) Probability
*   **Basis:** Assumes a well-defined experiment where all outcomes in the [[01_Definition_and_Terminology|Sample Space]] $S$ are *equally likely*. Based on logical reasoning and symmetry, not on observed data.
*   **Calculation:** Uses the formula derived from the sample space structure for an event $E$:
    $$ P(E) = \frac{\text{Number of outcomes favorable to event E}}{\text{Total number of possible outcomes in the Sample Space S}} = \frac{|E|}{|S|} $$
*   **When Used:** Primarily for idealized scenarios like fair coins, fair dice, drawing cards from a well-shuffled deck, or situations where symmetry can be strongly assumed.
*   **Example:**
    *   Experiment: Rolling a fair six-sided die. $S=\{1,2,3,4,5,6\}$, $|S|=6$.
    *   Event E: Rolling a number less than 3 ($E = \{1, 2\}$), $|E|=2$.
    *   Calculation: $P(E) = \frac{2}{6} = \frac{1}{3} \approx 0.333$.
*   **Limitation:** Requires the strong assumption of equally likely outcomes, which doesn't hold for many real-world situations (e.g., a biased coin, probability of rain).

### 2. Empirical (Frequentist or Statistical) Probability
*   **Basis:** Relies on observed data from repeating an experiment many times. It's based on the *relative frequency* of an event occurring in the long run.
*   **Calculation:** Let $n(E)$ be the number of times event $E$ occurred in $N$ total trials:
    $$ P(E) \approx \frac{n(E)}{N} = \frac{\text{Number of times event E occurred}}{\text{Total number of times the experiment was performed}} $$
*   **When Used:** For real-world situations where outcomes are not necessarily equally likely, or when the underlying theoretical model is unknown or complex. Examples include estimating the probability of a manufactured item being defective, the likelihood of a user clicking an ad based on past data, or the chance of rain based on historical weather patterns.
*   **Example:**
    *   Experiment: Observing $N=1000$ visitors to a specific webpage version in an [[../../AB Testing/Intro|A/B Test]].
    *   Observation: $n(E)=150$ visitors converted (e.g., made a purchase).
    *   Event E: A visitor converts.
    *   Calculation: $P(E) \approx \frac{150}{1000} = 0.15$ or 15%.
*   **Limitation:** Requires a large number of trials $N$ for the approximation to be reliable (related to the [[../05 Important Theorems/01_Law_of_Large_Numbers_LLN|Law of Large Numbers]]). The probability is an estimate based on past data and might change if the underlying conditions change.

### 3. Subjective Probability
*   **Basis:** Represents an individual's degree of belief or confidence in an event occurring. It's based on personal judgment, experience, intuition, and available (possibly incomplete) evidence.
*   **Calculation:** Not based on a strict formula, but assigned based on belief. However, these probabilities should still adhere to the basic axioms of probability (e.g., be between 0 and 1).
*   **When Used:** For unique events that cannot be repeated under identical conditions, or where objective data is scarce. Examples include the probability of a specific startup succeeding, the likelihood of a particular political candidate winning an election before any polls, or estimating the chance of completing a project by a deadline based on current progress.
*   **Example:**
    *   An experienced engineer might state, "Based on the complexity and the team's current velocity, I believe there's a 70% subjective probability we'll meet the Q3 deadline."
*   **Limitation:** Inherently personal and can vary significantly between individuals. It's harder to objectively verify or test compared to theoretical or empirical probabilities.

## Connections to Other Topics
*   Theoretical probability relies heavily on [[03_Combinatorics|Combinatorics]] for counting outcomes.
*   Empirical probability is closely linked to [[../05 Important Theorems/01_Law_of_Large_Numbers_LLN|Law of Large Numbers]] and is the foundation of [[../02 Inferential statistics/001 Inferential Statistics|Inferential Statistics]].
*   Subjective probability is central to [[../06_Bayes_Theorem|Bayesian statistics]], where prior beliefs are updated with evidence.
*   [[../../AB Testing/Intro|A/B testing]] relies heavily on empirical probability.

## Summary
*   **Theoretical Probability:** Based on symmetry and equally likely outcomes (e.g., fair coin $P(H) = 0.5$). Formula: $\frac{|E|}{|S|}$.
*   **Empirical Probability:** Based on observed frequencies from repeated trials (e.g., conversion rate from data). Formula: $\approx \frac{n(E)}{N}$.
*   **Subjective Probability:** Based on personal belief and judgment (e.g., confidence in project completion).
*   The appropriate type depends on the nature of the problem and available information.

## Sources
*   [Wikipedia: Probability Interpretations](https://en.wikipedia.org/wiki/Probability_interpretations)
*   [Stanford Encyclopedia of Philosophy: Interpretations of Probability](https://plato.stanford.edu/entries/probability-interpret/)
*   [Statistics How To: Theoretical Probability](https://www.statisticshowto.com/probability-and-statistics/theoretical-probability/)
*   [Investopedia: Empirical Probability](https://www.investopedia.com/terms/e/empiricalprobability.asp)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross) - Consult relevant chapters.

## TAGS
[[Probability]] [[Interpretations]] [[Theoretical Probability]] [[Empirical Probability]] [[Subjective Probability]] [[Frequentist]] [[Bayesian]] [[02 Math/index]] [[Statistics]]