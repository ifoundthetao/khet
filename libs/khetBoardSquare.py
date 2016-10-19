# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 02:42:10 2016

@author: tbolton
"""

class KhetBoardSquare(object):
    isInvalidForPlayer1 = 0
    isInvalidForPlayer2 = 0
    
    def __init__(self, position):
        self.position = position
        row = self.getRow()
        column = self.getColumn()
        
        if row == 0 or (column == 1 and (row == 0 or row == 7)):
            self.setIsInvalidForPlayer2(True)
        if row == 9 or (column == 8 and (row == 0 or row == 7)):
            self.setIsInvalidForPlayer1(True)        
        
    def getPosition(self):
        return self.position
    
    def getColumn(self):
        return self.position[0]
        
    def getRow(self):
        return self.position[1]
        
    def setIsInvalidForPlayer1(self, isValid):
        self.isInvalidForPlayer1 = isValid
        
    def setIsInvalidForPlayer2(self, isValid):
        self.isInvalidForPlayer2 = isValid
    
    def setOccupyingPiece(self, piece):
        self.piece = piece
        
    def isOccupied(self):
        return hasattr(self, 'piece')
        
    def removeOccupyingPiece(self):
        delattr(self, 'piece')
        
    def getPiece(self):
        return self.piece