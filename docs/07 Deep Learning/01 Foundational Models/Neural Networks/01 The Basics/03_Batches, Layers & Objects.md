#### Batches

- it allows to be compatible with parallel operations or calculations, reason why use GPU and not CPU
- it helps with generalization, inputs are features and to pass such samples of data in batches

batches help to keep prediction away from under or overfitting
*overfitting*: when all of the samples are shown together
*underfitting*: when samples are passes very few at a time
ultimately will hurt generalization output

common batches size to not have deal with above mentioned issues: 32 or 16, rarely 128

#### Adding Layer

```Python
import numpy as np

inputs = [[1, 2, 3, 2.5],
		  [2, 5, -1, 2],
		  [-1.5, 2.7, 3.3, -0.8]]
		  
weights1 = [[0.2, 0.8, -0.5, 1.0],
		   [0.5, -0.91, 0.26, -0.5],
		   [-0.26, -0.27, 0.17, 0.87]]
biases1 = [2, 3, 0.5]

weights2 = [[0.1, -0.14, 0.5],
		   [-0.5, 0.12, -0.33],
		   [-0.44, 0.73, -0.13]]
biases2 = [-1, 2, -0.5]

layer1_outputs = np.dot(inputs, nop.array(weights1).T) + biases1

layer2_outputs = np.dot(layer1_outputs, nop.array(weights2).T) + biases2

print(layer2_outputs)
#output
[[0.5031   -1.04185   -2.03875]
 [0.2434   -2.7332    -5.7633]
 [-0.99314 1.41254    -0.35655]]
```

#### Object Layer

```Python
import numpy as np

#input data to neural network
X = [[1, 2, 3, 2.5],
	[2, 5, -1, 2],
	[-1.5, 2.7, 3.3, -0.8]]

# Normalize dataset: 
# 1. scaling input data between -1 and +1
# 2. intialize biases as zero, 
# except when if output comes to be zero
# 3. take weights as random value

np.random.seed(0) #guassian distribution bounded around 0

#Initialize a layer

class Layer_Dense:
	def __init__(self, n_inputs, n_neurons): #features, random
		self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))
	def forward(self, inputs):
		self.output = np.dot(inputs, self.weights) + self.biases

# Note w/ this method we will not require transpose as we are defining the valid shape 


# print(0.10*np.random.randn(4,3))

#[[ 0.17640523  0.04001572  0.0978738 ]
# [ 0.22408932  0.1867558  -0.09772779]
# [ 0.09500884 -0.01513572 -0.01032189]
# [ 0.04105985  0.01440436  0.14542735]]

# print(np.zeros((1, 3)))
#array([[0., 0., 0.]])

layer1 = Layer_Dense(4, 5) #features: 4, random1: 5
layer2 = Layer_Dense(5, 2) #has to be: random1, random2: 2


layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)

#outputs
#[[ 0.10758131  1.03983522  0.24462411  0.31821498  0.18851053]
#  [-0.08349796  0.70846411  0.00293357  0.44701525  0.36360538]
#  [-0.50763245  0.55688422  0.07987797 -0.34889573 0.04553042]]
# [[ 0.148296   -0.08397602]
#  [ 0.14100315 -0.01340469]
#  [ 0.20124979 -0.07290616]]

```
