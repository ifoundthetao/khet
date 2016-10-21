# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:50:32 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetSingleDeflectorPiece(KhetPiece):
    def __init__(self, playersPiece, orientation = 0):
        super().__init__(playersPiece, orientation = 0)
        self.canReflect = True
        self.isSwappable = True
        
    def didReflect(self, shotDirection):
        if shotDirection == self.orientation \
        or shotDirection == ((self.orientation + 1) % 4):
            return True
        else:
            return False
            
    def wasShotFatal(self, shotDirection):
        wasReflected = self.didReflect(shotDirection)
        
        return not wasReflected