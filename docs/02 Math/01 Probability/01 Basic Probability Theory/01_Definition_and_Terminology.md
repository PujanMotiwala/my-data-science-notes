---
tags:
  - Probability
  - Foundations
  - Terminology
  - Math/index
  - Statistics
  - Core
  - Concept
---
# Basic Probability: Definitions and Terminology

## Definition / Introduction
*   Probability theory is the mathematical framework for quantifying uncertainty and the likelihood of events. It provides a precise language to reason about randomness.
*   Understanding these core terms is essential because they form the building blocks for analyzing data, building statistical models, interpreting [[Hypothesis testing|Hypothesis Tests]], and understanding algorithms in [[ML model|Machine Learning]] and AI.
*   This section covers the fundamental vocabulary. We will primarily discuss *theoretical probability* (based on models like fair coins or dice), but these terms also apply to *empirical probability* (based on observed data frequencies), which we'll explore later.

## Key Concepts

### 1. Experiment
*   **Definition:** Any process or action with an uncertain outcome that can be observed and repeated (at least conceptually). The set of potential outcomes is well-defined.
*   **Purpose:** Defines the specific scenario we are analyzing.
*   **Examples:**
    *   Flipping a fair coin.
    *   Rolling a standard six-sided die.
    *   Measuring the response time of a web server.
    *   Running an A/B test for a website button (observing one user's action).

### 2. Outcome
*   **Definition:** A single, specific possible result of an experiment. Outcomes are mutually exclusive (only one can occur per trial) and exhaustive (they cover all possibilities).
*   **Examples (corresponding to above):**
    *   Getting "Tails".
    *   Rolling a "6".
    *   A response time of "85 milliseconds".
    *   The user "Clicks" the button in the A/B test.

### 3. Sample Space ($\Omega$ or $S$)
*   **Definition:** The set containing *all possible* distinct outcomes of an experiment.
*   **Representation:** Usually denoted with $S = \{\text{outcome1}, \text{outcome2}, ...\}$.
*   **Purpose:** Defines the universe of possibilities for the experiment.
*   **Examples:**
    *   Experiment: Flipping one coin. Sample Space: $S = \{\text{Heads, Tails}\}$ or $S = \{H, T\}$
    *   Experiment: Rolling one die. Sample Space: $S = \{1, 2, 3, 4, 5, 6\}$
    *   Experiment: A/B test button click. Sample Space: $S = \{\text{Click, No Click}\}$
    *   Experiment: Flipping two coins. Sample Space: $S = \{HH, HT, TH, TT\}$

### 4. Event ($E, A, B, ...$)
*   **Definition:** A specific subset of the sample space; a collection of one or more outcomes that we might be interested in.
*   **Purpose:** Defines the specific result or set of results whose likelihood we want to measure.
*   **Types:**
    *   **Simple Event:** Contains exactly one outcome (e.g., rolling a 3: $\{3\}$).
    *   **Compound Event:** Contains more than one outcome (e.g., rolling an odd number: $\{1, 3, 5\}$).
*   **Examples:**
    *   Experiment: Rolling one die ($S = \{1, 2, 3, 4, 5, 6\}$)
        *   Event A: Rolling an even number. $A = \{2, 4, 6\}$
        *   Event B: Rolling a number greater than 4. $B = \{5, 6\}$
        *   Event C: Rolling a 3. $C = \{3\}$ (Simple event)
    *   Experiment: Flipping two coins ($S = \{HH, HT, TH, TT\}$)
        *   Event D: Getting exactly one Head. $D = \{HT, TH\}$

### 5. Probability Measure ($P$)
*   **Definition:** A function $P$ that assigns a numerical value between 0 and 1 (inclusive) to each event $E$ in the sample space, representing the likelihood of that event occurring. $P(E)$ denotes the probability of event E.
*   **Scale:**
    *   $P(E) = 0$: Event $E$ is impossible.
    *   $P(E) = 1$: Event $E$ is certain.
    *   $0 < P(E) < 1$: Event $E$ has some chance of occurring.
*   **Basic Rules (Axioms of Probability):**
    *   **Non-negativity:** For any event E, $P(E) \ge 0$.
    *   **Normalization:** The probability of the entire sample space S is 1: $P(S) = 1$. (Something *must* happen).
    *   **Additivity for Mutually Exclusive Events:** Events are **mutually exclusive** if they cannot occur at the same time (their intersection is empty, $A \cap B = \emptyset$; e.g., rolling a 1 and rolling a 6 on a single roll). If events $A$ and $B$ are mutually exclusive, then the probability that *either* $A$ or $B$ occurs is $P(A \cup B) = P(A) + P(B)$.
        *   *Contrast:* Rolling an even number ($A = \{2, 4, 6\}$) and rolling a number greater than 4 ($B = \{5, 6\}$) are *not* mutually exclusive because the outcome '6' is in both events ($A \cap B = \{6\}$). The simple addition rule does not directly apply here.

### Bridging to Calculation
*   In many simple experiments where all individual outcomes in the sample space are considered **equally likely** (like a fair coin or a fair die), the theoretical probability of an event E is calculated as:
    $$ P(E) = \frac{\text{Number of outcomes in event E}}{\text{Total number of outcomes in the Sample Space S}} $$
*   Example: For a fair die, $P(\text{Rolling an even number}) = P(\{2, 4, 6\}) = \frac{3}{6} = 0.5$.

## Connections to Other Topics
*   These terms are fundamental for [[02_Types_of_Probability|Types of Probability]], [[04_Conditional_Probability|Conditional Probability]], and [[06_Bayes_Theorem|Bayes' Theorem]].
*   Understanding sample spaces and events is key to defining [[02 Math/03 Linear Algebra/05 Norms/01_Definition|Random Variables]] and their [[02_Probability_Mass_Function_PMF|Probability Mass Functions (PMF)]] or [[03_Probability_Density_Function_PDF|Probability Density Functions (PDF)]].
*   Essential for framing questions in [[Hypothesis testing|Hypothesis Testing]].

## Summary
*   Probability provides a language for uncertainty.
*   **Experiment:** Process with uncertain outcomes.
*   **Outcome:** A single possible result.
*   **Sample Space ($S$):** Set of all possible outcomes.
*   **Event ($E$):** A subset of outcomes we're interested in.
*   **Probability ($P(E)$):** A number $[0, 1]$ indicating an event's likelihood.
*   Key axioms ensure probabilities are consistent (non-negative, sum to 1 for the sample space, additive for mutually exclusive events).
*   For equally likely outcomes, $P(E) = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}}$.

## Sources
*   [Khan Academy: Probability Basics](https://www.khanacademy.org/math/statistics-probability/probability-library)
*   [Stat Trek: Probability Definitions](https://stattrek.com/probability/probability-definitions)
*   [Seeing Theory: Basic Probability (Interactive)](https://seeing-theory.brown.edu/basic-probability/index.html#section1)
*   [LibreTexts Statistics: Basic Concepts of Probability](https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_(OpenStax)/03%3A_Probability_Topics/3.01%3A_Terminology)
*   Primary Textbooks: (e.g., "Probability and Statistics for Engineers and Scientists" by Walpole et al.; "A First Course in Probability" by Sheldon Ross)