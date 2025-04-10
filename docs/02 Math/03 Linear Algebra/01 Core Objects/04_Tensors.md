# Tensors

## Definition / Introduction
*   In the context of data science and deep learning (and some physics/engineering fields), a **tensor** can be thought of as a **generalization of scalars, vectors, and matrices to potentially more dimensions**.
*   It's a multi-dimensional array of numbers ([[01_Scalars|scalars]]).
*   While tensors have a more rigorous definition in physics and differential geometry involving basis vector transformations, in ML/DL we primarily use them as containers for numerical data with multiple axes.

## Key Concepts

### 1. Hierarchy of Tensors by Rank (Order / Number of Dimensions) [[Tensor Rank]]
*   The **rank** of a tensor is its number of axes or dimensions.
*   **Rank 0 Tensor:** A [[01_Scalars|Scalar]] (a single number). Has 0 axes. Shape: `()`
*   **Rank 1 Tensor:** A [[02_Vectors|Vector]] (a 1D array of numbers). Has 1 axis. Shape: `(n,)`
*   **Rank 2 Tensor:** A [[03_Matrices|Matrix]] (a 2D array of numbers). Has 2 axes (rows, columns). Shape: `(m, n)`
*   **Rank 3 Tensor:** A 3D array of numbers (like a cube or cuboid). Has 3 axes. Shape: `(d, m, n)`.
    *   Example: A color image might be represented as a Rank 3 tensor (height, width, color_channels=3). A batch of grayscale images could be (batch_size, height, width).
*   **Rank n Tensor:** An n-dimensional array of numbers. Has $n$ axes. Shape: $(d_1, d_2, ..., d_n)$.

### 2. Representation and Indexing
*   A tensor $\mathbf{T}$ requires multiple indices to access its elements. For a [[Tensor Rank|rank 3 tensor]], an element would be $T_{ijk}$ (element at index $i$ on axis 0, $j$ on axis 1, $k$ on axis 2).
*   Deep learning libraries (TensorFlow, PyTorch, JAX) use tensors as their fundamental data structure.

### 3. Shape
*   The **shape** of a tensor is a tuple of integers defining the size of the array along each dimension (axis).
*   Example Shapes:
    *   Scalar: `()`
    *   Vector (length 5): `(5,)`
    *   Matrix (3 rows, 4 cols): `(3, 4)`
    *   [[Tensor Rank|Rank 3]] Tensor (e.g., 10 images, 28x28 pixels): `(10, 28, 28)`

### 4. Examples in Data Science / AI
*   **Input Data (Deep Learning):** Tensors are the standard way to represent batches of data.
    *   Vector Data: `(batch_size, num_features)` - [[Tensor Rank|Rank 2]]
    *   Time Series / Sequence Data (NLP): `(batch_size, sequence_length, num_features)` - [[Tensor Rank|Rank 3]]
    *   Grayscale Images: `(batch_size, height, width)` or `(batch_size, height, width, 1)` - [[Tensor Rank|Rank 3]] or [[Tensor Rank|Rank 4]]
    *   Color Images: `(batch_size, height, width, num_channels=3)` - [[Tensor Rank|Rank 4]]
    *   Video Data: `(batch_size, num_frames, height, width, num_channels)` - [[Tensor Rank|Rank 5]]
*   **Model Parameters:** Weights and biases in neural network layers can be organized into tensors of various ranks.
*   **Intermediate Activations:** The outputs of layers in a neural network are tensors.

## Connections to Other Topics
*   Tensors generalize [[01_Scalars|Scalars]], [[02_Vectors|Vectors]], and [[03_Matrices|Matrices]].
*   Operations like addition, scalar multiplication, and more complex tensor operations (e.g., tensor product, contraction, reshaping) are defined on tensors. These are implemented efficiently in libraries like [[../../07 Deep Learning/03 Frameworks and Libraries/NumPy|NumPy]], [[../../07 Deep Learning/03 Frameworks and Libraries/TensorFlow|TensorFlow]], and [[../../07 Deep Learning/03 Frameworks and Libraries/PyTorch|PyTorch]].

## Summary
*   A **tensor** is a multi-dimensional array of numbers; a generalization of scalars, vectors, and matrices.
*   **[[Tensor Rank|Rank]]** (or order) refers to the number of dimensions/axes.
*   **Shape** defines the size along each dimension.
*   The fundamental data structure for representing data and parameters in **Deep Learning**.

## Sources
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 2) ([https://www.deeplearningbook.org/contents/linear_algebra.html](https://www.deeplearningbook.org/contents/linear_algebra.html))
*   [TensorFlow Core: Introduction to Tensors](https://www.tensorflow.org/guide/tensor)
*   [PyTorch: Tensors](https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)
*   [What's the difference between a matrix and a tensor?](https://datascience.stackexchange.com/questions/15116/whats-the-difference-between-a-matrix-and-a-tensor) (Discussion focusing on the ML context)

## TAGS
[[Linear Algebra]] [[Core Object]] [[Tensor]] [[Matrix]] [[Vector]] [[Scalar]] [[Tensor Rank]] [[Math]] [[Foundations]] [[Deep Learning]] [[TensorFlow]] [[PyTorch]]