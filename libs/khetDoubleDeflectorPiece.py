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
    
    def getReflectedDirection(self, shotDirection):
    	if self.isShotToFront(shotDirection): 
    		reflectedDirection = (self.orientation + 1) % 4
    	elif self.isShotToLeft(shotDirection):
    		reflectedDirection = (self.orientation + 0) % 4
    	elif self.isShotToRight(shotDirection):
    		reflectedDirection = (self.orientation + 3) % 4
    	else:
    		reflectedDirection = (self.orientation + 2) % 4
    	return reflectedDirection
    	
    	
    def isShotToFront(self, shotDirection):
    	isHeadShot = (self.orientation == ((shotDirection + 2) % 4))
    	return isHeadShot
    
    def isShotToLeft(self, shotDirection):
    	isShotToLeft = self.orientation == (shotDirection + 3) % 4
    	return isShotToLeft
    
    def isShotToRight(self, shotDirection):
    	isShotToRight = self.orientation == (shotDirection + 1) % 4
    	return isShotToRight
    
    def isShotToBack(self, shotDirection):
    	isShotToBack = self.orientation == shotDirection
    	return isShotToBack
