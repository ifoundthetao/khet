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
        self.selectedSquare = None
        
    def getSelectedSquare(self):
        return self.selectedSquare
        
    def setSelectedSquare(self, square):
        self.selectedSquare = square
    
    def hasSelectedSquare(self):
        return self.selectedSquare is not None
        
    def unselectSquare(self):
        self.selectedSquare = None
        
    def moveComplete(self):
        if self.playersTurn is self.FIRST_PLAYER:
            self.playersTurn = self.SECOND_PLAYER
        else:
            self.playersTurn = self.FIRST_PLAYER
        
    def getPlayersTurn(self):
        return self.playersTurn

    def getPlayerWhoIsWaiting(self):
        if self.playersTurn is self.FIRST_PLAYER:
            print ("SECOND PLAYER IS WAITING")
            waitingPlayer = self.SECOND_PLAYER
        else:
            print ("FIRST PLAYER IS WAITING")
            waitingPlayer = self.FIRST_PLAYER
        return waitingPlayer
