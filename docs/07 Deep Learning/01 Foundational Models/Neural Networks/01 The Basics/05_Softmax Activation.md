- specifically used for output layer 
- first step in training a model is to predict how wrong is the model ? as accuracy is not a good indicator for that. 
for example, we have two outpus, 
layer_outputs = [4.8, 1.21, 2.385]
layer_outpus = [4.8, 4.79, 4.25]

which one is more accurate? 
we cannot say first one as all output neurons are exclusive, so there is no way to say one way or the other. This is the reason we need another activation function. 

Problem: negative number are lost while going thorugh ReLU

Solutions: 
1. use absolute value or square of a value but it might mean we will loose the meaning behind negative value, for example: -9 != 9 in the output.
2. ...
#### Exponential Function
$$y = e^x$$
where, e is Euler's number (approx.) = 2.718281828459045
it is to solve negative issue by not removing the meaning of the negativity.
![[Pasted image 20230131230918.png]]





