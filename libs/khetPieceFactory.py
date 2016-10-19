# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 04:13:43 2016

@author: tbolton
"""
from .khetBlockerPiece import KhetBlockerPiece
from .khetDoubleDeflectorPiece import KhetDoubleDeflectorPiece
from .khetProtectedPiece import KhetProtectedPiece
from .khetShooterPiece import KhetShooterPiece
from .khetSingleDeflectorPiece import KhetSingleDeflectorPiece

class KhetPieceFactory(object):

    def __init__(self, board, skin):
        self.board = board
        self.skin = skin
        
    def getPreparedPiece(self, shorthand):
        piece = self.getPieceFromShorthand(shorthand[0])
        piece.setOrientation(shorthand[1])

        return piece

    def getPieceFromShorthand(self, shorthand):
        piece = ''
        if shorthand is self.board.PLAYER_ONE_PROTECTED_PIECE:
            imageLocation = self.skin.getFirstPlayerProtectedPieceImageLocation()
            piece = KhetProtectedPiece(playersPiece = 1, imageLocation = imageLocation)

        elif shorthand is self.board.PLAYER_ONE_SINGLE_DEFLECTOR:
            imageLocation = self.skin.getFirstPlayerSingleDeflectorImageLocation()
            piece = KhetSingleDeflectorPiece(playersPiece = 1, imageLocation = imageLocation)
            
        elif shorthand is self.board.PLAYER_ONE_BLOCKER:
            imageLocation = self.skin.getFirstPlayerBlockerImageLocation()
            piece = KhetBlockerPiece(playersPiece = 1, imageLocation = imageLocation)
            
        elif shorthand is self.board.PLAYER_ONE_DOUBLE_DEFLECTOR:
            imageLocation = self.skin.getFirstPlayerDoubleDeflectorImageLocation()
            piece = KhetDoubleDeflectorPiece(playersPiece = 1, imageLocation = imageLocation)
            
        elif shorthand is self.board.PLAYER_ONE_SHOOTER:
            imageLocation = self.skin.getFirstPlayerShooterImageLocation()
            piece = KhetShooterPiece(playersPiece = 1, imageLocation = imageLocation)
            
        elif shorthand is self.board.PLAYER_TWO_PROTECTED_PIECE:
            imageLocation = self.skin.getSecondPlayerProtectedPieceImageLocation()
            piece = KhetProtectedPiece(playersPiece = 2, imageLocation = imageLocation)
            
        elif shorthand is self.board.PLAYER_TWO_SINGLE_DEFLECTOR:
            imageLocation = self.skin.getSecondPlayerSingleDeflectorImageLocation()
            piece = KhetSingleDeflectorPiece(playersPiece = 2, imageLocation = imageLocation)
            
        elif shorthand is self.board.PLAYER_TWO_BLOCKER:
            imageLocation = self.skin.getSecondPlayerBlockerImageLocation()
            piece = KhetBlockerPiece(playersPiece = 2, imageLocation = imageLocation)
            
        elif shorthand is self.board.PLAYER_TWO_DOUBLE_DEFLECTOR:
            imageLocation = self.skin.getSecondPlayerDoubleDeflectorImageLocation()
            piece = KhetDoubleDeflectorPiece(playersPiece = 2, imageLocation = imageLocation)
            
        elif shorthand is self.board.PLAYER_TWO_SHOOTER:
            imageLocation = self.skin.getSecondPlayerShooterImageLocation()
            piece = KhetShooterPiece(playersPiece = 2, imageLocation = imageLocation)
            
        return piece