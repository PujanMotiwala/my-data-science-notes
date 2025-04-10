# Linear Independence

## Simple Idea
*   Imagine you have a set of [[../01 Core Objects/02_Vectors|vectors]]. They are **linearly independent** if none of the vectors in the set can be created by just stretching, shrinking, and adding together the *other* vectors in the set. Each vector adds a genuinely new direction or dimension that the others can't replicate.
*   If you *can* create one vector from the others, the set is **linearly dependent** – there's some redundancy in the directions they represent.

## Formal Definition
*   A set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, ..., \mathbf{v}_k\}$ is **linearly independent** if the only solution to the [[../02 Basic Operations/01_Vector_Operations|linear combination]] equation:
    $$ c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_k\mathbf{v}_k = \mathbf{0} $$
    is the **trivial solution**, where all the [[../01 Core Objects/01_Scalars|scalar]] coefficients are zero ($c_1 = c_2 = \dots = c_k = 0$). Here, $\mathbf{0}$ represents the zero vector.
*   If there exists *any* non-trivial solution (where at least one $c_i \neq 0$), then the set of vectors is **linearly dependent**.

## Key Concepts

### 1. Checking for Linear Independence
*   **Small Sets:**
    *   A set with one vector $\{\mathbf{v}\}$ is linearly independent unless $\mathbf{v} = \mathbf{0}$.
    *   Two vectors $\{\mathbf{u}, \mathbf{v}\}$ are linearly independent unless one is a scalar multiple of the other ($\mathbf{u} = c\mathbf{v}$). Geometrically, they don't lie on the same line through the origin.
*   **General Method (using Matrix):**
    1.  Form a [[../01 Core Objects/03_Matrices|matrix]] $\mathbf{A}$ where the vectors $\mathbf{v}_1, ..., \mathbf{v}_k$ are the columns: $\mathbf{A} = [\mathbf{v}_1 \dots \mathbf{v}_k]$.
    2.  The equation $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k = \mathbf{0}$ is equivalent to the homogeneous system $\mathbf{A}\mathbf{c} = \mathbf{0}$, where $\mathbf{c} = [c_1, ..., c_k]^T$.
    3.  Solve the system $\mathbf{A}\mathbf{c} = \mathbf{0}$.
    4.  If the only solution is $\mathbf{c} = \mathbf{0}$ (the trivial solution), the vectors (columns) are linearly independent.
    5.  If there are non-zero solutions for $\mathbf{c}$, the vectors are linearly dependent.
*   **Using Rank:** The columns of matrix $\mathbf{A}$ (size $m \times k$) are linearly independent if and only if the [[../04 Vector Spaces and Concepts/03_Rank|rank]] of the matrix equals the number of columns ($\text{rank}(\mathbf{A}) = k$). Requires $k \le m$.
*   **Using Determinant (for square matrices):** If $\mathbf{A}$ is a square matrix ($k=m=n$, number of vectors equals their dimension), the columns are linearly independent if and only if $\det(\mathbf{A}) \neq 0$.

### 2. Linear Dependence Implication
*   If a set $\{\mathbf{v}_1, ..., \mathbf{v}_k\}$ is linearly dependent, it means at least one vector in the set can be expressed as a [[../02 Basic Operations/01_Vector_Operations|linear combination]] of the others. This indicates redundancy within the set.

### 3. Geometric Interpretation
*   **Linearly Independent:** The vectors point in sufficiently "different" directions so that none lie in the geometric space (line, plane, hyperplane) [[../04 Vector Spaces and Concepts/02_Span_and_Basis|spanned]] by the others.
*   **Linearly Dependent:** At least one vector lies within the span (line, plane, hyperplane) of the other vectors.

## Connections to Other Topics
*   Fundamental concept for defining a [[../04 Vector Spaces and Concepts/02_Span_and_Basis|Basis]] of a [[../04 Vector Spaces and Concepts/Vector Space|Vector Space]]. A basis is a set of linearly independent vectors that also spans the space.
*   Determines the [[../04 Vector Spaces and Concepts/03_Rank|Rank]] of a matrix (which is the number of linearly independent columns or rows).
*   Related to whether a matrix is [[../03 Matrix Properties and Concepts/02_Inverse_Matrix|invertible]] ($\det(\mathbf{A}) \neq 0$ means columns are linearly independent for a square matrix).
*   In Machine Learning: Helps understand feature redundancy. If feature vectors are linearly dependent, it might indicate multicollinearity or that some features don't add new information.

## Summary
*   **Linearly Independent:** A set of vectors where none can be written as a linear combination of the others. The only way $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k = \mathbf{0}$ is if all $c_i = 0$. Each vector adds a new direction.
*   **Linearly Dependent:** At least one vector is redundant (a linear combination of others). There's a non-trivial solution (some $c_i \neq 0$) to $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k = \mathbf{0}$.
*   Checked using systems of equations ($\mathbf{Ac=0}$), [[../04 Vector Spaces and Concepts/03_Rank|rank]], or [[../03 Matrix Properties and Concepts/03_Determinant|determinants]] (for square matrices).
*   Essential for understanding basis, rank, and matrix invertibility.

## Sources
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 2 & 3)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   [Khan Academy: Linear Independence](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/linear-independence/v/linear-independence-definition)
*   [3Blue1Brown: Linear Combinations, Span, Basis | Essence of Linear Algebra](https://www.youtube.com/watch?v=k7RM-ot2NWY)

## TAGS
[[Linear Algebra]] [[Vector Space]] [[Linear Independence]] [[Linear Dependence]] [[Basis]] [[Span]] [[Rank]] [[Determinant]] [[02 Math/index]] [[Foundations]]