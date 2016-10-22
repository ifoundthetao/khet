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
        self.isMovable = True
        self.isShooter = False
        self.isSwapper = False
        self.isBlocker = False
        self.isReflecter = False
        self.isSwappable = False
        self.deathMeansGameEnd = False
        self.boardLocation = (None, None)
        
    def getOrientation(self):
        return self.orientation
        
    def setOrientation(self, orientation):
        self.orientation = orientation

    def getImageLocation(self):
        return self.imageLocation
        
    def setImageLocation(self, imageLocation):
        self.imageLocation = imageLocation
        
    def getBoardLocation(self):
        return self.boardLocation

    def setBoardLocation(self, boardLocation):
        self.boardLocation

    def isInReachOf(self, square):
        return True
        
    def isPlayerOne(self):
        return self.playersPiece == 1
    
    def isSelected(self):
        return self.selected
        
    def setIsSelected(self, isSelected):
        self.isSelected = isSelected
    
    def getPlayersPiece(self):
        return self.playersPiece
        
    def canMove(self):
        return self.isMovable
        
    def canShoot(self):
        return self.isShooter
        
    def canSwap(self):
        return self.isSwapper

    def canBeSwapped(self):
        return self.isSwappable
        
    def isGameFinishedWhenDead(self):
        return self.deathMeansGameEnd

    def didReflect(self, shotDirection):
        return self.isReflecter
        
    def didBlock(self, shotDirection):
        return self.isBlocker

    def wasShotFatal(self, shotDirection):
        return False
        