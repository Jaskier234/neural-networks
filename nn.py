import numpy as np

class NeuralNetwork():

    def __init__(self, shape=[1,1], learningRate=0.01, f=np.sign):
        self.activation=f
        # self.inpSize = shape[0]
        self.learningRate = learningRate
        self.weights=[]
        for i in range( len(shape)-1 ):
            self.weights.append( np.random.random( (shape[i], shape[i+1]) ) )

    def evaluate(self, inp=[]):
        inp = np.matrix(inp)
        for w in self.weights:
            inp = inp*w
            inp = self.activation(inp)
        return inp

    def learn():
        # ???

def sign(a):
  return np.sign(a)

def half(a):
    a = np.asarray(a)
    a = [ 1 if i >= 0.5 else 0 for i in a[0] ]
    return np.matrix(a)
