1. Setup & Load Data
	- venv: `img_class_cnn_env`
	- project name: `proj01_img_class_CNN`
	- Activate virtual environment on VS Code Jupyter notebook
	1.1 Install dependencies
	- create folders: `models`, `logs`, `sample_data`
	- add data in `sample_data` (ex: images from web)
	1.2 Remove dodgy images
	- remove smaller than 9kb images and all other files
	- use `imghdr.what(image_path)` in ['jpeg', 'jpg', 'png', 'bmp']
	- use `cv2.imread(image_path)` to turn images into numpy array
	1.3 Load data into pipeline (building data pipeline)
	- `tf.data.Dataset.method()` is an API used for loading images
	- But we will use it indirectly with Keras has a built-in function as well: `tf.keras.utils.image_dataset_from_directory('sample_data')`
		- builds dataset on the fly
		- builds layers and classes 
		- preprocessing out-of-the-box: resize images
		- can use below parameters:
			- `directory, labels='inferred', label_mode='int', class_names=None, color_mode='rgb', batch_size=32, image_size=(256, 256), shuffle=True, seed=None, validation_split=None, subset=None, interpolation='bilinear', follow_links=False, crop_to_aspect_ratio=False, **kwargs,`
	- Convert into explorable data
		- currently `data` is not actually data loaded in the memory, it is a generator
		- convert it into a NumPy iterator: `data.as_numpy_iterator()`
			- it helps to loop through and generate data into NumPy array
		- we can access a batch of it by: `data_iterator.next()`
			- batch:
				- tuple of (*images*, *labels*) `len(batch)` ⇾ `2`
				- `batch[0].shape` ⇾ `(32, 256, 256, 3)` ⇾ `image.shape`
				- `batch[1]` ⇾ 1D array (list) ⇾ `class labels`
				- you can change `batch` configurations while building pipeline above
		- Visualize it:
			- ![[Pasted image 20230219233049.png]]
2. Preprocessing Data
	2.1 Scale data
	- Convert NumPy array from (0 to 255) to (0 to 1) ⇾ model generalization is faster and better
		- `data = data.map(lambda x,y: (x/batch[0].max(), y))`
		- `batch[0].max()` ⇾ `255`
			- for more functions like `map`, `skip`, `take` go to: `https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map`
	- Split data
		- `len(data)` ⇾ number of batches ⇾ `18`
		- validation dataset helps reduce [[Overfitting]]
	```Python
# take first 70% of the data
train = data.take(train_size)
# 12 batches

# skip first 70% of the data and take next 10% of the data
val = data.skip(train_size).take(val_size)
# 4 batches

# skip first 70% of the data and take next 10% of the data
test = data.skip(train_size+val_size).take(test_size)
# 2 batches
	```

## 3. Deep Model

 ### 1.1 Build Model
- Install tensor dependencies
	- Import model API
		- `from tensorflow.keras.models import Sequential`
		- great for one data input and one data output from top to bottom
		- another API `import Functional`
			- for multiple inputs and outputs, multiple connections
	- Import layers (or forming architecture of deep neural network)
		- `from tensorflow.keras.layers import ..`
			- *Conv2D:* 
				- 2-dimensional convolutional network layer for spatial convolution over images.
				- Has channels or kernels
			- *MaxPool2D:* acts as a condensing layer
				- reduces into a format for input into dense layer
			- *Dense:* Hidden layers
			- *Flatten:* Flattens the input into 1 output 
			- *Dropout:* Used for regularization (not used in the project)
```Python
# INITIATION
# create sequential model 
model = Sequential() 

# ARCHITECTURE
# now we will create (or can use Sequential([Conv2D(),]) )
	# 3 convolutional blocks, 
	# flatten layer and 
	# dense layer

# INPUT LAYER:
# first convolutional layer w/ 16 filters, 3x3 kernel or pixel size, 1 stride (moving one pixels each time)), relu activation function, input shape
# these model or hyper parameters influences how model performs:
# # 16 filters
# # # 

# # 3x3 pixel size
# # # kernel size of the filter

# # 1 
# # # stride (as per model architecture)),

# # relu activation function 
# # # produce an ineffective linear model if not added

# # input shape
# # # specify input shape for the first layer only
# # # 256x256x3 (256x256 pixels, 3 channels deep (RGB))
model.add(Conv2D(16, (3,3), 1, activation='relu', input_shape=(256, 256, 3)))
# add max pooling layer:
# # 2x2 kernel size, 2 stride
# # to reduce the size of the image in half
model.add(MaxPool2D())

# FIRST HIDDEN LAYERS
# add convolutional layer
model.add(Conv2D(32, (3,3), 1, activation='relu'))
# add max pooling layer
model.add(MaxPool2D()) 

# SECOND HIDDEN LAYERS
# add convolutional layer
model.add(Conv2D(16, (3,3), 1, activation='relu'))
# add max pooling layer
model.add(MaxPool2D())

# Condence it down to single output for dense layer
model.add(Flatten()) # add flatten layer

# add dense layer: 256 neurons
model.add(Dense(256, activation='relu')) 
# we will get a single output as class
model.add(Dense(1, activation='sigmoid')) # add dense layer

```

 ### 1.2 Train Model




 ### 1.3 Plot Performance


## 4. Evaluate Performance

complete it from image classification jupyter notebook on github