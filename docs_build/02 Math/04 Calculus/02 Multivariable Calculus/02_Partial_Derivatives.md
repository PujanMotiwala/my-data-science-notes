---
tags:
- Calculus
- Derivative
- Foundations
- Gradient
- Machine Learning
- Multivariable Calculus
- Optimization
- Partial Derivative
- Rate of Change
- Slope
---

# Partial Derivatives

## Simple Idea
*   When dealing with a [[01_Functions_of_Multiple_Variables|function of multiple variables]] (like $z = f(x, y)$), a **partial derivative** measures the **rate of change** of the function's output with respect to **just one** of the input variables, while **holding all other input variables constant**.
*   Think of standing on a hillside (surface $z=f(x,y)$). The partial derivative with respect to $x$ tells you how steep the hill is if you walk *only* in the x-direction (East-West). The partial derivative with respect to $y$ tells you the steepness if you walk *only* in the y-direction (North-South).

## Formal Definition
*   For a function $z = f(x_1, x_2, ..., x_n)$, the **partial derivative** of $f$ with respect to the variable $x_i$ at a point $(a_1, ..., a_n)$ is found by treating all variables except $x_i$ as constants and taking the ordinary [[02_Derivatives|derivative]] with respect to $x_i$.
*   **Notation:**
    *   $\frac{\partial f}{\partial x_i}$ (Leibniz-style, "del f del x_i") - Most common.
    *   $f_{x_i}(x_1, ..., x_n)$ or $D_i f$ (Subscript notation).
*   **Limit Definition** (for $f(x, y)$ w.r.t $x$ at $(a, b)$):
    $$ \frac{\partial f}{\partial x}(a, b) = \lim_{h \to 0} \frac{f(a+h, b) - f(a, b)}{h} $$
    (Notice only $x$ changes by $h$, $y$ stays fixed at $b$).

## Key Concepts

### 1. Calculation
*   To find $\partial f / \partial x$, treat $y, z$, etc., as constants and apply the standard [[03_Rules_of_Differentiation|differentiation rules]] with respect to $x$.
*   To find $\partial f / \partial y$, treat $x, z$, etc., as constants and apply standard rules with respect to $y$.
*   **Example:** Let $f(x, y) = x^2 y^3 + 2x + y$.
    *   Find $\partial f / \partial x$: Treat $y^3$ and $y$ as constants.
        $\frac{\partial f}{\partial x} = \frac{\partial}{\partial x}(x^2 y^3) + \frac{\partial}{\partial x}(2x) + \frac{\partial}{\partial x}(y) = (2x)y^3 + 2 + 0 = 2xy^3 + 2$
    *   Find $\partial f / \partial y$: Treat $x^2$ and $2x$ as constants.
        $\frac{\partial f}{\partial y} = \frac{\partial}{\partial y}(x^2 y^3) + \frac{\partial}{\partial y}(2x) + \frac{\partial}{\partial y}(y) = x^2(3y^2) + 0 + 1 = 3x^2y^2 + 1$

### 2. Geometric Interpretation
*   For $z = f(x, y)$, $\partial f / \partial x$ at point $(a, b)$ is the slope of the curve formed by intersecting the surface $z=f(x,y)$ with the plane $y=b$, evaluated at $x=a$. It's the slope *parallel* to the xz-plane.
*   Similarly, $\partial f / \partial y$ is the slope of the curve formed by intersecting the surface with the plane $x=a$, evaluated at $y=b$. It's the slope *parallel* to the yz-plane.
    *(Visual Idea: Excalidraw showing a surface with tangent lines drawn in the x and y directions at a point).*

### 3. Higher-Order Partial Derivatives
*   Partial derivatives can be taken multiple times and with respect to different variables.
*   **Notation:**
    *   $\frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x} \left(\frac{\partial f}{\partial x}\right)$
    *   $\frac{\partial^2 f}{\partial y^2} = \frac{\partial}{\partial y} \left(\frac{\partial f}{\partial y}\right)$
    *   $\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial}{\partial y} \left(\frac{\partial f}{\partial x}\right)$ (Differentiate w.r.t. $x$ first, then $y$)
    *   $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial}{\partial x} \left(\frac{\partial f}{\partial y}\right)$ (Differentiate w.r.t. $y$ first, then $x$)
*   **Clairaut's Theorem (Equality of Mixed Partials):** If the second partial derivatives are continuous in a region, then the order of differentiation doesn't matter: $\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial^2 f}{\partial x \partial y}$.

## Connections to Other Topics & Relevance
*   **[[03_Gradient|Gradient]]:** The gradient of a multivariable function is a **[[../03 Linear Algebra/01 Core Objects/02_Vectors|vector]]** containing *all* of its first-order partial derivatives. $\nabla f = \left[ \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, ..., \frac{\partial f}{\partial x_n} \right]^T$. This vector points in the direction of the function's steepest ascent.
*   **[[02_Gradient_Descent|Gradient Descent]] & Optimization:** Partial derivatives are essential for finding the [[03_Gradient|gradient]] of the loss function with respect to model parameters. Gradient descent uses this gradient to update parameters. $w_i \leftarrow w_i - \eta \frac{\partial \text{Loss}}{\partial w_i}$ (where $\eta$ is learning rate).
*   **[[04_Directional_Derivatives|Directional Derivatives]]:** Measures the rate of change in *any* direction (not just parallel to axes), calculated using partial derivatives and the direction vector.
*   **[[01_Hessian_Matrix|Hessian Matrix]]:** A square matrix of all second-order partial derivatives. Used in second-order optimization methods and analyzing concavity/convexity.
*   **Jacobian Matrix:** Generalizes the gradient to vector-valued functions (functions with multiple outputs). Its entries are partial derivatives.

## Summary
*   **Partial Derivative ($\partial f / \partial x_i$)** measures the rate of change of a multivariable function $f$ with respect to **one variable $x_i$**, holding **others constant**.
*   Calculated using standard [[03_Rules_of_Differentiation|differentiation rules]], treating other variables as constants.
*   Geometrically, represents the slope of the function's surface in the direction parallel to an axis.
*   The components of the crucial **[[03_Gradient|Gradient]] vector** ($\nabla f$) are the partial derivatives.
*   Essential for multivariable optimization ([[02_Gradient_Descent|Gradient Descent]]) in ML/AI.

## Sources
*   Any standard Multivariable Calculus textbook (e.g., Stewart, Thomas, Anton).
*   [Khan Academy: Partial derivatives introduction](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/introduction-to-partial-derivatives)
*   [Paul's Online Math Notes: Partial Derivatives](https://tutorial.math.lamar.edu/Classes/CalcIII/PartialDerivs.aspx)