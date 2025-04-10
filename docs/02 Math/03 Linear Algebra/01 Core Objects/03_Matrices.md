# Matrices

## Definition / Introduction
*   A **matrix** is a rectangular array or grid of numbers ([[01_Scalars|scalars]]), arranged in rows and columns.
*   Matrices are used to represent linear transformations (like rotation, scaling, shearing), systems of linear equations, datasets, and parameters in machine learning models.
*   They provide a compact way to organize and manipulate related data or coefficients.

## Key Concepts

### 1. Representation
*   **Notation:** Usually denoted by uppercase bold letters (e.g., $\mathbf{A}, \mathbf{X}, \mathbf{W}$).
*   **Elements/Entries:** The individual numbers ([[01_Scalars|scalars]]) within the matrix. An entry is identified by its row index $i$ and column index $j$, often written as $A_{ij}$, $a_{ij}$, or $(\mathbf{A})_{ij}$.
*   **Dimensions (Shape):** Defined by the number of rows ($m$) and the number of columns ($n$). A matrix with $m$ rows and $n$ columns is called an "$m$ by $n$" matrix (written $m \times n$). $\mathbf{A} \in \mathbb{R}^{m \times n}$ is an $m \times n$ real matrix.
*   **Example:** A $2 \times 3$ matrix $\mathbf{A}$:
    $$ \mathbf{A} = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{bmatrix} $$

### 2. Rows and Columns
*   Each row of an $m \times n$ matrix can be viewed as a row [[02_Vectors|vector]] of dimension $n$.
*   Each column of an $m \times n$ matrix can be viewed as a column [[02_Vectors|vector]] of dimension $m$.

### 3. Special Types of Matrices
*   **Square Matrix:** Number of rows equals number of columns ($m = n$).
*   **[[../03 Matrix Properties and Concepts/01_Identity_Matrix|Identity Matrix ($\mathbf{I}$)]]:** A square matrix with 1s on the main diagonal (top-left to bottom-right) and 0s elsewhere. Acts like the number 1 in matrix multiplication.
*   **Zero Matrix ($\mathbf{0}$):** A matrix where all entries are 0.
*   **Diagonal Matrix:** A square matrix where all off-diagonal entries ($i \neq j$) are 0.
*   **Symmetric Matrix:** A square matrix where $A_{ij} = A_{ji}$ for all $i, j$ (equal to its transpose: $\mathbf{A} = \mathbf{A}^T$). [[../04 Expectation Variance Covariance/03_Covariance_and_Correlation|Covariance matrices]] are symmetric.
*   **Transpose ($\mathbf{A}^T$):** Obtained by swapping rows and columns. The transpose of an $m \times n$ matrix is an $n \times m$ matrix where $(\mathbf{A}^T)_{ij} = A_{ji}$.

### 4. Examples in Data Science / AI
*   **Dataset Representation:** An entire dataset can be represented as a matrix where rows correspond to data points (samples) and columns correspond to features. ($n_{\text{samples}} \times n_{\text{features}}$).
*   **Linear Transformations:** Matrices are used to represent linear operations like rotation, scaling, and shearing in computer graphics or feature transformations. Multiplying a vector by a matrix transforms the vector.
*   **Systems of Linear Equations:** The coefficients of a system $\mathbf{Ax = b}$ are represented by matrix $\mathbf{A}$.
*   **Neural Network Weights:** The weights connecting neurons between two layers are often stored in a matrix $\mathbf{W}$, where $W_{ij}$ might be the weight from neuron $j$ in the previous layer to neuron $i$ in the current layer.
*   **[[../04 Expectation Variance Covariance/03_Covariance_and_Correlation|Covariance Matrix]]:** A square matrix $\mathbf{\Sigma}$ representing the pairwise covariances between different features in a dataset. Used in PCA, etc. $\Sigma_{ij} = Cov(X_i, X_j)$.
*   **Adjacency Matrix:** Represents connections in a graph, where $A_{ij} = 1$ if node $i$ is connected to node $j$, and 0 otherwise.

## Connections to Other Topics
*   Matrices are composed of [[01_Scalars|Scalars]] and can be seen as collections of row or column [[02_Vectors|Vectors]].
*   [[../02 Basic Operations/02_Matrix_Operations|Matrix Operations]] (addition, scalar multiplication, matrix multiplication, transpose) define how matrices interact.
*   Concepts like [[../03 Matrix Properties and Concepts/02_Inverse_Matrix|Inverse]], [[../03 Matrix Properties and Concepts/03_Determinant|Determinant]], [[../04 Vector Spaces and Concepts/03_Rank|Rank]], [[../06 Decompositions and Factorizations/01_Eigenvalues_and_Eigenvectors|Eigenvalues/Eigenvectors]], and [[../06 Decompositions and Factorizations/02_Singular_Value_Decomposition_SVD|SVD]] are key properties and operations related to matrices.
*   [[04_Tensors|Tensors]] generalize matrices to more than two dimensions.

## Summary
*   A **matrix** ($\mathbf{A}$) is a rectangular array of numbers ([[01_Scalars|scalars]]) arranged in rows and columns. Dimensions are $m \times n$.
*   Used to represent datasets, linear transformations, systems of equations, model parameters (NN weights), covariance structures.
*   Fundamental object for manipulating blocks of data and representing linear relationships.

## Sources
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 1 & 2)
*   [Khan Academy: Introduction to Matrices](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:mat-intro/v/introduction-to-the-matrix)
*   [3Blue1Brown: Matrix Multiplication | Essence of Linear Algebra](https://www.youtube.com/watch?v=XkY2DOUCWMU) (Focuses on transformation aspect)

## TAGS
[[Linear Algebra]] [[Core Object]] [[Matrix]] [[Vector]] [[Math]] [[Foundations]] [[Machine Learning]] [[Deep Learning]] [[Linear Transformation]]