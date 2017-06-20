#Imports

##External
import pygame, sys, os, math
from pygame.locals import *
from precode import Vector2D

##General methods
from library import *

##Classes and global constants
from drawable import *
from drawconf import *
from config import *

#Since several of the methods in the Game class could be used in several games,
#it's an idea to make a base class that this one can inherit from.

class Game(object):
    """A class for running a game."""

    def __init__(self):
        """Create a new game."""

        self._screen = self._makeScreen()           #Initialize game window
        self._clock = pygame.time.Clock()           #Initialising game clock(used to make the animation run smoothly)
        self._font = makeFont(FONT, FONTSIZE)       #Create a standard font

        #Make key mappings for the player
        keys = self._makeControls()

        self.run()  #Run the game

    def _makeScreen(self):
        """Initializes and returns the pygame display (game window)."""

        #Centering the display on screen (taken from pygame FAQ)
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        #Starting pygame and setting up the display(game window)

        pygame.init()
        gamescreen = pygame.display.set_mode((RES_X, RES_Y))
        pygame.display.set_caption(CAPTION)

        return gamescreen

    def _makeLevel(self):
        """Default level generation for the game."""

        print("Please don't try to make a level for this abstract game class.")

    def _makeControls(self):
        """Generates a list containing the keys the player can use (as a tuple).
        This default function uses the arrow keys for left, right and up.

        First element is a surface supposed to hold a key image.
        Second element is text to accompany the image.
        Third element is a pygame key constant for the corresponding key.

        Returns the list of tuples.
        """

        return ([(IMAGE, KEYTEXT[0], pygame.K_LEFT),
                 (IMAGE, KEYTEXT[1], pygame.K_RIGHT),
                 (IMAGE, KEYTEXT[2], pygame.K_UP)])

    def update(self):
        """Update game objects (typically player controlled).

        returns False. Children should have the ability to return True if the game is supposed to keep running."""

        return False

    def tick(self):
        """wait for a while."""

        self._clock.tick(SFPS)

    def drawBackground(self):
        """Default function does nothing."""

        pass

    def drawForeground(self):
        """Default function does nothing."""

        pass

    def makeMenu(self):
        """Make a menu near the center of the screen. Will overwrite previously drawn objects."""

        #Draw a background and a header for the menu
        pygame.draw.rect(self._screen, LGRAY, (MENU_X, MENU_Y, MENU_W, MENU_H))
        textbox = self.makeTextbox(CAPTION, BLACK, font = makeFont(FONT, BIGSIZE))
        self._screen.blit(textbox, (MENU_HEAD_X, MENU_HEAD_Y))

        #Child classes should usually expand on the menu

    def makeTextbox(self, message, color, bgcolor = None, font = None):
        """Make a textbox displaying message.

        message: A text string to be displayed.
        color: The color to display the text with.
        bgcolor: A color for the textbox. The textbox will be transparent if no color is given.
        font: A font to use in the textbox. Will use the default font for the class if no other font is given.

        returns the textbox as a rendered pygame font.
        """

        if font == None:
            font = self._font
        if bgcolor == None:
            return font.render(message, True, color)
        else:
            return font.render(message, True, color, bgcolor)

    def run(self):
        """Run the game for a certain amound of time."""

        running = True

        while running:
            running = self.update()

            #clearing the layer and redrawing the background
            pygame.draw.rect(self._screen, LGRAY, (0, 0, RES_X, RES_Y))

            #Drawing static background objects
            self.drawBackground()
            self.makeMenu()

            #Drawing foreground objects
            self.drawForeground()

            #Wait for a while before updating the display window.
            self.tick()
            pygame.display.update()

        #Make sure the user can see the final results
        self.tick()
        return

if __name__ == '__main__':
    game = Game()
