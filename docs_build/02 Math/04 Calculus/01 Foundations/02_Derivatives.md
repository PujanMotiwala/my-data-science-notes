---
tags:
- Calculus
- Derivative
- Foundations
- Gradient Descent
- Limit
- Optimization
- Rate of Change
- Slope
- Tangent Line
---

# Derivatives

## Simple Idea
*   The **derivative** of a function tells you the **instantaneous rate of change** of the function's output with respect to its input.
*   Think of it as the **slope of the line tangent to the function's graph** at a specific point. It tells you how "steep" the function is at that exact point and whether it's increasing or decreasing.
*   If the function represents distance vs. time, the derivative is the instantaneous velocity. If it represents cost vs. quantity, the derivative is the marginal cost.

## Formal Definition
*   The derivative of a function $f(x)$ with respect to $x$ at a point $x = c$, denoted $f'(c)$, $\frac{dy}{dx} |_{x=c}$, or $\frac{d}{dx} f(x) |_{x=c}$, is defined using a [[01_Functions_Limits_Continuity|limit]]:
    $$ f'(c) = \lim_{h \to 0} \frac{f(c+h) - f(c)}{h} $$
*   This formula calculates the slope of the secant line between points $(c, f(c))$ and $(c+h, f(c+h))$ and finds the limit of this slope as the second point gets infinitely close to the first ($h \to 0$), giving the slope of the tangent line.
*   A function must be [[01_Functions_Limits_Continuity|continuous]] at a point to be differentiable there, but continuity does not guarantee differentiability (e.g., sharp corners, cusps).
*   The function $f'(x)$ which gives the derivative at *any* point $x$ is called the derivative function.

## Key Concepts

### 1. Interpretation as Slope
*   $f'(c) > 0$: Function $f$ is increasing at $x = c$.
*   $f'(c) < 0$: Function $f$ is decreasing at $x = c$.
*   $f'(c) = 0$: Function $f$ has a horizontal tangent at $x = c$ (often indicates a local maximum, minimum, or saddle point).

### 2. Interpretation as Rate of Change
*   Measures how sensitive the output $f(x)$ is to small changes in the input $x$. A large absolute value $|f'(c)|$ means the output changes rapidly near $c$; a small value means it changes slowly.

### 3. Notation
*   **Lagrange's notation:** $f'(x)$, $f''(x)$ (second derivative), $f^{(n)}(x)$ (n-th derivative).
*   **Leibniz's notation:** $\frac{dy}{dx}$, $\frac{d^2y}{dx^2}$, $\frac{d^ny}{dx^n}$. Useful for showing what the derivative is taken *with respect to*.

### 4. Higher-Order Derivatives
*   The second derivative, $f''(x)$, is the derivative of the first derivative $f'(x)$. It measures the rate of change of the slope, related to the **concavity** of the function's graph.
    *   $f''(x) > 0$: Concave up (like a cup).
    *   $f''(x) < 0$: Concave down (like a frown).

## Connections to Other Topics & Relevance
*   **[[01_Maxima_and_Minima|Optimization]]:** Finding where the derivative is zero ($f'(x) = 0$) is crucial for locating potential minima or maxima of a function. This is the foundation of optimization algorithms like [[02_Gradient_Descent|Gradient Descent]].
*   **[[02_Gradient_Descent|Gradient Descent]]:** Uses the derivative (or [[03_Gradient|gradient]] in higher dimensions) to determine the direction in which to adjust parameters to minimize a loss function. The derivative tells you which way is "downhill".
*   **[[02_Partial_Derivatives|Partial Derivatives]] & [[03_Gradient|Gradients]]:** Extend the concept of derivatives to functions of multiple variables.
*   **[[04_Chain_Rule|Chain Rule]]:** Essential rule for differentiating composite functions, forming the basis of backpropagation in neural networks.
*   **Taylor Series:** Derivatives are used to construct polynomial approximations of functions (Taylor expansions).

## Summary
*   The **Derivative ($f'(x)$ or $dy/dx$)** measures the **instantaneous rate of change** of a function $f(x)$.
*   Geometrically, it's the **slope of the tangent line** to the graph of $f(x)$.
*   Defined via a [[01_Functions_Limits_Continuity|limit]]: $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$.
*   $f'(x) = 0$ often indicates local optima (max/min).
*   Fundamental tool for **optimization** (like [[02_Gradient_Descent|Gradient Descent]]) and understanding how functions change.

## Sources
*   Any standard Calculus textbook (e.g., Stewart, Thomas, Anton).
*   [Khan Academy: Derivatives introduction](https://www.khanacademy.org/math/calculus-1/cs1-derivatives)
*   [Paul's Online Math Notes: The Definition of the Derivative](https://tutorial.math.lamar.edu/Classes/CalcI/DefnOfDerivative.aspx)
*   [3Blue1Brown: The Essence of Calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) (Excellent visual intuition)