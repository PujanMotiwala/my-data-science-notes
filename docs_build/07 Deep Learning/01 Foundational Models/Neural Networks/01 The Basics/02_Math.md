#### Homologous Shape

how are shapes decided in numpy ?

1. For a given list (1D array/vector)  $$[1,2,3,4]$$
   shape will be $$(4,)$$
2. For list of list (2D array/ matrix) $$ [[1,2,3,4], [5,6,7,8]] $$
   shape will be
   $$(2,4)$$

Meaning at each dimention, it has to have same size. This is called homologous shape.

#### tensor
An object that can be represented as an array, but it is not just an array

#### Dot product

```Python
a = [1, 2, 3]
b = [2, 3, 4] 

dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print(dot_product)
```
20

w/ numpy

```Python
import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2

output = np.dot(weights, inputs) + bias
print(output)
```
4.8

dot_product of a layer of neurons w/ numpy

```Python
import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
		   [0.5, -0.91, 0.26, -0.5],
		   [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases
print(output)
```
[4.8 1.21 2.385]

*Note: to not have shape errors, make sure shape is homologous and keep weights with shape (3,4) before inputs with shape (4,)*

#### Matrix Product 
$$\newcommand{\bm}[1]{\boldsymbol{#1}}$$
$$\bm{w} = \begin{bmatrix} 1 & 2 & 3 \\
2 & 4 & 5 \\
6 & 2 & 8
\end{bmatrix}$$

$$\bm{i} = \begin{bmatrix} 5 & 4 & 4 \\
6 & 3 & 9 \\
8 & 7 & 4
\end{bmatrix}$$
$$\bm{w} * \bm{i} = \begin{bmatrix} 1*5 + 2*6 + 3*8  & 1*4 + 2*3 + 3*7 & 1*4 + 2*9 + 3*4 \\
2*5 + 4*6 + 5*8  & 2*4 + 4*3 + 5*7 & 2*4 + 4*9 + 5*4 \\
6*5 + 2*6 + 8*8  & 6*4 + 2*3 + 8*7 & 6*4 + 2*9 + 8*4 \end{bmatrix}$$

$$\bm{x} * \bm{y} = \begin{bmatrix} 36  & 31 & 34 \\
74  & 55 & 64 \\
106  & 86 & 74 \end{bmatrix}$$

*Note: in order to do matrix product, we might require to transpose our weights matrix*

```Python
import numpy as np

inputs = [[1, 2, 3, 2.5],
		  [2, 5, -1, 2],
		  [-1.5, 2.7, 3.3, -0.8]]
		  
weights = [[0.2, 0.8, -0.5, 1.0],
		   [0.5, -0.91, 0.26, -0.5],
		   [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

# Shape Error w/ matrix product: np.dot(inputs, weights)
# (1 * 0.2) + (2 * 0.5) + (3 * (-0.26)) + (2.5 * ??)
# Before transpose, Input Shape: (3,4) & Weight Shape: (3,4)
# After transpose, Input Shape: (3,4) & Weight Shape: (4,3)
# Therefore for matrix product, 
# (R1, C1) * (R2, C2)
# we should have same shape for C1 & R2
# Answer will be (R3, C3) = (3,3)

T_weights = np.array(weights).T

#After transpose:
print(T_weights) 
#output:
[[0.2, 0.5, -0.26],
[0.8, -0.91, -0.27],
[-0.5, 0.26, 0.17],
[1.0, -0.5,  0.87]]
```

#### Matrix summation

Adding bias to the product of matrix gained above:
$$\bm{w} * \bm{i} + \bm{b} = \begin{bmatrix} 36  & 31 & 34 \\
74  & 55 & 64 \\
106  & 86 & 74 \end{bmatrix} + \begin{bmatrix} 1 &2 &3\end{bmatrix}$$
$$\bm{w} * \bm{i} + \bm{b} = \begin{bmatrix} 37  & 33 & 37 \\
75  & 57 & 67 \\
107  & 88 & 77 \end{bmatrix}$$
#### Scalar & Vector