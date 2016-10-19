# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:53:17 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetBlockerPiece(KhetPiece):
    def __init__(self, imageLocation, orientation, pieceType, playersPiece):
        super().__init__()
        """
        We probably don't need "canBlock", but it's descriptive
        """
        self.canBlock = True
        
    def wasShotFatal(self, shotDirection):
        wasBlocked = self.didBlock(shotDirection)
        
        return not wasBlocked

    def didBlock(self, shotDirection):
        if self.canBlock and shotDirection == self.orientation:
            return True
        else:
            return False