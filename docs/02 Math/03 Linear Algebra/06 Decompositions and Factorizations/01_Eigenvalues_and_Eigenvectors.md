# Eigenvalues and Eigenvectors

## Simple Idea
*   Imagine a square [[../01 Core Objects/03_Matrices|matrix]] $\mathbf{A}$ representing a linear transformation (like stretching, shearing, rotating). An **eigenvector** of $\mathbf{A}$ is a special non-zero [[../01 Core Objects/02_Vectors|vector]] $\mathbf{v}$ whose direction **does not change** when the transformation $\mathbf{A}$ is applied to it. It might get stretched or shrunk, but it still points along the same line through the origin.
*   The **eigenvalue** ($\lambda$) associated with that eigenvector $\mathbf{v}$ is the [[../01 Core Objects/01_Scalars|scalar]] factor by which the eigenvector is stretched or shrunk. $\mathbf{Av = \lambda v}$.

## Formal Definition
*   For a given $n \times n$ square matrix $\mathbf{A}$, a non-zero vector $\mathbf{v} \in \mathbb{C}^n$ is an **eigenvector** of $\mathbf{A}$ if there exists a scalar $\lambda \in \mathbb{C}$ such that:
    $$ \mathbf{A}\mathbf{v} = \lambda \mathbf{v} $$
*   The scalar $\lambda$ is called the **eigenvalue** corresponding to the eigenvector $\mathbf{v}$.
*   (The zero vector $\mathbf{v=0}$ is excluded because $\mathbf{A0 = \lambda 0}$ holds trivially for any $\lambda$).

## Key Concepts

### 1. Finding Eigenvalues
*   The defining equation $\mathbf{Av = \lambda v}$ can be rewritten as $\mathbf{Av - \lambda v = 0}$, or $\mathbf{Av - \lambda I v = 0}$ (where $\mathbf{I}$ is the [[../03 Matrix Properties and Concepts/01_Identity_Matrix|Identity matrix]]).
*   Factoring out $\mathbf{v}$: $(\mathbf{A} - \lambda \mathbf{I})\mathbf{v} = \mathbf{0}$.
*   For this equation to have a non-zero solution for $\mathbf{v}$ (which is required for an eigenvector), the matrix $(\mathbf{A} - \lambda \mathbf{I})$ must be **singular** ([[../03 Matrix Properties and Concepts/02_Inverse_Matrix|non-invertible]]).
*   This means the [[../03 Matrix Properties and Concepts/03_Determinant|determinant]] of $(\mathbf{A} - \lambda \mathbf{I})$ must be zero:
    $$ \det(\mathbf{A} - \lambda \mathbf{I}) = 0 $$
*   This equation is called the **characteristic equation** of matrix $\mathbf{A}$. Solving this polynomial equation for $\lambda$ yields the eigenvalues. The left side $p(\lambda) = \det(\mathbf{A} - \lambda \mathbf{I})$ is the characteristic polynomial of degree $n$.

### 2. Finding Eigenvectors
*   Once an eigenvalue $\lambda$ is found, substitute it back into the equation $(\mathbf{A} - \lambda \mathbf{I})\mathbf{v} = \mathbf{0}$.
*   Solve this homogeneous system of linear equations for the vector $\mathbf{v}$. The non-zero solutions $\mathbf{v}$ are the eigenvectors corresponding to that eigenvalue $\lambda$.
*   The set of all eigenvectors corresponding to a single eigenvalue $\lambda$, together with the zero vector, forms a subspace called the **eigenspace** for $\lambda$, denoted $E_\lambda$. Any non-zero vector in the eigenspace is an eigenvector.

### 3. Geometric Interpretation
*   Eigenvectors represent the **axes** or **directions** that remain invariant (up to scaling) under the linear transformation defined by $\mathbf{A}$.
*   Eigenvalues represent the **scaling factor** along those invariant directions.
    *   $|\lambda| > 1$: Stretching along the eigenvector direction.
    *   $0 < |\lambda| < 1$: Compression along the eigenvector direction.
    *   $\lambda < 0$: Stretching/compression plus a reflection (direction reversal).
    *   $\lambda = 1$: Vector remains unchanged (lies in the eigenspace $E_1$).
    *   $\lambda = 0$: Vector is mapped to the zero vector (lies in the null space / kernel). This happens if $\mathbf{A}$ is singular.
    *(Visual Idea: An Excalidraw showing a transformation (e.g., shear) applied to a grid, highlighting vectors that only scale (eigenvectors) versus those that change direction).*

### 4. Properties
*   An $n \times n$ matrix has exactly $n$ eigenvalues (roots of the characteristic polynomial), counting algebraic multiplicities, which may be real or complex conjugate pairs for real matrices.
*   Eigenvectors corresponding to *distinct* eigenvalues are [[../04 Vector Spaces and Concepts/01_Linear_Independence|linearly independent]].
*   The [[../03 Matrix Properties and Concepts/03_Determinant|determinant]] of $\mathbf{A}$ is the product of its eigenvalues: $\det(\mathbf{A}) = \prod_{i=1}^n \lambda_i$.
*   The [[../03 Matrix Properties and Concepts/04_Trace|trace]] of $\mathbf{A}$ is the sum of its eigenvalues: $\text{tr}(\mathbf{A}) = \sum_{i=1}^n \lambda_i$.
*   For **symmetric matrices** (real), eigenvalues are always real, and eigenvectors corresponding to distinct eigenvalues are orthogonal. Symmetric matrices are always diagonalizable by an orthogonal matrix.

## Connections to Other Topics & Relevance
*   **[[Eigendecomposition|Eigendecomposition]]:** If an $n \times n$ matrix $\mathbf{A}$ has $n$ linearly independent eigenvectors (is diagonalizable), it can be factorized as $\mathbf{A = V\Lambda V^{-1}}$, where $\mathbf{V}$ has eigenvectors as columns and $\mathbf{\Lambda}$ is a diagonal matrix of eigenvalues. This simplifies matrix powers ($\mathbf{A}^k = \mathbf{V\Lambda}^k \mathbf{V}^{-1}$) and understanding the transformation.
*   **Principal Component Analysis (PCA):** A fundamental dimensionality reduction technique. PCA finds the eigenvectors (principal components) and eigenvalues (variance along components) of the data's [[../04 Expectation Variance Covariance/03_Covariance_and_Correlation|covariance matrix]] (which is symmetric) to identify directions of maximum variance.
*   **Stability Analysis:** In dynamical systems ($\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t$) and differential equations ($\frac{d\mathbf{x}}{dt} = \mathbf{A}\mathbf{x}$), the eigenvalues of system matrix $\mathbf{A}$ determine the stability of equilibrium points (e.g., if all $|\lambda_i|<1$ for discrete systems, or $\text{Re}(\lambda_i)<0$ for continuous systems).
*   **Graph Theory:** Eigenvalues of adjacency or Laplacian matrices reveal properties of graphs (e.g., connectivity, clustering in spectral clustering).
*   **Quantum Mechanics:** Eigenvalues represent measurable quantities (like energy levels), and eigenvectors represent the corresponding states.

## Summary
*   **Eigenvectors ($\mathbf{v}$)** of a square matrix $\mathbf{A}$ are non-zero vectors whose direction is unchanged by transformation $\mathbf{A}$: $\mathbf{Av = \lambda v}$.
*   **Eigenvalues ($\lambda$)** are the scalar factors by which eigenvectors are scaled: $\mathbf{Av = \lambda v}$.
*   Eigenvalues $\lambda$ found by solving $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$ (characteristic equation).
*   Eigenvectors $\mathbf{v}$ found by solving $(\mathbf{A} - \lambda \mathbf{I})\mathbf{v} = \mathbf{0}$ for each $\lambda$.
*   Represent invariant directions and scaling factors of a linear transformation.
*   Used in PCA, stability analysis, graph analysis, and matrix decomposition.

## Sources
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 6)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   [Khan Academy: Eigenvalues and Eigenvectors](https://www.khanacademy.org/math/linear-algebra/alternate-bases/eigen-everything/v/eigenvectors-and-eigenvalues)
*   [3Blue1Brown: Eigenvectors and Eigenvalues | Essence of Linear Algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g) (Excellent geometric intuition)

## TAGS
[[Linear Algebra]] [[Matrix Decomposition]] [[Eigenvalue]] [[Eigenvector]] [[Eigenspace]] [[Characteristic Equation]] [[Determinant]] [[Trace]] [[PCA]] [[02 Math/index]] [[Foundations]] [[Machine Learning]]