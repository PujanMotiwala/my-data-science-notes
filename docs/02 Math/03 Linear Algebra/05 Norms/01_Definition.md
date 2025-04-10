# Vector and Matrix Norms: Definition

## Simple Idea
*   A **norm** is basically a way to measure the "size", "length", or "magnitude" of a [[../01 Core Objects/02_Vectors|vector]].
*   For [[../01 Core Objects/03_Matrices|matrices]], norms measure their "magnitude" in a way that often relates to how much they can "stretch" vectors during [[../02 Basic Operations/02_Matrix_Operations|matrix-vector multiplication]].
*   Norms provide a formal concept of distance in vector spaces.

## Formal Definition
*   A **norm** on a [[../04 Vector Spaces and Concepts/Vector Space|vector space]] $V$ is a function $\| \cdot \| : V \to \mathbb{R}$ that assigns a non-negative real-valued length or size to each vector $\mathbf{x} \in V$, satisfying the following properties for all vectors $\mathbf{x}, \mathbf{y} \in V$ and all [[../01 Core Objects/01_Scalars|scalars]] $\alpha \in \mathbb{R}$ (or $\mathbb{C}$):
    1.  **Non-negativity:** $\|\mathbf{x}\| \ge 0$.
    2.  **Definiteness:** $\|\mathbf{x}\| = 0$ if and only if $\mathbf{x} = \mathbf{0}$ (the zero vector).
    3.  **Absolute Homogeneity (Scaling):** $\|\alpha \mathbf{x}\| = |\alpha| \|\mathbf{x}\|$.
    4.  **Triangle Inequality:** $\|\mathbf{x} + \mathbf{y}\| \le \|\mathbf{x}\| + \|\mathbf{y}\|$. (The length of a side of a triangle is less than or equal to the sum of the lengths of the other two sides).

## Key Concepts

### 1. Purpose of Norms
*   **Measure Size/Length:** Quantify the magnitude of vectors.
*   **Define Distance:** The distance between two vectors $\mathbf{x}$ and $\mathbf{y}$ can be defined as the norm of their difference: $d(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|$.
*   **Measure Matrix Magnitude:** Quantify the "size" of a matrix, often related to its amplification effect on vectors.
*   **Regularization in ML:** Specific norms (like [[02_L1_Norm_Manhattan|L₁]] and [[03_L2_Norm_Euclidean|L₂]]) are used in [[../../06 Machine Learning/01 The Basics/02_Model Evaluation/Test metrics/Regularization/Regularization|regularization]] techniques to penalize large parameter values (weights) in models, helping to prevent [[../../06 Machine Learning/01 The Basics/02_Model Evaluation/Issues/Overfitting|overfitting]].
*   **Error Measurement:** Norms are used to measure the difference between predicted and actual values (e.g., the [[03_L2_Norm_Euclidean|L₂ norm]] of the error vector in Mean Squared Error).

### 2. Common Types of Vector Norms (Lₚ norms)
*   The most common vector norms belong to the family of **$L_p$ norms** (or p-norms), defined for $p \ge 1$:
    $$ \|\mathbf{x}\|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p} $$
*   We will cover the most important cases:
    *   **[[02_L1_Norm_Manhattan|L₁ Norm ($p=1$)]]**
    *   **[[03_L2_Norm_Euclidean|L₂ Norm ($p=2$)]]** (The standard Euclidean length)
    *   **L<0xE2><0x88><0x9E> Norm ($p=\infty$):** Maximum absolute value ($||\mathbf{x}||_\infty = \max_i |x_i|$).

### 3. Matrix Norms
*   Measuring the "size" of a matrix is more complex. Common matrix norms include:
    *   **[[04_Frobenius_Norm|Frobenius Norm]]**: Analogous to the vector L₂ norm, treating the matrix as a long vector of its elements.
    *   **Induced Norms (Operator Norms):** Defined based on how the matrix transforms vectors, measuring the maximum "stretching factor" applied to vectors according to a specific vector norm (e.g., induced L₁, L₂, L<0xE2><0x88><0x9E> norms). The induced L₂ norm is also called the spectral norm and equals the largest singular value.

## Connections to Other Topics
*   Used to define distance and convergence in [[../04 Vector Spaces and Concepts/Vector Space|vector spaces]].
*   Essential for [[../../06 Machine Learning/01 The Basics/02_Model Evaluation/Test metrics/Regularization/Regularization|regularization]] in machine learning ([[02_L1_Norm_Manhattan|L1 - Lasso]], [[03_L2_Norm_Euclidean|L2 - Ridge]]).
*   Used in optimization algorithms (e.g., checking convergence based on the norm of the gradient).
*   Fundamental to numerical analysis and error estimation.

## Summary
*   A **norm $\|\mathbf{x}\|$** is a function assigning a non-negative **size/length** to a vector (or matrix).
*   Must satisfy: Non-negativity, Definiteness ($\|\mathbf{x}\|=0 \iff \mathbf{x}=\mathbf{0}$), Scaling ($\|\alpha\mathbf{x}\| = |\alpha| \|\mathbf{x}\|$), Triangle Inequality ($\|\mathbf{x}+\mathbf{y}\| \le \|\mathbf{x}\|+\|\mathbf{y}\|$).
*   Used to measure vector magnitude, distance, matrix size, model parameter penalties (regularization), and errors.
*   Common vector norms include **L₁, L₂, L<0xE2><0x88><0x9E>**. Common matrix norm is **[[04_Frobenius_Norm|Frobenius]]**.

## Sources
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   *Introduction to Linear Algebra* by Gilbert Strang (Often discussed later, check index)
*   [Wikipedia: Norm (mathematics)](https://en.wikipedia.org/wiki/Norm_(mathematics))
*   *Numerical Linear Algebra* by Trefethen and Bau (Discusses matrix norms)

## TAGS
[[Linear Algebra]] [[Vector Norm]] [[Matrix Norm]] [[Norm]] [[Lp Norm]] [[L1 Norm]] [[L2 Norm]] [[Frobenius Norm]] [[Magnitude]] [[Distance]] [[Regularization]] [[Math]] [[Foundations]] [[Machine Learning]]