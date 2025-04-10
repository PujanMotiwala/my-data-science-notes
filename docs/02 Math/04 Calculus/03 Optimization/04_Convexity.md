# Convexity in Optimization

## Simple Idea
*   **Convex Function:** Think of a function whose graph looks like a **bowl shape**. If you pick any two points on the graph, the straight line segment connecting them lies *entirely above or on* the graph itself. There are no "dips" or "bumps" going upwards within the bowl.
*   **Convex Set:** A set of points where, if you pick any two points in the set, the straight line segment connecting them lies *entirely within* the set. There are no "holes" or "indentations".
*   **Why it Matters:** For convex functions defined on convex sets, optimization is much simpler: **any local minimum found is guaranteed to be the global minimum**. [[02_Gradient_Descent|Gradient Descent]] (and other methods) won't get stuck in a suboptimal valley.

## Formal Definitions

### 1. Convex Set
*   A set $S$ in $\mathbb{R}^n$ is **convex** if for any two points $\mathbf{x}, \mathbf{y} \in S$, the line segment connecting them is also entirely in $S$.
*   Mathematically: For any $\mathbf{x}, \mathbf{y} \in S$ and any $\theta$ with $0 \le \theta \le 1$:
    $$ \theta \mathbf{x} + (1-\theta) \mathbf{y} \in S $$

### 2. Convex Function
*   A real-valued function $f$ defined on a convex set $S$ is **convex** if for any two points $\mathbf{x}, \mathbf{y} \in S$ and any $\theta$ with $0 \le \theta \le 1$:
    $$ f(\theta \mathbf{x} + (1-\theta) \mathbf{y}) \le \theta f(\mathbf{x}) + (1-\theta) f(\mathbf{y}) $$
*   **Geometric Interpretation:** The function's graph lies below or on the line segment (chord) connecting any two points on the graph.
*   **Strictly Convex:** The inequality is strict (`<`) for $0 < \theta < 1$ and $\mathbf{x} \neq \mathbf{y}$. A strictly convex function has a unique global minimum (if one exists).

### 3. Concave Function
*   A function $f$ is **concave** if $-f$ is convex. The graph looks like an inverted bowl, and the line segment connecting two points lies *below or on* the graph.
    $$ f(\theta \mathbf{x} + (1-\theta) \mathbf{y}) \ge \theta f(\mathbf{x}) + (1-\theta) f(\mathbf{y}) $$

## Key Concepts & Properties

### 1. Identifying Convex Functions (Tests)
*   **First Derivative Condition (for differentiable $f$):** $f$ is convex iff its domain is convex and for all $\mathbf{x}, \mathbf{y}$ in the domain:
    $$ f(\mathbf{y}) \ge f(\mathbf{x}) + \nabla f(\mathbf{x})^T (\mathbf{y} - \mathbf{x}) $$
    (The function lies above its tangent lines/planes).
*   **Second Derivative Condition (for twice differentiable $f$):**
    *   Single Variable: $f$ is convex iff $f''(x) \ge 0$ for all $x$.
    *   Multiple Variables: $f$ is convex iff its **[[01_Hessian_Matrix|Hessian matrix]]** $\nabla^2 f(\mathbf{x})$ is **positive semidefinite** for all $\mathbf{x}$. (Positive semidefinite means $\mathbf{v}^T \mathbf{H} \mathbf{v} \ge 0$ for all vectors $\mathbf{v}$).

### 2. Importance in Optimization
*   **Global Optimality:** For a convex function $f$ defined on a convex set $S$, any point $\mathbf{x}^*$ where $\nabla f(\mathbf{x}^*) = \mathbf{0}$ (a critical point) is a **global minimum**.
*   **Convergence Guarantee:** Algorithms like [[02_Gradient_Descent|Gradient Descent]] are guaranteed to converge to the global minimum for convex functions (with appropriate [[02_Gradient_Descent|learning rate]]).
*   **Non-Convex Challenges:** Most [[../../07 Deep Learning/01 Foundational Models/Neural Networks/01 The Basics/01_Introduction|Deep Learning]] loss landscapes are **non-convex**, meaning they have many local minima and saddle points. This makes optimization much harder, and algorithms like GD only guarantee finding a local minimum, which might depend on initialization.

*(Visual Idea: Excalidraw showing a convex function (one valley) vs a non-convex function (multiple valleys, bumps). Show GD finding global min on convex, potentially getting stuck in local min on non-convex).*

### 3. Examples of Convex Functions
*   Linear functions: $f(\mathbf{x}) = \mathbf{a}^T \mathbf{x} + b$.
*   Affine functions (same as linear).
*   Quadratic functions: $f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^T \mathbf{A} \mathbf{x} + \mathbf{b}^T \mathbf{x} + c$, if matrix **A** is positive semidefinite.
*   Norms: Any [[../05 Norms/01_Definition|norm]] (e.g., [[../05 Norms/02_L1_Norm_Manhattan|L1]], [[../05 Norms/03_L2_Norm_Euclidean|L2]]) is a convex function.
*   Negative Logarithm: $f(x) = -\log x$ (for $x>0$).
*   Log-sum-exp: $f(\mathbf{x}) = \log(\sum_i e^{x_i})$.

## Connections to Other Topics & Relevance
*   **[[02_Gradient_Descent|Gradient Descent]] & Optimization Theory:** Explains why GD works perfectly for some problems (like [[../../06 Machine Learning/02 Supervised/01 Regression/01_Simple Linear Regression/Linear Regression|Linear Regression]] with MSE loss, [[../../06 Machine Learning/01 The Basics/02_Model Evaluation/Test metrics/Regularization/Ridge Regression|Ridge Regression]], [[../../06 Machine Learning/02 Supervised/02 Classification/02_Logistic Regression/Logistic Regression|Logistic Regression]], SVMs) which have convex loss functions, but faces challenges in Deep Learning.
*   **Linear Programming & Convex Optimization:** A whole field dedicated to efficiently solving optimization problems involving convex functions and sets.
*   **[[01_Hessian_Matrix|Hessian Matrix]]:** Used to test for convexity (positive semidefiniteness).

## Summary
*   **Convex Function:** Bowl-shaped graph; line segment between two graph points lies above or on the graph.
*   **Convex Set:** Line segment between any two points in the set stays within the set.
*   **Key Property:** For convex functions, **any local minimum is a global minimum**.
*   Tested using first derivative condition or second derivative condition ([[01_Hessian_Matrix|Hessian]] positive semidefinite).
*   Guarantees [[02_Gradient_Descent|Gradient Descent]] finds the global optimum. Most Deep Learning problems are non-convex.

## Sources
*   *Convex Optimization* by Boyd and Vandenberghe (Standard reference, advanced but comprehensive - available online free) ([https://web.stanford.edu/~boyd/cvxbook/](https://web.stanford.edu/~boyd/cvxbook/))
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 4 discusses convexity in optimization) ([https://www.deeplearningbook.org/](https://www.deeplearningbook.org/))
*   [Wikipedia: Convex function](https://en.wikipedia.org/wiki/Convex_function)
*   [Brief Introduction to Convex Optimization](https://www.cs.cmu.edu/~ggordon/10725-F12/slides/05-convexity.pdf) (Lecture slides often provide good summaries)

## TAGS
[[Calculus]] [[Optimization]] [[Convexity]] [[Convex Function]] [[Convex Set]] [[Global Minimum]] [[Local Minimum]] [[Gradient Descent]] [[Hessian Matrix]] [[02 Math/index]] [[Foundations]] [[Machine Learning]]