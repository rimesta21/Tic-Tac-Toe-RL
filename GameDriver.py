# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:34:35 2021

@author: rimes
"""

import numpy as np

class GameDriver:
    def __init__(self):
        self.board = np.full((3,3), '-')
        self.validMoves = []
        self.copyMoves = []
        for i in range(3):
            for j in range(3):
                self.validMoves.append((i,j))
                self.copyMoves.append((i,j))
    
    def userInputToCorrdinate(self, value):
        return self.copyMoves[value - 1]
        