# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:34:35 2021

@author: rimes
"""

import numpy as np
from Agent import Agent



class GameDriver:
    def __init__(self):
        self.board = np.array(range(1,10), dtype = str).reshape(3,3)
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
        #no winner
        return -1
    
    def printBoard(self):
        print(self.board)
        print()
        
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    cont = 'y'
    reset = False
    while cont == 'y':
        gd = GameDriver()
        userSym = ''
        userIn = input("Would you like to go first or second?. Press f for first and anything else for second.\n")
        if userIn.lower() == 'f':
            userSym = 'X'
            if not reset:
                ag = Agent('O')
            else:
                ag.reset('O')
        else:
            userSym = 'O'
            if not reset:
                ag = Agent('X')
            else:
                ag.reset('X')
        print("Okay great. Here is the starting board.")
        gd.printBoard()
        
        turn = 'O'
        count = 0
        tie = True
        #I'd prefer a do while but you know how it goes 
        while count < 10:
            #this is done so that turn can be presevred when the game ends
            if turn == 'O':
                turn = 'X'
            else:
                turn = 'O'
            
            if userSym == turn:
                while True:
                    userIn = int(input(prompt = "Please select an open position from 1-9.\n"))
                    if gd.userInputToCorrdinate(userIn) not in gd.validMoves:
                        print("I'm sorry that position is not availible. Please choice another.")
                    else:
                        break
                print()
                    
                gd.board[gd.userInputToCorrdinate(userIn)] = turn
                print("Your move has been made. This is the new board.")
                gd.printBoard()
                gd.validMoves.remove(gd.userInputToCorrdinate(userIn))
            else:
                move = ag.makeMove(gd.validMoves)
                gd.board[move] = turn
                print("The computer has made their move. This is the new board.")
                gd.printBoard()
                gd.validMoves.remove(move)
            if gd.checkWinner() == 1:
                print("Congratulations!! Looks like " + turn + " was paying attention.")
                tie = False
                break
            count += 1
        if tie:
            print("Looks like its a Tie! Good match!")
            turn = '-'
        ag.updatePositionValue(turn)
            
        print()
        cont = input("Would you like to play another game? Press y for yes and anything else for no.\n")
        if cont == 'y':
            print(ag.positionValues)
            reset = True
    
    save = input("Admin Question: Would you like to update the agent?\n")
    if save == 'y':
        fileName = input("What is the name of the file?\n")
        ag.saveValues(fileName)
            
                
        