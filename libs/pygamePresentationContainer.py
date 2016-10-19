# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:28:00 2016

@author: tbolton
"""
import pygame
from .khetPresentationContainer import KhetPresentationContainer

class PygamePresentationContainer(KhetPresentationContainer):
    quitEvent = pygame.QUIT

    def initialize(self):
        pygame.init()
        
    def update(self):
        pygame.display.update()
        
    def setTitle(self, title):
        pygame.display.set_caption(title)
    
    def createBoard(self, size):
        self.screen = pygame.display.set_mode(size)
        return self.screen
    
    def showEmptyBoard(self, boardLocation):
        backgroundImage = pygame.image.load(boardLocation)
        self.screen.blit(backgroundImage, (0, 0))        
    
    def quitPresenting(self):
        pygame.quit()
        
    def getEvents(self):
        return pygame.event.get()
        
    def displayBoard(self):
        pass
        