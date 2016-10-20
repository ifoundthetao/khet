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
        
    def getImageOffsets(self, rowNumber, columnNumber):
        widthOffset = self.BOARD_BORDER_OFFSET + ((1 + rowNumber) * self.BOARD_DIVIDER_OFFSET) + (rowNumber * self.PIECE_IMAGE_SIZE)
        heightOffset = self.BOARD_BORDER_OFFSET + ((1 + columnNumber) * self.BOARD_DIVIDER_OFFSET) + (columnNumber * self.PIECE_IMAGE_SIZE)
        
        return (widthOffset, heightOffset)
        
    def isCollision(self, rowNumber, columnNumber, eventX, eventY):
        widthOffset = self.BOARD_BORDER_OFFSET + ((1 + rowNumber) * self.BOARD_DIVIDER_OFFSET) + (rowNumber * self.PIECE_IMAGE_SIZE)
        heightOffset = self.BOARD_BORDER_OFFSET + ((1 + columnNumber) * self.BOARD_DIVIDER_OFFSET) + (columnNumber * self.PIECE_IMAGE_SIZE)

        isWidthColliding = False
        isHeightColliding = False

        if eventX >= widthOffset and eventX <= (widthOffset + self.PIECE_IMAGE_SIZE):
            isWidthColliding = True
        if eventY >= heightOffset and eventY <= (heightOffset + self.PIECE_IMAGE_SIZE):
            isHeightColliding = True
        
        isCollision = isWidthColliding and isHeightColliding        
        
        return isCollision