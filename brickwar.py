#Imports

from game import *
from brickers import *

class Brickwar(Game):
    """A class for running the Brick Warrior game."""

    def __init__(self):
        """Create a new game"""

        Game.__init__(self, False)
        self._level = 1 #Starts at level 1
        self._objects = self._makeLevel()
        self._brick = self._makeSelf()

        self.run()

    def _makeLevel(self):
        """Create a level from file"""

        objects = list()

        #Temporary version creates a default level without reading
        objects.append(Platform(0, 480, 180))
        objects.append(Platform(260, 480, 180))
        objects.append(Platform(520, 480, 180))
        objects.append(Platform(780, 480, 180))

        return objects

    def _makeSelf(self):
        """Make a brick for a player."""

        return Brick(0, 440, 40, RED)

    def drawBackground(self):
        """Draws background objects"""

        for item in self._objects:
            item.draw(self._screen)

    def drawForeground(self):
        """Draws foreground objects"""

        self._brick.draw(self._screen)

if __name__ == '__main__':
    game = Brickwar()
