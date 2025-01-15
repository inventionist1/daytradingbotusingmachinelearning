import numpy as np # type: ignore
import nnfs # type: ignore
from nnfs.datasets import spiral_data # type: ignore

nnfs.init()

class LayerDense:
    def __init__(self, nInputs, nNeurons):
        self.weights = 0.1*np.random.randn(nInputs, nNeurons)
        self.biases = np.zeros((1, nNeurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class ActivationReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class ACtivationSoftMax:
    def forward(self, inputs):
        expValues = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = expValues / np.sum(expValues, axis=1, keepdims=True)
        self.output = probabilities

X, y = spiral_data(samples=100, classes=3)

dense1 = LayerDense(2,3)
activation1 = ActivationReLU()

dense2 = LayerDense(3, 3)
activation2 = ACtivationSoftMax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])