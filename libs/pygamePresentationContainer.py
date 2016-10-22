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
        
    def getEvents(self, gameState, board):
        #We are doing this here, to keep it out of the main loop.
        #Hopefully this will keep things clean, and allow for other
        #styles of play.
        self.mousePositionX, self.mousePositionY = pygame.mouse.get_pos()
        self.board = board
        self.gameState = gameState
        
        return pygame.event.get()
        
    def displayBoard(self, board):
        for columnIndex, currentColumn in enumerate(board.boardState):
            for rowIndex, square in enumerate(currentColumn):
                if square.isOccupied():
                    piece = square.getPiece()
                    
                    orientation = piece.getOrientation()
                    imageLocation = piece.getImageLocation()
                    pieceImage = pygame.image.load(imageLocation)
                    
                    offsets = self.skin.getSquareOffsets(square.getRow(), square.getColumn())
                    if int(orientation) > 0:
                        rotatingDegrees = -1 * (90.0 * float(orientation))
                        
                        pieceImage = pygame.transform.rotate(pieceImage, rotatingDegrees)
                    self.screen.blit(pieceImage, offsets)
        self.update()

    def selectPiece(self):
        """
        We will return the pygame.MOUSEBUTTONDOWN when this is true
        that we are selecting a piece.
        
        otherwise it returns False
        """
        
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()
        if not isButtonOnePressed:
            return False
        isPieceSelected = False
        
        self.skin.getBoardPositionFromCoordinates(self.mousePositionX, self.mousePositionY)

        for columnIndex, column in enumerate(self.board.boardState):
            for rowIndex, currentSquare in enumerate(column):
                if (currentSquare.isOccupied()
                and self.gameState.getPlayersTurn() is currentSquare.piece.getPlayersPiece()
                and self.skin.isCollision(columnIndex, rowIndex, self.mousePositionX, self.mousePositionY)):
                    isPieceSelected = pygame.MOUSEBUTTONDOWN
                    selectedPiece = currentSquare.getPiece()
                    
        if isPieceSelected:
            self.gameState.setSelectedPiece(selectedPiece)
        return isPieceSelected
    
    def movePiece(self, eventType):
        """
        We will return the pygame.MOUSEBUTTONUP when this is true
        that we are moving a piece.
        
        otherwise it returns False
        """
        #print("Mouse button presses:", pygame.mouse.get_pressed())
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()
        
       
        if (not isButtonOnePressed 
        or not self.gameState.hasSelectedPiece()):
            return False
        
        piece = self.gameState.getSelectedPiece()
        if piece.canMove() is False:  #Looking at you, Sphinx!
            return False
           
        destinationSquare = self.skin.getBoardPositionFromCoordinates(self.mousePositionX, self.mousePositionY)
        if (destinationSquare.isOccupied()
        and piece.canSwap()
        and destinationSquare.getPiece().isSwappable()):
            # we will need to implement this later
            pass 
        
        if (destinationSquare.isValidForPlayer(self.gameState.getPlayersTurn())
        and piece.isInReachOf(destinationSquare)):
            print("Should be a valid move")
        
        print ("Move piece, event type:", pygame.MOUSEBUTTONUP)    
        return pygame.MOUSEBUTTONUP
