# Overview of Matrix Decompositions

## Simple Idea
*   Matrix decompositions (or factorizations) are ways of **breaking down a complex [[../01 Core Objects/03_Matrices|matrix]] into a product of simpler, structured matrices**.
*   Think of it like factoring a number (e.g., $12 = 2 \times 2 \times 3$). Factoring a matrix reveals its fundamental properties and makes certain computations much easier.

## Formal Definition
*   A matrix decomposition expresses a given matrix $\mathbf{A}$ as a product of two or more matrices with specific properties (e.g., diagonal, orthogonal, triangular).
    $$ \mathbf{A} = \mathbf{F}_1 \mathbf{F}_2 \dots \mathbf{F}_k $$
    where each $\mathbf{F}_i$ has useful characteristics.

## Why Decompose Matrices?
*   **Solving Linear Systems ($\mathbf{Ax=b}$):** Decompositions like LU or QR provide efficient and numerically stable ways to solve systems.
*   **Understanding Transformations:** Decompositions like [[01_Eigenvalues_and_Eigenvectors|Eigendecomposition]] and [[02_Singular_Value_Decomposition_SVD|SVD]] reveal the geometric action of the matrix (scaling, rotation).
*   **Simplifying Computations:** Calculating [[../03 Matrix Properties and Concepts/03_Determinant|determinants]] ($\det(\mathbf{A}) = \det(\mathbf{F}_1)\dots$), [[../03 Matrix Properties and Concepts/02_Inverse_Matrix|inverses]] ($\mathbf{A}^{-1} = \dots \mathbf{F}_2^{-1}\mathbf{F}_1^{-1}$), and matrix powers ($\mathbf{A}^k$) becomes easier using decomposed forms.
*   **Data Compression & [[../04 Vector Spaces and Concepts/03_Rank|Rank]] Reduction:** [[02_Singular_Value_Decomposition_SVD|SVD]] allows for low-rank approximation, compressing data by retaining essential components.
*   **Revealing Properties:** [[01_Eigenvalues_and_Eigenvectors|Eigenvalues]] from Eigendecomposition indicate stability; singular values from [[02_Singular_Value_Decomposition_SVD|SVD]] relate to matrix rank and energy/variance.
*   **Algorithm Development:** Many algorithms in machine learning (e.g., [[02_Singular_Value_Decomposition_SVD|PCA]], recommender systems) and numerical analysis rely directly on matrix decompositions.

## Key Decompositions Covered

### 1. [[Eigendecomposition|Eigendecomposition]] ($\mathbf{A = V\Lambda V^{-1}}$)
*   **Applies to:** Square matrices with a full set of linearly independent [[01_Eigenvalues_and_Eigenvectors|eigenvectors]] (diagonalizable matrices). Especially useful for symmetric matrices where $\mathbf{V}$ is orthogonal ($\mathbf{V}^{-1} = \mathbf{V}^T$).
*   **Components:**
    *   $\mathbf{V}$: Matrix whose columns are the [[01_Eigenvalues_and_Eigenvectors|eigenvectors]] of $\mathbf{A}$.
    *   $\mathbf{\Lambda}$ (Lambda): Diagonal matrix containing the corresponding [[01_Eigenvalues_and_Eigenvectors|eigenvalues]] ($\lambda_i$) of $\mathbf{A}$.
*   **Use:** Understanding transformation along invariant axes, calculating matrix powers easily ($\mathbf{A}^k = \mathbf{V\Lambda}^k \mathbf{V}^{-1}$), stability analysis.

### 2. [[02_Singular_Value_Decomposition_SVD|Singular Value Decomposition (SVD)]] ($\mathbf{A = U \Sigma V^T}$)
*   **Applies to:** *Any* $m \times n$ matrix (most general).
*   **Components:**
    *   $\mathbf{U}, \mathbf{V}$: [[Orthogonal Matrix|Orthogonal matrices]] containing left/right **singular vectors**.
    *   $\mathbf{\Sigma}$ (Sigma): Diagonal ($m \times n$) matrix containing non-negative **singular values** ($\sigma_i$).
*   **Use:** [[../04 Vector Spaces and Concepts/03_Rank|Rank]] determination ($\text{rank} = \#$ non-zero $\sigma_i$), low-rank approximation (compression, noise reduction), [[02_Singular_Value_Decomposition_SVD|PCA]], solving linear systems (via pseudoinverse), recommender systems.

## Other Common Decompositions (Brief Mention)

*   **LU Decomposition ($\mathbf{A = LU}$):** Factors a square matrix $\mathbf{A}$ (under certain conditions) into a **L**ower triangular matrix (with 1s on diagonal) and an **U**pper triangular matrix. Primarily used for efficient solving of $\mathbf{Ax=b}$ via forward/backward substitution.
*   **QR Decomposition ($\mathbf{A = QR}$):** Factors *any* $m \times n$ matrix $\mathbf{A}$ (with $m \ge n$ and linearly independent columns) into an **Q**rthogonal matrix ($m \times n$, $\mathbf{Q}^T\mathbf{Q}=\mathbf{I}$) and an **R**ight (upper) triangular matrix ($n \times n$). Used in solving least-squares problems ($\mathbf{A}^T\mathbf{Ax} = \mathbf{A}^T\mathbf{b} \implies \mathbf{R}^T\mathbf{Q}^T\mathbf{QRx} = \mathbf{R}^T\mathbf{Q}^T\mathbf{b} \implies \mathbf{Rx} = \mathbf{Q}^T\mathbf{b}$) and for eigenvalue algorithms (QR algorithm).
*   **Cholesky Decomposition ($\mathbf{A = LL^T}$ or $\mathbf{A = R^T R}$):** Factors a **symmetric, positive-definite** matrix $\mathbf{A}$ into a **L**ower triangular matrix $\mathbf{L}$ and its transpose $\mathbf{L}^T$ (or an upper triangular $\mathbf{R}$ and its transpose). Very efficient ($\sim \frac{1}{2}$ cost of LU) for solving systems with such matrices (common in statistics, e.g., with covariance matrices) and for Monte Carlo simulation of correlated variables.

## Connections to Other Topics
*   All decompositions rely on the fundamental concepts of [[../01 Core Objects/03_Matrices|matrices]], [[../02 Basic Operations/02_Matrix_Operations|matrix operations]], [[../04 Vector Spaces and Concepts/01_Linear_Independence|linear independence]], [[../04 Vector Spaces and Concepts/02_Span_and_Basis|span]], and [[../04 Vector Spaces and Concepts/03_Rank|rank]].
*   [[01_Eigenvalues_and_Eigenvectors|Eigenvalues]]/vectors and singular values/vectors are key outputs of specific decompositions.
*   [[Orthogonal Matrix|Orthogonal matrices]] (like $\mathbf{U}, \mathbf{V}, \mathbf{Q}$) play a crucial role as they represent rotations/reflections and preserve lengths and angles ($\|\mathbf{Qx}\|_2 = \|\mathbf{x}\|_2$), leading to numerical stability.

## Summary
*   **Matrix Decompositions** factorize matrices into simpler, structured components ($\mathbf{A} = \mathbf{F}_1\mathbf{F}_2\dots$).
*   Reveal matrix properties and simplify computations (solving systems, inverses, powers, determinants).
*   **[[Eigendecomposition|Eigendecomposition]] ($\mathbf{A=V\Lambda V^{-1}}$):** For diagonalizable square matrices, reveals invariant directions ([[01_Eigenvalues_and_Eigenvectors|eigenvectors]]) and scaling factors ([[01_Eigenvalues_and_Eigenvectors|eigenvalues]]).
*   **[[02_Singular_Value_Decomposition_SVD|SVD]] ($\mathbf{A=U\Sigma V^T}$):** For *any* matrix, reveals principal directions and scaling factors (singular vectors/values). Foundational for PCA, low-rank approximation.
*   Other types (LU, QR, Cholesky) exist for specific computational tasks (solving systems, least squares).

## Sources
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapters on Eigenvalues, SVD, Factorizations)
*   *Numerical Linear Algebra* by Trefethen and Bau (Focuses on computational aspects and stability)
*   [Wikipedia: Matrix decomposition](https://en.wikipedia.org/wiki/Matrix_decomposition)

## TAGS
[[Linear Algebra]] [[Matrix Decomposition]] [[Factorization]] [[Eigenvalue]] [[Eigenvector]] [[Eigendecomposition]] [[Singular Value Decomposition]] [[SVD]] [[LU Decomposition]] [[QR Decomposition]] [[Cholesky Decomposition]] [[Orthogonal Matrix]] [[02 Math/index]] [[Foundations]] [[Machine Learning]] [[Numerical Linear Algebra]]