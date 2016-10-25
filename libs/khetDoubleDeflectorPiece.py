# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:52:23 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetDoubleDeflectorPiece(KhetPiece):
    def __init__(self, playersPiece, orientation = 0):
        super().__init__(playersPiece, orientation)
        self.isReflecter = True
        self.isSwapper = True
        
    def didReflect(self, shotDirection):
        return self.getReflectionDirection(shotDirection)
    
    def getReflectionDirection(self, shotDirection):
        if self.isShotToFront(shotDirection): 
            reflectedDirection = ((int(self.orientation) + 3) % 4)
        elif self.isShotToLeft(shotDirection):
            reflectedDirection = ((int(self.orientation) + 0) % 4)
        elif self.isShotToRight(shotDirection):
            reflectedDirection = ((int(self.orientation) + 2) % 4)
        else:
            reflectedDirection = ((int(self.orientation) + 1) % 4)
        return reflectedDirection
        
    def isShotToFront(self, shotDirection):

        isHeadShot = int(self.orientation) == ((int(shotDirection) + 2) % 4)
        return isHeadShot
    
    def isShotToLeft(self, shotDirection):
        isShotToLeft = int(self.orientation) == ((int(shotDirection) + 3) % 4)
        return isShotToLeft
    
    def isShotToRight(self, shotDirection):
        isShotToRight = int(self.orientation) == ((int(shotDirection) + 1) % 4)
        return isShotToRight
    
    def isShotToBack(self, shotDirection):
        isShotToBack = int(self.orientation) == int(shotDirection)
        return isShotToBack
