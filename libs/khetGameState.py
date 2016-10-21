# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 23:17:55 2016

@author: tbolton
"""

class KhetGameState(object):
    FIRST_PLAYER = 1
    SECOND_PLAYER = 2
    
    def __init__(self):
        self.playersTurn = self.FIRST_PLAYER

        
    def getSelectedPiece(self):
        return self.selectedPiece
        
    def setSelectedPiece(self, piece):
        self.selectedPiece = piece
    
    def hasSelectedPiece(self):
        return hasattr(self, 'selectedPiece')
        
    def moveComplete(self):
        if self.playersTurn is self.FIRST_PLAYER:
            self.playersTurn = self.SECOND_PLAYER
        else:
            self.playersTurn = self.FIRST_PLAYER
        
    def getPlayersTurn(self):
        return self.playersTurn