# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j5uQ9Gnpn_WTdL-Hh6R-qU27fuXbyK6h
"""

#Code1

import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
 return 1 / (1 + np.exp(-x))
def relu(x):
 return np.maximum(0, x)
def tanh(x):
 return np.tanh(x)
def softmax(x):
 return np.exp(x) / np.sum(np.exp(x))
# Create x values
x = np.linspace(-10, 10, 100)
# Create plots for each activation function
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs[0, 0].plot(x, sigmoid(x))
axs[0, 0].set_title('Sigmoid')
axs[0, 1].plot(x, relu(x))
axs[0, 1].set_title('ReLU')
axs[1, 0].plot(x, tanh(x))
axs[1, 0].set_title('Tanh')
axs[1, 1].plot(x, softmax(x))
axs[1, 1].set_title('Softmax')
# Add common axis labels and titles
fig.suptitle('Common Activation Functions')
for ax in axs.flat:
 ax.set(xlabel='x', ylabel='y')
 
# Adjust spacing between subplots
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
# Show the plot
plt.show()

#Code2

list1=[0,0,1,1]
list2=[0,1,0,1]
list4=[]
list6=[]
list7=[]
for x in range(4):
    list3=list1[x]&list2[x]
    list4.append(list3)
    print(list4[x])

w1=int(input("enter weight 1:"))
w2=int(input("enter weight 2:"))
for x in range(4):
    list5=(list1[x]*w1)+(list2[x]*w2)
    list6.append(list5)
    print(list6[x])
th=int(input("choose threshold value from above list:"))
for x in range(4):
    if(th<=list6[x]):
        list7.append(1)
    else:
        list7.append(0)
    print(list7[x])

for x in range(4):
    if(list7[x]==list4[x]):
        print("satisfied")
    else:
        print("unsatisfied")

#Code3

import numpy as np
# Define the perceptron class
class Perceptron:
 def __init__(self, input_size, lr=0.1):
  self.W = np.zeros(input_size + 1)
  self.lr = lr
 def activation_fn(self, x):
  return 1 if x >= 0 else 0
 def predict(self, x):
   x = np.insert(x, 0, 1)
   z = self.W.T.dot(x)
   a = self.activation_fn(z)
   return a
 def train(self, X, Y, epochs):
  for _ in range(epochs):
   for i in range(Y.shape[0]):
    x = X[i]
    y = self.predict(x)
    e = Y[i] - y
    self.W = self.W + self.lr * e * np.insert(x, 0, 1)
# Define the input data and labels
X = np.array([
 [0,0,0,0,0,0,1,0,0,0], # 0
 [0,0,0,0,0,0,0,1,0,0], # 1
 [0,0,0,0,0,0,0,0,1,0], # 2
 [0,0,0,0,0,0,0,0,0,1], # 3
 [0,0,0,0,0,0,1,1,0,0], # 4
 [0,0,0,0,0,0,1,0,1,0], # 5
 [0,0,0,0,0,0,1,1,1,0], # 6
 [0,0,0,0,0,0,1,1,1,1], # 7
 [0,0,0,0,0,0,1,0,1,1], # 8
 [0,0,0,0,0,0,0,1,1,1], # 9
])
Y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
# Create the perceptron and train it
perceptron = Perceptron(input_size=10)
perceptron.train(X, Y, epochs=100)
# Test the perceptron on some input data
test_X = np.array([
 [0,0,0,0,0,0,1,0,0,0], # 0
 [0,0,0,0,0,0,0,1,0,0], # 1
 [0,0,0,0,0,0,0,0,1,0], # 2
 [0,0,0,0,0,0,0,0,0,1], # 3
 [0,0,0,0,0,0,1,1,0,0], # 4
 [0,0,0,0,0,0,1,0,1,0], # 5
 [0,0,0,0,0,0,1,1,1,0], # 6
 [0,0,0,0,0,0,1,1,1,1], # 7
 [0,0,0,0,0,0,1,0,1,1], # 8
 [0,0,0,0,0,0,0,1,1,1], # 9
])
for i in range(test_X.shape[0]):
 x = test_X[i]
 y = perceptron.predict(x)
 print(f'{x} is {"even" if y == 0 else "odd"}')

#Code4

import numpy as np
import matplotlib.pyplot as plt


def perceptron(x, w, b):
    return np.sign(np.dot(x, w) + b)


def perceptron_learning(X, Y, eta, epochs):
    w = np.zeros(X.shape[1])
    b = 0

    for epoch in range(epochs):
        for i in range(X.shape[0]):
            y_pred = perceptron(X[i], w, b)
            
            if y_pred != Y[i]:
                w += eta * Y[i] * X[i]
                b += eta * Y[i]

    return w, b


X = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
Y = np.array([0, 0, 0, 1])
Y[Y==0]=-1
w, b = perceptron_learning(X, Y, eta=0.3, epochs=6)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))
Z = np.array([perceptron(np.array([x, y]), w, b) 
for x, y in np.c_[xx.ravel(), yy.ravel()]])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
plt.xlabel('X1')
plt.ylabel('X2')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('Perceptron Decision Regions')
plt.show()

#Code5

import numpy as np

# Define two pairs of vectors
x1 = np.array([1, 1, 1, -1])
y1 = np.array([1, -1])
x2 = np.array([-1, -1, 1, 1])
y2 = np.array([-1, 1])

# Compute weight matrix W
W = np.outer(y1, x1) + np.outer(y2, x2)

# Define BAM function
def bam(x):
    y = np.dot(W, x)
    y = np.where(y >= 0, 1, -1)
    return y

# Test BAM with inputs
x_test = np.array([1, -1, -1, -1])
y_test = bam(x_test)

# Print output
print("Input x:", x_test)
print("Output y:", y_test)

#Code6&7


import numpy as np

# Define the parameters of the network
input_dim = 2    # Number of input nodes
hidden_dim = 4   # Number of hidden nodes
output_dim = 1   # Number of output nodes
learning_rate = 0.1
epochs = 10000

# Define the training data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [0]])

# Initialize the weights and biases
W1 = np.random.randn(input_dim, hidden_dim)
b1 = np.zeros((1, hidden_dim))
W2 = np.random.randn(hidden_dim, output_dim)
b2 = np.zeros((1, output_dim))

# Define the sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Train the network using backpropagation
for i in range(epochs):
    # Forward pass
    hidden_layer_input = np.dot(X, W1) + b1
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, W2) + b2
    output_layer_output = sigmoid(output_layer_input)

    # Backward pass
    output_error = Y - output_layer_output
    output_delta = output_error * sigmoid_derivative(output_layer_output)

    hidden_error = output_delta.dot(W2.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    W2 += learning_rate * hidden_layer_output.T.dot(output_delta)
    b2 += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
    W1 += learning_rate * X.T.dot(hidden_delta)
    b1 += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

# Test the network with some example inputs
x_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_test = np.array([[0], [1], [1], [0]])

hidden_layer_input = np.dot(x_test, W1) + b1
hidden_layer_output = sigmoid(hidden_layer_input)
output_layer_input = np.dot(hidden_layer_output, W2) + b2
output_layer_output = sigmoid(output_layer_input)

print("Input:")
print(x_test)
print("Output:")
print(output_layer_output)
print("Expected Output:")
print(y_test)



#Code8

import numpy as np

# Define the parameters of the network
n = 4   # Number of input nodes
m = 2   # Number of output nodes
rho = 0.5   # Vigilance parameter

# Define the input patterns
patterns = np.array([[1, 1, 0, 0],
                     [0, 0, 1, 1],
                     [1, 0, 1, 0],
                     [0, 1, 0, 1]])

# Initialize the weight matrix and bias vectors
weights = np.zeros((m, n))
bias = np.zeros(m)

# Define the ART function
def art(input_pattern, weights, bias, rho):
    # Normalize the input pattern
    x = input_pattern / np.sum(input_pattern)

    # Calculate the net input for each output node
    net = np.dot(weights, x) + bias

    # Find the winning node (the one with the highest net input)
    winner = np.argmax(net)

    # Calculate the resonance (similarity) between the input and the winning node
    resonance = np.dot(weights[winner], x) / (rho + np.sum(weights[winner]))

    # If the resonance is greater than the vigilance parameter, the input pattern
    # is classified as belonging to the winning node; otherwise, a new node is added
    if resonance >= rho:
        output_pattern = np.zeros(m)
        output_pattern[winner] = 1
        weights[winner] = ((np.sum(input_pattern) / np.sum(weights[winner])) * weights[winner]) + x
        bias[winner] = np.sum(input_pattern)
    else:
        output_pattern = np.zeros(m+1)
        output_pattern[-1] = 1
        weights = np.vstack([weights, x])
        bias = np.append(bias, np.sum(input_pattern))

    return output_pattern

# Test the ART network with each of the input patterns
for pattern in patterns:
    output_pattern = art(pattern, weights, bias, rho)
    print("Input pattern:")
    print(pattern)
    print("Output pattern:")
    print(output_pattern)
    print("Weights:")
    print(weights)
    print("Bias:")
    print(bias)
    print("=============================")

#Code9

import numpy as np

class HopfieldNetwork:
    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
        self.weights = np.zeros((n_neurons, n_neurons))
    
    def train(self, patterns):
        for pattern in patterns:
            self.weights += np.outer(pattern, pattern)
        np.fill_diagonal(self.weights, 0)
    
    def predict(self, pattern):
        energy = -0.5 * np.dot(np.dot(pattern, self.weights), pattern)
        return np.sign(np.dot(pattern, self.weights) + energy)

if __name__ == '__main__':
    patterns = np.array([
        [1, 1, -1, -1],
        [-1, -1, 1, 1],
        [1, -1, 1, -1],
        [-1, 1, -1, 1]
    ])
    n_neurons = patterns.shape[1]
    network = HopfieldNetwork(n_neurons)
    network.train(patterns)
    
    for pattern in patterns:
        prediction = network.predict(pattern)
        print('Input pattern:', pattern)
        print('Predicted pattern:', prediction)

import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
# Load CIFAR-10 dataset
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
# Define the model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
# Define data generators
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, 
horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
# Prepare the data
train_set = train_datagen.flow(X_train, y_train, batch_size=32)
test_set = test_datagen.flow(X_test, y_test, batch_size=32)
# Compile the model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
# Train the model
model.fit_generator(train_set, steps_per_epoch=len(X_train)//32, epochs=2, 
validation_data=test_set, validation_steps=len(X_test)//32)
# Evaluate the model
score = model.evaluate(test_set, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

#code12

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
model = Sequential([
 Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
 MaxPooling2D((2, 2)),
 Conv2D(64, (3, 3), activation='relu'),
 MaxPooling2D((2, 2)),
 Conv2D(64, (3, 3), activation='relu'),
 Flatten(),
 Dense(64, activation='relu'),
 Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=64, epochs=10, verbose=1)
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}")
print(f"Test Accuracy: {accuracy}")

#code 11

import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
df=load_breast_cancer()
X_train,X_test,y_train,y_test=train_test_split(df.data,df.target,test_size=0.20,random_state=42)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
model=tf.keras.models.Sequential([tf.keras.layers.Dense(1,activation='sigmoid',input_shape=(X
_train.shape[1],))])
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(X_train,y_train,epochs=5)
y_pred=model.predict(X_test)
test_loss,test_accuracy=model.evaluate(X_test,y_test)
print("accuracy is",test_accuracy)