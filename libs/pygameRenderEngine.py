import pygame

class PygameRenderEngine(object):
    """
    This class will share a lot with the base RenderEngine class
    however the purpose is to abstract away the lower / lowest level calls
    for rendering. Those calls should mainly sit with the rendering library
    which will give us a bit more flexibility and speed to add new rendering engines.
    """
    DOWN = 2
    LEFT = 3
    RIGHT = 1
    UP = 0

    VALID_EVENT = pygame.MOUSEBUTTONDOWN
    QUIT_EVENT = pygame.QUIT

    def createBoard(self, size):
        self.screen = pygame.display.set_mode(size)

    def initialize(self):
        pygame.init()
        
    def update(self):
        pygame.display.update()
        
    def setTitle(self, title):
        pygame.display.set_caption(title)

    def showEmptyBoard(self, skin):
        #TODO: Rename method to getBoardImageLocation
        boardImageLocation = skin.getBoardLocation()
        backgroundImage = self.loadImage(boardImageLocation)
        self.renderToScreenWithOffset(imageResource = backgroundImage, offset = (0, 0))

    def quitPresenting(self):
        pygame.quit()

    def getQuitEvent(self):
        return pygame.QUIT
        
    def getEvents(self):
        """
        We are doing this here, to keep it out of the main loop.
        Hopefully this will keep things clean, and allow for other
        styles of play.
        """
        self.mousePositionX, self.mousePositionY = pygame.mouse.get_pos()
        
        event = pygame.event.wait()
        return [event] + pygame.event.get()

    def displayOrientedImage(self, skin, square):
        piece = square.getPiece()
        
        orientation = piece.getOrientation()
        imageLocation = piece.getImageLocation()
        pieceImage = self.loadImage(imageLocation)
        
        offsets = self.skin.getSquareOffsets(square.getColumn(), square.getRow())
        if int(orientation) > 0:
            rotatingDegrees = -1 * (90.0 * float(orientation))
            
            pieceImage = self.rotateImage(imageResource = pieceImage, degrees = rotatingDegrees)
        self.renderToScreenWithOffset(imageResource = pieceImage, offset = offsets)

    def rotateImage(self, imageResource, degrees):
        return pygame.transform.rotate(imageResource, degrees)

    def getMouseClicks(self):
        return pygame.mouse.get_pressed()

    def showOrientationIcon(self, skin, gameState):
        self.gameState.setSelectedSquare(selectedSquare)
        imageLocation = self.skin.getOrientationChangeIconLocation()
        orientationChangeIcon = self.loadImage(imageLocation)
        offsets = self.skin.getSquareOffsets(selectedSquare.getColumn(), selectedSquare.getRow())
        self.renderToScreenWithOffset(imageResource = orientationChangeIcon, offset = offsets)                
        self.update()

    #def drawStraightShot(self, orientation, square):


    def drawReflectedShot(self, shotDirection, boardLocation):
        initialShotDirection = int(shotDirection)
        shotDirection = int(piece.getReflectionDirection(shotDirection))
        
        imageLocation = self.skin.getReflectedShotLocation()                    
        shotImage = self.loadImage(imageLocation)
        
        rotatingDegrees = None
        if shotDirection == self.LEFT:
            if initialShotDirection == self.UP:
                rotatingDegrees = float(3.0 * 90) * -1
        elif shotDirection == self.RIGHT:
            if initialShotDirection == self.UP:
                rotatingDegrees = float(2.0 * 90) * -1
            else:
                rotatingDegrees = float(1.0 * 90) * -1
        elif shotDirection == self.UP:
            if initialShotDirection == self.LEFT:
                rotatingDegrees = float(1.0 * 90) * -1
        else:
            if initialShotDirection == self.LEFT:
                rotatingDegrees = float(2.0 * 90) * -1
            else:
                rotatingDegrees = float(3.0 * 90) * -1
        if rotatingDegrees is not None:
            shotImage = self.rotateImage(imageResource = shotImage, degrees = rotatingDegrees)

        column, row = boardLocation
        offsets = self.skin.getSquareOffsets(column, row)
        self.renderToScreenWithOffset(imageResource = shotImage, offset = offsets)                
        self.update()

    #def drawHitShot(self, orientation, square):

    def showOrientationIcon(self, skin, boardLocation):
        column, row = boardLocation
        imageLocation = skin.getOrientationChangeIconLocation()
        orientationChangeIcon = self.loadImage(imageLocation)
        offsets = skin.getSquareOffsets(column, row)
        self.renderToScreenWithOffset(imageResource = orientationChangeIcon, offset = offsets)                
        self.update()

    def displayBoard(self, board, skin):
        self.showEmptyBoard(skin = skin)
        for columnIndex, currentColumn in enumerate(board.boardState):
            for rowIndex, square in enumerate(currentColumn):
                if square.isOccupied():
                    piece = square.getPiece()
                    
                    orientation = piece.getOrientation()
                    imageLocation = piece.getImageLocation()
                    pieceImage = self.loadImage(imageLocation)
                    
                    offsets = skin.getSquareOffsets(square.getColumn(), square.getRow())
                    if int(orientation) > 0:
                        rotatingDegrees = -1 * (90.0 * float(orientation))
                        
                        pieceImage = self.rotateImage(imageResource = pieceImage, degrees = rotatingDegrees)
                    self.renderToScreenWithOffset(imageResource = pieceImage, offset =  offsets)
        self.update()
        
    def loadImage(self, imageLocation):
        return pygame.image.load(imageLocation)

    def renderToScreenWithOffset(self, imageResource, offset):
        self.screen.blit(imageResource, offset)


    def getBoardPositionOfEvent(self, skin):
        return skin.getBoardPositionFromCoordinates(self.mousePositionX, self.mousePositionY)
