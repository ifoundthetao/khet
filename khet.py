# -*- coding: utf-8 -*-
"""
Khet Clone
Created on Sun Oct 16 16:04:55 2016

@author: tbolton
"""

import sys, pygame

pygame.init()

boardWidth = 697
boardHeight = 559
BOARD_BORDER_OFFSET = 1 #one pixel for black border
BOARD_DIVIDER_OFFSET = 5 #5 pixels per divider, column 3 would be 15 (3cols*5px)
size = (boardWidth, boardHeight)

# Let's throw down some defines...
RED_PHARAOH = 'p'
RED_PYRAMID = 'y'
RED_ANUBIS = 'a'
RED_SCARAB = 's'
RED_SPHINX = 'x'

GRAY_PHARAOH = 'P'
GRAY_PYRAMID = 'Y'
GRAY_ANUBIS = 'A'
GRAY_SCARAB = 'S'
GRAY_SPHINX = 'X'

RED_PHARAOH_FILE = './khet_images./pharaoh_red.png'
RED_PYRAMID_FILE = './khet_images/pyramid_mirror_red.png'
RED_ANUBIS_FILE = './khet_images/anubis_red.png'
RED_SCARAB_FILE = './khet_images/scarab_red.png'
RED_SPHINX_FILE = './khet_images/sphinx_red.png'

GRAY_PHARAOH_FILE = './khet_images/pharaoh_gray.png'
GRAY_PYRAMID_FILE = './khet_images/pyramid_mirror_gray.png'
GRAY_ANUBIS_FILE = './khet_images/anubis_gray.png'
GRAY_SCARAB_FILE = './khet_images/scarab_gray.png'
GRAY_SPHINX_FILE = './khet_images/sphinx_gray.png'

def setupClassicConfiguration(board):
    firstPlayerPieces = [
        ['x2', '00', '00', '00', 'a2', 'p0', 'a2', 'y2', '00', '00'],
        ['00', '00', 'y3', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00'],
        ['y1', '00', '00', '00', 's1', 's0', '00', 'y2', '00', '00'],
        ['y2', '00', '00', '00', '00', '00', '00', 'y1', '00', '00'],
        ['00', '00', '00', '00', '00', '00', 'y2', '00', '00', '00'],
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00']
    ]    
    
    secondPlayerPieces =[
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', 'Y1', '00', '00', '00', '00', '00', '00'],
        ['00', '00', 'Y3', '00', '00', '00', '00', '00', '00', 'Y0'],
        ['00', '00', 'Y0', '00', 'S0', 'S1', '00', '00', '00', 'Y3'],
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', '00', '00', '00', '00', 'Y1', '00', '00'],
        ['00', '00', 'Y0', 'A0', 'P4', 'A0', '00', '00', '00', 'X0']
    ]
    
    playerPieces = [
        ['x2', '00', '00', '00', 'a2', 'p0', 'a2', 'y2', '00', '00'],
        ['00', '00', 'y3', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', 'Y0', '00', '00', '00', '00', '00', '00'],
        ['y1', '00', 'Y3', '00', 's1', 's0', '00', 'y2', '00', 'Y0'],
        ['y2', '00', 'Y0', '00', 'S0', 'S1', '00', 'y1', '00', 'Y3'],
        ['00', '00', '00', '00', '00', '00', 'y2', '00', '00', '00'],
        ['00', '00', '00', '00', '00', '00', '00', 'Y1', '00', '00'],
        ['00', '00', 'Y0', 'A0', 'P0', 'A0', '00', '00', '00', 'X0']
    ]    
    
    secondPlayerPieces =[
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', 'Y1', '00', '00', '00', '00', '00', '00'],
        ['00', '00', 'Y3', '00', '00', '00', '00', '00', '00', 'Y0'],
        ['00', '00', 'Y0', '00', 'S0', 'S1', '00', '00', '00', 'Y3'],
        ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00'],
        ['00', '00', '00', '00', '00', '00', '00', 'Y1', '00', '00'],
        ['00', '00', 'Y0', 'A0', 'P4', 'A0', '00', '00', '00', 'X0']
    ]
    
    
    
    
    for columnIndex, currentColumn in enumerate(playerPieces):
        for rowIndex, currentRow in enumerate(currentColumn):
            if currentRow is not '00':
                imageLocation = getImageFromBoardShortHand(currentRow)
                
                pieceImage = pygame.image.load(imageLocation)
                offsets = getImageOffsets(rowIndex, columnIndex)
                if int(currentRow[1]) > 0:
                    rotatingDegrees = -1 *(90.0 * float(currentRow[1]))
                    print ("Value:", "Degrees:",  rotatingDegrees, "Location:", imageLocation)
                    pieceImage = pygame.transform.rotate(pieceImage, rotatingDegrees)
                screen.blit(pieceImage, offsets)

    return screen
    
def getImageOffsets(rowNumber, columnNumber):
    widthOffset = BOARD_BORDER_OFFSET + ((1 + rowNumber) * BOARD_DIVIDER_OFFSET) + (rowNumber * 64)
    heightOffset = BOARD_BORDER_OFFSET + ((1 + columnNumber) * BOARD_DIVIDER_OFFSET) + (columnNumber * 64)
    
    return (widthOffset, heightOffset)

def getImageFromBoardShortHand(shortHand):
    if shortHand[0] is RED_PHARAOH:
        imageString = RED_PHARAOH_FILE
    elif shortHand[0] is RED_PYRAMID:
        imageString = RED_PYRAMID_FILE
    elif shortHand[0] is RED_ANUBIS:
        imageString = RED_ANUBIS_FILE
    elif shortHand[0] is RED_SCARAB:
        imageString = RED_SCARAB_FILE
    elif shortHand[0] is RED_SPHINX:
        imageString = RED_SPHINX_FILE
    elif shortHand[0] is GRAY_PHARAOH:
        imageString = GRAY_PHARAOH_FILE
    elif shortHand[0] is GRAY_PYRAMID:
        imageString = GRAY_PYRAMID_FILE
    elif shortHand[0] is GRAY_ANUBIS:
        imageString = GRAY_ANUBIS_FILE
    elif shortHand[0] is GRAY_SCARAB:
        imageString = GRAY_SCARAB_FILE
    elif shortHand[0] is GRAY_SPHINX:
        imageString = GRAY_SPHINX_FILE
    else:
        imageString = ''
    return imageString

# Set the board size
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Khet 2.0')

backgroundImage = pygame.image.load('khet_images/khet_board.png')

screen.blit(backgroundImage, (0, 0))
screen = setupClassicConfiguration(screen)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        
