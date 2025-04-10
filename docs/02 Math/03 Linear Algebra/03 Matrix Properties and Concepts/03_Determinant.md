# Determinant

## Simple Idea
*   Think of the determinant of a square [[../01 Core Objects/03_Matrices|matrix]] as a [[../01 Core Objects/01_Scalars|scalar]] value that tells you about the **scaling factor** of the linear transformation represented by that matrix.
*   Specifically, it tells you how much the **area** (in 2D) or **volume** (in 3D) changes when you apply the matrix transformation. A determinant of 0 means the transformation squashes space into a lower dimension (like flattening a 3D object onto a plane or a 2D shape onto a line).

## Formal Definition
*   The determinant is a [[../01 Core Objects/01_Scalars|scalar]] value that can only be computed for a **square matrix** $\mathbf{A}$ ($n \times n$). It is denoted as $\det(\mathbf{A})$ or $|\mathbf{A}|$.
*   Its calculation encodes properties related to the matrix's invertibility and the geometric scaling effect of the corresponding linear transformation.

## Key Concepts

### 1. Calculation
*   **For a 2x2 Matrix:** If $\mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, then:
    $$ \det(\mathbf{A}) = |\mathbf{A}| = ad - bc $$
*   **For a 3x3 Matrix:** Using cofactor expansion (e.g., along the first row):
    $$ |\mathbf{A}| = a \begin{vmatrix} e & f \\ h & i \end{vmatrix} - b \begin{vmatrix} d & f \\ g & i \end{vmatrix} + c \begin{vmatrix} d & e \\ g & h \end{vmatrix} $$
    $$ |\mathbf{A}| = a(ei - fh) - b(di - fg) + c(dh - eg) $$
    (Where $\begin{vmatrix} \dots \end{vmatrix}$ indicates the determinant of the 2x2 submatrix).
*   **For Larger Matrices:** Cofactor expansion can be used recursively, but it becomes computationally very expensive ($\mathcal{O}(n!)$). Methods based on row reduction (Gaussian elimination) to reach triangular form are more practical ($\mathcal{O}(n^3)$):
    *   Swapping two rows multiplies the determinant by -1.
    *   Multiplying a row by a scalar $k$ multiplies the determinant by $k$.
    *   Adding a multiple of one row to another *does not change* the determinant.
    *   The determinant of a triangular matrix (upper or lower) is the product of its diagonal entries.

### 2. Geometric Interpretation
*   $|\det(\mathbf{A})|$ represents the factor by which **area** (in 2D) or **volume** (in 3D) or **hypervolume** (in higher dimensions) is scaled when applying the linear transformation defined by $\mathbf{A}$.
*   **Sign of the Determinant:**
    *   $\det(\mathbf{A}) > 0$: Transformation preserves orientation (e.g., doesn't flip shapes inside-out).
    *   $\det(\mathbf{A}) < 0$: Transformation reverses orientation (e.g., like looking in a mirror).
    *   $\det(\mathbf{A}) = 0$: Transformation collapses space into a lower dimension (area/volume becomes zero). The matrix is **singular** ([[02_Inverse_Matrix|non-invertible]]).

### 3. Properties of Determinants
*   $\det(\mathbf{A}) \neq 0$ if and only if $\mathbf{A}$ is [[02_Inverse_Matrix|invertible]].
*   $\det(\mathbf{I}) = 1$ (The [[01_Identity_Matrix|Identity matrix]] doesn't scale volume or change orientation).
*   $\det(\mathbf{A}^T) = \det(\mathbf{A})$ (Transpose has the same determinant).
*   $\det(\mathbf{AB}) = \det(\mathbf{A}) \det(\mathbf{B})$ (Determinant of a product is the product of determinants). This reflects composing scaling factors of transformations. Requires $\mathbf{A}, \mathbf{B}$ to be square matrices of the same size.
*   $\det(\mathbf{A}^{-1}) = 1 / \det(\mathbf{A}) = (\det(\mathbf{A}))^{-1}$ (if $\mathbf{A}$ is invertible).
*   $\det(k\mathbf{A}) = k^n \det(\mathbf{A})$ for an $n \times n$ matrix $\mathbf{A}$ and scalar $k$.

## Connections to Other Topics
*   Crucial for determining if a [[02_Inverse_Matrix|Matrix Inverse]] exists.
*   Used in Cramer's rule for solving systems of linear equations $\mathbf{Ax=b}$ (though often not computationally preferred).
*   Appears in the change of variables formula for multivariable calculus integration ([[../04 Calculus/04 Advanced Topics/02_Jacobian_Matrix|Jacobian determinant]]).
*   Related to [[../06 Decompositions and Factorizations/01_Eigenvalues_and_Eigenvectors|Eigenvalues]] (the determinant is the product of the eigenvalues, counting algebraic multiplicities).

## Summary
*   The **Determinant ($\det(\mathbf{A})$ or $|\mathbf{A}|$)** is a scalar value associated with a **square matrix**.
*   Geometrically represents the **volume scaling factor** (and orientation change) of the associated linear transformation.
*   $\det(\mathbf{A}) = 0 \iff$ the matrix collapses space $\iff$ matrix is **singular (non-invertible)**.
*   $\det(\mathbf{A}) \neq 0 \iff$ matrix is **invertible**.
*   Key Property: $\det(\mathbf{AB}) = \det(\mathbf{A})\det(\mathbf{B})$.

## Sources
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 5)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   [Khan Academy: Determinant](https://www.khanacademy.org/math/linear-algebra/matrix-transformations/matrix-determinants/v/determinant-of-a-2x2-matrix)
*   [3Blue1Brown: The Determinant | Essence of Linear Algebra](https://www.youtube.com/watch?v=Ip3X9LOh2dk) (Excellent geometric intuition)

## TAGS
[[Linear Algebra]] [[Matrix Property]] [[Determinant]] [[Matrix Inverse]] [[Singular Matrix]] [[Linear Transformation]] [[Eigenvalues]] [[Math]] [[Foundations]]