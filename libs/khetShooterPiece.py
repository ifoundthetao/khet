# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:53:40 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetShooterPiece(KhetPiece):
    def __init__(self, playersPiece, orientation = 0):
        super().__init__(playersPiece, orientation)
        self.isShooter = True
        self.isMovable = False
        
    def canShoot(self):
        return True
    
    def shoot(self):
        #Not sure what to do here... 
        pass

    def setOrientation(self, orientation):
        orientation = int(orientation) % 4
        if self.playersPiece == 1:
            self.orientation = 1 if int(orientation) == 1 else 2
        else:
            self.orientation = 0 if int(orientation) == 0 else 3

