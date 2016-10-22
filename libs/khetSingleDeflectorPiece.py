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
        if self.reflectionDirection(shotDirection) is not None:
            return self.reflectionDirection(shotDirection)
        else:
            return False
            
    def wasShotFatal(self, shotDirection):
        wasReflected = self.didReflect(shotDirection)
        
        return not wasReflected

    def reflectionDirection(self, shotDirection):
        if (self.orientation + 1) % 4 == shotDirection:
        	reflectionDirection = self.orientation
        elif (self.orientation + 2) % 4 == shotDirection:
        	reflectionDirection = (self.orientation + 3 ) % 6
        else:
        	reflectionDirection = None
        	print("Should not be here.")
        
        return reflectionDirection