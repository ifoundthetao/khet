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

    def __init__(self, board):
        self.board = board
    def getPreparedPiece(self, shorthand):
        piece = self.getPieceFromShorthand(shorthand[0])
        piece.setOrientation(shorthand[1])

        return piece

    def getPieceFromShorthand(self, shorthand):
        if shorthand is self.board.PLAYER_ONE_PROTECTED_PIECE:
            piece = KhetProtectedPiece(playersPiece = 1)
        elif shorthand is self.board.PLAYER_ONE_SINGLE_DEFLECTOR:
            piece = KhetSingleDeflectorPiece(playersPiece = 1)
        elif shorthand is self.board.PLAYER_ONE_BLOCKER:
            piece = KhetBlockerPiece(playersPiece = 1)
        elif shorthand is self.board.PLAYER_ONE_DOUBLE_DEFLECTOR:
            piece = KhetDoubleDeflectorPiece(playersPiece = 1)
        elif shorthand is self.board.PLAYER_ONE_SHOOTER:
            piece = KhetShooterPiece(playersPiece = 1)
        elif shorthand is self.board.PLAYER_TWO_PROTECTED_PIECE:
            piece = KhetProtectedPiece(playersPiece = 2)
        elif shorthand is self.board.PLAYER_TWO_SINGLE_DEFLECTOR:
            piece = KhetSingleDeflectorPiece(playersPiece = 2)
        elif shorthand is self.board.PLAYER_TWO_BLOCKER:
            piece = KhetBlockerPiece(playersPiece = 2)
        elif shorthand is self.board.PLAYER_TWO_DOUBLE_DEFLECTOR:
            piece = KhetDoubleDeflectorPiece(playersPiece = 2)
        elif shorthand is self.board.PLAYER_TWO_SHOOTER:
            piece = KhetShooterPiece(playersPiece = 1)

        return piece