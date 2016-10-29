# -*- coding: utf-8 -*-
"""
Khet Clone
Created on Sun Oct 16 16:04:55 2016

@author: tbolton
"""

import sys
from libs.khetBoard import KhetBoard
from libs.khetSkin import KhetSkin
from libs.khetPresentationContainer import KhetPresentationContainer
from libs.khetGameState import KhetGameState
from libs.pygameRenderEngine import PygameRenderEngine

defaultSkin = KhetSkin('default')
renderEngine = PygameRenderEngine()
gameState = KhetGameState()
board = KhetBoard(defaultSkin)

presentationContainer = KhetPresentationContainer( 
    skin = defaultSkin,
    board = board,
    gameState = gameState,
    renderEngine = renderEngine
)
presentationContainer.setRenderEngine(renderEngine)

presentationContainer.initialize()

# Set the board size
screen = presentationContainer.createBoard(defaultSkin.getBoardSize())

presentationContainer.setTitle('Khet 2.0')
presentationContainer.showEmptyBoard()
presentationContainer.update()

board.initializeBoard(screen, defaultSkin)

presentationContainer.setBoard(board)
presentationContainer.setGameState(gameState)

presentationContainer.displayBoard()

while presentationContainer.GAME_IS_IN_PROGRESS:
    shouldUpdate = False
    for event in presentationContainer.getEvents():
        if event.type is presentationContainer.quitEvent:
            presentationContainer.quitPresenting()
            sys.exit()
        elif event.type is presentationContainer.isMovePiece():
            presentationContainer.movePiece()
            print("Event loop picked up piece movement")
            #shouldUpdate = True
        elif event.type is presentationContainer.isChangePieceOrientation():
            presentationContainer.changePieceOrientation()
            print("Event loop should change piece orientation")
        elif event.type is presentationContainer.selectSquare():
            print("Event loop picked up piece selection.")
            #shouldUpdate = True            
        if shouldUpdate:
            #presentationContainer.displayBoard()
            assert 1 == 1
