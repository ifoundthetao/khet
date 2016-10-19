# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:53:40 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetShooterPiece(KhetPiece):
    def __init__(self, imageLocation, playersPiece, orientation = 0):
        super().__init__(imageLocation, orientation, playersPiece)
        self.canShoot = True
        
    def canShoot(self):
        return True
    
    def shoot(self):
        #Not sure what to do here... 
        pass