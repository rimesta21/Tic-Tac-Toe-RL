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
    
    def checkWinner(self):
        #checks first row
        if all([i == self.board[0,0] for i in self.board[0, 1:]]):
            return 1
        #checks middle row
        if all([i == self.board[1,0] for i in self.board[1, 1:]]):
            return 1
        #checks last row
        if all([i == self.board[2,0] for i in self.board[2, 1:]]):
            return 1
        #checks first column
        if all([i == self.board[0,0] for i in self.board[1:, 0]]):
            return 1
        #checks middle column
        if all([i == self.board[0,1] for i in self.board[1:, 1]]):
            return 1
        #checks last column
        if all([i == self.board[0,2] for i in self.board[1:, 2]]):
            return 1
        #checks diagonal
        if all([self.board[i,i] == self.board[0,0] for i in range(1,self.board.shape[0])]):
            return 1
        #checks anti-diagonal
        j = 1
        temp = []
        for i in range(1, self.board.shape[0]):
            temp.append(self.board[i,j] == self.board[0,2])
            j -= 1
        if all(temp):
            return 1
        #check for tie
        if '-' not in self.board:
            return 0
        #no winner
        return -1
            
                
        