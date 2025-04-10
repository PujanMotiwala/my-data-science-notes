# L₁ Norm (Manhattan Norm)

## Simple Idea
*   The **L₁ norm** of a [[../01 Core Objects/02_Vectors|vector]] measures its "length" by summing the **absolute values** of all its components.
*   Imagine moving along a city grid (like Manhattan) where you can only travel horizontally or vertically. The L₁ norm is the total distance you travel along the grid lines from the origin to the vector's endpoint.

## Formal Definition
*   For a vector $\mathbf{x} = [x_1, x_2, ..., x_n]^T$ in $\mathbb{R}^n$, the **L₁ norm**, denoted $||\mathbf{x}||_1$, is defined as:
    $$ ||\mathbf{x}||_1 = \sum_{i=1}^n |x_i| = |x_1| + |x_2| + \dots + |x_n| $$
*   It is a specific case of the [[01_Definition|Lₚ norm]] family where $p=1$.

## Key Concepts

### 1. Calculation
*   Simply sum the absolute values of all elements.
*   **Example:** If $\mathbf{x} = [1, -3, 2]^T$, then $||\mathbf{x}||_1 = |1| + |-3| + |2| = 1 + 3 + 2 = 6$.

### 2. Geometric Interpretation ("Manhattan Distance")
*   In 2D, for a vector $[x_1, x_2]^T$, $||\mathbf{x}||_1 = |x_1| + |x_2|$. This represents the distance from the origin $(0,0)$ to the point $(x_1, x_2)$ if movement is restricted to horizontal and vertical paths.
*   The set of all vectors with $||\mathbf{x}||_1 = 1$ (the "unit ball" in the L₁ norm) forms a square (or diamond) shape rotated by 45 degrees in 2D, or an octahedron in 3D.
    *(Visual Idea: An Excalidraw showing the L₁ unit "circle" (diamond) vs the L₂ unit circle (circle) would highlight the difference).*

### 3. Properties
*   Satisfies all the properties of a [[01_Definition|norm]]: Non-negativity, Definiteness, Absolute Homogeneity, Triangle Inequality.

## Connections to Other Topics & Relevance
*   **[[../../06 Machine Learning/01 The Basics/02_Model Evaluation/Test metrics/Regularization/Lasso Regression|Lasso Regression (L1 Regularization)]]:** This is the most significant application in machine learning. Lasso adds a penalty term to the loss function proportional to the L₁ norm of the model's weight vector ($\lambda ||\mathbf{w}||_1$).
*   **Sparsity:** A key effect of L₁ regularization is that it tends to produce **sparse** solutions, meaning many of the weights ($w_i$) are driven to exactly **zero**. This effectively performs automatic **feature selection**, as features corresponding to zero weights are removed from the model. The sharp corners of the L₁ "ball" encourage solutions (where level sets of the loss function first touch the ball) to land on the axes where some components are zero.
*   **Robustness:** L₁ norm is sometimes considered more robust to outliers than the [[03_L2_Norm_Euclidean|L₂ norm]] when used in loss functions (e.g., Mean Absolute Error (MAE), $\frac{1}{n}||\mathbf{y}_{\text{pred}} - \mathbf{y}_{\text{actual}}||_1$, uses L₁, whereas Mean Squared Error (MSE) uses L₂). Minimizing sum of absolute errors is less sensitive to large individual errors.
*   **Compressed Sensing:** L₁ minimization is used in signal processing to reconstruct signals from incomplete measurements, leveraging the assumption that the original signal is sparse in some basis.

## Summary
*   The **L₁ norm ($||\mathbf{x}||_1$)** is the **sum of the absolute values** of a vector's components.
*   Also known as the **Manhattan** or **Taxicab** norm.
*   Formula: $||\mathbf{x}||_1 = \sum |x_i|$.
*   Crucially used in **[[../../06 Machine Learning/01 The Basics/02_Model Evaluation/Test metrics/Regularization/Lasso Regression|Lasso (L1) Regularization]]** in machine learning.
*   Promotes **sparsity** (zeroing out weights/coefficients), leading to feature selection.

## Sources
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   *The Elements of Statistical Learning* by Hastie, Tibshirani, Friedman (Chapter 3 discusses Lasso)
*   [Wikipedia: Norm (mathematics)#Taxicab norm or Manhattan norm](https://en.wikipedia.org/wiki/Norm_(mathematics)#Taxicab_norm_or_Manhattan_norm)
*   [Explanation of L1 vs L2 Regularization](https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c)

## TAGS
[[Linear Algebra]] [[Vector Norm]] [[Norm]] [[L1 Norm]] [[Manhattan Norm]] [[Magnitude]] [[Distance]] [[Regularization]] [[Lasso Regression]] [[Sparsity]] [[Feature Selection]] [[02 Math/index]] [[Foundations]] [[Machine Learning]]