---
tags:
- Core Object
- Deep Learning
- Foundations
- Linear Algebra
- Machine Learning
- NLP
- Vector
- Vector Space
---

# Vectors

## Definition / Introduction
*   In Linear Algebra, a **vector** is an ordered list (or array) of numbers ([[01_Scalars|scalars]]). It can be thought of as representing a point in space or a quantity having both **magnitude** and **direction**.
*   Vectors are fundamental objects used to represent data points, features, parameters in models, embeddings, and directions in multi-dimensional spaces.
*   They are typically represented as **column vectors** (most common in ML/DL contexts) or row vectors.

## Key Concepts

### 1. Representation
*   **Notation:** Usually denoted by lowercase bold letters (e.g., $\mathbf{v}, \mathbf{x}, \mathbf{w}$) or lowercase letters with an arrow (e.g., $\vec{v}$).
*   **Components/Elements:** The individual numbers ([[01_Scalars|scalars]]) within the vector. $v_i$ is the $i$-th component.
*   **Dimension:** The number of components ($n$) in the vector determines its dimension. A vector $\mathbf{v} \in \mathbb{R}^n$ is an n-dimensional real vector.
*   **Column Vector:** Written vertically:
    $$ \mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n $$
*   **Row Vector:** Written horizontally:
    $$ \mathbf{v}^T = \begin{bmatrix} v_1 & v_2 & \dots & v_n \end{bmatrix} \in \mathbb{R}^{1 \times n} $$
    Often represented as the **[[02_Matrix_Operations|transpose]]** (denoted by $T$) of a column vector.

### 2. Geometric Interpretation
*   A vector $\mathbf{v}$ in $\mathbb{R}^n$ can be visualized (for $n=2, 3$) as:
    *   An **arrow** starting from the origin $\mathbf{0} = [0, ..., 0]^T$ and ending at the point specified by its components $(v_1, v_2, ..., v_n)$.
    *   The **position vector** of the point $(v_1, v_2, ..., v_n)$ relative to the origin.
*   The **magnitude** (or length or [[03_L2_Norm_Euclidean|norm]], often $||\mathbf{v}||$) of the vector corresponds to the length of the arrow.
*   The **direction** corresponds to the orientation of the arrow in space.

### 3. Algebraic Interpretation
*   An ordered list of numbers representing attributes or coordinates.

### 4. Examples in Data Science / AI
*   **Data Point:** A single observation (e.g., a user, an image) can be represented as a vector where each component is a feature value (e.g., $[\text{age}, \text{income}, \text{pages\_visited}]^T$).
*   **Feature Vector:** The collection of features for one data point.
*   **Parameters/Weights:** The weights connecting neurons in a layer, or the weights of a linear model, are often organized into vectors (or [[03_Matrices|matrices]]).
*   **Word Embeddings (NLP):** Words are represented as dense vectors in a high-dimensional space, where similar words have vectors close to each other (e.g., Word2Vec, GloVe).
*   **Gradients:** The [[../04 Calculus/02 Multivariable Calculus/03_Gradient|gradient]] $\nabla f$ of a scalar function $f$ with respect to multiple variables is a vector pointing in the direction of the steepest ascent. Used in optimization.

## Connections to Other Topics
*   Vectors are composed of [[01_Scalars|Scalars]].
*   [[01_Vector_Operations|Vector Operations]] (addition, scalar multiplication, dot product) define how vectors interact.
*   Vectors form the columns or rows of [[03_Matrices|Matrices]].
*   The concept of [[01_Linear_Independence|Linear Independence]], [[02_Span_and_Basis|Span, and Basis]] revolves around vectors.
*   [[02 Math/03 Linear Algebra/05 Norms/01_Definition|Norms]] measure the magnitude (length) of vectors.

## Summary
*   A **vector** ($\mathbf{v}$) is an ordered list (array) of numbers ([[01_Scalars|scalars]]).
*   Represents magnitude and direction, or a point/location in space $\mathbb{R}^n$.
*   Typically written as column vectors $\begin{bmatrix} ... \end{bmatrix}$ in ML contexts. Dimension = number of components.
*   Fundamental for representing data points, features, parameters, embeddings, and gradients.

## Sources
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   *Introduction to Linear Algebra* by Gilbert Strang (Chapter 1)
*   [Khan Academy: Vectors](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/vectors/v/vector-introduction-linear-algebra)
*   [3Blue1Brown: Vectors | Essence of Linear Algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs) (Excellent visual intuition)