# Matrix Inverse

## Simple Idea
*   Think of the inverse of a [[../01 Core Objects/03_Matrices|matrix]] $\mathbf{A}$, called $\mathbf{A}^{-1}$, like the reciprocal $1/c$ of a number $c$. Just as $c \times (1/c) = 1$, multiplying a matrix by its inverse gives the [[01_Identity_Matrix|Identity Matrix]]: $\mathbf{A} \mathbf{A}^{-1} = \mathbf{I}$.
*   It allows you to "undo" the linear transformation represented by the matrix $\mathbf{A}$.

## Formal Definition
*   For a **square matrix** $\mathbf{A}$ ($n \times n$), its inverse $\mathbf{A}^{-1}$ is another $n \times n$ square matrix such that:
    $$ \mathbf{A} \mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{I}_n $$
    where $\mathbf{I}_n$ is the $n \times n$ [[01_Identity_Matrix|Identity Matrix]].
*   If such a matrix $\mathbf{A}^{-1}$ exists, $\mathbf{A}$ is called **invertible** or **non-singular**. Otherwise, it's called **non-invertible** or **singular**.

## Key Concepts

### 1. Existence of the Inverse
*   **Not all square matrices have an inverse.**
*   A square matrix $\mathbf{A}$ is invertible if and only if any of the following equivalent conditions hold:
    *   Its [[03_Determinant|Determinant]] is non-zero ($\det(\mathbf{A}) \neq 0$).
    *   Its columns (or rows) are [[../04 Vector Spaces and Concepts/01_Linear_Independence|linearly independent]].
    *   Its [[../04 Vector Spaces and Concepts/03_Rank|Rank]] equals its dimension ($n$ for an $n \times n$ matrix). $\text{rank}(\mathbf{A}) = n$.
    *   The equation $\mathbf{Ax = 0}$ has only the trivial solution $\mathbf{x = 0}$.
    *   It does not map any non-zero [[../01 Core Objects/02_Vectors|vector]] to the zero vector (its null space contains only the zero vector).

### 2. Finding the Inverse
*   **For a 2x2 Matrix:** If $\mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, the inverse is:
    $$ \mathbf{A}^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix} $$
    Note that $ad-bc = \det(\mathbf{A})$. If $\det(\mathbf{A}) = 0$, the inverse doesn't exist.
*   **For Larger Matrices:** Common methods include:
    *   **Gauss-Jordan Elimination:** Augment matrix $\mathbf{A}$ with the identity matrix $\mathbf{I}$ ($[\mathbf{A} | \mathbf{I}]$) and perform row operations to transform $\mathbf{A}$ into $\mathbf{I}$. The right side will become $\mathbf{A}^{-1}$ ($[\mathbf{I} | \mathbf{A}^{-1}]$).
    *   **Using Adjoint and Determinant:** $\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})} \text{adj}(\mathbf{A})$, where $\text{adj}(\mathbf{A})$ is the adjugate matrix (transpose of the cofactor matrix). Often computationally intensive.
*   **Numerical Methods:** In practice (data science), inverses are often computed using numerical libraries (like NumPy/SciPy's `linalg.inv`) which employ stable algorithms (often based on LU or QR decomposition), rather than calculating by hand or using the adjoint formula. Direct computation can be numerically unstable for ill-conditioned matrices.

### 3. Properties of Inverses
*   $(\mathbf{A}^{-1})^{-1} = \mathbf{A}$ (The inverse of the inverse is the original matrix).
*   $(\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$ (Reverse order law, similar to transpose). Requires A and B to be invertible square matrices of the same size.
*   $(\mathbf{A}^T)^{-1} = (\mathbf{A}^{-1})^T$ (Inverse of transpose is transpose of inverse).
*   $(k\mathbf{A})^{-1} = \frac{1}{k} \mathbf{A}^{-1}$ for a non-zero [[../01 Core Objects/01_Scalars|scalar]] $k$.

### 4. Use Cases
*   **Solving Systems of Linear Equations:** If $\mathbf{Ax = b}$ and $\mathbf{A}$ is invertible, the unique solution is $\mathbf{x = A^{-1}b}$. (Though direct inversion is often avoided numerically in favor of methods like Gaussian elimination or LU decomposition for solving systems).
*   **Undoing Transformations:** If $\mathbf{y} = \mathbf{Ax}$ represents a transformation, $\mathbf{x = A^{-1}y}$ recovers the original vector $\mathbf{x}$.
*   **Theoretical Tool:** Used in derivations, like the Normal Equation in [[../../06 Machine Learning/02 Supervised/01 Regression/01_Simple Linear Regression/Linear Regression|Linear Regression]]: $\boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$.

## Connections to Other Topics
*   Closely related to the [[03_Determinant|Determinant]] (non-zero determinant $\iff$ invertible).
*   Related to [[../04 Vector Spaces and Concepts/01_Linear_Independence|Linear Independence]] and [[../04 Vector Spaces and Concepts/03_Rank|Rank]].
*   Used in computing [[../06 Decompositions and Factorizations/03_Overview|matrix decompositions]].

## Summary
*   The **Matrix Inverse ($\mathbf{A}^{-1}$)** "undoes" the operation of matrix $\mathbf{A}$: $\mathbf{A} \mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{I}$.
*   Exists only for **square** matrices that are **non-singular** (or invertible).
*   A matrix is invertible $\iff$ its [[03_Determinant|determinant]] is non-zero $\iff$ columns are [[../04 Vector Spaces and Concepts/01_Linear_Independence|linearly independent]] $\iff$ [[../04 Vector Spaces and Concepts/03_Rank|rank]] equals dimension.
*   Used for solving $\mathbf{Ax=b}$ (as $\mathbf{x = A^{-1}b}$) and in theoretical derivations.

## Sources
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 2)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   [Khan Academy: Matrix Inverse](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:finding-the-inverse-of-a-matrix-using-gaussian-elimination/v/finding-the-inverse-of-a-3x3-matrix-using-gaussian-elimination)
*   [3Blue1Brown: Inverse Matrices | Essence of Linear Algebra](https://www.youtube.com/watch?v=uQhTuRlWMxw)

## TAGS
[[Linear Algebra]] [[Matrix Property]] [[Matrix Inverse]] [[Invertible Matrix]] [[Non-singular Matrix]] [[Identity Matrix]] [[Determinant]] [[02 Math/index]] [[Foundations]]