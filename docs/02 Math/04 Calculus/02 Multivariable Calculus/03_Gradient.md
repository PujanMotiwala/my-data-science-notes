# Gradient

## Simple Idea
*   Imagine you're standing on a hillside represented by a [[01_Functions_of_Multiple_Variables|function]] $z = f(x, y)$. The **gradient** at your location is a **[[../03 Linear Algebra/01 Core Objects/02_Vectors|vector]]** that points in the direction you should walk to go **uphill the steepest**.
*   The *length* (magnitude) of this gradient vector tells you *how steep* that steepest slope actually is. A longer vector means a steeper slope.

## Formal Definition
*   For a [[01_Functions_of_Multiple_Variables|scalar-valued function of multiple variables]] $f(x_1, x_2, ..., x_n)$, its gradient is a **[[../03 Linear Algebra/01 Core Objects/02_Vectors|vector]]** whose components are the **[[02_Partial_Derivatives|partial derivatives]]** of $f$ with respect to each variable.
*   **Notation:** $\nabla f$ ("nabla f" or "del f").
*   **Definition:**
    $$ \nabla f(x_1, ..., x_n) = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix} $$
*   The gradient evaluated at a specific point $\mathbf{a} = (a_1, ..., a_n)$, denoted $\nabla f(\mathbf{a})$, gives the vector of steepest ascent *at that point*.

## Key Concepts

### 1. Direction of Steepest Ascent
*   The gradient vector $\nabla f(\mathbf{a})$ points in the direction in which the function $f$ increases most rapidly at the point $\mathbf{a}$.
*   The direction of **steepest descent** (fastest decrease) is simply the opposite direction: $-\nabla f(\mathbf{a})$.

### 2. Magnitude Represents Steepness
*   The [[../03 Linear Algebra/05 Norms/03_L2_Norm_Euclidean|magnitude (L₂ norm)]] of the gradient vector, $||\nabla f(\mathbf{a})||$, gives the *rate of change* of the function in the direction of steepest ascent at point $\mathbf{a}$. A larger magnitude means a steeper increase.

### 3. Orthogonality to Level Sets/Surfaces
*   The gradient vector $\nabla f(\mathbf{a})$ at a point $\mathbf{a}$ is always **orthogonal (perpendicular)** to the [[01_Functions_of_Multiple_Variables|level set]] (for 2 variables) or level surface (for 3+ variables) that passes through that point $\mathbf{a}$.
    *(Visual Idea: Excalidraw showing contour lines of a function and gradient vectors at various points, always perpendicular to the contours and pointing uphill).*

### 4. Calculation
*   Find all the first-order [[02_Partial_Derivatives|partial derivatives]] of the function.
*   Assemble them into a column vector.
*   **Example:** Let $f(x, y) = x^2 + y^2$.
    *   $\frac{\partial f}{\partial x} = 2x$
    *   $\frac{\partial f}{\partial y} = 2y$
    *   $\nabla f(x, y) = \begin{bmatrix} 2x \\ 2y \end{bmatrix}$
    *   At point (1, 2): $\nabla f(1, 2) = \begin{bmatrix} 2(1) \\ 2(2) \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$. This vector points away from the origin (the minimum) in the direction of steepest ascent.

## Connections to Other Topics & Relevance
*   **[[../03 Optimization/02_Gradient_Descent|Gradient Descent]]:** This is the core application. Gradient descent algorithms iteratively update parameters by moving in the direction *opposite* to the gradient ($-\nabla f$) of the loss function, thereby moving towards a minimum.
*   **[[04_Directional_Derivatives|Directional Derivatives]]:** The gradient is used to calculate the rate of change in *any* direction using the dot product: $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$ (where $\mathbf{u}$ is a unit vector).
*   **[[../01 Foundations/02_Derivatives|Derivative Generalization]]:** The gradient generalizes the concept of the derivative to multivariable functions. While the derivative $f'(x)$ is a scalar slope, the gradient $\nabla f$ is a vector indicating direction and magnitude of maximum change.
*   **Backpropagation:** Computes the gradient of the loss function with respect to all network weights and biases.

## Summary
*   The **Gradient ($\nabla f$)** of a multivariable function $f$ is a **[[../03 Linear Algebra/01 Core Objects/02_Vectors|vector]]** containing all its first-order **[[02_Partial_Derivatives|partial derivatives]]**.
    $$ \nabla f = \left[ \frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n} \right]^T $$
*   Points in the direction of **steepest ascent** of the function.
*   Its magnitude $||\nabla f||$ is the rate of change in that steepest direction.
*   Crucial for optimization algorithms like **[[../03 Optimization/02_Gradient_Descent|Gradient Descent]]**, which moves opposite to the gradient ($-\nabla f$).

## Sources
*   Any standard Multivariable Calculus textbook (e.g., Stewart, Thomas, Anton).
*   [Khan Academy: Gradient](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/gradient-and-directional-derivatives/v/gradient)
*   [Paul's Online Math Notes: Gradient Vector](https://tutorial.math.lamar.edu/Classes/CalcIII/GradientVector.aspx)

## TAGS
[[Calculus]] [[Multivariable Calculus]] [[Gradient]] [[Partial Derivative]] [[Vector]] [[Optimization]] [[Gradient Descent]] [[Directional Derivative]] [[Math]] [[Foundations]] [[Machine Learning]]