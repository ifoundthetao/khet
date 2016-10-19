# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:14:32 2016

@author: tbolton

"""
from .khetPiece import KhetPiece

class KhetProtectedPiece(KhetPiece):
    def __init__(self, imageLocation, orientation, pieceType, playersPiece):
        super().__init__()
        self.isGameFinishedWhenDead = True