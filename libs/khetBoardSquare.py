# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 02:42:10 2016

@author: tbolton
"""

class KhetBoardSquare(object):
    isValidForPlayer1 = True
    isValidForPlayer2 = True
    
    def __init__(self, position):
        self.position = position
        row = self.getRow()
        column = self.getColumn()
        
        if row == 0 or (column == 1 and (row == 0 or row == 7)):
            self.setIsValidForPlayer2(False)
        if row == 9 or (column == 8 and (row == 0 or row == 7)):
            self.setIsValidForPlayer1(False)
        
    def getPosition(self):
        return self.position
    
    def getColumn(self):
        return self.position[0]
        
    def getRow(self):
        return self.position[1]
        
    def setIsValidForPlayer1(self, isValid):
        self.isValidForPlayer1 = isValid
        
    def setIsValidForPlayer2(self, isValid):
        self.isValidForPlayer2 = isValid
    
    def setOccupyingPiece(self, piece):
        self.piece = piece
        
    def isOccupied(self):
        return hasattr(self, 'piece')
        
    def removeOccupyingPiece(self):
        delattr(self, 'piece')
        
    def getPiece(self):
        return self.piece
        
    def isValidForPlayer(self, playerNumber):
        if playerNumber is 1:
            return self.isValidForPlayer1
        else:
            return self.isValidForPlayer2
