import numpy as np

class Perceptron():

  def __init__(self, inpS, learningRate=0.01, f=np.sign ):
    self.activation = f
    self.inpSize = inpS
    self.w = np.random.random(inpS)
    self.lr = learningRate

  def evaluate(self, inp=[] ):
    if len(inp) != self.inpSize:
      print( 'Nie odpowiedni rozmiar wejścia (evaluate)' )
    ans = [ i*j for i,j in zip(inp,self.w) ]
    return self.activation( sum(ans) )

  def learn(self, inp=[], des=0, maxInp=1):
    if len(inp) != self.inpSize:
      print( 'Nie odpowiedni rozmiar wejścia (learn)' )
    inp = [ i/maxInp for i in inp ]
    delta = des - self.evaluate(inp)
    self.w = [ w+delta*i*self.lr for w,i in zip(self.w,inp) ]
    return delta

def sign(a):
  return np.sign(a)

def half(a):
  if a >= 0.5:
    return 1
  else:
    return 0
