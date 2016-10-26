# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:50:32 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetSingleDeflectorPiece(KhetPiece):
    def __init__(self, playersPiece, orientation = 0):
        super().__init__(playersPiece, orientation)
        self.isReflecter = True
        self.isSwappable = True
        
    def didReflect(self, shotDirection):
        if self.getReflectionDirection(shotDirection) is not None:
            return self.getReflectionDirection(shotDirection)
        else:
            return False
            
    def wasShotFatal(self, shotDirection):
        
        wasReflected = self.didReflect(shotDirection)
        return wasReflected is False

    def getReflectionDirection(self, shotDirection):
        shotDirection = int(shotDirection)
        if self.isShotToFront(shotDirection):
            reflectionDirection = (int(self.orientation) + 3 ) % 4
        elif self.isShotToLeft(shotDirection):
            reflectionDirection = self.orientation
        else:
            reflectionDirection = None
        
        return reflectionDirection
        
    def isShotToFront(self, shotDirection):
        shotDirection = int(shotDirection)
        isHeadShot = (int(self.orientation) == int((shotDirection + 2) % 4))
        return isHeadShot
    
    def isShotToLeft(self, shotDirection):
        shotDirection = int(shotDirection)
        isShotToLeft = (int(self.orientation) == int((shotDirection + 3) % 4))
        return isShotToLeft
