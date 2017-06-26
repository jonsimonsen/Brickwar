#Imports

from game import *
from brickers import *

class Brickwar(Game):
    """A class for running the Brick Warrior game."""

    def __init__(self):
        """Create a new game"""

        print("t1")
        Game.__init__(self, False)
        print("t2")
        self._level = 1 #Starts at level 1
        print("t3")
        self._objects = self._makeLevel()
        print("t4")

        self.run()
        print("t5")

    def _makeLevel(self):
        """Create a level from file"""

        objects = list()

        #Temporary version creates a default level without reading
        objects.append(Platform(0, 480, 260))
        objects.append(Platform(340, 480, 260))
        objects.append(Platform(680, 480, 260))
        objects.append(Platform(1020, 480, 260))

        return objects

    def drawBackground(self):
        """Draws background objects"""

        for item in self._objects:
            item.draw(self._screen)

if __name__ == '__main__':
    game = Brickwar()
