---
tags:
- Calculus
- Derivative
- Directional Derivative
- Dot Product
- Foundations
- Gradient
- Multivariable Calculus
- Rate of Change
- Slope
- Unit Vector
---

# Directional Derivatives

## Simple Idea
*   We know [[02_Partial_Derivatives|partial derivatives]] ($\partial f/\partial x$, $\partial f/\partial y$) tell us the rate of change of a multivariable function $f(x, y)$ strictly along the x or y axes.
*   The **directional derivative** generalizes this: it measures the rate of change (the slope) of the function $f$ at a specific point **in any arbitrary direction** specified by a unit vector $\mathbf{u}$.
*   Imagine standing on that hillside ($z=f(x,y)$) again. The directional derivative tells you how steep the slope is right under your feet if you take a step in the specific compass direction $\mathbf{u}$ (e.g., northeast).

## Formal Definition
*   Let $f(x_1, ..., x_n)$ be a scalar function of multiple variables, and let $\mathbf{u} = [u_1, ..., u_n]^T$ be a **unit vector** (meaning its [[../03 Linear Algebra/05 Norms/03_L2_Norm_Euclidean|L₂ norm]] is 1, $||\mathbf{u}|| = 1$) specifying a direction.
*   The **directional derivative** of $f$ at a point $\mathbf{a} = (a_1, ..., a_n)$ in the direction of $\mathbf{u}$ is denoted $D_{\mathbf{u}}f(\mathbf{a})$.
*   It can be calculated using the [[03_Gradient|gradient]] of $f$ and the [[../03 Linear Algebra/02 Basic Operations/01_Vector_Operations|dot product]]:
    $$ D_{\mathbf{u}}f(\mathbf{a}) = \nabla f(\mathbf{a}) \cdot \mathbf{u} $$
*   **Limit Definition:** It can also be defined using a limit, showing the rate of change along the direction $\mathbf{u}$:
    $$ D_{\mathbf{u}}f(\mathbf{a}) = \lim_{h \to 0} \frac{f(\mathbf{a} + h\mathbf{u}) - f(\mathbf{a})}{h} $$

## Key Concepts

### 1. Requirement of Unit Vector
*   The direction vector $\mathbf{u}$ **must be a unit vector** for the formula $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$ to directly represent the rate of change *per unit distance* in that direction.
*   If given a direction vector $\mathbf{v}$ that is not a unit vector, first normalize it: $\mathbf{u} = \mathbf{v} / ||\mathbf{v}||$.

### 2. Calculation using Gradient
*   Find the [[03_Gradient|gradient]] vector $\nabla f$ (vector of partial derivatives).
*   Ensure the direction vector $\mathbf{u}$ is a unit vector.
*   Calculate the [[../03 Linear Algebra/02 Basic Operations/01_Vector_Operations|dot product]] between the gradient evaluated at the point $\mathbf{a}$ and the unit direction vector $\mathbf{u}$.
*   **Example:** Let $f(x, y) = x^2 y$. Find the directional derivative at point $(1, 2)$ in the direction of vector $\mathbf{v} = [3, 4]^T$.
    1.  Find gradient: $\nabla f = [\partial f/\partial x, \partial f/\partial y]^T = [2xy, x^2]^T$.
    2.  Evaluate gradient at (1, 2): $\nabla f(1, 2) = [2(1)(2), 1^2]^T = [4, 1]^T$.
    3.  Normalize direction vector $\mathbf{v}$: $||\mathbf{v}|| = \sqrt{3^2 + 4^2} = \sqrt{9+16} = 5$. So, $\mathbf{u} = \mathbf{v} / 5 = [3/5, 4/5]^T$.
    4.  Calculate dot product:
        $D_{\mathbf{u}}f(1, 2) = \nabla f(1, 2) \cdot \mathbf{u} = [4, 1]^T \cdot [3/5, 4/5]^T$
        $D_{\mathbf{u}}f(1, 2) = (4)(3/5) + (1)(4/5) = 12/5 + 4/5 = 16/5 = 3.2$.
    *Interpretation:* At point (1, 2), if you move one unit in the direction [3/5, 4/5], the function value increases at a rate of 3.2.

### 3. Relationship to Gradient
*   Recall the geometric definition of the dot product: $\nabla f \cdot \mathbf{u} = ||\nabla f|| \, ||\mathbf{u}|| \cos(\theta)$, where $\theta$ is the angle between the gradient $\nabla f$ and the direction vector $\mathbf{u}$.
*   Since $||\mathbf{u}|| = 1$, we have $D_{\mathbf{u}}f = ||\nabla f|| \cos(\theta)$.
*   This shows:
    *   The directional derivative is **maximized** when $\mathbf{u}$ points in the *same* direction as the gradient $\nabla f$ ($\theta = 0$, $\cos(0)=1$). The maximum rate of change is $||\nabla f||$.
    *   The directional derivative is **minimized** (most negative) when $\mathbf{u}$ points in the *opposite* direction to the gradient $\nabla f$ ($\theta = 180^\circ$, $\cos(180^\circ)=-1$). The minimum rate of change is $-||\nabla f||$.
    *   The directional derivative is **zero** when $\mathbf{u}$ is *orthogonal* to the gradient $\nabla f$ ($\theta = 90^\circ$, $\cos(90^\circ)=0$). This means moving along a level set/surface.

## Connections to Other Topics & Relevance
*   Provides a more complete picture of how a function changes around a point than [[02_Partial_Derivatives|partial derivatives]] alone.
*   Directly uses the [[03_Gradient|Gradient]].
*   Used in physics and engineering to analyze fields (e.g., temperature gradients, fluid flow) in specific directions.
*   Helps build intuition for optimization: knowing the rate of change in any direction confirms that the [[03_Gradient|gradient]] points towards the fastest increase.

## Summary
*   The **Directional Derivative ($D_{\mathbf{u}}f$)** measures the rate of change of a multivariable function $f$ at a point $\mathbf{a}$ in the direction of a **unit vector $\mathbf{u}$**.
*   Formula: $D_{\mathbf{u}}f(\mathbf{a}) = \nabla f(\mathbf{a}) \cdot \mathbf{u}$.
*   Geometrically, it's the slope of the function's surface along the direction $\mathbf{u}$.
*   Maximized when $\mathbf{u}$ aligns with the [[03_Gradient|gradient]] $\nabla f$.
*   Zero when $\mathbf{u}$ is orthogonal to $\nabla f$ (along a level set).

## Sources
*   Any standard Multivariable Calculus textbook (e.g., Stewart, Thomas, Anton).
*   [Khan Academy: Directional derivatives](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/gradient-and-directional-derivatives/v/directional-derivative)
*   [Paul's Online Math Notes: Directional Derivatives](https://tutorial.math.lamar.edu/Classes/CalcIII/DirectionalDeriv.aspx)