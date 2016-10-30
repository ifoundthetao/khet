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
        
    def getPreparedPiece(self, shorthand, boardLocation):
        pieceShorthand = shorthand[0]
        orientation = shorthand[1]

        return self.getPieceFromShorthandAndSetAttributes(
            shorthand = pieceShorthand,
            orientation = orientation,
            boardLocation = boardLocation
        )

    def getPieceFromShorthandAndSetAttributes(self, shorthand, orientation, boardLocation):
        if shorthand is self.board.PLAYER_ONE_PROTECTED_PIECE:
            imageLocation = self.skin.getFirstPlayerProtectedPieceImageLocation()
            piece = KhetProtectedPiece(orientation = orientation, boardLocation = boardLocation, imageLocation = imageLocation, playersPiece = 1)

        elif shorthand is self.board.PLAYER_ONE_SINGLE_DEFLECTOR:
            imageLocation = self.skin.getFirstPlayerSingleDeflectorImageLocation()
            piece = KhetSingleDeflectorPiece(orientation = orientation, boardLocation = boardLocation, imageLocation = imageLocation, playersPiece = 1)
            
        elif shorthand is self.board.PLAYER_ONE_BLOCKER:
            imageLocation = self.skin.getFirstPlayerBlockerImageLocation()
            piece = KhetBlockerPiece(orientation = orientation, boardLocation = boardLocation, imageLocation = imageLocation, playersPiece = 1)
            
        elif shorthand is self.board.PLAYER_ONE_DOUBLE_DEFLECTOR:
            imageLocation = self.skin.getFirstPlayerDoubleDeflectorImageLocation()
            piece = KhetDoubleDeflectorPiece(orientation = orientation, boardLocation = boardLocation, imageLocation = imageLocation, playersPiece = 1)
            
        elif shorthand is self.board.PLAYER_ONE_SHOOTER:
            imageLocation = self.skin.getFirstPlayerShooterImageLocation()
            piece = KhetShooterPiece(orientation = orientation, boardLocation = boardLocation, imageLocation = imageLocation, playersPiece = 1)
            
        elif shorthand is self.board.PLAYER_TWO_PROTECTED_PIECE:
            imageLocation = self.skin.getSecondPlayerProtectedPieceImageLocation()
            piece = KhetProtectedPiece(orientation = orientation, boardLocation = boardLocation, imageLocation = imageLocation, playersPiece = 2)
            
        elif shorthand is self.board.PLAYER_TWO_SINGLE_DEFLECTOR:
            imageLocation = self.skin.getSecondPlayerSingleDeflectorImageLocation()
            piece = KhetSingleDeflectorPiece(orientation = orientation, boardLocation = boardLocation, imageLocation = imageLocation, playersPiece = 2)
            
        elif shorthand is self.board.PLAYER_TWO_BLOCKER:
            imageLocation = self.skin.getSecondPlayerBlockerImageLocation()
            piece = KhetBlockerPiece(orientation = orientation, boardLocation = boardLocation, imageLocation = imageLocation, playersPiece = 2)
            
        elif shorthand is self.board.PLAYER_TWO_DOUBLE_DEFLECTOR:
            imageLocation = self.skin.getSecondPlayerDoubleDeflectorImageLocation()
            piece = KhetDoubleDeflectorPiece(orientation = orientation, boardLocation = boardLocation, imageLocation = imageLocation, playersPiece = 2)
            
        elif shorthand is self.board.PLAYER_TWO_SHOOTER:
            imageLocation = self.skin.getSecondPlayerShooterImageLocation()
            piece = KhetShooterPiece(orientation = orientation, boardLocation = boardLocation, imageLocation = imageLocation, playersPiece = 2)
        else:
            piece = ''
        return piece
