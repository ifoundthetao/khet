import pygame
from .renderEngine import RenderEngine

class PygameRenderEngine(RenderEngine):
    """
    This class will share a lot with the base RenderEngine class
    however the purpose is to abstract away the lower / lowest level calls
    for rendering. Those calls should mainly sit with the rendering library
    which will give us a bit more flexibility and speed to add new rendering engines.
    """
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

    def loadImage(self, imageLocation):
        return pygame.image.load(imageLocation)

    def renderToScreenWithOffset(self, imageResource, offset):
        self.screen.blit(imageResource, offset)

    def getBoardLocationOfEvent(self, skin):
        return skin.getBoardLocationFromCoordinates(self.mousePositionX, self.mousePositionY)

    def isUserTryingToSelectSquare(self):
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()
        return isButtonOnePressed or isButtonThreePressed

    def isUserTryingToChangeOrientation(self):
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()
        return isButtonThreePressed 

    def isUserTryingToMovePiece(self):
        (isButtonOnePressed, isButtonTwoPressed, isButtonThreePressed) = pygame.mouse.get_pressed()
        return isButtonOnePressed 

    def rotateImage(self, imageResource, degrees):
        return pygame.transform.rotate(imageResource, degrees)
