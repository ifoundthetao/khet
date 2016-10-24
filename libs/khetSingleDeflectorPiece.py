# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:50:32 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetSingleDeflectorPiece(KhetPiece):
    def __init__(self, playersPiece, orientation = 0):
        super().__init__(playersPiece, orientation = 0)
        self.isReflecter = True
        self.isSwappable = True
        
    def didReflect(self, shotDirection):
        if self.getReflectionDirection(shotDirection) is not None:
            return self.getReflectionDirection(shotDirection)
        else:
            return False
            
    def wasShotFatal(self, shotDirection):
        #print('Type of piece:', type(self))
        
        wasReflected = self.didReflect(shotDirection)
        #print('was this reflected:', wasReflected)
        return not wasReflected

    def getReflectionDirection(self, shotDirection):
        shotDirection = int(shotDirection)
        if self.isShotToFront(shotDirection):
            reflectionDirection = (int(self.orientation) + 3 ) % 4
        elif self.isShotToLeft(shotDirection):
            reflectionDirection = self.orientation
        else:
            reflectionDirection = None
        
        #print ('getReflectedDirection:', reflectionDirection)
        return reflectionDirection
        
    def isShotToFront(self, shotDirection):
        shotDirection = int(shotDirection)
        """
        print("isShotToFront")
        print("Shot Direction:", shotDirection)
        print("Piece Orientation:", self.orientation)
        print("(Shot direction + 2) % 4):", ((shotDirection + 2) % 4))
        """
        isHeadShot = (int(self.orientation) == int((shotDirection + 2) % 4))
        #print("isHeadShot:", isHeadShot)
        return isHeadShot
    
    def isShotToLeft(self, shotDirection):
        shotDirection = int(shotDirection)
        """
        print("isShotToLeft")
        print("Shot Direction:", shotDirection)
        print("Shot Orientation:", self.orientation)
        print("(Shot direction + 3) % 4):", ((shotDirection + 3) % 4))
        """
        isShotToLeft = (int(self.orientation) == int((shotDirection + 3) % 4))
        #print("isShotToLeft:", isShotToLeft)
        return isShotToLeft
