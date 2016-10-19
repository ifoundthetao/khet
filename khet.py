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

presentationContainer = PygamePresentationContainer()

presentationContainer.initialize()

defaultSkin = KhetSkin('default')

# Set the board size
screen = presentationContainer.createBoard(defaultSkin.getBoardSize())

presentationContainer.setTitle('Khet 2.0')


presentationContainer.showEmptyBoard(defaultSkin.getBoardLocation())
presentationContainer.update()

board = KhetBoard(defaultSkin)

screen = board.initializeBoard(screen)

#presentationContainer.displayBoard()
presentationContainer.update()

while True:
    for event in presentationContainer.getEvents():
        if event.type is presentationContainer.quitEvent:
            presentationContainer.quitPresenting()
            sys.exit()