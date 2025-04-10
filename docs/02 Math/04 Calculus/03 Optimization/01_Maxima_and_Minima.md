# Maxima and Minima (Optimization Basics)

## Simple Idea
*   Finding maxima (peaks) and minima (valleys) of functions is a core task in optimization. Calculus gives us tools to find these points.
*   **Single Variable:** Think about finding the highest or lowest point on a curve $y=f(x)$. At these points, the slope ([[../01 Foundations/02_Derivatives|derivative]]) is usually zero (the tangent line is horizontal).
*   **Multiple Variables:** Think about finding peaks or valley bottoms on a surface $z=f(x, y)$. At these points, the "ground" is flat in *all* directions, meaning all [[../02 Multivariable Calculus/02_Partial_Derivatives|partial derivatives]] (and thus the [[../02 Multivariable Calculus/03_Gradient|gradient]]) must be zero.

## Formal Definitions

### 1. Local vs. Global Extrema
*   **Local Maximum:** A point $c$ where $f(c) \ge f(x)$ for all $x$ in some open interval *around* $c$. It's a peak in its immediate neighborhood.
*   **Local Minimum:** A point $c$ where $f(c) \le f(x)$ for all $x$ in some open interval *around* $c$. It's a valley bottom in its immediate neighborhood.
*   **Global Maximum:** A point $c$ where $f(c) \ge f(x)$ for *all* $x$ in the function's entire domain. The absolute highest point.
*   **Global Minimum:** A point $c$ where $f(c) \le f(x)$ for *all* $x$ in the function's entire domain. The absolute lowest point.
*   **Extrema:** Collective term for maxima and minima.

### 2. Critical Points
*   **Single Variable:** A point $c$ in the domain of $f$ is a **critical point** if either $f'(c) = 0$ or $f'(c)$ does not exist.
*   **Multiple Variables:** A point $\mathbf{a}$ in the domain of $f$ is a **critical point** if either $\nabla f(\mathbf{a}) = \mathbf{0}$ (the zero vector, meaning *all* partial derivatives are zero) or if $\nabla f(\mathbf{a})$ does not exist.
*   **Fermat's Theorem (for local extrema):** If $f$ has a local maximum or minimum at an interior point $c$ (or $\mathbf{a}$) and the derivative (or gradient) exists there, then $f'(c) = 0$ (or $\nabla f(\mathbf{a}) = \mathbf{0}$).
*   **Important:** The condition $f'(c)=0$ or $\nabla f(\mathbf{a})=\mathbf{0}$ is *necessary* for a local extremum (if the derivative/gradient exists), but it is *not sufficient*. Points where the derivative/gradient is zero could also be **saddle points**.

## Key Concepts: Finding and Classifying Extrema

### 1. First Derivative Test (Single Variable)
*   Find critical points (where $f'(x)=0$ or DNE).
*   Check the sign of $f'(x)$ on either side of a critical point $c$:
    *   If $f'$ changes from + to - at $c$: Local maximum.
    *   If $f'$ changes from - to + at $c$: Local minimum.
    *   If $f'$ does not change sign: Neither (possibly saddle point or inflection).

### 2. Second Derivative Test (Single Variable)
*   Find critical points where $f'(c)=0$.
*   Evaluate the second derivative $f''(c)$:
    *   If $f''(c) > 0$: $f$ is concave up, so $c$ is a local minimum.
    *   If $f''(c) < 0$: $f$ is concave down, so $c$ is a local maximum.
    *   If $f''(c) = 0$: The test is inconclusive.

### 3. Second Derivative Test (Multiple Variables - using Hessian)
*   Find critical points where $\nabla f(\mathbf{a}) = \mathbf{0}$.
*   Compute the **[[../04 Advanced Topics/01_Hessian_Matrix|Hessian matrix]]** $\mathbf{H}(\mathbf{a})$, the matrix of second partial derivatives evaluated at $\mathbf{a}$.
*   Calculate the [[../03 Linear Algebra/03 Matrix Properties and Concepts/03_Determinant|determinant]] of the Hessian, $D = \det(\mathbf{H}(\mathbf{a}))$. Let $f_{xx} = \partial^2 f / \partial x^2$ evaluated at $\mathbf{a}$.
    *   If $D > 0$ and $f_{xx}(\mathbf{a}) > 0$: Local minimum. (Hessian is positive definite).
    *   If $D > 0$ and $f_{xx}(\mathbf{a}) < 0$: Local maximum. (Hessian is negative definite).
    *   If $D < 0$: Saddle point. (Hessian is indefinite).
    *   If $D = 0$: The test is inconclusive.

### 4. Finding Global Extrema (on a closed interval/region)
*   Find all critical points inside the interval/region.
*   Evaluate the function $f$ at these critical points.
*   Evaluate the function $f$ at the boundaries of the interval/region.
*   The largest value found is the global maximum; the smallest is the global minimum.

## Connections to Other Topics & Relevance
*   **[[02_Gradient_Descent|Gradient Descent]] & Optimization Algorithms:** These algorithms aim to find minima (usually local minima) of loss functions by iteratively moving towards points where the [[../02 Multivariable Calculus/03_Gradient|gradient]] is zero.
*   **Model Training:** Finding the optimal parameters for a machine learning model involves minimizing a loss function, i.e., finding its minimum value.
*   **Maximum Likelihood Estimation (MLE):** A statistical method that finds parameter values maximizing the likelihood function (finding a maximum).
*   **[[04_Convexity|Convex Functions]]:** For convex functions, any local minimum is also a global minimum, which significantly simplifies optimization.

## Summary
*   **Extrema** are maximum or minimum values of a function.
*   **Local Extrema** occur at **critical points** where the [[../01 Foundations/02_Derivatives|derivative]] $f'(x)=0$ (single var) or the [[../02 Multivariable Calculus/03_Gradient|gradient]] $\nabla f(\mathbf{a})=\mathbf{0}$ (multi var), or where they don't exist.
*   **First/Second Derivative Tests** (single var) or the **Second Derivative Test using the [[../04 Advanced Topics/01_Hessian_Matrix|Hessian Matrix]]** (multi var) help classify critical points as local maxima, minima, or saddle points.
*   Finding extrema is the core goal of **optimization**.

## Sources
*   Any standard Calculus textbook (e.g., Stewart, Thomas, Anton).
*   [Khan Academy: Critical points, Minima & Maxima](https://www.khanacademy.org/math/calculus-1/cs1-applications-of-derivatives/cs1-critical-points-and-extrema/v/minima-maxima-and-critical-points) (Single Var), [Second derivative test](https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/optimizing-multivariable-functions/v/second-derivative-test) (Multi Var)
*   [Paul's Online Math Notes: Finding Absolute Extrema](https://tutorial.math.lamar.edu/Classes/CalcI/AbsExtrema.aspx), [Absolute Minima and Maxima (Multivariable)](https://tutorial.math.lamar.edu/Classes/CalcIII/AbsMinMax.aspx)

## TAGS
[[Calculus]] [[Optimization]] [[Maxima]] [[Minima]] [[Extrema]] [[Critical Point]] [[Derivative]] [[Gradient]] [[Hessian Matrix]] [[Second Derivative Test]] [[02 Math/index]] [[Foundations]] [[Machine Learning]]