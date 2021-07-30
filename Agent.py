# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:23:06 2021

@author: rimes
"""

import nupmy as np

class Agent:
  def __init__(self, symbol):
    self.positionValues = np.zeros((3,3))
    self.symbol = symbol
    self.states = []
    self.lr = 0.2
    self.expr = 0.3
  
  
  def makeMove(self, validMoves):
    maxValue = 0
    move = ()
    
    if np.random.uniform(0,1) <= self.expr:
        move = np.random.choice(validMoves)
    else:
        for i in validMoves:
            currValue = self.positionValues[i]
            if currValue >= maxValue:
                maxValue = currValue
                move = i
    
    return move
        