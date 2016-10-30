class RenderEngine(object):
    """
    Base class for rendering libraries to interface with.

    At the end are the methods which need to be filled out, they have "pass" in them.

    Also, need to define "VALID_EVENT" and "QUIT_EVENT"
    """
    DOWN = 2
    LEFT = 3
    RIGHT = 1
    UP = 0

    VALID_EVENT = 'NEEDS TO BE DEFINED'
    QUIT_EVENT = 'NEEDS TO BE DEFINED'

    def showEmptyBoard(self, skin):
        boardImageLocation = skin.getBoardImageLocation()
        backgroundImage = self.loadImage(boardImageLocation)
        self.renderToScreenWithOffset(imageResource = backgroundImage, offset = (0, 0))

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

    def showOrientationIcon(self, skin, gameState):
        self.gameState.setSelectedSquare(selectedSquare)
        imageLocation = self.skin.getOrientationChangeIconLocation()
        orientationChangeIcon = self.loadImage(imageLocation)
        offsets = self.skin.getSquareOffsets(selectedSquare.getColumn(), selectedSquare.getRow())
        self.renderToScreenWithOffset(imageResource = orientationChangeIcon, offset = offsets)                
        self.update()

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

    #def drawStraightShot(self, orientation, square):


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

    def createBoard(self, size):
        pass

    def initialize(self):
        pass
        
    def update(self):
        pass
        
    def setTitle(self, title):
        pass

    def quitPresenting(self):
        pass

    def getQuitEvent(self):
        pass
        
    def getEvents(self):
        pass

    def loadImage(self, imageLocation):
        pass

    def renderToScreenWithOffset(self, imageResource, offset):
        pass

    def getBoardPositionOfEvent(self, skin):
        pass

    def isUserTryingToSelectSquare(self):
        pass

    def isUserTryingToChangeOrientation(self):
        pass

    def isUserTryingToMovePiece(self):
        pass

    def rotateImage(self, imageResource, degrees):
        pass
