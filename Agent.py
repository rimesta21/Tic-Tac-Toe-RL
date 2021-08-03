# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:23:06 2021

@author: rimes
"""

import numpy as np

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
        move = validMoves[np.random.randint(len(validMoves))]
    else:
        for i in validMoves:
            currValue = self.positionValues[i]
            if currValue >= maxValue:
                maxValue = currValue
                move = i
    self.states.append(move)
    return move

  def updatePositionValue(self, symbol):
      if symbol == self.symbol:
          reward = 1
      elif symbol == '-':
          reward = 0
      else:
          reward = -1
      for i in reversed(self.states):
          reward = self.positionValues[i] + self.lr * (reward - self.positionValues[i])
          self.positionValues[i] = reward
    
  def reset(self, symbol):
      self.symbol = symbol
      self.states = []
                
    
  def saveValues(self, fileName):
      f = open(fileName, "w+")
        
      for i in range(self.positionValues.shape[0]):
          for j in self.positionValues[i]:
             f.write(str(j) + ", ")
          f.write("\n")
      f.close()
        
    