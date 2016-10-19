# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:04:12 2016

@author: tbolton
"""

class KhetPiece(object):
    
    def __init__(self, imageLocation, orientation, pieceType, playersPiece):
        self.pieceType = pieceType
        self.imageLocation = imageLocation
        self.orientation = orientation
        self.playersPiece = playersPiece
        self.canMove = True
        self.canShoot = False
        self.canSwap = False
        self.canBlock = False
        self.canReflect = False
        self.isGameFinishedWhenDead = False
        
    def getOrientation(self):
        return self.orientation
        
    def setOrientation(self, orientation):
        self.orientation = orientation
        
    def wasShotFatal(self, shotDirection):
        return False
    
    def didReflect(self, shotDirection):
        return self.canReflect
        
    def didBlock(self, shotDirection):
        return self.canBlock
        
    def canShoot(self):
        return self.canShoot