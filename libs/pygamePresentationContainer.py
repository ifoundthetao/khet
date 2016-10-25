# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:28:00 2016

@author: tbolton
"""
import pygame
from .khetPresentationContainer import KhetPresentationContainer

class PygamePresentationContainer(KhetPresentationContainer):
    quitEvent = pygame.QUIT
    GAME_IS_IN_PROGRESS = True
    
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
        
        if not selectedSquare.isInReachOf(destinationSquare):
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
        LEFT = 3
        UP = 0
        RIGHT = 1
        DOWN = 2
        
        if self.gameState.getPlayersTurn() is 1:
            print ("Player 1 is Shooting!")
            startingLocation = self.board.boardState[0][0]
            shooterPiece = startingLocation.getPiece()
                
        else:
            print ("Player 2 is Shooting!")
            startingLocation = self.board.boardState[9][7]
            shooterPiece = startingLocation.getPiece()
            
        column = startingLocation.getColumn()
        row = startingLocation.getRow()
        stillBouncing = True
        shotDirection = int(shooterPiece.getOrientation())
        while stillBouncing:
            print("column:", column, "row:", row)
            print("Shot direction:", shotDirection)
            if shotDirection == LEFT:
                print ("shooting left")
                targetRow = row
                targetColumn = column - 1
            elif shotDirection == RIGHT:
                print ("shooting right")
                targetRow = row
                targetColumn = column + 1
            elif shotDirection == UP:
                print ("shooting up")
                targetRow = row - 1 
                targetColumn = column
                print("Target row and column:", row, column)
            else:
                print ("shooting down")
                targetRow = row + 1 
                targetColumn = column
                print("Target row and column:", row, column)

            if targetColumn < 0 or targetColumn > 9:
                stillBouncing = False
                continue
            if targetRow < 0 or targetRow > 7:
                stillBouncing = False
                continue
            
            targetSquare = self.board.boardState[targetColumn][targetRow]

            if targetSquare.isOccupied():
                print ("targetSquare is occupied")
                piece = targetSquare.getPiece()
                # We know that if a shot was fatal, 
                # then single reflectors will be dead
                # So we assume if it was not reflected,
                # it was blocked,
                # and thus no longer bounces.
                if not piece.wasShotFatal(shotDirection):
                    print ("shot was not fatal")
                    wasReflected = piece.didReflect(shotDirection)
                    if wasReflected is False:
                        print("Shot was blocked")
                        stillBouncing = False
                    else:
                        initialShotDirection = int(shotDirection)
                        print("Shot was reflected")
                        shotDirection = int(piece.getReflectionDirection(shotDirection))
                        
                        imageLocation = self.skin.getReflectedShotLocation()                    
                        shotImage = pygame.image.load(imageLocation)
                        
                        rotatingDegrees = None
                        if shotDirection == LEFT:
                            if initialShotDirection == UP:
                                rotatingDegrees = float(3.0 * 90) * -1
                        elif shotDirection == RIGHT:
                            if initialShotDirection == UP:
                                rotatingDegrees = float(2.0 * 90) * -1
                            else:
                                rotatingDegrees = float(1.0 * 90) * -1
                        elif shotDirection == UP:
                            if initialShotDirection == LEFT:
                                rotatingDegrees = float(1.0 * 90) * -1
                        else:
                            if initialShotDirection == LEFT:
                                rotatingDegrees = float(2.0 * 90) * -1
                            else:
                                rotatingDegrees = float(3.0 * 90) * -1
                        if rotatingDegrees is not None:
                            shotImage = pygame.transform.rotate(shotImage, rotatingDegrees)

                        offsets = self.skin.getSquareOffsets(targetSquare.getColumn(), targetSquare.getRow())
                        self.screen.blit(shotImage, offsets)                
                        self.update()
                else:
                    print("Shot was fatal")
                    stillBouncing = False
                    if targetSquare.piece.isGameFinishedWhenDead():
                        self.GAME_IS_IN_PROGRESS = False
                    #self.board.boardState[targetSquare.getRow()][targetSquare.getColumn()].removeOccupyingPiece()
                    self.board.boardState[targetSquare.getColumn()][targetSquare.getRow()].removeOccupyingPiece()
                    imageLocation = self.skin.getHitShotLocation()                    
                    shotImage = pygame.image.load(imageLocation)

                    if (shotDirection == LEFT
                    or shotDirection == RIGHT):
                        rotatingDegrees = 90.0
                        shotImage = pygame.transform.rotate(shotImage, rotatingDegrees)

                    #offsets = self.skin.getSquareOffsets(square.getRow(), square.getColumn())
                    offsets = self.skin.getSquareOffsets(targetSquare.getColumn(), targetSquare.getRow())
                    self.screen.blit(shotImage, offsets)                
                    self.update()
            else:
                imageLocation = self.skin.getStraightShotLocation()                    
                shotImage = pygame.image.load(imageLocation)

                if (shotDirection == LEFT
                or shotDirection == RIGHT):
                    rotatingDegrees = 90.0
                    shotImage = pygame.transform.rotate(shotImage, rotatingDegrees)

                #offsets = self.skin.getSquareOffsets(square.getRow(), square.getColumn())
                offsets = self.skin.getSquareOffsets(targetSquare.getColumn(), targetSquare.getRow())
                self.screen.blit(shotImage, offsets)                
                self.update()
            row = targetSquare.getRow()
            column = targetSquare.getColumn()

                
