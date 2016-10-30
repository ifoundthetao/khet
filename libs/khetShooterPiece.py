# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:53:40 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetShooterPiece(KhetPiece):
    def __init__(self, playersPiece, orientation, imageLocation, boardLocation):
        super().__init__(playersPiece, orientation, imageLocation, boardLocation)
        self.isShooter = True
        self.isMovable = False
        
    def canShoot(self):
        return True
    
    def shoot(self):
        #Not sure what to do here... 
        pass

    def setOrientation(self, orientation):
        orientation = int (int(self.orientation) + 1) % 4
        if self.playersPiece == 1:
            self.orientation = 2 if int(orientation) == 2 else 1
        else:
            self.orientation = 0 if int(orientation) == 0 else 3

