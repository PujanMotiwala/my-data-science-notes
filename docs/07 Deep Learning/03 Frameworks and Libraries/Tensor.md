### Introduction
- Tensors are the basic building block of all the machine learning and deep learning.
- Their job is to represent data in a numerical way
- For example, you could represent an #image as a tensor with shape `[3, 224, 224]` which would mean `[colour_channels, height, width]`, as in the image has `3` colour channels (red, green, blue), a height of `224` pixels and a width of `224` pixels.

### Language
*tensor-speak*

### Creating tensors

#### First a scalar
- A single number
- A scalar is a single number, and in tensor-speak it's a zero dimension tensor. (Ref: [[02_Math]])
- Usually used as variable `a`

##### Initialize a scalar
```python
# Scalar
scalar = torch.tensor(7)
scalar
```
tensor(7)

- That means, although `scalar` is a single number, it's of type `torch.Tensor`.

##### Checking dimensions of a tensor
```python
scalar.ndim
```
0

##### from `torch.Tensor` to a Python integer
```Python
# Get the Python number within a tensor (only works with one-element tensors)
scalar.item()
```
7

#### Second a vector 

- *A number with direction (e.g. wind speed with direction) but can also have many other numbers*
- A vector is a single dimension tensor but can contain many numbers. (Ref: [[02_Math]])
- As in, you could have a vector `[3, 2]` to describe `[bedrooms, bathrooms]` in your house. Or you could have `[3, 2, 2]` to describe `[bedrooms, bathrooms, car_parks]` in your house.
- The important trend here is that a vector is flexible in what it can represent (the same with tensors).
- Usually used as variable `y`

##### Initialize a vector
```Python
# Vector
vector = torch.tensor([7, 7])
vector
```
tensor([7, 7])

##### Checking dimensions of a tensor
```Python
# Check the number of dimensions of vector
vector.ndim
```
1

*Number of dimensions a tensor in PyTorch = Number of square brackets on the outside (`[`) and you only need to count one side.*

##### Checking shape
- The shape tells you how the elements inside them are arranged.
```Python
# Check shape of vector
vector.shape
```
torch.Size([2])

#### Third the Matrix
- *A 2-dimensional array of numbers*
- Usually used as variable `Q`

#####  Initialize a matrix
```Python
MATRIX = torch.tensor([[7, 8], [9, 10]])
print(MATRIX)
```
tensor([[ 7, 8], 
			[ 9, 10]])

##### Dimension & Shape
```Python
print("Dimentions: ", MATRIX.ndim) # two dimensions

print("Shape: ", MATRIX.shape) #two elements deep and two elements wide
```
Dimentions: 2 
Shape: torch.Size([2, 2])

##### Lets Tensor now

- *An n-dimensional array of numbers*
- Usually used as variable `X`

```Python
# Initialize a tensor

TENSOR = torch.tensor([[[1, 2, 3], [3, 6, 9],[2, 4, 5]]])
print(TENSOR)

# Check number of dimensions for TENSOR
print("Dimentions: ", TENSOR.ndim)

# Check number of size for TENSOR
print("Shape: ", TENSOR.shape) # The dimensions go outer to inner.
```
tensor([[[1, 2, 3], 
			 [3, 6, 9], 
			 [2, 4, 5]]])
Dimensions: 3
Shape: torch.Size([1, 3, 3])

- when building machine learning models with PyTorch, it's rare you'll create tensors by hand (like what we've being doing). 
- Instead, a machine learning model often starts out with large random tensors of numbers and adjusts these random numbers as it works through data to better represent it.
- In essence:
`Start with random numbers -> look at data -> update random numbers -> look at data -> update random numbers...`

- As a data scientist, you can define how the machine learning model starts (initialization), looks at data (representation) and updates (optimization) its random numbers.

#####  Create a tensor of random numbers w/ [`torch.rand()`](https://pytorch.org/docs/stable/generated/torch.rand.html)
```Python
# Create a random tensor of size (3, 4)
random_tensor = torch.rand(size=(3, 4))
random_tensor, random_tensor.dtype
```
(tensor([[0.3554, 0.3453, 0.3330, 0.2967],
         [0.1251, 0.0410, 0.0230, 0.8989],
         [0.2398, 0.1786, 0.7962, 0.1559]]),
 torch.float32)

- The flexibility of `torch.rand()` is that we can adjust the `size` to be whatever we want.
- For example, say you wanted a random tensor in the common image shape of `[224, 224, 3]` (`[height, width, color_channels`]).

```Python
# Create a random tensor of size (224, 224, 3)
random_image_size_tensor = torch.rand(size=(224, 224, 3))
random_image_size_tensor.shape, random_image_size_tensor.ndim
```
(torch.Size([224, 224, 3]), 3)







