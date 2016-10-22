# -*- coding: utf-8 -*-
"""
Khet Clone
Created on Sun Oct 16 16:04:55 2016

@author: tbolton
"""

import sys
from libs.khetBoard import KhetBoard
from libs.khetSkin import KhetSkin
from libs.pygamePresentationContainer import PygamePresentationContainer
from libs.khetGameState import KhetGameState

GAME_IS_IN_PROGRESS = True

defaultSkin = KhetSkin('default')
presentationContainer = PygamePresentationContainer(defaultSkin)

presentationContainer.initialize()

# Set the board size
screen = presentationContainer.createBoard(defaultSkin.getBoardSize())

presentationContainer.setTitle('Khet 2.0')
presentationContainer.showEmptyBoard()
presentationContainer.update()

gameState = KhetGameState()

board = KhetBoard(defaultSkin)
board.initializeBoard(screen, defaultSkin)

presentationContainer.setBoard(board)
presentationContainer.setGameState(gameState)

presentationContainer.displayBoard()

while GAME_IS_IN_PROGRESS:
    shouldUpdate = False
    for event in presentationContainer.getEvents():
        if event.type is presentationContainer.quitEvent:
            presentationContainer.quitPresenting()
            sys.exit()
        elif event.type is presentationContainer.selectSquare():
            print("Event loop picked up piece selection.")
            #shouldUpdate = True
        elif event.type is presentationContainer.movePiece(event.type):
            print("Event loop picked up piece movement")
            shouldUpdate = True
            
            
        if shouldUpdate:
            print ("We should be updating...")
            presentationContainer.displayBoard()