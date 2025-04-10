# Matrix Operations

## Definition / Introduction
*   Matrix operations define how [[03_Matrices|matrices]] interact with each other, with [[02_Vectors|vectors]], and with [[01_Scalars|scalars]].
*   These operations allow us to manipulate blocks of data, solve systems of equations, represent and combine linear transformations, and perform computations essential to machine learning models.
*   Core operations include matrix addition, scalar multiplication, matrix-vector multiplication, matrix-matrix multiplication, and transposition.

## Key Concepts

### 1. Matrix Addition and Subtraction
*   **Definition:** Adding or subtracting two matrices of the **same dimensions** by adding/subtracting their corresponding elements.
*   **Rule:** If $\mathbf{A}$ and $\mathbf{B}$ are both $m \times n$ matrices, then $(\mathbf{A} + \mathbf{B})_{ij} = A_{ij} + B_{ij}$ and $(\mathbf{A} - \mathbf{B})_{ij} = A_{ij} - B_{ij}$. The result is also an $m \times n$ matrix.
*   **Cannot** add/subtract matrices of different shapes.
*   **Properties:** Commutative ($\mathbf{A}+\mathbf{B} = \mathbf{B}+\mathbf{A}$), Associative ($(\mathbf{A}+\mathbf{B})+\mathbf{C} = \mathbf{A}+(\mathbf{B}+\mathbf{C})$).

### 2. Scalar Multiplication
*   **Definition:** Multiplying a matrix $\mathbf{A}$ by a scalar $c$.
*   **Rule:** If $c$ is a scalar and $\mathbf{A}$ is an $m \times n$ matrix, then $(c\mathbf{A})_{ij} = c \cdot A_{ij}$. The result $c\mathbf{A}$ is an $m \times n$ matrix where every element is multiplied by $c$.
*   **Properties:** Distributive ($c(\mathbf{A}+\mathbf{B}) = c\mathbf{A} + c\mathbf{B}$, $(c+d)\mathbf{A} = c\mathbf{A} + d\mathbf{A}$), Associative ($(cd)\mathbf{A} = c(d\mathbf{A})$).

### 3. Matrix-Vector Multiplication
*   **Definition:** Multiplying an $m \times n$ matrix $\mathbf{A}$ by an $n \times 1$ column vector $\mathbf{x}$. The number of **columns in the matrix** ($n$) must equal the number of **rows (components) in the vector** ($n$).
*   **Result:** An $m \times 1$ column vector $\mathbf{y}$. $\mathbf{y} = \mathbf{Ax}$.
*   **Rule (Dot Product View):** The $i$-th element of the resulting vector $\mathbf{y}$ ($y_i$) is the [[01_Vector_Operations|dot product]] of the **$i$-th row of matrix $\mathbf{A}$** (viewed as a row vector) with the vector $\mathbf{x}$.
    $$ y_i = (\text{Row } i \text{ of } \mathbf{A}) \cdot \mathbf{x} = \sum_{j=1}^n A_{ij} x_j $$
*   **Rule (Linear Combination View):** The resulting vector $\mathbf{y}$ is a [[01_Vector_Operations|linear combination]] of the **columns of matrix $\mathbf{A}$**, where the coefficients are the elements of vector $\mathbf{x}$.
    $$ \mathbf{y} = x_1 (\text{Col } 1 \text{ of } \mathbf{A}) + x_2 (\text{Col } 2 \text{ of } \mathbf{A}) + \dots + x_n (\text{Col } n \text{ of } \mathbf{A}) $$
*   **Significance:** Represents applying a linear transformation (defined by $\mathbf{A}$) to a vector ($\mathbf{x}$), resulting in a transformed vector ($\mathbf{y}$). Core operation in solving $\mathbf{Ax=b}$ and in neural network layers ($\text{output} = \text{activation}(\mathbf{W}\mathbf{input} + \mathbf{b})$).

### 4. Matrix-Matrix Multiplication
*   **Definition:** Multiplying an $m \times n$ matrix $\mathbf{A}$ by an $n \times p$ matrix $\mathbf{B}$. The number of **columns in the first matrix ($\mathbf{A}$)** ($n$) must equal the number of **rows in the second matrix ($\mathbf{B}$)** ($n$).
*   **Result:** An $m \times p$ matrix $\mathbf{C}$. $\mathbf{C} = \mathbf{AB}$.
*   **Rule:** The element $C_{ij}$ (in row $i$, column $j$ of the result) is the [[01_Vector_Operations|dot product]] of the **$i$-th row of matrix $\mathbf{A}$** with the **$j$-th column of matrix $\mathbf{B}$**.
    $$ C_{ij} = (\text{Row } i \text{ of } \mathbf{A}) \cdot (\text{Col } j \text{ of } \mathbf{B}) = \sum_{k=1}^n A_{ik} B_{kj} $$
*   **Properties:**
    *   **NOT Commutative:** In general, $\mathbf{AB \neq BA}$ (BA might not even be defined or have different dimensions). Order matters!
    *   **Associative:** $(\mathbf{AB})\mathbf{C} = \mathbf{A}(\mathbf{BC})$.
    *   **Distributive:** $\mathbf{A}(\mathbf{B}+\mathbf{C}) = \mathbf{AB} + \mathbf{AC}$, $(\mathbf{A}+\mathbf{B})\mathbf{C} = \mathbf{AC} + \mathbf{BC}$.
*   **Significance:** Represents composing linear transformations (applying transformation B then transformation A). Fundamental to many algorithms and deep learning computations.

### 5. Transposition
*   **Definition:** Swapping the rows and columns of a matrix $\mathbf{A}$ to get its transpose $\mathbf{A}^T$.
*   **Rule:** $(\mathbf{A}^T)_{ij} = A_{ji}$. If $\mathbf{A}$ is $m \times n$, then $\mathbf{A}^T$ is $n \times m$.
*   **Properties:**
    *   $(\mathbf{A}^T)^T = \mathbf{A}$
    *   $(\mathbf{A} + \mathbf{B})^T = \mathbf{A}^T + \mathbf{B}^T$
    *   $(c\mathbf{A})^T = c\mathbf{A}^T$
    *   **(Reverse Order Law):** $(\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T$ (Order reverses!)

## Connections to Other Topics
*   Matrix multiplication allows solving systems of linear equations $\mathbf{Ax=b}$.
*   Core operations used in defining and computing [[02_Inverse_Matrix|Matrix Inverses]], [[03_Determinant|Determinants]], and performing matrix [[03_Overview|Decompositions]] (like SVD, Eigendecomposition).
*   Foundation for computations in [[../../06 Machine Learning/02 Supervised/01 Regression/01_Simple Linear Regression/Linear Regression|Linear Regression]] (Normal Equation involves $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$), [[../../07 Deep Learning/01 Foundational Models/Neural Networks/01 The Basics/01_Introduction|Neural Networks]], Principal Component Analysis (PCA), etc.

## Summary
*   **Matrix Addition/Subtraction:** Element-wise, requires same dimensions.
*   **Scalar Multiplication:** Multiply every element by the scalar.
*   **Matrix-Vector Multiplication ($\mathbf{Ax=y}$):** Result $y_i$ is dot product of $\text{Row } i \text{ of } \mathbf{A}$ with $\mathbf{x}$. Transforms vector $\mathbf{x}$. Requires $\text{cols}(\mathbf{A}) = \text{rows}(\mathbf{x})$.
*   **Matrix-Matrix Multiplication ($\mathbf{AB=C}$):** Result $C_{ij}$ is dot product of $\text{Row } i \text{ of } \mathbf{A}$ with $\text{Col } j \text{ of } \mathbf{B}$. Composes transformations. Requires $\text{cols}(\mathbf{A}) = \text{rows}(\mathbf{B})$. **Not commutative**.
*   **Transpose ($\mathbf{A}^T$):** Swap rows and columns. $(\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T$.

## Sources
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 2)
*   [Khan Academy: Matrix Operations](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices) (Multiple videos on addition, mult, etc.)
*   [3Blue1Brown: Matrix Multiplication | Essence of Linear Algebra](https://www.youtube.com/watch?v=XkY2DOUCWMU)

## TAGS
[[Linear Algebra]] [[Basic Operation]] [[Matrix]] [[Vector]] [[Matrix Multiplication]] [[Matrix Addition]] [[Scalar Multiplication]] [[Transpose]] [[02 Math/index]] [[Foundations]] [[Machine Learning]] [[Deep Learning]]