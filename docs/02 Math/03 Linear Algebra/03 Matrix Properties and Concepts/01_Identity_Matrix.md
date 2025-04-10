# Identity Matrix

## Simple Idea
*   Think of the Identity Matrix as the number **1** in the world of [[../01 Core Objects/03_Matrices|matrix]] multiplication. Multiplying any matrix by the Identity matrix (of the right size) leaves the original matrix unchanged.

## Formal Definition
*   The **Identity Matrix**, denoted as $\mathbf{I}$ or $\mathbf{I}_n$ (where $n$ is the dimension), is a square [[../01 Core Objects/03_Matrices|matrix]] ($n \times n$) with **1s** on the main diagonal (from top-left to bottom-right) and **0s** everywhere else.

## Key Concepts

### 1. Representation
*   **Structure:** $(\mathbf{I}_n)_{ij} = 1$ if $i=j$ (on the diagonal), and $(\mathbf{I}_n)_{ij} = 0$ if $i \neq j$ (off-diagonal). Using Kronecker delta: $(\mathbf{I}_n)_{ij} = \delta_{ij}$.
*   **Examples:**
    $$ \mathbf{I}_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \quad \quad \mathbf{I}_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} $$

### 2. Multiplicative Identity Property
*   For any $m \times n$ matrix $\mathbf{A}$:
    $$ \mathbf{I}_m \mathbf{A} = \mathbf{A} $$
*   For any $n \times p$ matrix $\mathbf{B}$:
    $$ \mathbf{B} \mathbf{I}_p = \mathbf{B} $$
*   **Requirement:** The Identity matrix must have compatible dimensions for the [[../02 Basic Operations/02_Matrix_Operations|matrix multiplication]] to be defined. $\mathbf{I}_n$ multiplies $n \times p$ matrices on the left, $\mathbf{I}_n$ multiplies $m \times n$ matrices on the right.

### 3. Role in Linear Transformations
*   As a transformation, the Identity matrix represents "doing nothing". Applying $\mathbf{I}$ to a [[../01 Core Objects/02_Vectors|vector]] $\mathbf{x}$ results in the same vector $\mathbf{x}$: $\mathbf{Ix = x}$.

## Connections to Other Topics
*   Crucial for defining the [[02_Inverse_Matrix|Matrix Inverse]] ($\mathbf{A}^{-1}$), where $\mathbf{A} \mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{I}$.
*   Used in solving systems of linear equations $\mathbf{Ax = b}$.
*   Appears in various matrix [[../06 Decompositions and Factorizations/03_Overview|decompositions]].

## Summary
*   The **Identity Matrix ($\mathbf{I}$)** is the matrix equivalent of the number 1 for multiplication.
*   Square matrix with 1s on diagonal, 0s elsewhere.
*   $\mathbf{IA = A}$ and $\mathbf{AI = A}$ (when dimensions match).
*   Represents a "do nothing" linear transformation.

## Sources
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 2)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   [Khan Academy: Identity Matrix](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:identity-matrix/v/identity-matrix)

## TAGS
[[Linear Algebra]] [[Matrix Property]] [[Identity Matrix]] [[Matrix Multiplication]] [[Math]] [[Foundations]]