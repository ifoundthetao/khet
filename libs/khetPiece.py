# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:04:12 2016

@author: tbolton
"""

class KhetPiece(object):
    
    def __init__(self, playersPiece, orientation = 0, imageLocation = ''):
        self.imageLocation = imageLocation
        self.orientation = orientation
        self.playersPiece = playersPiece
        self.canMove = True
        self.canShoot = False
        self.canSwap = False
        self.canBlock = False
        self.canReflect = False
        self.isGameFinishedWhenDead = False
        self.boardLocation = (None, None)
        self.isSwappable = False
        
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
        
    def canSwap(self):
        return self.canSwap
        
    def setImageLocation(self, imageLocation):
        self.imageLocation = imageLocation
        
    def getImageLocation(self):
        return self.imageLocation
        
    def setBoardLocation(self, boardLocation):
        self.boardLocation
    
    def getBoardLocation():
        return self.boardLocation

    def isSelected(self):
        return self.selected
        
    def setIsSelected(self, isSelected):
        self.isSelected = isSelected
    
    def getPlayersPiece(self):
        return self.playersPiece
        
    def isSwappable(self):
        return self.isSwappable
        
    def isInReachOf(self, square):
        return True
        
    def isPlayerOne(self):
        return self.playersPiece == 1
        
    def canMove(self):
        return self.canMove