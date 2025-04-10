# Functions of Multiple Variables

## Simple Idea
*   Instead of having just one input $x$ determining the output $y$ (like $y = f(x)$), functions of multiple variables have **two or more inputs** that together determine the output.
*   Think of a topographical map: the height (output) depends on your location specified by two coordinates, latitude and longitude (inputs). Or the temperature in a room depends on your $(x, y, z)$ position.

## Formal Definition
*   A **function of $n$ variables** $f$ assigns a unique output value $z$ (usually a real number) to each input vector $(x_1, x_2, ..., x_n)$ from a domain $D$ in $n$-dimensional space ($\mathbb{R}^n$).
*   Notation: $z = f(x_1, x_2, ..., x_n)$ or $z = f(\mathbf{x})$, where $\mathbf{x}$ is the input vector.
*   **Domain:** The set of all possible input vectors $(x_1, ..., x_n)$ for which the function is defined.
*   **Range:** The set of all possible output values $z$.

## Key Concepts

### 1. Visualization
*   **Two Variables ($z = f(x, y)$):** The graph is a **surface** in 3D space. For each point $(x, y)$ in the domain (on the xy-plane), the height of the surface above/below that point is $z = f(x, y)$.
*   **Three or More Variables:** Direct graphing is impossible (requires >3 dimensions). We often visualize using:
    *   **Level Sets (Contour Maps):** For $z = f(x, y)$, level sets are curves in the xy-plane where $f(x, y) = c$ (constant). Like contour lines on a topographical map showing points of equal height.
    *   **Level Surfaces:** For $w = f(x, y, z)$, level surfaces are surfaces in 3D space where $f(x, y, z) = c$.

### 2. Examples in Data Science / AI
*   **Loss Functions:** Often functions of many variables (the model's parameters/weights $w_1, w_2, ..., w_n$). The loss $L$ depends on all weights: $L = f(w_1, ..., w_n)$. Optimization aims to find the weights that minimize this function.
*   **Prediction Models:** A model predicting house price ($y$) based on size ($x_1$) and location ($x_2$) is a function $y = f(x_1, x_2)$.
*   **Image Representation:** Pixel intensity can be a function of coordinates $I = f(\text{row}, \text{column})$.

### 3. Limits and Continuity
*   The concepts of [[../01 Foundations/01_Functions_Limits_Continuity|limits]] and [[../01 Foundations/01_Functions_Limits_Continuity|continuity]] extend to multiple variables, but become more complex. A limit requires the function to approach the same value regardless of the path taken towards the point $(x_0, y_0, ...)$. Continuity requires the limit to exist, the function to be defined, and the limit to equal the function value, just like the single-variable case.

## Connections to Other Topics
*   Foundation for **Multivariable Calculus**: We need functions of multiple variables to define [[02_Partial_Derivatives|Partial Derivatives]], [[03_Gradient|Gradients]], [[04_Directional_Derivatives|Directional Derivatives]], and multiple integrals.
*   Essential for understanding and optimizing [[../../06 Machine Learning/ML model|Machine Learning]] models, particularly their **loss functions**.
*   Relates to [[../03 Linear Algebra/01 Core Objects/02_Vectors|vector]] inputs $\mathbf{x} = (x_1, ..., x_n)$.

## Summary
*   **Functions of Multiple Variables** take multiple inputs (e.g., $x_1, x_2, ...$) to produce a single output $z = f(x_1, x_2, ...)$.
*   Graph of $z=f(x,y)$ is a **surface** in 3D. Visualized using **level sets/contour maps**.
*   Fundamental for representing complex relationships, especially **loss functions** in ML/AI.
*   Prerequisite for multivariable differentiation and integration.

## Sources
*   Any standard Multivariable Calculus textbook (e.g., Stewart, Thomas, Anton).
*   [Khan Academy: Introduction to Multivariable Calculus](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/introduction-to-partial-derivatives) (Introduces alongside partial derivatives)
*   [Paul's Online Math Notes: Functions of Several Variables](https://tutorial.math.lamar.edu/Classes/CalcIII/MultiVrbleFcns.aspx)

## TAGS
[[Calculus]] [[Multivariable Calculus]] [[Function]] [[Level Set]] [[Contour Map]] [[Surface]] [[Loss Function]] [[02 Math/index]] [[Foundations]]