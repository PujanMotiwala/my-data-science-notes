#### Why Activation is used ?

- if we just use weights and biases, our activation function will be linear activation function as shown below. 
- output: y = x
- can only fit linear function
![[Pasted image 20230131213848.png]]

If we try to fit linear function with a non-linear data, it is not possible to fit correctly

![[Pasted image 20230131214100.png]]

### Non-linear functions

#### Step Activation Function

A step function is a mathematical function that maps its input to one of two possible outputs based on a threshold value. The output is either a fixed value for inputs below the threshold or another fixed value for inputs above the threshold. The step function is commonly used as an activation function in artificial neural networks, particularly in perceptrons, which are simple models for binary classification problems. The step function can be represented graphically as a stair-step shaped curve, with sudden transitions from one output value to another at the threshold value. In recent years, other activation functions, such as sigmoid and ReLU, have become more popular in neural network models due to their improved performance and numerical stability.

- output:  0 / 1

![[Pasted image 20230131212415.png]]

#### Sigmoid Activation Function

- it is little bit more reliable, due to granularity of the output
- output:  0<= x <= inf
- Issue: Vanishing gradient problem, more complicated 

![[Pasted image 20230131212945.png]]


#### Rectified Linear unit activation function
- Most popular activation function
- output:  0<= x <= inf
- Fits better non-linear function as shown below:

![[Pasted image 20230131214257.png]]

- it is almost linear, but it is as powerful as sigmoid activation function, it is superfast. 
- 
How does it fit sin function wave ?
- first neuron can set an activation like shown below:
![[Pasted image 20230131215117.png]]
- second neuron can set a deactivation, which moves overall function vertically. 

![[Pasted image 20230131215218.png]]
- next we can adjust the weight coming into the second neuron which will negate it. thus we can define when the neuron gets deactivate. 

![[Pasted image 20230131215357.png]]
- now we have lost the slope, now we will adjust second neuron to the output layer negating it, which will flip our function back. now what we have is two neurons activate as well as deactivate. Slope is correct, but there is alignment issue. 
![[Pasted image 20230131215620.png]]

- idea here is that to use top 7 neuron pairs to fit the correct shape of the sin function, bottom are used to offset and line up correctly. 
![[Pasted image 20230131215811.png]]

- now we need to activate the neuron exactly to previous area of effect
![[Pasted image 20230131215938.png]]

- only when both neurons are activated, there area of shape comes to play 
![[Pasted image 20230131220321.png]]

Note: we are ignoring most of the weights, when we have all weights then the line fits substancially well. 

In the example, ReLU Activation weights: (1, 64, 64, 1)

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

inputs = [0, 2, -1, 3.3,-2.7, 1.1, 2.2, -100]
output = []

# logic of ReLU

for i in inputs:
	if i > 0:
		output.append(i)
	elif  i <= 0:
		output.append(0)

# OR

for i in inputs:
	output.append(max(0, i))

print(output)
# [0, 2, 0, 3.3, 0, 1.1, 2.2, 0]

```

#### Rectified Linear Object

```Python
#Example dataset

import numpy as np

# ref: https://cs231n.github.io/neural-networks-case-study/
def create_data(points classes):
	X = np.zeros((ponts*classes, 2))
	y = np.zeros(points*classes, dtype='uint8')
	for class_number in range(classes):
		ix = range(points*class_number, points*(class_number+1))
		r = np.linspace(0.0, 1, points) #radius
		t = np.linspace(class_number*4, 
						(class_number+1)*4, points) + 
							np.random.randn(points)*0.2
		X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
		y[ix] = class_number
	return X, y

import matplotlib.plt

print("here")
X, y = create_data(100, 3) #feature set, classes

plt.scatter(X[:,0], X[:,1], c=y, cmap="brg")
plt.show()
```

```Python
import numpy as np

# pip install nnfs
import nnfs 
from nnfs.datasets import spiral_data #same as above

nnfs.init()
#- same datatype
#- for datasets

#input data to neural network
#X = [[1, 2, 3, 2.5],
#	[2, 5, -1, 2],
#	[-1.5, 2.7, 3.3, -0.8]]

X, y = spiral_data(100, 3)

#Initialize a layer

class Layer_Dense:
	def __init__(self, n_inputs, n_neurons): #features, random
		self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))
	def forward(self, inputs):
		self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
	def forward(self, inputs):
		self.output = np.maximum(0, inputs)

layer1 = Layer_Dense(2, 5) #features: x & y, neurons
activation1 = Activation_ReLU()


layer1.forward(X)
print(layer1.output) #many negative values
activation1.forward(layer1.output) #negative values to 0
print(activation1.output) #non-negative values

#optimizer will help to tune