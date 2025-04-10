# Matrix Rank

## Simple Idea
*   Think of the **rank** of a [[03_Matrices|matrix]] as the "true dimension" of the space [[02_Span_and_Basis|spanned]] by its rows or columns. It tells you how many directions are genuinely independent or non-redundant within the matrix.
*   A matrix might have many columns, but if some are just [[01_Linear_Independence|linear combinations]] of others, the rank tells you the number of columns that are truly needed to represent the core information.

## Formal Definition
*   The **rank** of a matrix $\mathbf{A}$, denoted $\text{rank}(\mathbf{A})$, is defined as the **dimension** of its **[[02_Span_and_Basis|Column Space]]** (Col(A)).
    $$ \text{rank}(\mathbf{A}) = \dim(\text{Col}(\mathbf{A})) $$
*   Equivalently, it is also the dimension of its **[[02_Span_and_Basis|Row Space]]** (Row(A)).
    $$ \text{rank}(\mathbf{A}) = \dim(\text{Row}(\mathbf{A})) $$
*   The rank represents the maximum number of [[01_Linear_Independence|linearly independent]] columns (or rows) in the matrix.

## Key Concepts

### 1. Relationship between Row Rank and Column Rank
*   A fundamental theorem states that for any $m \times n$ matrix $\mathbf{A}$, the dimension of the row space is equal to the dimension of the column space.
    $$ \dim(\text{Row}(\mathbf{A})) = \dim(\text{Col}(\mathbf{A})) = \text{rank}(\mathbf{A}) $$

### 2. Calculating Rank
*   **Gaussian Elimination (Row Echelon Form):** Reduce the matrix $\mathbf{A}$ to its Row Echelon Form (REF) or Reduced Row Echelon Form (RREF) using elementary row operations. The rank is equal to the **number of non-zero rows** (or equivalently, the number of **pivot positions**) in the echelon form. This is the most common practical method.
*   **Using Linear Independence:** Find the maximum number of columns (or rows) that form a [[01_Linear_Independence|linearly independent]] set.

### 3. Properties of Rank
*   For an $m \times n$ matrix $\mathbf{A}$:
    *   $0 \le \text{rank}(\mathbf{A}) \le \min(m, n)$. The rank cannot exceed the number of rows or columns.
*   **Full Rank:**
    *   A matrix has **full row rank** if $\text{rank}(\mathbf{A}) = m$ (number of rows). Its rows are [[01_Linear_Independence|linearly independent]]. Requires $m \le n$.
    *   A matrix has **full column rank** if $\text{rank}(\mathbf{A}) = n$ (number of columns). Its columns are [[01_Linear_Independence|linearly independent]]. Requires $n \le m$.
    *   A square $n \times n$ matrix has **full rank** if $\text{rank}(\mathbf{A}) = n$. This is equivalent to the matrix being [[02_Inverse_Matrix|invertible]] and having a non-zero [[03_Determinant|determinant]].
*   **Rank of Transpose:** $\text{rank}(\mathbf{A}^T) = \text{rank}(\mathbf{A})$.
*   **Rank of Product:** $\text{rank}(\mathbf{AB}) \le \min(\text{rank}(\mathbf{A}), \text{rank}(\mathbf{B}))$.
*   **Rank and [[02_Inverse_Matrix|Invertibility]]:** An $n \times n$ matrix $\mathbf{A}$ is invertible if and only if $\text{rank}(\mathbf{A}) = n$.
*   **Rank-Nullity Theorem:** For an $m \times n$ matrix $\mathbf{A}$, $\text{rank}(\mathbf{A}) + \text{nullity}(\mathbf{A}) = n$, where $\text{nullity}(\mathbf{A})$ is the dimension of the null space (the space of solutions to $\mathbf{Ax=0}$).

### 4. Geometric Interpretation
*   The rank tells you the dimension of the output space when the matrix $\mathbf{A}$ is viewed as a linear transformation. If $\text{rank}(\mathbf{A}) < n$ for an $n \times n$ matrix, the transformation collapses the n-dimensional input space into a lower-dimensional subspace (a line, a plane, etc.) which is the column space.
    *(Visual Idea: A 3x3 matrix with rank 2 maps all points in 3D space onto a specific plane through the origin. An Excalidraw showing this collapse would be illustrative).*

## Connections to Other Topics & Relevance
*   **[[01_Linear_Independence|Linear Independence]]:** Rank is defined by the maximum number of linearly independent rows/columns.
*   **[[02_Span_and_Basis|Basis]] and Dimension:** Rank is the dimension of the column/row space.
*   **[[02_Inverse_Matrix|Matrix Invertibility]] & [[03_Determinant|Determinant]]:** A square matrix is invertible $\iff$ it has full rank $\iff$ its determinant is non-zero.
*   **Solving Linear Systems $\mathbf{Ax=b}$:** The rank determines the existence and uniqueness of solutions (related via Rank-Nullity Theorem and comparing rank(A) to rank([A|b])).
*   **Dimensionality Reduction (PCA, SVD):** Techniques like [[02_Singular_Value_Decomposition_SVD|Singular Value Decomposition (SVD)]] reveal the rank of a matrix (number of non-zero singular values) and can be used to find low-rank approximations, effectively reducing the dimensionality of data by identifying the most significant "directions" (independent components).
*   **Model Identifiability:** In statistics, the rank of design matrices relates to whether model parameters can be uniquely estimated.

## Summary
*   The **Rank** of a matrix $\mathbf{A}$ ($\text{rank}(\mathbf{A})$) is the maximum number of **[[01_Linear_Independence|linearly independent]]** columns (or rows).
*   It equals the **dimension** of the [[02_Span_and_Basis|Column Space]] (and Row Space).
*   Found by counting non-zero rows (pivots) in Row Echelon Form.
*   $\text{rank}(\mathbf{A}) \le \min(\text{rows}, \text{columns})$.
*   A square matrix is [[02_Inverse_Matrix|invertible]] $\iff$ it has **full rank**.
*   Indicates the "true dimension" of the information captured or the output space of the transformation represented by the matrix.

## Sources
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 3)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   [Khan Academy: Matrix Rank](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/null-and-column-spaces/v/rank-of-a-matrix)

## TAGS
[[Linear Algebra]] [[Vector Space]] [[Matrix Rank]] [[Rank]] [[Linear Independence]] [[Column Space]] [[Row Space]] [[Dimension]] [[Matrix Invertibility]] [[02 Math/index]] [[Foundations]] [[Dimensionality Reduction]]