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