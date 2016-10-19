# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:14:32 2016

@author: tbolton

"""
from .khetPiece import KhetPiece

class KhetProtectedPiece(KhetPiece):
    def __init__(self, imageLocation, playersPiece, orientation = 0):
        super().__init__(imageLocation, playersPiece, orientation)
        self.isGameFinishedWhenDead = True