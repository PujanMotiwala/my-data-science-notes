# Vector Operations

## Definition / Introduction
*   Vector operations define how [[../01 Core Objects/02_Vectors|vectors]] interact with each other and with [[../01 Core Objects/01_Scalars|scalars]].
*   These operations form the basis of linear algebra and allow us to manipulate vectors algebraically and understand their geometric relationships.
*   The core operations are vector addition, scalar multiplication, and the dot product (inner product).

## Key Concepts

### 1. Vector Addition
*   **Definition:** Adding two vectors of the **same dimension** by adding their corresponding components.
*   **Algebraic Rule:** If $\mathbf{u} = [u_1, u_2, ..., u_n]^T$ and $\mathbf{v} = [v_1, v_2, ..., v_n]^T$, then:
    $$ \mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{bmatrix} $$
*   **Geometric Interpretation:** The "tip-to-tail" rule or parallelogram rule. Place the tail of vector $\mathbf{v}$ at the tip of vector $\mathbf{u}$. The sum $\mathbf{u} + \mathbf{v}$ is the vector from the origin (tail of $\mathbf{u}$) to the tip of $\mathbf{v}$. It forms the diagonal of the parallelogram spanned by $\mathbf{u}$ and $\mathbf{v}$.
*   **Properties:** Commutative ($\mathbf{u}+\mathbf{v} = \mathbf{v}+\mathbf{u}$), Associative ($(\mathbf{u}+\mathbf{v})+\mathbf{w} = \mathbf{u}+(\mathbf{v}+\mathbf{w})$).

### 2. Scalar Multiplication
*   **Definition:** Multiplying a vector by a scalar $c$, which scales the vector's magnitude and/or reverses its direction.
*   **Algebraic Rule:** If $c$ is a scalar and $\mathbf{v} = [v_1, v_2, ..., v_n]^T$, then:
    $$ c\mathbf{v} = \begin{bmatrix} c v_1 \\ c v_2 \\ \vdots \\ c v_n \end{bmatrix} $$
*   **Geometric Interpretation:**
    *   Multiplying by $c > 1$ stretches the vector.
    *   Multiplying by $0 < c < 1$ shrinks the vector.
    *   Multiplying by $c = -1$ reverses the vector's direction.
    *   Multiplying by $c < 0$ stretches/shrinks and reverses direction.
    *   The resulting vector $c\mathbf{v}$ lies on the same line through the origin as $\mathbf{v}$.
*   **Properties:** Distributive ($c(\mathbf{u}+\mathbf{v}) = c\mathbf{u} + c\mathbf{v}$, $(c+d)\mathbf{v} = c\mathbf{v} + d\mathbf{v}$), Associative ($(cd)\mathbf{v} = c(d\mathbf{v})$).

### 3. Linear Combination
*   **Definition:** A vector formed by adding scalar multiples of other vectors. Given vectors $\mathbf{v}_1, \mathbf{v}_2, ..., \mathbf{v}_k$ and scalars $c_1, c_2, ..., c_k$, a linear combination is:
    $$ \mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_k\mathbf{v}_k = \sum_{i=1}^k c_i \mathbf{v}_i $$
*   **Significance:** Fundamental concept related to [[../04 Vector Spaces and Concepts/02_Span_and_Basis|Span]] and [[../04 Vector Spaces and Concepts/01_Linear_Independence|Linear Independence]].

### 4. Dot Product (Inner Product or Scalar Product)
*   **Definition:** An operation between two vectors of the **same dimension** ($n$) that results in a **single scalar value**.
*   **Algebraic Rule:** If $\mathbf{u} = [u_1, ..., u_n]^T$ and $\mathbf{v} = [v_1, ..., v_n]^T$, their dot product (denoted $\mathbf{u} \cdot \mathbf{v}$ or $\mathbf{u}^T\mathbf{v}$) is:
    $$ \mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T\mathbf{v} = u_1 v_1 + u_2 v_2 + \dots + u_n v_n = \sum_{i=1}^n u_i v_i $$
    *(Note: $\mathbf{u}^T\mathbf{v}$ emphasizes viewing it as matrix multiplication of a $1 \times n$ row vector by an $n \times 1$ column vector).*
*   **Geometric Interpretation:** Relates to the angle $\theta$ between the two vectors and their [[../05 Norms/03_L2_Norm_Euclidean|magnitudes (L₂ norms)]] $||\mathbf{u}||_2, ||\mathbf{v}||_2$:
    $$ \mathbf{u} \cdot \mathbf{v} = ||\mathbf{u}||_2 \, ||\mathbf{v}||_2 \cos(\theta) $$
*   **Significance & Use Cases:**
    *   **Calculating Vector Length:** $\mathbf{v} \cdot \mathbf{v} = ||\mathbf{v}||_2^2$ (L₂ norm squared).
    *   **Calculating Angle Between Vectors:** $\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{||\mathbf{u}||_2 \, ||\mathbf{v}||_2}$.
    *   **Checking Orthogonality:** Two non-zero vectors $\mathbf{u}$ and $\mathbf{v}$ are orthogonal (perpendicular) if and only if their dot product is zero ($\mathbf{u} \cdot \mathbf{v} = 0$, since $\cos(90^\circ) = 0$).
    *   **Projection:** Calculating the projection of one vector onto another involves the dot product. $\text{proj}_{\mathbf{v}} \mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{||\mathbf{v}||_2^2} \mathbf{v}$.
    *   **Similarity Measure:** In ML/NLP, the cosine similarity ($\cos(\theta)$) measures the similarity in direction between vectors (e.g., word embeddings).
    *   **Weighted Sums:** If $\mathbf{w}$ is a vector of weights and $\mathbf{x}$ is a feature vector, $\mathbf{w} \cdot \mathbf{x} = \mathbf{w}^T \mathbf{x}$ calculates the weighted sum, a core operation in linear models and neural networks.
*   **Properties:** Commutative ($\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$), Distributive ($\mathbf{u} \cdot (\mathbf{v}+\mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$), Scalar Multiplication ($(c\mathbf{u}) \cdot \mathbf{v} = c(\mathbf{u} \cdot \mathbf{v})$).

## Connections to Other Topics
*   These operations define the structure of a [[../04 Vector Spaces and Concepts/Vector Space|Vector Space]].
*   The dot product is used to define [[../05 Norms/03_L2_Norm_Euclidean|vector norms (lengths)]] and angles.
*   Essential for understanding [[../02 Basic Operations/02_Matrix_Operations|Matrix Operations]], especially matrix-vector multiplication.
*   Core components of many algorithms in optimization (gradients), machine learning (linear models, neural nets), and physics simulations.

## Summary
*   **Vector Addition ($\mathbf{u}+\mathbf{v}$):** Component-wise addition (Tip-to-tail geometry). Requires same dimension.
*   **Scalar Multiplication ($c\mathbf{v}$):** Multiply each component by a scalar (scales vector length/direction).
*   **Dot Product ($\mathbf{u} \cdot \mathbf{v}$ or $\mathbf{u}^T\mathbf{v}$):** Sum of component-wise products ($\sum u_i v_i$). Results in a scalar. Geometric meaning: $||\mathbf{u}||_2 \, ||\mathbf{v}||_2 \cos(\theta)$. Used for length, angle, orthogonality checks, projections, weighted sums. Requires same dimension.

## Sources
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 1)
*   [Khan Academy: Vector Operations](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/vectors/v/adding-vectors) (Addition/Scalar Mult), [Dot Product](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/dot-cross-products/v/vector-dot-product-and-vector-length)
*   [3Blue1Brown: Dot Products | Essence of Linear Algebra](https://www.youtube.com/watch?v=LyGKycYT2v0)

## TAGS
[[Linear Algebra]] [[Basic Operation]] [[Vector]] [[Vector Addition]] [[Scalar Multiplication]] [[Dot Product]] [[Inner Product]] [[Linear Combination]] [[Orthogonality]] [[Math]] [[Foundations]] [[Machine Learning]]