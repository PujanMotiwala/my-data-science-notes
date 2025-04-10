# Combinatorics: Counting Techniques

## Definition / Introduction
*   Combinatorics is the branch of mathematics concerned with counting arrangements and combinations of objects.
*   In probability, it's crucial for determining the size of [[01_Definition_and_Terminology|Sample Spaces]] and Events, especially when dealing with [[02_Types_of_Probability|Theoretical Probability]] where outcomes are equally likely.
*   The two fundamental concepts are permutations (where order matters) and combinations (where order does not matter).

## Key Concepts

### 1. Factorial (!)
*   **Definition:** The factorial of a non-negative integer $n$, denoted by $n!$, is the product of all positive integers less than or equal to $n$.
*   **Formula:** $n! = n \times (n-1) \times (n-2) \times \dots \times 3 \times 2 \times 1$
*   **Special Case:** $0! = 1$ (by definition, related to the empty product).
*   **Purpose:** Used as a building block in permutation and combination formulas.
*   **Example:** $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$.

### 2. Permutation (Order Matters)
*   **Definition:** An arrangement of objects in a specific order. It counts the number of ways to choose and arrange $k$ objects from a set of $n$ distinct objects.
*   **Notation:** $P(n, k)$, ${}_n P_k$, or $P^n_k$.
*   **Formula:**
    $$ P(n, k) = \frac{n!}{(n-k)!} $$
*   **Intuition:** For the first position, you have $n$ choices. For the second, $n-1$ choices remain, ..., down to $n-k+1$ choices for the k-th position. $n \times (n-1) \times \dots \times (n-k+1)$.
*   **When Used:** When the sequence or order of selection is important.
*   **Examples:**
    *   How many ways can you arrange 3 books (A, B, C) on a shelf? (Here $n=3, k=3$)
        $P(3, 3) = \frac{3!}{(3-3)!} = \frac{3!}{0!} = \frac{6}{1} = 6$. The arrangements are ABC, ACB, BAC, BCA, CAB, CBA.
    *   How many ways can 3 horses finish 1st and 2nd in a race with 8 horses? (Here $n=8, k=2$)
        $P(8, 2) = \frac{8!}{(8-2)!} = \frac{8!}{6!} = \frac{8 \times 7 \times 6!}{6!} = 8 \times 7 = 56$.

### 3. Combination (Order Does NOT Matter)
*   **Definition:** A selection of objects where the order of selection is irrelevant. It counts the number of ways to choose $k$ objects from a set of $n$ distinct objects, without regard to the order.
*   **Notation:** $C(n, k)$, ${}_n C_k$, $\binom{n}{k}$ (read as "n choose k"). This is also known as the Binomial Coefficient.
*   **Formula:**
    $$ C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!} $$
*   **Intuition:** First find the number of permutations $P(n, k)$. Since order doesn't matter, divide by the number of ways to arrange the chosen $k$ objects ($k!$). $C(n, k) = P(n, k) / k!$.
*   **When Used:** When only the composition of the group matters, not the sequence of selection.
*   **Examples:**
    *   How many ways can you choose a committee of 3 people from a group of 5? (Here $n=5, k=3$)
        $C(5, 3) = \binom{5}{3} = \frac{5!}{3!(5-3)!} = \frac{5!}{3! 2!} = \frac{5 \times 4 \times 3!}{3! (2 \times 1)} = \frac{5 \times 4}{2} = 10$.
    *   How many different 5-card hands can be dealt from a standard 52-card deck? (Here $n=52, k=5$)
        $C(52, 5) = \binom{52}{5} = \frac{52!}{5! 47!} = \frac{52 \times 51 \times 50 \times 49 \times 48}{5 \times 4 \times 3 \times 2 \times 1} = 2,598,960$.

### Variations (Brief Mention)
*   **Permutations with Repetition:** Number of ways to arrange $n$ objects where there are $n_1$ identical objects of type 1, $n_2$ of type 2, ..., $n_k$ of type k. Formula: $\frac{n!}{n_1! n_2! \dots n_k!}$. (Example: Arrangements of letters in "MISSISSIPPI").
*   **Combinations with Repetition:** Number of ways to choose $k$ items from $n$ types where repetition is allowed (e.g., choosing scoops of ice cream). Formula: $C(n+k-1, k) = \binom{n+k-1}{k}$.

## Connections to Other Topics
*   Essential for calculating [[02_Types_of_Probability|Theoretical Probabilities]].
*   The Binomial Coefficient $\binom{n}{k}$ is fundamental to the [[../03 Common Probability Distributions/02_Binomial_Distribution|Binomial Distribution]].
*   Used in sampling techniques in [[../02 Inferential statistics/001 Inferential Statistics|Statistics]].
*   Relevant in analyzing algorithm complexity (e.g., number of pairs).

## Summary
*   Combinatorics provides tools for counting arrangements and selections.
*   **Factorial ($n!$)** is a basic building block.
*   **Permutations ($P(n, k)$):** Order matters. Formula: $\frac{n!}{(n-k)!}$.
*   **Combinations ($C(n, k)$ or $\binom{n}{k}$):** Order does NOT matter. Formula: $\frac{n!}{k!(n-k)!}$.
*   Knowing whether order matters is key to choosing the correct technique.

## Sources
*   [Khan Academy: Combinatorics](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:prob-comb)
*   [Math is Fun: Combinations and Permutations](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)
*   [Brilliant.org: Combinatorics](https://brilliant.org/wiki/combinatorics/)
*   (Introductory Discrete Mathematics or Probability textbooks)

## TAGS
[[Probability]] [[Combinatorics]] [[Counting]] [[Permutation]] [[Combination]] [[Factorial]] [[Binomial Coefficient]] [[Math]] [[Statistics]]