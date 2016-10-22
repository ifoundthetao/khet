# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:09:51 2016
Game Board class for Khet
@author: tbolton


Layout can be any layout, but first we are starting with
the "Classical" layout, then we will implement the other
two layouts

Eventually we will add in an option for custom layouts
Then maybe a "randomized" layout.
"""
import json
from .khetBoardSquare import KhetBoardSquare
from .khetPieceFactory import KhetPieceFactory

class KhetBoard(object):

    # Let's throw down some defines...
    PLAYER_ONE_PROTECTED_PIECE = 'p'
    PLAYER_ONE_SINGLE_DEFLECTOR = 'y'
    PLAYER_ONE_BLOCKER = 'a'
    PLAYER_ONE_DOUBLE_DEFLECTOR = 's'
    PLAYER_ONE_SHOOTER = 'x'
    
    PLAYER_TWO_PROTECTED_PIECE = 'P'
    PLAYER_TWO_SINGLE_DEFLECTOR = 'Y'
    PLAYER_TWO_BLOCKER = 'A'
    PLAYER_TWO_DOUBLE_DEFLECTOR = 'S'
    PLAYER_TWO_SHOOTER = 'X'
    
    EMPTY_SPACE_ON_BOARD = '00'
    
    def __init__(self, skin, layout = 'classical'):
        if layout is 'classical':
            layout = 'board_setups/classical.json'
            #Create default layout object
        
        self.layout = layout
        self.skin = skin

    def initializeBoard(self, screen, skin):
        with open(self.layout, encoding = 'utf-8') as board_file:
            self.boardState = playerPieces = json.load(board_file)

        for columnIndex, currentColumn in enumerate(playerPieces):
            for rowIndex, boardFileSquarePosition in enumerate(currentColumn):
                currentSquare = KhetBoardSquare((columnIndex, rowIndex))

                if boardFileSquarePosition != self.EMPTY_SPACE_ON_BOARD:
                    pieceFactory = KhetPieceFactory(self, skin)
                    piece = pieceFactory.getPreparedPiece(boardFileSquarePosition, (columnIndex, rowIndex))
                    currentSquare.setOccupyingPiece(piece)
                self.boardState[columnIndex][rowIndex] = currentSquare
        return screen
