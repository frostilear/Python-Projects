#Neural Network Finally!
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_derivative(x):
    return x*(1-x)
Traning_Data=np.array([[0,0,1],
                        [1,1,1],
                        [1,0,1],
                        [0,1,1]])
Traning_Output=np.array([[0,1,1,0]]).T
np.random.seed(1)
Synaptic_Weights=2 * np.random.random((3,1))- 1
print("Random starting synaptic weights: ")
print(Synaptic_Weights)

for number in range(50000):
    input_layer=Traning_Data
    outputs=sigmoid(np.dot(input_layer,Synaptic_Weights))
    error=Traning_Output-outputs
    Tweaks=error*sigmoid_derivative(outputs)
    Synaptic_Weights+=np.dot(input_layer.T,Tweaks)
print("synaptic wieghts after training: ")
print(Synaptic_Weights)
print("outputs after training: ")
print(outputs)