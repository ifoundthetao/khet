# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:02:23 2016

@author: tbolton
"""

class KhetSkin(object):
    PLAYER_ONE_PHARAOH_FILE =  'pharaoh_red.png'
    PLAYER_ONE_PYRAMID_FILE =  'pyramid_mirror_red.png'
    PLAYER_ONE_ANUBIS_FILE =   'anubis_red.png'
    PLAYER_ONE_SCARAB_FILE =   'scarab_red.png'
    PLAYER_ONE_SPHINX_FILE =   'sphinx_red.png'

    PLAYER_TWO_PHARAOH_FILE = 'pharaoh_gray.png'
    PLAYER_TWO_PYRAMID_FILE = 'pyramid_mirror_gray.png'
    PLAYER_TWO_ANUBIS_FILE =  'anubis_gray.png'
    PLAYER_TWO_SCARAB_FILE =  'scarab_gray.png'
    PLAYER_TWO_SPHINX_FILE =  'sphinx_gray.png'

    BOARD_LOCATION = 'khet_board.png'
    
    BOARD_BORDER_OFFSET = 1 #one pixel for black border
    BOARD_DIVIDER_OFFSET = 5 #5 pixels per divider, column 3 would be 15 (3cols*5px)
    PIECE_IMAGE_SIZE = 64
    
    BOARD_HEIGHT = 559
    BOARD_WIDTH = 697

    def __init__(self, name):
        """ 
        The skin name relates to the actual directory name in "skins"
        we aren't going to worry about unique names right now.
        
        If this becomes an issue later, it seems we will have scaling issues,
        and we will tackle it then.
        
        Another thing, I know right now we are just using the same
        names for everything, but I abstracted the names out
        because if I wanted to do a space version with aliens
        I don't want to be annoyed that I have "Scarab" when it 
        is something different.
        """
        self.name = 'khet_images/' + name
        self.initializeBoardSquareAreas()
        

    def getFirstPlayerProtectedPieceImageLocation(self):
        """
        This is a Pharaoh in Khet
        """
        return self.name + '/' + self.PLAYER_ONE_PHARAOH_FILE

    def getFirstPlayerSingleDeflectorImageLocation(self):
        """
        This is a pyramid in Khet
        """
        return self.name + '/' + self.PLAYER_ONE_PYRAMID_FILE
        
    def getFirstPlayerBlockerImageLocation(self):
        """
        This is an Anubis in Khet
        """
        return self.name + '/' + self.PLAYER_ONE_ANUBIS_FILE
                
    def getFirstPlayerDoubleDeflectorImageLocation(self):
        """
        This is a Scarab in Khet
        """
        return self.name + '/' + self.PLAYER_ONE_SCARAB_FILE
        
    def getFirstPlayerShooterImageLocation(self):
        """
        This is a Sphinx in Khet
        """
        return self.name + '/' + self.PLAYER_ONE_SPHINX_FILE   
        
    def getSecondPlayerProtectedPieceImageLocation(self):
        """
        This is a Pharaoh in Khet
        """
        return self.name + '/' + self.PLAYER_TWO_PHARAOH_FILE

    def getSecondPlayerSingleDeflectorImageLocation(self):
        """
        This is a pyramid in Khet
        """
        return self.name + '/' + self.PLAYER_TWO_PYRAMID_FILE
        
    def getSecondPlayerBlockerImageLocation(self):
        """
        This is an Anubis in Khet
        """
        return self.name + '/' + self.PLAYER_TWO_ANUBIS_FILE
                
    def getSecondPlayerDoubleDeflectorImageLocation(self):
        """
        This is a Scarab in Khet
        """
        return self.name + '/' + self.PLAYER_TWO_SCARAB_FILE
        
    def getSecondPlayerShooterImageLocation(self):
        """
        This is a Sphinx in Khet
        """
        return self.name + '/' + self.PLAYER_TWO_SPHINX_FILE
        
    def getBoardLocation(self):
        return self.name + '/' + self.BOARD_LOCATION
        
    def getBoardHeight(self):
        return self.BOARD_HEIGHT
        
    def getBoardWidth(self):
        return self.BOARD_WIDTH
        
    def getBoardSize(self):
        return (self.BOARD_WIDTH, self.BOARD_HEIGHT)
        
    def getSquareOffsets(self, columnIndex, rowIndex):
        heightOffset = (self.BOARD_BORDER_OFFSET 
                    + ((1 + rowIndex) * self.BOARD_DIVIDER_OFFSET)
                    + (rowIndex * self.PIECE_IMAGE_SIZE))
        widthOffset = (self.BOARD_BORDER_OFFSET
                     + ((1 + columnIndex) * self.BOARD_DIVIDER_OFFSET)
                     + (columnIndex * self.PIECE_IMAGE_SIZE))
        
        return (widthOffset, heightOffset)
        
    def isCollision(self, columnIndex, rowIndex, eventX, eventY):
        isWidthColliding = False
        isHeightColliding = False

        (squareLeft,
        squareRight,
        squareTop,
        squareBottom) = self.getSquareDimensionsOnBoard(columnIndex, rowIndex)

        if eventX >= squareLeft and eventX <= squareRight:
            isWidthColliding = True
        if eventY >= squareTop and eventY <= squareBottom:
            isHeightColliding = True
        
        isCollision = isWidthColliding and isHeightColliding
        
        return isCollision
        
    def getBoardPositionFromCoordinates(self, x, y):
        for columnIndex, column in enumerate(self.boardSquareAreas):
            for rowIndex, square in enumerate(column):
                if self.isCollision(columnIndex, rowIndex, x, y):
                    return (columnIndex, rowIndex)

        
    def initializeBoardSquareAreas(self):
        squares = [[0 for x in range(10)] for x in range(8)]
        
        for columnIndex, column in enumerate(squares):
            for rowIndex, square in enumerate(column):
                squareDimensions = self.getSquareDimensionsOnBoard(columnIndex, rowIndex)
                squares[columnIndex][rowIndex] = squareDimensions
                
        self.boardSquareAreas = squares
                
    def getSquareDimensionsOnBoard(self, columnIndex, rowIndex):
        squareLeft, squareTop = self.getSquareOffsets(columnIndex, rowIndex)
        squareRight = squareLeft + self.PIECE_IMAGE_SIZE
        squareBottom = squareTop + + self.PIECE_IMAGE_SIZE
        
        return (squareLeft, squareRight, squareTop, squareBottom)
        
    def getImageLocationBasedOnPiece(self, piece):
        if type(piece).__name__ is 'KhetProtectedPiece':
            if piece.isPlayerOne() is True:
                imageLocation = self.getFirstPlayerProtectedPieceImageLocation()
            else:
                imageLocation = self.getSecondPlayerProtectedPieceImageLocation()
        elif type(piece).__name__ is 'KhetBlockerPiece':
            if piece.isPlayerOne() is True:
                imageLocation = self.getFirstPlayerBlockerImageLocation()
            else:
                imageLocation = self.getSecondPlayerBlockerImageLocation()
        elif type(piece).__name__ is 'KhetShooterPiece':
            if piece.isPlayerOne() is True:
                imageLocation = self.getFirstPlayerShooterImageLocation()
            else:
                imageLocation = self.getSecondPlayerShooterImageLocation()
        elif type(piece).__name__ is 'KhetSingleDeflectorPiece':
            if piece.isPlayerOne() is True:
                imageLocation = self.getFirstPlayerSingleDeflectorImageLocation()
            else:
                imageLocation = self.getSecondPlayerSingleDeflectorImageLocation()
        elif type(piece).__name__ is 'KhetDoubleDeflectorPiece':
            if piece.isPlayerOne() is True:
                imageLocation = self.getFirstPlayerDoubleDeflectorImageLocation()
            else:
                imageLocation = self.getSecondPlayerDoubleDeflectorImageLocation()
        else:
            imageLocation = self.getSecondPlayerDoubleDeflectorImageLocation()            
            print("Nothing!")
            
        return imageLocation
        