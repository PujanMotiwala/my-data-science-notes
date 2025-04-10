---
tags:
- Calculus
- Deep Learning
- Foundations
- Gradient
- Gradient Descent
- Learning Rate
- Local Minimum
- Loss Function
- Machine Learning
- Optimization
---

# Gradient Descent

## Simple Idea
*   Gradient Descent is an algorithm used to find a **local minimum** of a function (typically a [[01_Functions_of_Multiple_Variables|multivariable function]] like a machine learning loss function).
*   Imagine you are blindfolded on a hilly terrain (the loss surface) and want to reach the bottom of a valley. The strategy is:
    1.  Feel the slope under your feet (calculate the [[03_Gradient|Gradient]]). The gradient tells you the direction of steepest *uphill*.
    2.  Take a small step in the exact *opposite* direction (downhill).
    3.  Repeat steps 1 and 2 until you reach a point where the ground feels flat (gradient is close to zero), hoping it's a valley bottom (a local minimum).

## Formal Definition
*   Gradient Descent is an iterative **optimization algorithm** for finding a local minimum of a differentiable function $f(\mathbf{w})$, often representing a loss or cost function where $\mathbf{w}$ is a vector of parameters (e.g., model weights).
*   It updates the parameters $\mathbf{w}$ in the opposite direction of the [[03_Gradient|gradient]] $\nabla f(\mathbf{w})$ at the current point.

## The Algorithm

1.  **Initialization:** Start with an initial guess for the parameters $\mathbf{w}_0$. Choose a **learning rate** $\eta$ (eta), which is a small positive scalar. Set iteration counter $t = 0$.
2.  **Iteration:** Repeat until convergence (e.g., gradient is very small, or changes in $\mathbf{w}$ are minimal):
    a.  **Compute Gradient:** Calculate the gradient of the function $f$ evaluated at the current parameters $\mathbf{w}_t$: $\nabla f(\mathbf{w}_t)$.
    b.  **Update Parameters:** Update the parameters by taking a step proportional to the negative gradient:
        $$ \mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla f(\mathbf{w}_t) $$
    c.  Increment counter: $t = t + 1$.
3.  **Output:** The final parameters $\mathbf{w}_{t}$ are an approximation of a local minimum.

## Key Concepts

### 1. Gradient ($\nabla f$)
*   As calculated using [[02_Partial_Derivatives|partial derivatives]], the gradient $\nabla f(\mathbf{w}_t)$ provides the direction of steepest *increase* of the function $f$ at the current parameter values $\mathbf{w}_t$.

### 2. Negative Gradient ($-\nabla f$)
*   By moving in the direction *opposite* to the gradient, we ensure that we are locally decreasing the function value (moving downhill).

### 3. Learning Rate ($\eta$)
*   **Role:** Controls the **size of the step** taken in each iteration.
*   **Choosing $\eta$:** This is a critical hyperparameter.
    *   **Too small $\eta$:** Convergence will be very slow.
    *   **Too large $\eta$:** The algorithm might overshoot the minimum, oscillate wildly, or even diverge (function value increases).
    *(Visual Idea: Excalidraw showing contour plot with GD steps. One with small eta (slow), one with large eta (overshooting/diverging), one with good eta).*
*   Often requires tuning. Adaptive learning rate methods ([[03_Gradient_Descent_Variants|variants like Adam, RMSprop]]) adjust $\eta$ automatically during training.

### 4. Convergence
*   The algorithm ideally stops when it reaches a point where $\nabla f(\mathbf{w}) \approx \mathbf{0}$, indicating a flat region (potential local minimum, maximum, or saddle point). In practice, convergence is often determined by:
    *   The magnitude of the gradient $||\nabla f(\mathbf{w}_t)||$ falling below a small threshold.
    *   The change in parameters $||\mathbf{w}_{t+1} - \mathbf{w}_t||$ or the change in the function value $|f(\mathbf{w}_{t+1}) - f(\mathbf{w}_t)|$ being very small.
    *   Reaching a maximum number of iterations.

### 5. Local vs. Global Minima
*   Gradient Descent **guarantees convergence to a local minimum** (or saddle point) for typical functions used in ML.
*   It does **not** guarantee finding the **global minimum** if the function is non-convex (has multiple valleys). The minimum found depends heavily on the starting point $\mathbf{w}_0$.
*   For [[04_Convexity|convex functions]], the local minimum *is* the global minimum, so GD finds the optimal solution.

## Connections to Other Topics & Relevance
*   **Core Training Algorithm:** The most fundamental optimization algorithm used to train the vast majority of [[../../06 Machine Learning/ML model|Machine Learning]] and [[../../07 Deep Learning/01 Foundational Models/Neural Networks/01 The Basics/01_Introduction|Deep Learning]] models by minimizing their loss functions.
*   **Backpropagation:** In neural networks, backpropagation is the algorithm used to efficiently *compute* the gradient $\nabla f(\mathbf{w}_t)$ needed for the Gradient Descent update step.
*   **[[03_Gradient_Descent_Variants|Variants (SGD, Mini-batch, Adam etc.)]]:** Address limitations of basic GD (speed, convergence issues) and are standard practice.
*   Requires concepts of [[01_Functions_of_Multiple_Variables|multivariable functions]], [[02_Partial_Derivatives|partial derivatives]], and the [[03_Gradient|gradient]].

## Summary
*   **Gradient Descent** is an iterative algorithm to find a **local minimum** of a function $f(\mathbf{w})$.
*   It repeatedly takes steps **opposite** to the direction of the **[[03_Gradient|gradient]]**: $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla f(\mathbf{w}_t)$.
*   The **learning rate ($\eta$)** controls the step size.
*   Converges to local minima (global minima only if the function is [[04_Convexity|convex]]).
*   The **workhorse optimization algorithm** for training ML/DL models.

## Sources
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapters 4 & 8) ([https://www.deeplearningbook.org/](https://www.deeplearningbook.org/))
*   [Wikipedia: Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
*   [StatQuest: Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8) (Excellent conceptual explanation)
*   Many ML/DL course notes (e.g., Andrew Ng's courses on Coursera).