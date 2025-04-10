---
tags:
- Eigenvalues
- Foundations
- Linear Algebra
- Matrix Property
- Trace
---

# Matrix Trace

## Simple Idea
*   The trace of a square [[03_Matrices|matrix]] is simply the **sum of the elements on its main diagonal** (the one running from the top-left to the bottom-right).

## Formal Definition
*   For an $n \times n$ square matrix $\mathbf{A}$, the trace, denoted as $\text{tr}(\mathbf{A})$, is defined as:
    $$ \text{tr}(\mathbf{A}) = \sum_{i=1}^n A_{ii} = A_{11} + A_{22} + \dots + A_{nn} $$

## Key Concepts

### 1. Calculation
*   Straightforward summation of diagonal elements.
*   **Example:** If $\mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$, then $\text{tr}(\mathbf{A}) = 1 + 5 + 9 = 15$.

### 2. Properties of the Trace
*   **Linearity:** Trace is a linear operator.
    *   $\text{tr}(\mathbf{A} + \mathbf{B}) = \text{tr}(\mathbf{A}) + \text{tr}(\mathbf{B})$
    *   $\text{tr}(c\mathbf{A}) = c \cdot \text{tr}(\mathbf{A})$ (where $c$ is a [[01_Scalars|scalar]])
*   **Trace of Transpose:** $\text{tr}(\mathbf{A}^T) = \text{tr}(\mathbf{A})$ (The diagonal elements remain the same).
*   **Cyclic Property (Important!):** The trace is invariant under cyclic permutations of matrix products (assuming the products result in square matrices):
    $$ \text{tr}(\mathbf{ABC}) = \text{tr}(\mathbf{BCA}) = \text{tr}(\mathbf{CAB}) $$
    *   A common case: $\text{tr}(\mathbf{AB}) = \text{tr}(\mathbf{BA})$ (even if $\mathbf{AB \neq BA}$, provided both products $\mathbf{AB}$ and $\mathbf{BA}$ are square). If $\mathbf{A}$ is $m \times n$ and $\mathbf{B}$ is $n \times m$, then $\mathbf{AB}$ is $m \times m$ and $\mathbf{BA}$ is $n \times n$, but still $\text{tr}(\mathbf{AB}) = \text{tr}(\mathbf{BA})$.
*   **Trace and [[01_Eigenvalues_and_Eigenvectors|Eigenvalues]]:** The trace of a square matrix is equal to the **sum of its eigenvalues** (counting algebraic multiplicities). $\text{tr}(\mathbf{A}) = \sum_{i=1}^n \lambda_i$.

## Connections to Other Topics & Relevance
*   **[[01_Eigenvalues_and_Eigenvectors|Eigenvalues]]:** Provides a way to find the sum of eigenvalues without calculating them individually. Along with the [[03_Determinant|determinant]] (product of eigenvalues), gives useful checks.
*   **Machine Learning / Statistics:**
    *   Appears in some derivations involving matrix calculus and probability distributions (e.g., related to the Multivariate [[../03 Common Probability Distributions/05_Normal_Gaussian_Distribution|Normal distribution]]).
    *   Used in defining certain matrix [[04_Frobenius_Norm|norms]], like the squared Frobenius norm: $||\mathbf{A}||_F^2 = \text{tr}(\mathbf{A}^T\mathbf{A}) = \text{tr}(\mathbf{A}\mathbf{A}^T)$.
    *   Can appear in objective functions or regularization terms in some advanced models.
    *   Expectation of quadratic forms: $E[\mathbf{x}^T\mathbf{A}\mathbf{x}] = \text{tr}(\mathbf{A}\Sigma) + \boldsymbol{\mu}^T\mathbf{A}\boldsymbol{\mu}$ where $\mathbf{x}$ has mean $\boldsymbol{\mu}$ and covariance $\Sigma$.
*   **Quantum Mechanics:** The trace has important uses in quantum mechanics and statistical mechanics (e.g., calculating expectation values).

## Summary
*   The **Trace ($\text{tr}(\mathbf{A})$)** of a square matrix $\mathbf{A}$ is the **sum of its diagonal elements** $\sum A_{ii}$.
*   It's a linear operator: $\text{tr}(\mathbf{A}+\mathbf{B}) = \text{tr}(\mathbf{A})+\text{tr}(\mathbf{B})$, $\text{tr}(c\mathbf{A}) = c \cdot \text{tr}(\mathbf{A})$.
*   Invariant under cyclic permutations: $\text{tr}(\mathbf{AB}) = \text{tr}(\mathbf{BA})$.
*   Equals the sum of the matrix's [[01_Eigenvalues_and_Eigenvectors|eigenvalues]].

## Sources
*   [Wikipedia: Trace (linear algebra)](https://en.wikipedia.org/wiki/Trace_(linear_algebra))
*   *Introduction to Linear Algebra* by Gilbert Strang (Usually introduced later, check index)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   *The Matrix Cookbook* by Petersen and Pedersen ([https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf))