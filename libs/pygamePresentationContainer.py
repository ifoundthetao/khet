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
        #We are doing this here, to keep it out of the main loop.
        #Hopefully this will keep things clean, and allow for other
        #styles of play.
        self.mousePositionX, self.mousePositionY = pygame.mouse.get_pos()
        
        return pygame.event.get()
        
    def displayBoard(self, board):
        for columnIndex, currentColumn in enumerate(board.boardState):
            for rowIndex, square in enumerate(currentColumn):
                if square.isOccupied():
                    piece = square.getPiece()
                    
                    orientation = piece.getOrientation()
                    imageLocation = piece.getImageLocation()
                    pieceImage = pygame.image.load(imageLocation)
                    
                    offsets = self.skin.getImageOffsets(square.getRow(), square.getColumn())
                    if int(orientation) > 0:
                        rotatingDegrees = -1 * (90.0 * float(orientation))
                        
                        pieceImage = pygame.transform.rotate(pieceImage, rotatingDegrees)
                    self.screen.blit(pieceImage, offsets)
        self.update()

    def selectPiece(self, board, eventType):
        """
        We will return the pygame.MOUSEBUTTONDOWN when this is true
        otherwise it returns False
        """
        
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()
        if not isButtonOnePressed:
            return False
        pieceSelected = False
        for columnIndex, column in enumerate(board.boardState):
            for rowIndex, currentSquare in enumerate(column):
                #board.skin.getImageOffsets(columnIndex, rowIndex)
                if currentSquare.isOccupied() \
                and self.skin.isCollision(rowIndex, columnIndex, self.mousePositionX, self.mousePositionY):
                    pieceSelected = pygame.MOUSEBUTTONDOWN

        return pieceSelected
                
        
