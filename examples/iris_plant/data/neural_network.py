'''
Artificial Intelligence Techniques SL	
artelnics@artelnics.com	

Your model has been exported to this python file.
You can manage it with the 'NeuralNetwork' class.	
Example:

	model = NeuralNetwork()	
	sample = [input_1, input_2, input_3, input_4, ...] 	 	
	outputs = model.calculate_output(sample)

	Inputs Names: 	
	1 )sepal_lenght
	2 )sepal_width
	3 )petal_lenght
	4 )petal_width

You can predict with a batch of samples using calculate_batch_output method	
IMPORTANT: input batch must be <class 'numpy.ndarray'> type	
Example_1:	
	model = NeuralNetwork()	
	input_batch = np.array([[1, 2], [4, 5]], np.int32)	
	outputs = model.calculate_batch_output(input_batch)
Example_2:	
	input_batch = pd.DataFrame( {'col1': [1, 2], 'col2': [3, 4]})	
	outputs = model.calculate_batch_output(input_batch.values)
'''

import numpy as np

class NeuralNetwork:
 
	def __init__(self):
 
		self.parameters_number = 27
 
	def scaling_layer(self,inputs):

		outputs = [None] * 4

		outputs[0] = inputs[0]*2.415266275-14.11320591
		outputs[1] = inputs[1]*4.588562965-14.02876568
		outputs[2] = inputs[2]*1.132953048-4.257637501
		outputs[3] = inputs[3]*2.623853445-3.146874905

		return outputs;


	def perceptron_layer_1(self,inputs):

		combinations = [None] * 3

		combinations[0] = -0.502284 -0.262351*inputs[0] +0.425987*inputs[1] -0.668783*inputs[2] -0.624135*inputs[3] 
		combinations[1] = -2.08545 -0.130762*inputs[0] -0.576229*inputs[1] +1.99443*inputs[2] +1.41635*inputs[3] 
		combinations[2] = 0.462892 +0.260135*inputs[0] -0.430484*inputs[1] +0.656358*inputs[2] +0.604672*inputs[3] 
		
		activations = [None] * 3

		activations[0] = np.tanh(combinations[0])
		activations[1] = np.tanh(combinations[1])
		activations[2] = np.tanh(combinations[2])

		return activations;


	def probabilistic_layer(self, inputs):

		combinations = [None] * 3

		combinations[0] = 0.265959 +1.30834*inputs[0] -0.596008*inputs[1] -1.33945*inputs[2] 
		combinations[1] = -0.391851 -0.966543*inputs[0] -2.11191*inputs[1] +0.905591*inputs[2] 
		combinations[2] = 0.125989 -0.459693*inputs[0] +2.39002*inputs[1] +0.559947*inputs[2] 
		
		activations = [None] * 3

		sum_ = 0;

		sum_ = 	np.exp(combinations[0]) + 	np.exp(combinations[1]) + 	np.exp(combinations[2]);

		activations[0] = np.exp(combinations[0])/sum_;
		activations[1] = np.exp(combinations[1])/sum_;
		activations[2] = np.exp(combinations[2])/sum_;

		return activations;


	def calculate_output(self, inputs):

		output_scaling_layer = self.scaling_layer(inputs)

		output_perceptron_layer_1 = self.perceptron_layer_1(output_scaling_layer)

		output_probabilistic_layer = self.probabilistic_layer(output_perceptron_layer_1)

		return output_probabilistic_layer


	def calculate_batch_output(self, input_batch):

		output = []

		for i in range(input_batch.shape[0]):

			inputs = list(input_batch[i])

			output_scaling_layer = self.scaling_layer(inputs)

			output_perceptron_layer_1 = self.perceptron_layer_1(output_scaling_layer)

			output_probabilistic_layer = self.probabilistic_layer(output_perceptron_layer_1)

			output = np.append(output,output_probabilistic_layer, axis=0)

		return output
