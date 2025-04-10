---
tags:
- Dimensionality Reduction
- Foundations
- Linear Algebra
- Low-Rank Approximation
- Machine Learning
- Matrix Decomposition
- Orthogonal Matrix
- PCA
- Pseudoinverse
- Rank
- Recommender Systems
- SVD
- Singular Value
- Singular Value Decomposition
- Singular Vector
---

# Singular Value Decomposition (SVD)

## Simple Idea
*   Think of Singular Value Decomposition (SVD) as a way to break down *any* [[03_Matrices|matrix]] $\mathbf{A}$ (even non-square ones) into three simpler matrices: $\mathbf{U}$, $\mathbf{\Sigma}$ (Sigma), and $\mathbf{V}^T$.
*   **Geometric Intuition:** SVD describes the action of matrix $\mathbf{A}$ as a combination of three fundamental geometric operations:
    1.  A **rotation** (or reflection) in the input space, described by $\mathbf{V}^T$. This aligns the input basis vectors along principal directions.
    2.  A **scaling** along these principal axes, defined by the diagonal matrix $\mathbf{\Sigma}$. Some axes might be scaled to zero if the matrix reduces dimension.
    3.  Another **rotation** (or reflection) in the output space, described by $\mathbf{U}$. This aligns the scaled axes into the final output orientation.
*   It essentially finds the most important "input directions" (right-singular vectors in $\mathbf{V}$), "output directions" (left-singular vectors in $\mathbf{U}$), and "stretching factors" (singular values in $\mathbf{\Sigma}$) associated with the matrix transformation.

## Formal Definition
*   Any $m \times n$ matrix $\mathbf{A}$ with real entries can be factorized into the product of three matrices:
    $$ \mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T $$
*   Where:
    *   $\mathbf{U}$: An $m \times m$ **[[Orthogonal Matrix|orthogonal matrix]]** ($\mathbf{U}^T\mathbf{U} = \mathbf{U}\mathbf{U}^T = \mathbf{I}_m$). Its columns $\mathbf{u}_i$ are the **left-singular vectors** of $\mathbf{A}$. They form an orthonormal [[02_Span_and_Basis|basis]] for the output space $\mathbb{R}^m$. The first $r = \text{rank}(\mathbf{A})$ columns $\{\mathbf{u}_1, ..., \mathbf{u}_r\}$ form a basis for the [[02_Span_and_Basis|column space]] Col(A).
    *   $\mathbf{\Sigma}$ (Sigma): An $m \times n$ **diagonal matrix** (same dimensions as $\mathbf{A}$, possibly rectangular). The diagonal entries $\sigma_i = \Sigma_{ii}$ are the **singular values** of $\mathbf{A}$. They are non-negative and ordered from largest to smallest ($\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$, and $\sigma_{r+1} = \dots = \sigma_{\min(m,n)} = 0$). All off-diagonal entries are zero.
    *   $\mathbf{V}^T$: An $n \times n$ **[[Orthogonal Matrix|orthogonal matrix]]** ($\mathbf{V}^T\mathbf{V} = \mathbf{V}\mathbf{V}^T = \mathbf{I}_n$). Its *rows* are the transposes of the **right-singular vectors** $\mathbf{v}_i$ of $\mathbf{A}$. The columns of $\mathbf{V}$ (the $\mathbf{v}_i$) form an orthonormal [[02_Span_and_Basis|basis]] for the input space $\mathbb{R}^n$. The first $r$ columns $\{\mathbf{v}_1, ..., \mathbf{v}_r\}$ form a basis for the [[02_Span_and_Basis|row space]] Row(A). The remaining $\{\mathbf{v}_{r+1}, ..., \mathbf{v}_n\}$ form a basis for the null space Null(A).

## Key Concepts

### 1. Singular Values ($\sigma_i$)
*   The non-zero singular values $\sigma_1, ..., \sigma_r$ are the square roots of the non-zero [[01_Eigenvalues_and_Eigenvectors|eigenvalues]] ($\lambda_i$) of both $\mathbf{A}^T\mathbf{A}$ and $\mathbf{A}\mathbf{A}^T$. (These two symmetric, positive semidefinite matrices share the same non-zero eigenvalues $\lambda_i = \sigma_i^2$).
    $$ \sigma_i = \sqrt{\lambda_i(\mathbf{A}^T\mathbf{A})} = \sqrt{\lambda_i(\mathbf{A}\mathbf{A}^T)} \quad \text{for } i=1, ..., r $$
*   They represent the "magnitudes" or "stretching factors" of the transformation $\mathbf{A}$ along the principal directions defined by the singular vectors.
*   The number of non-zero singular values is equal to the [[03_Rank|rank]] $r$ of the matrix $\mathbf{A}$.

### 2. Singular Vectors ($\mathbf{u}_i$ and $\mathbf{v}_i$)
*   **Right-singular vectors (columns of $\mathbf{V}$):** Orthonormal [[01_Eigenvalues_and_Eigenvectors|eigenvectors]] of $\mathbf{A}^T\mathbf{A}$. Satisfy $\mathbf{A}^T\mathbf{A}\mathbf{v}_i = \sigma_i^2 \mathbf{v}_i$. They form an orthonormal basis for the input space $\mathbb{R}^n$.
*   **Left-singular vectors (columns of $\mathbf{U}$):** Orthonormal [[01_Eigenvalues_and_Eigenvectors|eigenvectors]] of $\mathbf{A}\mathbf{A}^T$. Satisfy $\mathbf{A}\mathbf{A}^T\mathbf{u}_i = \sigma_i^2 \mathbf{u}_i$. They form an orthonormal basis for the output space $\mathbb{R}^m$.
*   **Relationship:** The singular vectors and values link the input and output spaces via $\mathbf{A}$:
    $$ \mathbf{A}\mathbf{v}_i = \sigma_i \mathbf{u}_i $$
    $$ \mathbf{A}^T\mathbf{u}_i = \sigma_i \mathbf{v}_i $$
    The matrix $\mathbf{A}$ maps a right-singular vector $\mathbf{v}_i$ to a scaled version ($\sigma_i$) of the corresponding left-singular vector $\mathbf{u}_i$.

### 3. Economy (Thin) SVD
*   For a "tall" matrix ($m > n$), often only the first $n$ columns of $\mathbf{U}$ and the top $n \times n$ block of $\mathbf{\Sigma}$ are computed and stored. This is called the **thin SVD**: $\mathbf{A} = \mathbf{U}_n \mathbf{\Sigma}_n \mathbf{V}^T$, where $\mathbf{U}_n$ is $m \times n$ with orthonormal columns and $\mathbf{\Sigma}_n$ is $n \times n$ diagonal. This captures all the non-zero singular values and is often sufficient and more memory-efficient. Similar reduction exists for "wide" matrices ($m < n$).

### 4. Low-Rank Approximation (Truncated SVD)
*   A key application is approximating $\mathbf{A}$ using only the $k$ largest singular values and corresponding singular vectors (where $k < r = \text{rank}(\mathbf{A})$). This is the **truncated SVD**:
    $$ \mathbf{A}_k = \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T $$
    where $\mathbf{U}_k$ uses the first $k$ columns of $\mathbf{U}$, $\mathbf{\Sigma}_k$ uses the top-left $k \times k$ block of $\mathbf{\Sigma}$ (containing $\sigma_1, ..., \sigma_k$), and $\mathbf{V}_k^T$ uses the first $k$ rows of $\mathbf{V}^T$ (or first $k$ columns of $\mathbf{V}$). $\mathbf{A}_k$ is an $m \times n$ matrix with rank $k$.
*   **Eckart-Young-Mirsky Theorem:** $\mathbf{A}_k$ is the **best rank-$k$ approximation** of $\mathbf{A}$ in terms of minimizing the [[04_Frobenius_Norm|Frobenius norm]] (and spectral norm) of the difference: $||\mathbf{A} - \mathbf{A}_k||_F$ is minimized.
*   Larger singular values ($\sigma_i$) correspond to dimensions capturing more "energy" or variance in the data represented by $\mathbf{A}$.

## Connections to Other Topics & Relevance
*   **[[03_Rank|Rank Determination]]:** Number of non-zero singular values $\sigma_i$ = $\text{rank}(\mathbf{A})$.
*   **[[02_Inverse_Matrix|Matrix Inverse]] & Pseudoinverse:** If $\mathbf{A}$ is square and invertible, $\mathbf{A}^{-1} = \mathbf{V} \mathbf{\Sigma}^{-1} \mathbf{U}^T$ (where $\mathbf{\Sigma}^{-1}$ has $1/\sigma_i$ on diagonal). More generally, the **pseudoinverse** $\mathbf{A}^+$ (useful for non-square or singular matrices) is defined as $\mathbf{A}^+ = \mathbf{V} \mathbf{\Sigma}^+ \mathbf{U}^T$, where $\mathbf{\Sigma}^+$ has $1/\sigma_i$ for non-zero $\sigma_i$ and 0 elsewhere. SVD provides a numerically stable way to compute (pseudo)inverses.
*   **Principal Component Analysis (PCA):** SVD is the computational backbone of PCA. Applying SVD to the (mean-centered) data matrix $\mathbf{X}$ (or its covariance matrix) directly reveals the principal components (related to $\mathbf{U}$ or $\mathbf{V}$) and the variance captured by each component (related to $\sigma_i^2$).
*   **Dimensionality Reduction:** Truncated SVD provides a powerful way to reduce the dimensions of data while retaining the most important information (basis of many techniques).
*   **Recommender Systems:** Used in matrix factorization methods (like FunkSVD) to find latent factors for users and items from sparse rating matrices.
*   **Image Compression:** Truncated SVD can compress images by storing only the most significant singular values and vectors.
*   **Noise Reduction:** Small singular values often correspond to noise; setting them to zero (truncation) can help denoise data.
*   **Solving Linear Systems & Least Squares:** SVD provides robust solutions to $\mathbf{Ax=b}$, especially for ill-conditioned or non-square systems (via the pseudoinverse).

## Summary
*   **Singular Value Decomposition (SVD)** factorizes *any* $m \times n$ matrix $\mathbf{A}$ into $\mathbf{U \Sigma V^T}$.
*   $\mathbf{U}$ ($m \times m$), $\mathbf{V}$ ($n \times n$) are **[[Orthogonal Matrix|orthogonal matrices]]** containing left/right **singular vectors** (orthonormal bases for output/input spaces).
*   $\mathbf{\Sigma}$ ($m \times n$) is a **diagonal** matrix containing non-negative **singular values** ($\sigma_i$, ordered largest to smallest), representing scaling factors. $\sigma_i = \sqrt{\lambda_i(\mathbf{A}^T\mathbf{A})}$.
*   $\text{rank}(\mathbf{A})$ = number of non-zero $\sigma_i$.
*   **Truncated SVD** ($\mathbf{A} \approx \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T$) provides the best **low-rank approximation**.
*   Fundamental tool for PCA, dimensionality reduction, recommender systems, solving linear systems, image compression, computing pseudoinverses, and more.

## Sources
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 7)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   [Wikipedia: Singular value decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition)
*   [Explanation & Applications of SVD](https://towardsdatascience.com/singular-value-decomposition-svd-the-swiss-army-knife-of-linear-algebra-5523d55cb8f4)
*   [StatQuest: SVD Explained](https://www.youtube.com/watch?v=mBcLRGuAFUk) (Highly recommended visual explanation)
*   *Numerical Linear Algebra* by Trefethen and Bau