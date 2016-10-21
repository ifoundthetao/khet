# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:52:23 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetDoubleDeflectorPiece(KhetPiece):
    def __init__(self, playersPiece, orientation = 0):
        super().__init__(playersPiece, orientation = 0)
        self.canReflect = True
        
    def didReflect(self, shotDirection):
        return True
    
    def swapPiece(self):
        """
        Needs work on this
        """
        pass