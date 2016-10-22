# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:28:00 2016

@author: tbolton
"""
import pygame
from .khetPresentationContainer import KhetPresentationContainer

class PygamePresentationContainer(KhetPresentationContainer):
    quitEvent = pygame.QUIT

    def setBoard(self, board):
        self.board = board
    
    def setGameState(self, gameState):
        self.gameState = gameState

    def initialize(self):
        pygame.init()
        
    def update(self):
        pygame.display.update()
        
    def setTitle(self, title):
        pygame.display.set_caption(title)
    
    def createBoard(self, size):
        self.screen = pygame.display.set_mode(size)
        return self.screen
    
    def showEmptyBoard(self):
        boardLocation = self.skin.getBoardLocation()
        backgroundImage = pygame.image.load(boardLocation)
        self.screen.blit(backgroundImage, (0, 0))        
    
    def quitPresenting(self):
        pygame.quit()
        
    def getEvents(self):
        """
        We are doing this here, to keep it out of the main loop.
        Hopefully this will keep things clean, and allow for other
        styles of play.
        """
        self.mousePositionX, self.mousePositionY = pygame.mouse.get_pos()
        
        return pygame.event.get()
        
    def displayBoard(self):
        self.showEmptyBoard()
        for columnIndex, currentColumn in enumerate(self.board.boardState):
            for rowIndex, square in enumerate(currentColumn):
                if square.isOccupied():
                    piece = square.getPiece()
                    
                    orientation = piece.getOrientation()
                    imageLocation = piece.getImageLocation()
                    pieceImage = pygame.image.load(imageLocation)
                    
                    #offsets = self.skin.getSquareOffsets(square.getRow(), square.getColumn())
                    offsets = self.skin.getSquareOffsets(square.getColumn(), square.getRow())
                    if int(orientation) > 0:
                        rotatingDegrees = -1 * (90.0 * float(orientation))
                        
                        pieceImage = pygame.transform.rotate(pieceImage, rotatingDegrees)
                    self.screen.blit(pieceImage, offsets)
        self.update()

    def selectSquare(self):
        """
        We will return the pygame.MOUSEBUTTONDOWN when this is true
        that we are selecting a piece.
        
        otherwise it returns False
        """
        
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()
        if not isButtonOnePressed:
            return False
        isSquareSelected = False
        
        print("type of skin:", type(self.skin))
        (column, row) = self.skin.getBoardPositionFromCoordinates(self.mousePositionX, self.mousePositionY)
        
        potentiallySelectedSquare = self.board.boardState[column][row]
        
        if (potentiallySelectedSquare.isOccupied()
        and self.gameState.getPlayersTurn() is potentiallySelectedSquare.piece.getPlayersPiece()):
            isSquareSelected = pygame.MOUSEBUTTONDOWN
            selectedSquare = potentiallySelectedSquare

        if isSquareSelected:
            self.gameState.setSelectedSquare(selectedSquare)

        return isSquareSelected
    
    def movePiece(self, eventType):
        """
        We will return the pygame.MOUSEBUTTONUP when this is true
        that we are moving a piece.
        
        otherwise it returns False
        """
        #print("Mouse button presses:", pygame.mouse.get_pressed())
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()

        if (not isButtonOnePressed 
        or not self.gameState.hasSelectedSquare()):
            return False
        
        selectedSquare = self.gameState.getSelectedSquare()
        piece = selectedSquare.getPiece()
        if not piece.canMove():  #Looking at you, Sphinx!
            print("Piece cannot move")
            #just for the sake of bugs, we will
            return False
            
        column, row = self.skin.getBoardPositionFromCoordinates(self.mousePositionX, self.mousePositionY)
        destinationSquare = self.board.boardState[column][row]
        
        if not piece.isInReachOf(destinationSquare):
            print("Piece is out of reach!")
            return False

        if not destinationSquare.isValidForPlayer(self.gameState.getPlayersTurn()):
            print("Destination Square is invalid")
            return False

        if (destinationSquare.isOccupied()
        and not piece.canSwap()):
            print("Destination square is occupied, and we cannot swap!")
            return False

        if (destinationSquare.isOccupied()
        and piece.canSwap()
        and not destinationSquare.getPiece().canBeSwapped()):
            print("Destination square is occupiece, we can swap, but the piece is not swappable")
            return False

        if (destinationSquare.isOccupied()
        and piece.canSwap()
        and destinationSquare.getPiece().canBeSwapped()):
            print("We would be swapping now")
            swappeePiece = self.board.boardState[column][row].getPiece()
            self.board.boardState[selectedSquare.getColumn()][selectedSquare.getRow()].setOccupyingPiece(swappeePiece)
        
        elif (destinationSquare.isValidForPlayer(self.gameState.getPlayersTurn())):
            print("We should be moving")
            self.board.boardState[selectedSquare.getColumn()][selectedSquare.getRow()].removeOccupyingPiece()

        self.board.boardState[column][row].setOccupyingPiece(piece)
        self.gameState.unselectSquare()
        self.fireShotAfterTurn()
        self.gameState.moveComplete()        
        return pygame.MOUSEBUTTONDOWN

    def fireShotAfterTurn(self):
        print ("Player", self.gameState.getPlayersTurn() , "Shooting!")