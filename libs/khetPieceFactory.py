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
        piece = self.getPieceFromShorthand(shorthand[0])
        piece.setOrientation(shorthand[1])
        piece.setBoardLocation(boardLocation)
        piece.setImageLocation(self.skin.getImageLocationBasedOnPiece(piece))
        return piece

    def getPieceFromShorthand(self, shorthand):
        if shorthand is self.board.PLAYER_ONE_PROTECTED_PIECE:
            piece = KhetProtectedPiece(playersPiece = 1)

        elif shorthand is self.board.PLAYER_ONE_SINGLE_DEFLECTOR:
            piece = KhetSingleDeflectorPiece(playersPiece = 1)
            
        elif shorthand is self.board.PLAYER_ONE_BLOCKER:
            imageLocation = self.skin.getFirstPlayerBlockerImageLocation()
            piece = KhetBlockerPiece(playersPiece = 1)
            
        elif shorthand is self.board.PLAYER_ONE_DOUBLE_DEFLECTOR:
            imageLocation = self.skin.getFirstPlayerDoubleDeflectorImageLocation()
            piece = KhetDoubleDeflectorPiece(playersPiece = 1)
            
        elif shorthand is self.board.PLAYER_ONE_SHOOTER:
            imageLocation = self.skin.getFirstPlayerShooterImageLocation()
            piece = KhetShooterPiece(playersPiece = 1)
            
        elif shorthand is self.board.PLAYER_TWO_PROTECTED_PIECE:
            imageLocation = self.skin.getSecondPlayerProtectedPieceImageLocation()
            piece = KhetProtectedPiece(playersPiece = 2)
            
        elif shorthand is self.board.PLAYER_TWO_SINGLE_DEFLECTOR:
            imageLocation = self.skin.getSecondPlayerSingleDeflectorImageLocation()
            piece = KhetSingleDeflectorPiece(playersPiece = 2)
            
        elif shorthand is self.board.PLAYER_TWO_BLOCKER:
            imageLocation = self.skin.getSecondPlayerBlockerImageLocation()
            piece = KhetBlockerPiece(playersPiece = 2)
            
        elif shorthand is self.board.PLAYER_TWO_DOUBLE_DEFLECTOR:
            imageLocation = self.skin.getSecondPlayerDoubleDeflectorImageLocation()
            piece = KhetDoubleDeflectorPiece(playersPiece = 2)
            
        elif shorthand is self.board.PLAYER_TWO_SHOOTER:
            imageLocation = self.skin.getSecondPlayerShooterImageLocation()
            piece = KhetShooterPiece(playersPiece = 2)
        else:
            piece = ''
        return piece