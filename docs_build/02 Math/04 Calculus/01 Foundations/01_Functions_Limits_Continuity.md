---
tags:
- Calculus
- Continuity
- Foundations
- Function
- Limit
---

# Functions, Limits, and Continuity

## Simple Idea
*   **Function:** Think of a function like a recipe or a machine: you put something in (input $x$), and it gives you something specific out (output $y$ or $f(x)$). For each valid input, there's exactly one output.
*   **Limit:** A limit explores what happens to the function's output as the input gets *extremely close* to a particular value, without necessarily reaching it. It's about the *approaching* behavior or the trend near a point.
*   **Continuity:** A function is continuous if you can draw its graph without lifting your pen. There are no sudden jumps, breaks, or holes in the graph. Limits are essential for defining continuity.

## Formal Definitions

### 1. Function
*   A **function** $f$ from a set $A$ (the **domain**) to a set $B$ (the **codomain**) is a rule that assigns to each element $x \in A$ exactly one element $y \in B$. We write $y = f(x)$.
*   The **range** of the function is the subset of $B$ containing all actual output values $f(x)$.

### 2. Limit
*   Let $f(x)$ be a function defined near $x = c$ (but not necessarily at $x = c$). The **limit** of $f(x)$ as $x$ approaches $c$ is $L$, written as:
    $$ \lim_{x \to c} f(x) = L $$
    if the values of $f(x)$ can be made arbitrarily close to $L$ by taking $x$ sufficiently close to $c$ (but not equal to $c$).
*   This requires the limit from the left ($\lim_{x \to c^-} f(x)$) and the limit from the right ($\lim_{x \to c^+} f(x)$) to both exist and be equal to $L$.

### 3. Continuity
*   A function $f$ is **continuous** at a point $x = c$ if three conditions are met:
    1.  $f(c)$ is defined (the function exists at $c$).
    2.  $\lim_{x \to c} f(x)$ exists (the limit exists at $c$).
    3.  $\lim_{x \to c} f(x) = f(c)$ (the limit value equals the function's value).
*   A function is continuous on an interval if it is continuous at every point in that interval.

## Key Concepts & Relevance

*   **Functions in DS/AI:** Models are essentially complex functions mapping inputs (features) to outputs (predictions). Loss functions map model parameters to an error value. Activation functions introduce non-linearities.
*   **Limits Foundation:** Limits are the theoretical underpinning for [[02_Derivatives|Derivatives]] and [[01_Definite_and_Indefinite_Integrals|Integrals]], the two main branches of calculus. Understanding the concept of "approaching" is key.
*   **Continuity Importance:** Many theorems and algorithms in calculus and optimization (like finding minima/maxima using [[02_Derivatives|derivatives]]) assume the function is continuous and/or differentiable (which requires continuity). Smooth, predictable behavior is often desired. Discontinuities can cause problems for algorithms like [[02_Gradient_Descent|Gradient Descent]].

## Connections to Other Topics
*   Prerequisite for understanding [[02_Derivatives|Derivatives]] (defined as a limit of a difference quotient).
*   Prerequisite for understanding [[01_Definite_and_Indefinite_Integrals|Integrals]] (defined as a limit of Riemann sums).
*   Types of functions (linear, polynomial, exponential, logarithmic) are fundamental building blocks in modeling.

## Summary
*   **Function:** Maps each input $x$ from a domain to exactly one output $f(x)$.
*   **Limit:** Describes the value $f(x)$ approaches as $x$ gets arbitrarily close to a point $c$. ($\lim_{x \to c} f(x) = L$).
*   **Continuity:** A function is continuous at $c$ if it's defined at $c$, its limit exists at $c$, and the limit equals the function value ($\lim_{x \to c} f(x) = f(c)$). Graph has no breaks.
*   These concepts form the bedrock upon which calculus (derivatives and integrals) is built.

## Sources
*   Any standard Calculus textbook (e.g., Stewart, Thomas, Anton).
*   [Khan Academy: Limits and Continuity](https://www.khanacademy.org/math/calculus-1/cs1-limits-and-continuity)
*   [Paul's Online Math Notes: Limits, Continuity](https://tutorial.math.lamar.edu/Classes/CalcI/LimitsIntro.aspx), ([https://tutorial.math.lamar.edu/Classes/CalcI/Continuity.aspx](https://tutorial.math.lamar.edu/Classes/CalcI/Continuity.aspx))