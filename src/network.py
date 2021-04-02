import numpy as np
import copy

INPUTS = 9
HIDDEN1_LAYER = 20
HIDDEN2_LAYER = 20
HIDDEN3_LAYER = 10
OUTPUTS = 3

class Network:
    def __init__(self):
        self.fitness = 0

        self.w1 = np.random.randn(INPUTS, HIDDEN1_LAYER)
        self.w2 = np.random.randn(HIDDEN1_LAYER, HIDDEN2_LAYER)
        self.w3 = np.random.randn(HIDDEN2_LAYER, HIDDEN3_LAYER)
        self.w4 = np.random.randn(HIDDEN3_LAYER, OUTPUTS)
    
    def forward(self, inputs):
        net = np.matmul(inputs, self.w1)
        net = self.relu(net)
        net = np.matmul(net, self.w2)
        net = self.relu(net)
        net = np.matmul(net, self.w3)
        net = self.relu(net)
        net = np.matmul(net, self.w4)
        net = self.sigmoid(net)
        return np.argmax(self.softmax(net))

    def relu(self, x):
        return x * (x >= 0)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x))

    def crossover(self, otherNetwork):
        child = copy.deepcopy(otherNetwork)
        
        cut_point = np.random.randint(INPUTS)
        child.w1[:cut_point, :] = self.w1[:cut_point, :]
        cut_point = np.random.randint(HIDDEN1_LAYER)
        child.w2[:cut_point, :] = self.w2[:cut_point, :]
        cut_point = np.random.randint(HIDDEN2_LAYER)
        child.w3[:cut_point, :] = self.w3[:cut_point, :]
        cut_point = np.random.randint(HIDDEN3_LAYER)
        child.w4[:cut_point, :] = self.w4[:cut_point, :]

        return child

    def mutation(self, prob):
        for i in range(INPUTS):
            for j in range(HIDDEN1_LAYER):
                rand = np.random.random()
                if rand < prob:
                    self.w1[i, j] += np.random.randn() / 5
                
                if self.w1[i, j] > 1:
                    self.w1[i, j] = 1
                elif self.w1[i, j] < -1:
                    self.w1[i, j] = -1
        
        for i in range(HIDDEN1_LAYER):
            for j in range(HIDDEN2_LAYER):
                rand = np.random.random()
                if rand < prob:
                    self.w2[i, j] += np.random.randn() / 5
                
                if self.w2[i, j] > 1:
                    self.w2[i, j] = 1
                elif self.w2[i, j] < -1:
                    self.w2[i, j] = -1
        
        for i in range(HIDDEN2_LAYER):
            for j in range(HIDDEN3_LAYER):
                rand = np.random.random()
                if rand < prob:
                    self.w3[i, j] += np.random.randn() / 5
                
                if self.w3[i, j] > 1:
                    self.w3[i, j] = 1
                elif self.w3[i, j] < -1:
                    self.w3[i, j] = -1
        
        for i in range(HIDDEN3_LAYER):
            for j in range(OUTPUTS):
                rand = np.random.random()
                if rand < prob:
                    self.w4[i, j] += np.random.randn() / 5
                
                if self.w4[i, j] > 1:
                    self.w4[i, j] = 1
                elif self.w4[i, j] < -1:
                    self.w4[i, j] = -1
        
