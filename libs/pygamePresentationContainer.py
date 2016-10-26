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
        if (not isButtonOnePressed
        and not isButtonThreePressed
        ):
            return False
        isSquareSelected = False
        
        (column, row) = self.skin.getBoardPositionFromCoordinates(self.mousePositionX, self.mousePositionY)
        if column is None and row is None:
            return False

        
        potentiallySelectedSquare = self.board.boardState[column][row]
        
        if (potentiallySelectedSquare.isOccupied()
        and self.gameState.getPlayersTurn() is potentiallySelectedSquare.piece.getPlayersPiece()):
            isSquareSelected = pygame.MOUSEBUTTONDOWN
            selectedSquare = potentiallySelectedSquare

        self.displayBoard()

        if isSquareSelected:
            self.gameState.setSelectedSquare(selectedSquare)
            imageLocation = self.skin.getOrientationChangeIconLocation()
            orientationChangeIcon = pygame.image.load(imageLocation)
            offsets = self.skin.getSquareOffsets(selectedSquare.getColumn(), selectedSquare.getRow())
            self.screen.blit(orientationChangeIcon, offsets)                
            self.update()

        return isSquareSelected

    def changePieceOrientation(self):
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()

        selectedSquare = self.gameState.getSelectedSquare()
        piece = selectedSquare.getPiece()
        widthOffset, heightOffset = self.skin.getSquareOffsets(selectedSquare.getColumn(), selectedSquare.getRow())

        halfPieceSize = (self.skin.PIECE_IMAGE_SIZE / 2)
        if (abs(self.mousePositionX - widthOffset) <= halfPieceSize):
            piece.setOrientation(int(piece.getOrientation()) - 1)
        else:
            piece.setOrientation(int(piece.getOrientation()) + 1)

        column, row = self.skin.getBoardPositionFromCoordinates(self.mousePositionX, self.mousePositionY)
        if column is None and row is None:
            return False

        self.board.boardState[column][row].setOccupyingPiece(piece)
        self.gameState.unselectSquare()
        self.displayBoard()
        self.fireShotAfterTurn()
        self.gameState.moveComplete()        


    def isChangePieceOrientation(self):
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()

        """
        Button three being pressed is for changing the piece orientation
        """
        if (not isButtonThreePressed 
        or not self.gameState.hasSelectedSquare()):
            return False

        column, row = self.skin.getBoardPositionFromCoordinates(self.mousePositionX, self.mousePositionY)
        if column is None and row is None:
            return False

        destinationSquare = self.board.boardState[column][row]

        selectedSquare = self.gameState.getSelectedSquare()
        piece = selectedSquare.getPiece()

        widthOffset, heightOffset = self.skin.getSquareOffsets(selectedSquare.getColumn(), selectedSquare.getRow())
        xRelativeToSquare = self.mousePositionX - widthOffset
        yRelativeToSquare = self.mousePositionY - heightOffset

        halfPieceSize = (self.skin.PIECE_IMAGE_SIZE / 2)
        if (
            ((xRelativeToSquare <= halfPieceSize and xRelativeToSquare >= 0)
            and (yRelativeToSquare >= 0 and yRelativeToSquare <=halfPieceSize))
        or  ((xRelativeToSquare >= halfPieceSize and xRelativeToSquare <= self.skin.PIECE_IMAGE_SIZE)
            and (yRelativeToSquare >= 0 and yRelativeToSquare <=halfPieceSize))
        ):
            return pygame.MOUSEBUTTONDOWN
            
        return False
        

    def isMovePiece(self):
        """
        We will return the pygame.MOUSEBUTTONUP when this is true
        that we are moving a piece.
        
        otherwise it returns False
        """
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()

        """
        Button one being pressed is for moving the actual piece
        """
        if (not isButtonOnePressed 
        or not self.gameState.hasSelectedSquare()):
            return False
        
        selectedSquare = self.gameState.getSelectedSquare()
        piece = selectedSquare.getPiece()
        if not piece.canMove():  #Looking at you, Sphinx!
            return False
            
        column, row = self.skin.getBoardPositionFromCoordinates(self.mousePositionX, self.mousePositionY)
        if column is None and row is None:
            return False

        destinationSquare = self.board.boardState[column][row]
        
        if not selectedSquare.isInReachOf(destinationSquare):
            return False

        if not destinationSquare.isValidForPlayer(self.gameState.getPlayersTurn()):
            return False

        if (destinationSquare.isOccupied()
        and not piece.canSwap()):
            return False

        if (destinationSquare.isOccupied()
        and piece.canSwap()
        and not destinationSquare.getPiece().canBeSwapped()):
            return False

        if (destinationSquare.isOccupied()
        and piece.canSwap()
        and destinationSquare.getPiece().canBeSwapped()
        and not selectedSquare.isValidForPlayer(self.gameState.getPlayerWhoIsWaiting())):
            return False

        #We will be moving a piece.
        return pygame.MOUSEBUTTONDOWN

    def movePiece(self):
        """
        We are moving (and swapping pieces) in this method
        They can probably be decoupled later.
        """
        selectedSquare = self.gameState.getSelectedSquare()
        piece = selectedSquare.getPiece()
        column, row = self.skin.getBoardPositionFromCoordinates(self.mousePositionX, self.mousePositionY)
        if column is None and row is None:
            return False

        destinationSquare = self.board.boardState[column][row]
        
        if (destinationSquare.isOccupied()
        and piece.canSwap()
        and destinationSquare.getPiece().canBeSwapped()):
            swappeePiece = self.board.boardState[column][row].getPiece()
            self.board.boardState[selectedSquare.getColumn()][selectedSquare.getRow()].setOccupyingPiece(swappeePiece)
        
        elif (destinationSquare.isValidForPlayer(self.gameState.getPlayersTurn())):
            self.board.boardState[selectedSquare.getColumn()][selectedSquare.getRow()].removeOccupyingPiece()

        self.board.boardState[column][row].setOccupyingPiece(piece)
        self.gameState.unselectSquare()
        self.displayBoard()
        self.fireShotAfterTurn()
        self.gameState.moveComplete()        
        return pygame.MOUSEBUTTONDOWN

    def fireShotAfterTurn(self):
        LEFT = 3
        UP = 0
        RIGHT = 1
        DOWN = 2
        
        if self.gameState.getPlayersTurn() is 1:
            startingLocation = self.board.boardState[0][0]
            shooterPiece = startingLocation.getPiece()
                
        else:
            startingLocation = self.board.boardState[9][7]
            shooterPiece = startingLocation.getPiece()
            
        column = startingLocation.getColumn()
        row = startingLocation.getRow()
        stillBouncing = True
        shotDirection = int(shooterPiece.getOrientation())
        while stillBouncing:
            if shotDirection == LEFT:
                targetRow = row
                targetColumn = column - 1
            elif shotDirection == RIGHT:
                targetRow = row
                targetColumn = column + 1
            elif shotDirection == UP:
                targetRow = row - 1 
                targetColumn = column
            else:
                targetRow = row + 1 
                targetColumn = column

            if targetColumn < 0 or targetColumn > 9:
                stillBouncing = False
                continue
            if targetRow < 0 or targetRow > 7:
                stillBouncing = False
                continue
            
            targetSquare = self.board.boardState[targetColumn][targetRow]

            if targetSquare.isOccupied():
                piece = targetSquare.getPiece()
                # We know that if a shot was fatal, 
                # then single reflectors will be dead
                # So we assume if it was not reflected,
                # it was blocked,
                # and thus no longer bounces.
                if not piece.wasShotFatal(shotDirection):
                    wasReflected = piece.didReflect(shotDirection)
                    if wasReflected is False:
                        stillBouncing = False
                    else:
                        initialShotDirection = int(shotDirection)
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
                    stillBouncing = False
                    if targetSquare.piece.isGameFinishedWhenDead():
                        self.GAME_IS_IN_PROGRESS = False
                    self.board.boardState[targetSquare.getColumn()][targetSquare.getRow()].removeOccupyingPiece()
                    imageLocation = self.skin.getHitShotLocation()                    
                    shotImage = pygame.image.load(imageLocation)

                    rotatingDegrees = None
                    if shotDirection == LEFT:
                        rotatingDegrees = -90.0
                    if shotDirection == RIGHT:
                        rotatingDegrees = 90.0
                    if shotDirection == UP:
                        rotatingDegrees = 180.0
                    if rotatingDegrees is not None:
                        shotImage = pygame.transform.rotate(shotImage, rotatingDegrees)


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

                offsets = self.skin.getSquareOffsets(targetSquare.getColumn(), targetSquare.getRow())
                self.screen.blit(shotImage, offsets)                
                self.update()
            row = targetSquare.getRow()
            column = targetSquare.getColumn()
