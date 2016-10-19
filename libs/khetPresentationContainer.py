# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:22:38 2016

@author: tbolton
"""

class KhetPresentationContainer(object):
    """
    This class is basically a contract for other Presentation containers
    to use to build off of.
    
    This way, we can use different presentation models and keep the logic
    buried in the class, rather than mixed in with the rest of the code.
    """
    def __init__(self):
        pass
        
    def initialize(self):
        pass
    
    def update(self):
        pass
    
    def setTitle(self, title):
        pass
    
    def createBoard(self, size):
        pass
    
    def showEmptyBoard(self, skin):
        pass
    
    def quitPresenting(self):
        pass
    
    def getEvents(self):
        pass
    
    def displayBoard(self, board):
        pass