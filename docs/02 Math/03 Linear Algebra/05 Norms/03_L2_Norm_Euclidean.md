# L₂ Norm (Euclidean Norm)

## Simple Idea
*   The **L₂ norm** is what we typically think of as the standard "length" or "distance" of a [[../01 Core Objects/02_Vectors|vector]] in everyday geometry (Euclidean space).
*   It's calculated using the Pythagorean theorem in multiple dimensions: the square root of the sum of the squares of the components.

## Formal Definition
*   For a vector $\mathbf{x} = [x_1, x_2, ..., x_n]^T$ in $\mathbb{R}^n$, the **L₂ norm**, denoted $||\mathbf{x}||_2$ or often just $||\mathbf{x}||$ (when the context is clear), is defined as:
    $$ ||\mathbf{x}||_2 = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2} $$
*   It is a specific case of the [[01_Definition|Lₚ norm]] family where $p=2$.

## Key Concepts

### 1. Calculation
*   Square each element, sum them up, and take the square root.
*   **Example:** If $\mathbf{x} = [3, 4]^T$, then $||\mathbf{x}||_2 = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.
*   **Example:** If $\mathbf{x} = [1, -1, 2]^T$, then $||\mathbf{x}||_2 = \sqrt{1^2 + (-1)^2 + 2^2} = \sqrt{1 + 1 + 4} = \sqrt{6} \approx 2.45$.

### 2. Geometric Interpretation ("Euclidean Distance")
*   $||\mathbf{x}||_2$ represents the straight-line distance from the origin $\mathbf{0}=(0, ..., 0)$ to the point defined by the vector $\mathbf{x}$ in Euclidean space.
*   The **Euclidean distance** between two vectors $\mathbf{x}$ and $\mathbf{y}$ is given by $||\mathbf{x} - \mathbf{y}||_2$.
*   The set of all vectors with $||\mathbf{x}||_2 = 1$ (the "unit ball") forms a circle in 2D, a sphere in 3D, and a hypersphere in higher dimensions.
    *(Visual Idea: An Excalidraw showing the L₂ unit circle vs the L₁ unit diamond).*

### 3. Relationship to Dot Product
*   The L₂ norm squared is equal to the [[../02 Basic Operations/01_Vector_Operations|dot product]] of the vector with itself:
    $$ ||\mathbf{x}||_2^2 = x_1^2 + \dots + x_n^2 = \mathbf{x} \cdot \mathbf{x} = \mathbf{x}^T \mathbf{x} $$

### 4. Properties
*   Satisfies all the properties of a [[01_Definition|norm]]: Non-negativity, Definiteness, Absolute Homogeneity, Triangle Inequality.
*   It's induced by the standard dot product (inner product).

## Connections to Other Topics & Relevance
*   **Distance Calculation:** The fundamental measure of distance in Euclidean geometry and many algorithms (e.g., k-Nearest Neighbors).
*   **[[../../06 Machine Learning/01 The Basics/02_Model Evaluation/Test metrics/Regularization/Ridge Regression|Ridge Regression (L2 Regularization)]]:** Adds a penalty term proportional to the *squared* L₂ norm of the model's weight vector ($\lambda ||\mathbf{w}||_2^2$) to the loss function. (Note: Using the *squared* L₂ norm $||\mathbf{w}||_2^2 = \mathbf{w}^T\mathbf{w}$ is common for mathematical convenience in differentiation, but it has a similar effect to penalizing the L₂ norm itself).
*   **Effect of L2 Regularization:** Shrinks weights towards zero but rarely makes them *exactly* zero (unlike [[02_L1_Norm_Manhattan|L1]]). Helps prevent [[../../06 Machine Learning/01 The Basics/02_Model Evaluation/Issues/Overfitting|overfitting]] by discouraging overly large weights. Solutions tend to be distributed within the L₂ "ball" (circle/sphere), generally not hitting axes.
*   **Loss Functions (MSE):** The Mean Squared Error (MSE) loss function is based on the squared L₂ norm of the error vector between predictions and actual values: $MSE = \frac{1}{n} ||\mathbf{y}_{\text{pred}} - \mathbf{y}_{\text{actual}}||_2^2$.
*   **Vector Magnitude:** Standard way to measure the magnitude or length of vectors in physics and engineering.

## Summary
*   The **L₂ norm ($||\mathbf{x}||_2$ or $||\mathbf{x}||$)** is the standard **Euclidean length** of a vector.
*   Calculated as the **square root of the sum of the squared components**.
*   Formula: $||\mathbf{x}||_2 = \sqrt{\sum x_i^2} = \sqrt{\mathbf{x}^T\mathbf{x}}$.
*   Represents straight-line distance from the origin.
*   Foundation for **[[../../06 Machine Learning/01 The Basics/02_Model Evaluation/Test metrics/Regularization/Ridge Regression|Ridge (L2) Regularization]]** (shrinks weights, prevents large values) and **Mean Squared Error (MSE)** loss.

## Sources
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 1)
*   [Wikipedia: Euclidean norm](https://en.wikipedia.org/wiki/Euclidean_norm)
*   [Explanation of L1 vs L2 Regularization](https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c)

## TAGS
[[Linear Algebra]] [[Vector Norm]] [[Norm]] [[L2 Norm]] [[Euclidean Norm]] [[Magnitude]] [[Distance]] [[Regularization]] [[Ridge Regression]] [[MSE]] [[Dot Product]] [[02 Math/index]] [[Foundations]] [[Machine Learning]]