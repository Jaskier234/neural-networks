#-*- coding: utf-8 -*-

class Perceptron:

    def __init__( self, wagi=[] ):
        self.wagi = wagi
        self.output = 0

    def getOutput( self, input=[] ):
        self.output = 0
        for i in range(len(input)):
            self.output += self.wagi[i]*input[i]

        # aktywacja
        if self.output > 0:
            return 1
        else:
            return -1

    def train( self, point ):
        input = [point.x, point.y]
        guess = self.getOutput( input )
        ans = point.label
        error = ans - guess
        self.wagi = [ w + error * i for w, i in zip(self.wagi,input) ]
