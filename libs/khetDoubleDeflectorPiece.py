# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:52:23 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetDoubleDeflectorPiece(KhetPiece):
    def __init__(self, playersPiece, orientation = 0):
        super().__init__(playersPiece, orientation = 0)
        self.isReflecter = True
        self.isSwapper = True
        
    def didReflect(self, shotDirection):
        return self.reflectionDirection(shotDirection)
    
    def reflectionDirection(self, shotDirection):
        if (self.orientation + 1) % 4 == shotDirection:
            reflectionDirection = self.orientation
        elif (self.orientation + 2) % 4 == shotDirection:
            reflectionDirection = (self.orientation + 3 ) % 4
        elif (self.orientation + 3) % 4 == shotDirection:
            reflectionDirection = (self.orientation + 3) % 4
        else:
            reflectionDirection = self.orientation
        return reflectionDirection